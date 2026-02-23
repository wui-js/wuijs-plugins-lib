> [!NOTE]
> Para la versión en español de este documento, consulte [LEEME.md](./LEEME.md).

# wuijs-plugins-lib

<div align="center">
	<img src="https://github.com/wuijsproject/wuijs-plugins-lib/blob/main/imgs/logo/wuijs-plugins-logotype-color.svg" width="220" height="220">
</div>

Library version: `0.1.0` ([Change Log](./CHANGELOG.md))

Document version: `0.1.0.20260223.0`

Licence: `Apache License 2.0`

Author: `Sergio E. Belmar V. <wuijs.project@gmail.com>`

> [!NOTE]
> The first two sections of the library version number correspond to the highest version of the classes that make up the library,
> while the third section corresponds to the modification number of the general version.

## Index

*   [Overview](#overview)
*   [Installation](#install)
*   [Plugins](#plugins)
	*   [WUIPluginThemes](#WUIPluginThemes)
	*   [WUIPluginSelector](#WUIPluginSelector)

<a name="overview"></a>

## Overview

WUIJS Plugins Lib is an open-source JavaScript/CSS library that provides a collection of plugins for WUIJS Lib classes, making it easier to quickly develop web applications.

### Table of Plugins

| Plugin Name                             | Version | Description |
| --------------------------------------- | -------:| ----------- |
| [WUIPluginThemes](#WUIPluginThemes)     | `0.1`   | Plugin for managing pre-designed themes and light and dark modes. |
| [WUIPluginSelector](#WUIPluginSelector) | `0.2`   | Modal selector based on WUIModal. |

### Directory Map

```bash
wuijs-lib/
├── imgs/
│   └── logo/
├── src/
│   └── WUI/
└── tools/
```

| Path                              | Description |
| --------------------------------- | ----------- |
| [imgs](imgs/)                     | Images used in the documentation. |
| [imgs/logo](imgs/logo/)           | Project logo and isotype in SVG and PNG format. |
| [src](src/)                       | Main sources of the latest version. |
| [src/WUIPlugins](src/WUIPlugins/) | WUI JS Plugins Library. |
| [tools](tools/)                   | Complementary tools. |

<a name="install"></a>

## Install

To install the WUIJS Plugins library, it must be cloned from the official GitHub repository (`wuijsproject/wuijs-plugins-lib`). Assuming the project where it will be deployed has a download directory: `./downloads`, a source directory `./src`, and within that, a libraries directory `./src/Libraries`, type the following in the terminal:

```bash
cd ./downloads
git clone https://git@github.com/wuijsproject/wuijs-plugins-lib.git
cp -r ./wuijs-plugins-lib/src/WUIPlugins ../src/Libraries/
```

Optionally, it can be downloaded from the same repository in ZIP format.

```bash
cd ./downloads
wget https://github.com/wuijsproject/wuijs-plugins-lib/archive/refs/heads/main.zip
unzip main.zip
cp -r ./wuijs-plugins-lib-main/src/WUIPlugins ../src/Libraries/
```

> [!TIP]
> It is recommended that the `/WUIPlugins` directory be located in the same directory as the main library `/WUI`.

<a name="plugins"></a>

## Plugins

<a name="WUIPluginThemes"></a>

### WUIPluginThemes

Version: `0.1`

Plugin for managing pre-designed themes and light and dark modes.

#### Description

WUIPluginThemes provides a theming system for web applications through two layers of CSS variables:

- **Primitives** (`--wuiplugin-theme-*`): color, typography, and spacing tokens with explicit light (`-light`) and dark (`-dark`) mode variants, plus common values without a mode suffix.
- **Components** (`--wui-*` and `--wuiplugin-*`): variables consumed by WUIJS Lib components, defined as references to the primitives via `var()`.

#### Covered Components

WUIPluginThemes provides theme support for the following WUIJS Lib components:

- `wui-scrolly`
- `wui-icon`
- `wui-loader`
- `wui-tooltip`
- `wui-modal`
- `wui-paging`
- `wui-slider`
- `wui-tabs`
- `wui-menubar`
- `wui-list`
- `wui-table`
- `wui-form`
- `wui-selectpicker`
- `wui-datepicker`
- `wui-timepicker`
- `wui-colorpicker`
- `wui-switch`
- `wui-intensity`
- `wui-button`

It also provides theme support for the `wuiplugin-selector` plugin.

#### Sources

| Type | File |
| ---- | ---- |
| CSS  | [src/WUIPlugins/Themes/WUIPluginThemes-0.1.css](https://github.com/wuijsproject/wuijs-plugins-lib/blob/main/src/WUIPlugins/Themes/WUIPluginThemes-0.1.css) |
| JS   | [src/WUIPlugins/Themes/WUIPluginThemes-0.1.js](https://github.com/wuijsproject/wuijs-plugins-lib/blob/main/src/WUIPlugins/Themes/WUIPluginThemes-0.1.js) |
| CSS  | [src/WUIPlugins/Themes/WUIPluginThemes-0.1-theme-1-light.css](https://github.com/wuijsproject/wuijs-plugins-lib/blob/main/src/WUIPlugins/Themes/WUIPluginThemes-0.1-theme-1-light.css) |
| CSS  | [src/WUIPlugins/Themes/WUIPluginThemes-0.1-theme-1-dark.css](https://github.com/wuijsproject/wuijs-plugins-lib/blob/main/src/WUIPlugins/Themes/WUIPluginThemes-0.1-theme-1-dark.css) |

#### Constructor

| Tipo            | Descripción |
| --------------- | ----------- |
| WUIPluginThemes | `WUIPluginThemes()` |

#### Class Properties

| Name    | Type     | Description |
| ------- | -------- | ----------- |
| version | `string` | Plugin version. |

#### Instance Properties

It does not have instance properties.

#### Methods

| Method           | Return type | Description |
| ---------------- | ----------- | ----------- |
| getScheme        | `string`    | `getScheme()`<br><br>Returns the value of the CSS `color-scheme` property defined on the `<html>` element. Possible values: `"light"`, `"dark"`, `"light dark"`, `""`. |
| getCurrentScheme | `string`    | `getCurrentScheme()`<br><br>Returns the operating system's preferred color scheme, regardless of the scheme configured in the application. Possible values: `"light"`, `"dark"`. |
| getTheme         | `string`    | `getTheme()`<br><br>Returns the active theme name based on the CSS classes present on `document.body`. Possible values: `"theme-1"`, `"theme-default"`, `""`. |
| setScheme        | `void`      | `setScheme(scheme)`<br><br>Sets the application's color scheme. Updates the CSS classes on `document.body` and the `color-scheme` attribute on the `<html>` element. If the new scheme differs from the current one, automatically activates the background transition. The transition duration is controlled by the CSS variable `--wuiplugin-theme-transition-delay` (default value: `0.4s`). Possible values: `"light"`, `"dark"`, `"light dark"`, `"system"`. |

#### CSS Classes

**Base class:**

| Class              | Description |
| ------------------ | ----------- |
| `wuiplugin-themes` | **Required.** Must be present on the root element. Activates the CSS variables for WUIJS Lib components. |

**Theme classes:**

| Class           | Description |
| --------------- | ----------- |
| `theme-1`       | Default theme. |
| `theme-default` | Alias for `theme-1`. |

**Color mode classes:**

| Class    | `color-scheme` | Description |
| -------- | -------------- | ----------- |
| `light`  | `light`        | Forces light mode. |
| `dark`   | `dark`         | Forces dark mode. |
| `system` | `light dark`   | Automatic mode via the CSS `light-dark()` function. Adapts to the operating system's preferred color scheme. |

> [!NOTE]
> The `system` mode requires browser support for the CSS `light-dark()` function (available in modern browsers since 2024).

**Transition class:**

| Class        | Description |
| ------------ | ----------- |
| `transition` | Activates the background transition during a scheme change. Added and removed automatically by `setScheme()`. Must not be used manually. |

#### CSS Variables

Primitive variables are defined with two suffix variants: `{variable}-light` for light mode and `{variable}-dark` for dark mode. Values without a suffix are common to both modes.

**Colors (with `-light` and `-dark` variants):**

| Base variable                               | Description |
| ------------------------------------------- | ----------- |
| `--wuiplugin-theme-graycolor-max`           | Maximum gray (white in light, black in dark). |
| `--wuiplugin-theme-graycolor-high`          | High gray. |
| `--wuiplugin-theme-graycolor-half`          | Mid gray. |
| `--wuiplugin-theme-graycolor-low`           | Low gray. |
| `--wuiplugin-theme-graycolor-min`           | Minimum gray (black in light, white in dark). |
| `--wuiplugin-theme-shadowcolor-high`        | Strong shadow color. |
| `--wuiplugin-theme-shadowcolor-low`         | Soft shadow color. |
| `--wuiplugin-theme-bordercolor-max`         | Maximum border color. |
| `--wuiplugin-theme-bordercolor-high`        | High border color. |
| `--wuiplugin-theme-bordercolor-low`         | Low border color. |
| `--wuiplugin-theme-bgcolor-overlay`         | Overlay background color. |
| `--wuiplugin-theme-bgcolor-box`             | Dialog and panel background color. |
| `--wuiplugin-theme-bgcolor-out`             | Background color in normal state. |
| `--wuiplugin-theme-bgcolor-over`            | Background color in hover or selected state. |
| `--wuiplugin-theme-bgcolor-scroll`          | Scrollbar color. |
| `--wuiplugin-theme-bgcolor-icon`            | Icon fill color. |
| `--wuiplugin-theme-bgcolor-highcontrast`    | High-contrast background color (tooltips, etc.). |
| `--wuiplugin-theme-textcolor-title`         | Title text color. |
| `--wuiplugin-theme-textcolor-active`        | Active state text color. |
| `--wuiplugin-theme-textcolor-focus`         | Focused state text color. |
| `--wuiplugin-theme-utilitycolor-hightlight` | Primary accent color (links, buttons, selections). |
| `--wuiplugin-theme-utilitycolor-warning`    | Warning or error color. |
| `--wuiplugin-theme-utilitycolor-disabled`   | Disabled element color. |
| `--wuiplugin-theme-intencitycolor-low`      | Low intensity color. |
| `--wuiplugin-theme-intencitycolor-half`     | Medium intensity color. |
| `--wuiplugin-theme-intencitycolor-high`     | High intensity color. |

**Typography and metrics (common, no mode variant):**

| Variable                                  | Default value                           | Description |
| ----------------------------------------- | --------------------------------------- | ----------- |
| `--wuiplugin-theme-borderradius-low`      | `10px`                                  | Low border radius. |
| `--wuiplugin-theme-borderradius-half`     | `15px`                                  | Medium border radius. |
| `--wuiplugin-theme-borderradius-high`     | `17px`                                  | High border radius. |
| `--wuiplugin-theme-borderradius-round`    | `50%`                                   | Circular border radius. |
| `--wuiplugin-theme-titlefont`             | `Arial, Helvetica, Verdana, sans-serif` | Font family for titles. |
| `--wuiplugin-theme-input-opener-iconsize` | `30px`                                  | Opener icon size for form fields. |
| `--wuiplugin-theme-transition-delay`      | `0.4s`                                  | Color scheme transition duration. |














#### Implementation

**Using the main source file:**

```html
<link rel="stylesheet" href="WUIPluginThemes-0.1.css">
<script src="WUIPluginThemes-0.1.js" defer></script>
```

**Using pre-generated files** (no `var()` chaining, better compatibility):

```html
<link rel="stylesheet" href="WUIPluginThemes-0.1-theme-1-light.css">
<link rel="stylesheet" href="WUIPluginThemes-0.1-theme-1-dark.css">
```

> [!NOTE]
> When using pre-generated files, both files can be loaded simultaneously. The active mode is determined by the CSS classes present on the root element.

#### Setup

Apply the `wuiplugin-themes` class to the root element of the application (usually `<body>`), along with the theme class and the initial color mode class:

```html
<body class="wuiplugin-themes theme-1 light">
```

#### Theme Customization

To create an additional theme, define a new CSS rule overriding the primitive variables you want to change:

```css
.wuiplugin-themes:is(.theme-2) {
    --wuiplugin-theme-utilitycolor-hightlight-light: #e91e63;
    --wuiplugin-theme-utilitycolor-hightlight-dark: #f06292;
    --wuiplugin-theme-bgcolor-out-light: #fff8f9;
    --wuiplugin-theme-bgcolor-out-dark: #1a0a0d;
}
```

Activate the new theme on the root element:

```html
<body class="wuiplugin-themes theme-2 light">
```

To generate the pre-generated CSS files for the new theme:

```bash
python tools/css-theme-maker.py -t theme-2
```

#### Theme Generation Tool

The `tools/css-theme-maker.py` script generates pre-generated CSS files by resolving all `var()` references in the source file, producing a flat CSS file for each color mode.

```bash
python tools/css-theme-maker.py

python tools/css-theme-maker.py --css <css-path> -o <output-directory> -t <theme-name>
```

| Option          | Default                                            | Description |
| --------------- | -------------------------------------------------- | ----------- |
| `--css`         | `../src/WUIPlugins/Themes/WUIPluginThemes-0.1.css` | Path to the source CSS file. |
| `-o`, `--out`   | `../src/WUIPlugins/Themes/`                        | Output directory for generated files. |
| `-t`, `--theme` | `theme-1`                                          | Name of the theme to extract and resolve. |

Output files follow the pattern `{base-name}-{theme}-light.css` and `{base-name}-{theme}-dark.css`.

<a name="WUIPluginSelector"></a>

### WUIPluginSelector

Version: `0.2`

Modal selector based on WUIModal.
