#!/usr/bin/env python3
"""WUIPluginBodyTheme settings check: structure of each theme against the reference theme (default)."""

import sys, os, re, glob, difflib

# ── ANSI colors ───────────────────────────────────────────────────────────────
CYAN  = "\033[96m"
GREEN = "\033[92m"
RED   = "\033[91m"
RESET = "\033[0m"

# ── Paths ─────────────────────────────────────────────────────────────────────
REPO      = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
THEMES    = os.path.join(REPO, "src", "wui-js", "plugins", "bodytheme")
REFERENCE = "default"

def getSettingsPath(theme):
	files = glob.glob(os.path.join(THEMES, theme, "settings-*.css"))
	version = lambda path: [int(n) for n in re.findall(r"\d+", os.path.basename(path))]
	return max(files, key=version) if files else None

def getStructure(path, theme):
	"""
	Returns the structure of a settings file as a list of lines: block openings and closings,
	section comments and variable names. The theme selector is normalized to <theme>.
	"""
	items = []
	selector = re.compile(r"\.wuiplugin-bodytheme\." + re.escape(theme) + r"\b")
	content = re.sub(r"/\*.*?@file.*?\*/", "", open(path, encoding="utf-8").read(), count=1, flags=re.S)
	for line in content.splitlines():
		line = line.strip()
		if line == "":
			continue
		if line.endswith("{"):
			items.append(selector.sub(".wuiplugin-bodytheme.<theme>", line))
		elif line == "}":
			items.append("}")
		elif re.match(r"^/\*.*\*/$", line):
			items.append(line)
		else:
			m = re.match(r"^(--[\w-]+)\s*:", line)
			items.append(m.group(1) if m else "? " + line)
	return items

def main():
	args = [a for a in sys.argv[1:] if a.strip()]
	names = args[0].split(",") if args else sorted(
		d for d in os.listdir(THEMES) if d != REFERENCE and getSettingsPath(d)
	)
	refPath = getSettingsPath(REFERENCE)
	reference = getStructure(refPath, REFERENCE)
	fails = 0
	print(f"── reference {CYAN}{REFERENCE}{RESET} ({os.path.basename(refPath)}): {len(reference)} items ──\n")
	for name in names:
		path = getSettingsPath(name)
		if not path:
			print(f"  [{RED}fail{RESET}] {CYAN}{name}{RESET}: settings file not found")
			fails += 1
			continue
		items = getStructure(path, name)
		if items == reference:
			print(f"  [{GREEN}pass{RESET}] {CYAN}{name}{RESET} ({os.path.basename(path)})")
			continue
		fails += 1
		print(f"  [{RED}fail{RESET}] {CYAN}{name}{RESET} ({os.path.basename(path)}): structure differs from {REFERENCE}")
		diff = difflib.unified_diff(reference, items, REFERENCE, name, n=1, lineterm="")
		for line in list(diff)[2:]:
			print("         " + line)
	print(f"\n── {len(names)} theme(s) checked, {fails} fail(s) ──")
	sys.exit(1 if fails else 0)

if __name__ == "__main__":
	main()
