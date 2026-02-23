# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**WUIJS Plugins Lib** is a vanilla JavaScript/CSS plugin library that extends WUIJS Lib classes. It has no build system, no package manager, and no transpilation — source files are the distributable files.

Current library version: `0.1.0`. Version numbering: first two sections = highest plugin version, third = general modification number.

## Development

There is no build step. Use **VS Code Live Server** on port `5501` for local development.

To regenerate pre-resolved theme CSS files after editing `WUIPluginThemes-X.X.css`:

```bash
# From the tools/ directory
python css-theme-maker.py

# Custom options
python css-theme-maker.py --css ../src/WUIPlugins/Themes/WUIPluginThemes-0.1.css -o ../src/WUIPlugins/Themes/ -t theme-1
```

This script reads the source theme CSS, resolves all `var()` references, and outputs flat `{basename}-{theme}-light.css` and `{basename}-{theme}-dark.css` files.

## Source Structure

```
src/WUIPlugins/
  Selector/
    WUIPluginSelector-{version}.js   # Plugin JS class
    WUIPluginSelector-{version}.css  # Plugin CSS
  Themes/
    WUIPluginThemes-{version}.css              # Master theme file (source of truth)
    WUIPluginThemes-{version}-{theme}-light.css  # Generated: resolved light values
    WUIPluginThemes-{version}-{theme}-dark.css   # Generated: resolved dark values
    WUIPluginThemes-{version}.js               # Theme controller class
tools/
  css-theme-maker.py   # Generates resolved theme CSS files
```

## Architecture

### Plugin Pattern

Each plugin is a single `.js` file containing one ES6 class that **extends a WUIJS Lib base class** (e.g., `WUIPluginSelector extends WUIModal`). The library itself (WUIJS Lib) is a peer dependency, not included here.

Plugins follow this pattern:
- `static version` property on the class
- `static #defaults` object defining all configurable properties with defaults
- Private `#properties` object backing all public getters/setters (with type validation in setters)
- `#htmlElements` object holding DOM references
- `#buildHTML()` / `#loadHTML()` to create or reuse existing DOM structure
- `init()` sets up DOM and event handlers (calls `super.init()`)
- `open()` / `close()` / `destroy()` lifecycle methods (call `super` equivalents)

### Theming System (`WUIPluginThemes`)

The CSS theming architecture has two layers:

1. **Primitive variables** (`--wuiplugin-theme-*`): Defined per theme (`.wuiplugin-themes:is(.theme-1, .theme-default)`) with `-light`/`-dark` suffixes for mode variants, and unsuffixed for common values.

2. **Component variables** (`--wui-*` and `--wuiplugin-*`): Defined on `.wuiplugin-themes` using `var()` references to the primitives above. These are the variables consumed by WUIJS Lib components.

The `WUIPluginThemes` JS class handles scheme switching by toggling `.light`, `.dark`, or `.system` classes on `document.body` and setting `document.documentElement.style.colorScheme`. The `.system` class uses CSS `light-dark()` for native OS color scheme detection.

Adding `.transition` class (done automatically during scheme switch) enables smooth background-color transitions via `--wuiplugin-theme-transition-delay`.

### File Naming Convention

New plugins should follow: `WUIPlugin{Name}-{major}.{minor}.js` and corresponding `.css`.

### CSS Variable Naming Convention

- `--wuiplugin-theme-*`: Primitive/semantic tokens in WUIPluginThemes
- `--wui-*`: Component-level tokens consumed by WUIJS Lib components
- `--wuiplugin-{plugin-name}-*`: Plugin-specific tokens (e.g., `--wuiplugin-selector-*`)

## Other Rules

- Always code in English.
- Always answer in Spanish.
- Use CamelCase as the naming convention for variables and functions in JavaScript and Python.
- Use SnakeCase as the naming convention for variables in CSS.
- Do not add comments to the code.
