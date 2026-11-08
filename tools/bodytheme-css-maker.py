#!/usr/bin/env python3
"""Make the light and dark CSS files of a body theme from the WUIPluginBodyTheme CSS file."""

import os
import re
import argparse

# Default arguments
DEFAULT_SOURCE_PATH = "../src/wui-js/plugins/bodytheme/wuiplugin-bodytheme-0.16.css"
DEFAULT_THEMES_DIR  = "../src/wui-js/plugins/bodytheme"
DEFAULT_NAME        = "default"
DEFAULT_VERSION     = "0.16"

# Get arguments
parser = argparse.ArgumentParser(
	description="Make CSS theme files from WUIPluginBodyTheme CSS files.",
	formatter_class=argparse.ArgumentDefaultsHelpFormatter
)
parser.add_argument("-p", "--plugin",    type=str, help="Path to the body themes plugin CSS source file.", default=DEFAULT_SOURCE_PATH)
parser.add_argument("-d", "--directory", type=str, help="Themes base directory.", default=DEFAULT_THEMES_DIR)
parser.add_argument("-n", "--name",      type=str, help="Theme name.", default=DEFAULT_NAME)
parser.add_argument("-v", "--version",   type=str, help="Theme version.", default=DEFAULT_VERSION)
args = parser.parse_args()

TOKEN_PREFIX = "--wuiplugin-bodytheme-"

RE_VAR_DECL     = re.compile(r'^\s*(--[a-zA-Z0-9-]+):\s*(.+?);\s*$')
RE_PROP_DECL    = re.compile(r'^\s*([a-z-]+):\s*(.+?);\s*$')
RE_COMMENT_LINE = re.compile(r'^\s*/\*\s*(.+)\s*\*/\s*$')
RE_BLOCK_END    = re.compile(r'^\s*}\s*$')

def resolveValue(value, lookup):
	"""
	Replaces var(--name) in value with the value from lookup.
	"""
	pattern = r'var\((--[a-zA-Z0-9-]+)\)'
	# helper for re.sub
	def replaceMatch(match):
		varName = match.group(1)
		# If var_name is in lookup, use it. Otherwise keep original var(...)
		return lookup.get(varName, match.group(0))
	newValue = re.sub(pattern, replaceMatch, value)
	return newValue

def resolveLightDark(value, mode):
	"""
	Replaces every light-dark(a, b) in value with a (light mode) or b (dark mode).
	Arguments are split at the top-level comma, so nested functions are preserved.
	"""
	while True:
		start = value.find("light-dark(")
		if start < 0:
			return value
		depth = 0
		comma = -1
		end = -1
		for i in range(start + len("light-dark("), len(value)):
			char = value[i]
			if char == "(":
				depth += 1
			elif char == ")":
				if depth == 0:
					end = i
					break
				depth -= 1
			elif char == "," and depth == 0 and comma < 0:
				comma = i
		if end < 0 or comma < 0:
			return value
		light = value[start + len("light-dark("):comma].strip()
		dark  = value[comma + 1:end].strip()
		value = value[:start] + (light if mode == "light" else dark) + value[end + 1:]

def readHeader(lines):
	"""
	Returns the leading /* ... */ comment block of a file (only the first comment).
	"""
	header = []
	for line in lines:
		if not header and line.strip() == "":
			continue
		if not header and not line.strip().startswith("/*"):
			break
		header.append(line)
		if line.strip().endswith("*/"):
			break
	return header

def parseSettingsFile(filepath, targetTheme):
	"""
	Reads a theme settings CSS file (e.g. settings-0.2.css) and extracts the
	CSS variable declarations of the block that matches the target_theme selector,
	including the blocks nested in @media rules.

	Returns:
		header   (list[str])  header comment lines from the file
		settings (dict)       { '--var-name': 'value', ... } (tokens and --wui-* overrides)
		medias   (list)       [ { 'query': '@media ...', 'settings': { ... } }, ... ]
	"""
	with open(filepath, 'r', encoding='utf-8') as f:
		lines = f.readlines()
	header   = readHeader(lines)
	settings = {}
	medias   = []
	# Matches:  .wuiplugin-bodytheme.theme-default {
	# or:       .wuiplugin-bodytheme:is(.theme-1, .theme-default) {
	settingsStart = re.compile(r'^\s*\.wuiplugin-bodytheme(?::is\((.+)\)|(\.[\w-]+))\s*{')
	mediaStart    = re.compile(r'^\s*(@media[^{]+?)\s*{')
	target = None
	media  = None
	for line in lines:
		mediaMatch = mediaStart.match(line)
		if mediaMatch:
			media = {'query': mediaMatch.group(1), 'settings': {}}
			continue
		settMatch = settingsStart.match(line)
		if settMatch:
			selectors = settMatch.group(1) or settMatch.group(2)
			if f".{targetTheme}" in selectors or targetTheme in selectors:
				target = media['settings'] if media else settings
			continue
		if RE_BLOCK_END.match(line):
			if target is not None:
				target = None
			elif media is not None:
				if media['settings']:
					medias.append(media)
				media = None
			continue
		if target is not None:
			m = RE_VAR_DECL.match(line)
			if m:
				name, val = m.groups()
				target[name] = val
	return header, settings, medias

def parseCssFile(filepath):
	"""
	Reads the base CSS file (e.g. wuiplugin-bodytheme-0.16.css) and extracts:
	  - header     : leading comment block
	  - components : list of items (vars, comments, empty lines) inside
					 the .wuiplugin-bodytheme { } variables block
	  - globals    : property declarations of the :where(.wuiplugin-bodytheme) rule
	  - medias     : variable declarations of the @media rules
					 [ { 'query': '@media ...', 'vars': [ (name, value), ... ] }, ... ]

	Note: the .system, .light, .dark and .transition blocks are intentionally ignored:
		  static themes resolve every token to its mode value.
	"""
	with open(filepath, 'r', encoding='utf-8') as f:
		lines = f.readlines()
	header     = readHeader(lines)
	components = []
	globals_   = []
	medias     = []
	componentsStart = re.compile(r'^\s*\.wuiplugin-bodytheme\s*{')
	globalsStart    = re.compile(r'^\s*:where\(\.wuiplugin-bodytheme\)\s*{')
	mediaStart      = re.compile(r'^(@media[^{]+?)\s*{')
	depth = 0
	block = None
	media = None
	firstComponents = True
	for line in lines:
		stripped = line.strip()
		opens = stripped.endswith("{")
		if RE_BLOCK_END.match(line):
			depth -= 1
			if depth == 0 and media is not None:
				medias.append(media)
				media = None
			block = None
			continue
		if opens:
			depth += 1
			mediaMatch = mediaStart.match(line)
			if depth == 1 and mediaMatch:
				media = {'query': mediaMatch.group(1), 'vars': []}
			elif media is not None:
				# Inside @media only the .wuiplugin-bodytheme variables block is kept
				block = 'media' if componentsStart.match(line) else 'ignored'
			elif componentsStart.match(line) and firstComponents:
				block = 'components'
				firstComponents = False
			elif globalsStart.match(line):
				block = 'globals'
			else:
				block = 'ignored'
			continue
		if block == 'media':
			m = RE_VAR_DECL.match(line)
			if m:
				media['vars'].append(m.groups())
			continue
		if block == 'components':
			if RE_COMMENT_LINE.match(line):
				components.append({'type': 'comment', 'content': line})
			elif RE_VAR_DECL.match(line):
				name, val = RE_VAR_DECL.match(line).groups()
				# Only keep --wui-*, --wuiplugin-* and --wuiview-* variables
				if name.startswith(('--wui-', '--wuiplugin-', '--wuiview-')):
					indent = re.findall(r'^\s*', line)[0]
					components.append({'type': 'var', 'name': name, 'value': val, 'indent': indent})
			elif stripped == '':
				components.append({'type': 'empty', 'content': line})
		elif block == 'globals':
			m = RE_PROP_DECL.match(line)
			if m:
				globals_.append(m.groups())
	return header, components, globals_, medias

def getModeTokens(settings, mode):
	"""
	Returns the theme tokens for a mode: common tokens plus the mode tokens without
	their -light / -dark suffix. Component overrides (--wui-*) are not included.
	"""
	suffix = f"-{mode}"
	tokens = {}
	for name, value in settings.items():
		if name.startswith(TOKEN_PREFIX) and not name.endswith('-light') and not name.endswith('-dark'):
			tokens[name] = value
	for name, value in settings.items():
		if name.startswith(TOKEN_PREFIX) and name.endswith(suffix):
			tokens[name[:-len(suffix)]] = value
	return tokens

def resolveComponents(mode, settings, components):
	"""
	Resolves every component variable of the base block for a mode.
	Component overrides of the settings file replace the base value in place.

	Returns:
		tokens   (dict)  resolved theme tokens
		resolved (dict)  { '--wui-name': 'value', ... } in base block order
		extra    (dict)  overrides that do not exist in the base block
	"""
	tokens    = getModeTokens(settings, mode)
	overrides = {name: value for name, value in settings.items() if not name.startswith(TOKEN_PREFIX)}
	lookup    = {name: resolveLightDark(value, mode) for name, value in tokens.items()}
	resolved  = {}
	for item in components:
		if item['type'] != 'var':
			continue
		name  = item['name']
		value = overrides.get(name, item['value'])
		value = resolveLightDark(resolveValue(value, lookup), mode)
		resolved[name] = value
		# Store for future self-reference within the same block
		lookup[name] = value
	extra = {}
	# Two passes, so overrides that reference other overrides declared later are also resolved
	for _ in range(2):
		for name, value in overrides.items():
			if name not in resolved:
				extra[name] = resolveLightDark(resolveValue(value, lookup), mode)
				lookup[name] = extra[name]
	return lookup, resolved, extra

def generateTheme(mode, themeName, header, settings, settingMedias, components, globals_, baseMedias, outputPath):
	selector = f".wuiplugin-bodytheme.{themeName}.{mode}"
	tokens, resolved, extra = resolveComponents(mode, settings, components)
	# 1. Header
	outputFilename = os.path.basename(outputPath)
	outputLines = []
	for line in header:
		line = re.sub(r'(@file\s+)\S+', lambda m: m.group(1) + outputFilename, line)
		outputLines.append(line)
	outputLines.append("\n")  # spacing
	# 2. Variables block: theme tokens and resolved component variables
	outputLines.append(selector + " {\n")
	outputLines.append(f"	color-scheme: {mode};\n")
	outputLines.append("\n")
	outputLines.append("	/* wuiplugin-bodytheme */\n")
	outputLines.append("\n")
	outputLines.append(f'	--wuiplugin-bodytheme-name: "{themeName}";\n')
	for name in getModeTokens(settings, mode):
		if name != f"{TOKEN_PREFIX}name":
			outputLines.append(f"	{name}: {tokens[name]};\n")
	for item in components:
		if item['type'] in ('comment', 'empty'):
			outputLines.append(item['content'])
		elif item['type'] == 'var':
			outputLines.append(f"{item['indent']}{item['name']}: {resolved[item['name']]};\n")
	if extra:
		outputLines.append("\n")
		outputLines.append("	/* components */\n")
		outputLines.append("\n")
		for name, value in extra.items():
			outputLines.append(f"	{name}: {value};\n")
	outputLines.append("}\n")
	# 3. Global rule (page font and background), with zero specificity like in the base file
	if globals_:
		outputLines.append("\n")
		outputLines.append(f":where({selector}) " + "{\n")
		for prop, value in globals_:
			outputLines.append(f"	{prop}: {resolveLightDark(resolveValue(value, tokens), mode)};\n")
		outputLines.append("}\n")
	# 4. @media rules of the base file (literal component values)
	for media in baseMedias:
		outputLines.append("\n")
		outputLines.append(media['query'] + " {\n")
		outputLines.append("\n")
		outputLines.append(f"	{selector} " + "{\n")
		for name, value in media['vars']:
			outputLines.append(f"		{name}: {resolveLightDark(resolveValue(value, tokens), mode)};\n")
		outputLines.append("	}\n")
		outputLines.append("}\n")
	# 5. @media rules of the settings file: only the values that change in this mode
	for media in settingMedias:
		mediaSettings = dict(settings)
		mediaSettings.update(media['settings'])
		mediaTokens, mediaResolved, mediaExtra = resolveComponents(mode, mediaSettings, components)
		changes = [(name, value) for name, value in mediaTokens.items() if tokens.get(name) != value]
		changes += [(name, value) for name, value in mediaResolved.items() if resolved.get(name) != value]
		changes += [(name, value) for name, value in mediaExtra.items() if extra.get(name) != value]
		# Component values are also stored in the tokens lookup, so keep each name once
		changes = list(dict(changes).items())
		if not changes:
			continue
		outputLines.append("\n")
		outputLines.append(media['query'] + " {\n")
		outputLines.append("\n")
		outputLines.append(f"	{selector} " + "{\n")
		for name, value in changes:
			outputLines.append(f"		{name}: {value};\n")
		outputLines.append("	}\n")
		outputLines.append("}\n")
	with open(outputPath, 'w', encoding='utf-8') as f:
		f.writelines(outputLines)
	print(f"Generated {outputPath}")

def main():
	# Derive paths from --directory, --name and --version
	outDir       = os.path.join(args.directory, args.name)
	settingsPath = os.path.join(outDir, f"settings-{args.version}.css")
	# Create output directory if it doesn't exist
	os.makedirs(outDir, exist_ok=True)
	# Parse setting variables from the theme file
	settHeader, settings, settingMedias = parseSettingsFile(settingsPath, args.name)
	if not settings:
		print(f"Warning: No setting variables found for theme '{args.name}' in '{settingsPath}'.")
		print("Check that the theme selector exists in that file.")
	# Parse component variables from the base CSS file
	baseHeader, components, globals_, baseMedias = parseCssFile(args.plugin)
	# Use the settings file header for the output files
	header = settHeader if settHeader else baseHeader
	# Generate Light  →  e.g. light-0.2.css
	lightFile = os.path.join(outDir, f"light-{args.version}.css")
	generateTheme('light', args.name, header, settings, settingMedias, components, globals_, baseMedias, lightFile)
	# Generate Dark   →  e.g. dark-0.2.css
	darkFile = os.path.join(outDir, f"dark-{args.version}.css")
	generateTheme('dark', args.name, header, settings, settingMedias, components, globals_, baseMedias, darkFile)

if __name__ == "__main__":
	main()
