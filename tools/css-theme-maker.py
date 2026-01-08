import os
import re
import argparse

# Default arguments
css_path = "../src/WUIPlugins/Themes/WUIPluginsThemes-0.1.css"
out_dir = "../src/WUIPlugins/Themes/"

# Get arguments
parser = argparse.ArgumentParser(
    description="Make CSS themes from WUIPluginsThemes CSS file.",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)
parser.add_argument("--css", type=str, help="Path to the CSS file.", default=css_path)
parser.add_argument("--out", type=str, help="Output directory for CSS themes.", default=out_dir)
args = parser.parse_args()

def resolve_value(value, lookup):
    """
    Replaces var(--name) in value with the value from lookup.
    """
    pattern = r'var\((--[a-zA-Z0-9-]+)\)'
    
    # helper for re.sub
    def repl(match):
        var_name = match.group(1)
        # If var_name is in lookup, use it. Otherwise keep original var(...)
        return lookup.get(var_name, match.group(0))

    # Keep resolving until no more changes (to handle nested vars if any, 
    # though strict top-down should handle single-level dependencies)
    # Just one pass is usually enough if we trust topological order or 
    # if we only care about resolving against the primitives/previous lines.
    # However, to be safe against `rgb(from var(--a) ...)` where `var(--a)` is simple:
    
    new_value = re.sub(pattern, repl, value)
    
    # If the resolution introduced new vars (unlikely in this specific CSS structure 
    # but possible), we might want another pass. 
    # Given the requirements, one pass using fully-populated lookup (primitives + previous wui vars) is best.
    
    return new_value

def parse_css_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    header = []
    primitives = {}
    components = []
    
    # State flags
    in_header = True
    in_primitives = False
    in_components = False
    
    # Regexes
    # Header: assume lines starting with /* at the top
    primitives_start = re.compile(r'^\.wuiplugins-themes:is')
    components_start = re.compile(r'^\.wuiplugins-themes\s*{')
    block_end = re.compile(r'^\s*}\s*$')
    
    var_decl = re.compile(r'^\s*(--[a-zA-Z0-9-]+):\s*(.+?);\s*$')
    comment_line = re.compile(r'^\s*/\*\s*(.+)\s*\*/\s*$')

    for line in lines:
        stripped = line.strip()
        
        # Header capture
        if in_header:
            if stripped.startswith('/*') or stripped.startswith('*') or stripped == '':
                if stripped.startswith('/*') and 'theme:' in stripped:
                     # This seems to be the start of content logic, stop header
                     in_header = False
                elif stripped != '':
                    header.append(line)
            else:
                in_header = False
        
        # Check block starts
        if primitives_start.match(line):
            in_primitives = True
            continue
        if components_start.match(line):
            in_components = True
            continue
            
        # Check block ends
        if block_end.match(line):
            if in_primitives:
                in_primitives = False
            elif in_components:
                in_components = False
            continue

        if in_primitives:
            m = var_decl.match(line)
            if m:
                name, val = m.groups()
                primitives[name] = val
                
        if in_components:
            # We want to preserve comments and layout as much as possible, 
            # or at least the variables.
            # The task asks to "preserve comments with names of each class".
            if comment_line.match(line):
                components.append({'type': 'comment', 'content': line})
            elif var_decl.match(line):
                m = var_decl.match(line)
                if m:
                    name, val = m.groups()
                    # Only keep --wui-* variables
                    if name.startswith('--wui-'):
                        components.append({'type': 'var', 'name': name, 'value': val, 'indent': line[:line.find('--')]})
            elif stripped == '':
                 components.append({'type': 'empty', 'content': line})


    return header, primitives, components

def generate_theme(mode, header, primitives, components, output_path):
    # 1. Build lookup for this mode
    lookup = {}
    suffix = f"-{mode}"
    
    # Add primitives
    for name, value in primitives.items():
        # strict name match
        lookup[name] = value
        
        # Mode-specific resolution logic
        # If we have --foo-light, mapped to --foo
        if name.endswith(suffix):
            base_name = name[:-len(suffix)]
            lookup[base_name] = value
            
    # Also ensure common variables (without -light/-dark) are available if not overwritten
    # (The loop above adds everything, so --foo is in lookup. 
    # If --foo-light existed, we added --foo pointing to its value, overwriting if --foo existed?
    # In the CSS, --wuiplugins-theme-graycolor-max-light exists. --wuiplugins-theme-graycolor-max DOES NOT exist in primitives block.
    # But --wuiplugins-theme-borderradius-low exists and has no suffix.
    # So logic:
    #   Iterate all primitives.
    #   If endswith suffix: lookup[base] = val
    #   Else if not endswith opposite suffix: lookup[name] = val)
    
    # Refined Lookup Construction
    refined_lookup = {}
    opposite_suffix = "-dark" if mode == "light" else "-light"
    
    for name, value in primitives.items():
        if name.endswith(suffix):
            base = name[:-len(suffix)]
            refined_lookup[base] = value
        elif name.endswith(opposite_suffix):
            pass
        else:
            refined_lookup[name] = value
            
    # 2. Process components for output
    output_lines = []
    output_lines.extend(header)
    output_lines.append("\n") # spacing
    
    class_name = f".wuiplugins-themes.{mode} " + "{\n"
    output_lines.append(class_name)
    
    # Use refined_lookup to resolve vars. 
    # Also add resolved vars to refined_lookup so subsequent vars can use them.
    
    for item in components:
        if item['type'] == 'comment':
            output_lines.append(item['content'])
        elif item['type'] == 'empty':
            output_lines.append(item['content'])
        elif item['type'] == 'var':
            name = item['name']
            raw_val = item['value']
            resolved = resolve_value(raw_val, refined_lookup)
            
            # Write to output
            indent = item['indent']
            output_lines.append(f"{indent}{name}: {resolved};\n")
            
            # Store for future self-reference
            refined_lookup[name] = resolved
            
    output_lines.append("}\n")
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.writelines(output_lines)
    print(f"Generated {output_path}")

def main():
    # Create output directory if it doesn't exist
    os.makedirs(args.out, exist_ok=True)
    
    # Parse source
    header, primitives, components = parse_css_file(args.css)
    
    # Extract base name for output
    base_name = os.path.basename(args.css)
    if base_name.endswith('.css'):
        base_name = base_name[:-4]
        
    # Generate Light
    light_file = os.path.join(args.out, f"{base_name}-light.css")
    generate_theme('light', header, primitives, components, light_file)
    
    # Generate Dark
    dark_file = os.path.join(args.out, f"{base_name}-dark.css")
    generate_theme('dark', header, primitives, components, dark_file)

if __name__ == "__main__":
    main()
