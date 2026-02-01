import os
import re
import argparse

# Default arguments
default_css_path = "../src/WUIPlugins/Themes/WUIPluginThemes-0.1.css"
default_out_dir = "../src/WUIPlugins/Themes/"
default_theme = "theme-1"

# Get arguments
parser = argparse.ArgumentParser(
    description="Make CSS themes from WUIPluginThemes CSS file.",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)
parser.add_argument("--css", type=str, help="Path to the CSS file.", default=default_css_path)
parser.add_argument("-o", "--out", type=str, help="Output directory for CSS themes.", default=default_out_dir)
parser.add_argument("-t", "--theme", type=str, help="Theme name to extract and use in output.", default=default_theme)
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

    new_value = re.sub(pattern, repl, value)
    return new_value

def parse_css_file(filepath, target_theme):
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
    primitives_start = re.compile(r'^\.wuiplugin-themes:is\((.+)\)\s*{')
    components_start = re.compile(r'^\.wuiplugin-themes\s*{')
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
        prim_match = primitives_start.match(line)
        if prim_match:
            # Check if this block contains our target theme
            selectors = prim_match.group(1)
            # selectors will be something like ".theme-1, .theme-default"
            if f".{target_theme}" in selectors:
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

def generate_theme(mode, theme_name, header, primitives, components, output_path):
    # 1. Build lookup for this mode
    lookup = {}
    suffix = f"-{mode}"
    opposite_suffix = "-dark" if mode == "light" else "-light"
    
    # Simple resolution logic: preferred suffix > base name > ignored other suffix
    
    # First pass: map everything to ensure we have base values
    # We need to treat "no suffix" as base, but "suffix" overrides it.
    
    # Let's iterate keys and resolve "best match" for each base variable present
    
    # But wait, primitives contains ALL matched lines.
    # E.g. --gray-max-light, --gray-max-dark, --borderradius-low
    
    resolved_primitives = {}
    
    # 1. Add common variables (no usage suffix)
    for name, value in primitives.items():
        if not name.endswith('-light') and not name.endswith('-dark'):
            resolved_primitives[name] = value

    # 2. Add/Override with specific mode variables
    for name, value in primitives.items():
        if name.endswith(suffix):
            base_name = name[:-len(suffix)]
            resolved_primitives[base_name] = value
            
    # Now resolved_primitives has the correct values for this mode
    
    # 2. Process components for output
    output_lines = []
    output_lines.extend(header)
    output_lines.append("\n") # spacing
    
    class_name = f".wuiplugin-themes.{theme_name}.{mode} " + "{\n"
    output_lines.append(class_name)
    
    # Lookup for resolution (starts with resolved primitives)
    lookup = resolved_primitives.copy()
    
    for item in components:
        if item['type'] == 'comment':
            output_lines.append(item['content'])
        elif item['type'] == 'empty':
            output_lines.append(item['content'])
        elif item['type'] == 'var':
            name = item['name']
            raw_val = item['value']
            resolved = resolve_value(raw_val, lookup)
            
            # Write to output
            indent = item['indent']
            output_lines.append(f"{indent}{name}: {resolved};\n")
            
            # Store for future self-reference
            lookup[name] = resolved
            
    output_lines.append("}\n")
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.writelines(output_lines)
    print(f"Generated {output_path}")

def main():
    # Create output directory if it doesn't exist
    os.makedirs(args.out, exist_ok=True)
    
    # Parse source
    header, primitives, components = parse_css_file(args.css, args.theme)
    
    if not primitives:
        print(f"Warning: No primitive variables found for theme '{args.theme}'. Check if the theme exists in the CSS file.")
    
    # Extract base name for output
    base_name = os.path.basename(args.css)
    if base_name.endswith('.css'):
        base_name = base_name[:-4]
        
    # Generate Light
    # FileName format: "WUIPluginThemes-0.1-theme-1-light.css"
    light_file = os.path.join(args.out, f"{base_name}-{args.theme}-light.css")
    generate_theme('light', args.theme, header, primitives, components, light_file)
    
    # Generate Dark
    dark_file = os.path.join(args.out, f"{base_name}-{args.theme}-dark.css")
    generate_theme('dark', args.theme, header, primitives, components, dark_file)

if __name__ == "__main__":
    main()
