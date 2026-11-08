#!/usr/bin/env python3
"""Clone an existing body theme as a starting point for a new one."""

import os
import re
import argparse

# Default arguments
DEFAULT_THEMES_DIR     = "../src/wui-js/plugins/bodytheme"
DEFAULT_SOURCE         = "default"
DEFAULT_SOURCE_VERSION = "0.16"
DEFAULT_VERSION        = "0.1"

# Get arguments
parser = argparse.ArgumentParser(
	description="Clone an existing theme as a starting point for a new one.",
	formatter_class=argparse.ArgumentDefaultsHelpFormatter
)
parser.add_argument("-d", "--directory",      type=str, help="Themes base directory.", default=DEFAULT_THEMES_DIR)
parser.add_argument("-s", "--source",         type=str, help="Name of the theme to clone.", default=DEFAULT_SOURCE)
parser.add_argument("-S", "--source-version", type=str, help="Version of the theme to clone.", default=DEFAULT_SOURCE_VERSION)
parser.add_argument("-n", "--name",           type=str, help="Name of the new theme.", required=True)
parser.add_argument("-v", "--version",        type=str, help="Version of the new theme.", default=DEFAULT_VERSION)
args = parser.parse_args()

def main():
	sourceDir  = os.path.join(args.directory, args.source)
	targetDir  = os.path.join(args.directory, args.name)
	sourcePath = os.path.join(sourceDir, f"settings-{args.source_version}.css")
	targetFile = f"settings-{args.version}.css"
	targetPath = os.path.join(targetDir, targetFile)
	if not os.path.isfile(sourcePath):
		print(f"Error: source settings file not found: {sourcePath}")
		exit(1)
	if os.path.exists(targetPath):
		print(f"Error: target already exists: {targetPath}")
		exit(1)
	os.makedirs(targetDir, exist_ok=True)
	with open(sourcePath, 'r', encoding='utf-8') as f:
		content = f.read()
	# Replace the theme selector (also inside @media rules)
	content = re.sub(
		r'(\.wuiplugin-bodytheme\.)' + re.escape(args.source) + r'\b',
		r'\g<1>' + args.name,
		content
	)
	# Replace the header fields and the theme name variable
	content = re.sub(r'(@file\s+)\S+', r'\g<1>' + targetFile, content, count=1)
	content = re.sub(r'(@theme\s+)\S+', r'\g<1>' + args.name, content, count=1)
	content = re.sub(r'(@version\s+)\S+', r'\g<1>' + args.version, content, count=1)
	content = re.sub(r'(--wuiplugin-bodytheme-name:\s*)"[^"]*"', r'\g<1>"' + args.name + '"', content)
	with open(targetPath, 'w', encoding='utf-8') as f:
		f.write(content)
	print(f"Cloned '{args.source}' {args.source_version} → '{args.name}' {args.version}")
	print(f"Created: {targetPath}")
	print(f"Next: edit {targetPath} (values only, keep its structure), then run bodytheme-css-maker.py -n {args.name} -v {args.version}")
	print(f"Check: python3 ../tests/settings-check.py {args.name}")

if __name__ == "__main__":
	main()
