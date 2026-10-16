[English](wuiplugin-bodytheme-en.md) | [Español](wuiplugin-bodytheme-es.md)

[wuijs-plugins-lib](../../README-en.md)

# WUIPluginBodyTheme

Version: `0.15`

Plugin for managing pre-designed themes and light and dark modes.

## Description

WUIPluginBodyTheme provides a theming system for web applications through two layers of CSS variables.
Unlike a standalone plugin class, it extends the `WUIBody` class from `wuijs-main-lib`: on load, it attaches a `theme` namespace to `WUIBody.prototype`, exposing `getScheme`, `getCurrentScheme`, `getTheme` and `setScheme` on any `WUIBody` instance as `body.theme.*`.

## Covered Components

WUIPluginBodyTheme provides theme support for the following WUI/JS Main Lib components:

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
- `wui-datepicker`
- `wui-timepicker`
- `wui-colorpicker`
- `wui-switch`
- `wui-intensity`
- `wui-button`
- `wui-codebox` (lab package)
- `wui-markdown` (lab package)
- `wui-tree` (lab package)

## Sources

| Type | File |
| ---- | ---- |
| CSS  | [src/wui-js/plugins/bodytheme/wuiplugin-bodytheme-0.15.css](https://github.com/wui-js/wuijs-plugins-lib/blob/main/src/wui-js/plugins/bodytheme/wuiplugin-bodytheme-0.15.css) |
| JS   | [src/wui-js/plugins/bodytheme/wuiplugin-bodytheme-0.15.js](https://github.com/wui-js/wuijs-plugins-lib/blob/main/src/wui-js/plugins/bodytheme/wuiplugin-bodytheme-0.15.js) |
| CSS  | [src/wui-js/plugins/bodytheme/default/settings-0.15.css](https://github.com/wui-js/wuijs-plugins-lib/blob/main/src/wui-js/plugins/bodytheme/default/settings-0.15.css) |
| CSS  | [src/wui-js/plugins/bodytheme/default/light-0.15.css](https://github.com/wui-js/wuijs-plugins-lib/blob/main/src/wui-js/plugins/bodytheme/default/light-0.15.css) |
| CSS  | [src/wui-js/plugins/bodytheme/default/dark-0.15.css](https://github.com/wui-js/wuijs-plugins-lib/blob/main/src/wui-js/plugins/bodytheme/default/dark-0.15.css) |

## Dependencies

| Class     | Version | Description |
| --------- |:-------:| ----------- |
| `WUIBody` | `0.5`   | Base class extended by the plugin. Required. |

## Constructor

It does not add a constructor; it extends the `WUIBody` prototype. Instantiate `WUIBody` directly (`new WUIBody([properties])`).

## Class Properties

| Name    | Type     | Description |
| ------- | -------- | ----------- |
| version | `string` | Plugin version. |

## Instance Properties

It does not have instance properties.

## Methods

`WUIBody.prototype.theme` is a read-only namespace getter. Its methods are called as `body.theme.*` on a `WUIBody` instance:

| Method           | Return type | Description |
| ---------------- | ----------- | ----------- |
| getScheme        | `string`    | `theme.getScheme()`<br><br>Returns the value of the CSS `color-scheme` property defined on the `<html>` element. Possible values: `"light"`, `"dark"`, `"light dark"`, `""`. |
| getCurrentScheme | `string`    | `theme.getCurrentScheme()`<br><br>Returns the operating system's preferred color scheme, regardless of the scheme configured in the application. Possible values: `"light"`, `"dark"`. |
| getTheme         | `string`    | `theme.getTheme()`<br><br>Returns the active theme name based on the CSS classes present on `document.body`. |
| setScheme        | `void`      | `theme.setScheme(scheme)`<br><br>Sets the application's color scheme. Updates the CSS classes on `document.body` and the `color-scheme` attribute on the `<html>` element. If the new scheme differs from the current one, automatically activates the background transition. The transition duration is controlled by the CSS variable `--wuiplugin-bodytheme-transition-delay` (default value: `0.4s`). Possible values: `"light"`, `"dark"`, `"light dark"`, `"system"`. |

## Predefined themes

| Name      | Description |
| --------- | ----------- |
| `default` | Default theme. |

## CSS Variables

The theme setting variables are defined in the file `src/wui-js/plugins/bodytheme/{theme-name}/{version}.css` and are organized in two suffix variants: `{variable}-light` for light mode and `{variable}-dark` for dark mode.
Values without a suffix are common to both modes.

**Colors (with variations by color mode):**

| Base variable                                                 | Description |
| ------------------------------------------------------------- | ----------- |
| `--wuiplugin-bodytheme-graycolor-max-(light\|dark)`           | Maximum gray (white in light, black in dark). |
| `--wuiplugin-bodytheme-graycolor-high-(light\|dark)`          | High gray. |
| `--wuiplugin-bodytheme-graycolor-half-(light\|dark)`          | Mid gray. |
| `--wuiplugin-bodytheme-graycolor-low-(light\|dark)`           | Low gray. |
| `--wuiplugin-bodytheme-graycolor-min-(light\|dark)`           | Minimum gray (black in light, white in dark). |
| `--wuiplugin-bodytheme-shadowcolor-high-(light\|dark)`        | Strong shadow color. |
| `--wuiplugin-bodytheme-shadowcolor-low-(light\|dark)`         | Soft shadow color. |
| `--wuiplugin-bodytheme-bordercolor-max-(light\|dark)`         | Maximum border color. |
| `--wuiplugin-bodytheme-bordercolor-high-(light\|dark)`        | High border color. |
| `--wuiplugin-bodytheme-bordercolor-low-(light\|dark)`         | Low border color. |
| `--wuiplugin-bodytheme-bgcolor-overlay-(light\|dark)`         | Overlay background color. |
| `--wuiplugin-bodytheme-bgcolor-box-(light\|dark)`             | Dialog and panel background color. |
| `--wuiplugin-bodytheme-bgcolor-out-(light\|dark)`             | Background color in normal state. |
| `--wuiplugin-bodytheme-bgcolor-over-(light\|dark)`            | Background color in hover or selected state. |
| `--wuiplugin-bodytheme-bgcolor-scroll-(light\|dark)`          | Scrollbar color. |
| `--wuiplugin-bodytheme-bgcolor-icon-(light\|dark)`            | Icon fill color. |
| `--wuiplugin-bodytheme-bgcolor-highcontrast-(light\|dark)`    | High-contrast background color (tooltips, etc.). |
| `--wuiplugin-bodytheme-textcolor-title-(light\|dark)`         | Title text color. |
| `--wuiplugin-bodytheme-textcolor-active-(light\|dark)`        | Active state text color. |
| `--wuiplugin-bodytheme-textcolor-focus-(light\|dark)`         | Focused state text color. |
| `--wuiplugin-bodytheme-utilitycolor-hightlight-(light\|dark)` | Primary accent color (links, buttons, selections). |
| `--wuiplugin-bodytheme-utilitycolor-warning-(light\|dark)`    | Warning or error color. |
| `--wuiplugin-bodytheme-utilitycolor-disabled-(light\|dark)`   | Disabled element color. |
| `--wuiplugin-bodytheme-intencitycolor-low-(light\|dark)`      | Low intensity color. |
| `--wuiplugin-bodytheme-intencitycolor-half-(light\|dark)`     | Medium intensity color. |
| `--wuiplugin-bodytheme-intencitycolor-high-(light\|dark)`     | High intensity color. |

**Typography and metrics (common, no color mode variant):**

| Variable                                      | Default value                           | Description |
| --------------------------------------------- | --------------------------------------- | ----------- |
| `--wuiplugin-bodytheme-borderradius-low`      | `10px`                                  | Low border radius. |
| `--wuiplugin-bodytheme-borderradius-half`     | `15px`                                  | Medium border radius. |
| `--wuiplugin-bodytheme-borderradius-high`     | `17px`                                  | High border radius. |
| `--wuiplugin-bodytheme-borderradius-round`    | `50%`                                   | Circular border radius. |
| `--wuiplugin-bodytheme-titlefont`             | `Arial, Helvetica, Verdana, sans-serif` | Font family for titles. |
| `--wuiplugin-bodytheme-input-opener-iconsize` | `30px`                                  | Opener icon size for form fields. |
| `--wuiplugin-bodytheme-transition-delay`      | `0.4s`                                  | Color scheme transition duration. |

## Implementation

There are two implementation modes:

**Using generated CSS files**:

Use only the generated CSS files (`[light|dark]-{version}.css`) located in the theme directory (`src/wui-js/plugins/bodytheme/{name}/`).
Recommended if dynamic switching between light and dark modes is not required.

HTML head:

```html
<link type="text/css" rel="stylesheet" href="./libraries/wui-js/plugins/bodytheme/default/dark-0.15.css">
```

HTML code:

```html
<body class="wuiplugin-bodytheme default dark"></body>
```

**Using JS class instantiation:**

It requires the implementation of the JS class `WUIBody`, the plugin JS/CSS files `wuiplugin-bodytheme-0.15.{js,css}` and the theme settings CSS file `wui-js/plugins/bodytheme/{name}/settings-{version}.css`.
Additionally, the viewer where it is displayed must support the CSS function `light-dark()` [https://www.w3schools.com/cssref/func_light-dark.php](https://www.w3schools.com/cssref/func_light-dark.php)

CSS code:

```css
html,
body {
	height: 100%;
	margin: 0;
	padding: 0;
}

nav {
	display: flex;
	margin: 10px;
	align-items: center;
	gap: 10px;
}
```

HTML head:

```html
<link type="text/css" rel="stylesheet" href="./libraries/wui-js/main/switch/wui-switch-0.7.css">
<link type="text/css" rel="stylesheet" href="./libraries/wui-js/plugins/bodytheme/wuiplugin-bodytheme-0.15.css">
<link type="text/css" rel="stylesheet" href="./libraries/wui-js/plugins/bodytheme/default/settings-0.15.css">
<script type="text/javascript" src="./libraries/wui-js/main/body/wui-body-0.5.js"></script>
<script type="text/javascript" src="./libraries/wui-js/main/switch/wui-switch-0.7.js"></script>
<script type="text/javascript" src="./libraries/wui-js/plugins/bodytheme/wuiplugin-bodytheme-0.15.js"></script>
```

> [!TIP]
> When using the plugin, it is not necessary to load the `.root.css` files of the components.

HTML code:

```html
<body class="wuiplugin-bodytheme default light">
	<nav>
		<div class="wui-switch my-switch">
			<input type="checkbox" name="mySwitch">
		</div>
	</nav>
</body>
```

JS code:

```js
const init = () => {
	const body = new WUIBody();
	const switchbox = new WUISwitch({
		selector: ".wui-switch.my-switch",
		value: "1",
		activated: false,
		onChange: (value, activated) => {
			body.theme.setScheme(activated ? "dark" : "light");
		}
	});
	switchbox.init();
}

window.addEventListener("DOMContentLoaded", init);
```

> [!TIP]
> You can check this working example at the link: [http://docs.wuijs.dev/pages/docs/home/?id=wuijs-demos-plugin-bodytheme-switchmode&lang=en](http://docs.wuijs.dev/pages/docs/home/?id=wuijs-demos-plugin-bodytheme-switchmode&lang=en).

## Theme Cloning Tool

The `tools/bodytheme-clone.py` script creates a new theme by copying the configuration file of an existing theme and replacing its CSS selector. It is the recommended starting point before running `bodytheme-css-maker.py`.

```bash
python ./bodytheme-clone.py -n <new-theme-name>

python ./bodytheme-clone.py -d <themes-directory> -s <source-theme> -n <new-theme-name> -v <theme-version>
```

| Option                 | Default value                                                  | Description |
| ---------------------- | -------------------------------------------------------------- | ----------- |
| `-p`,<br>`--plugin`    | `../src/wui-js/plugins/bodytheme/wuiplugin-bodytheme-0.15.css` | Path to the bodytheme plugin CSS source file. |
| `-d`,<br>`--directory` | `../src/wui-js/plugins/bodytheme`                              | Themes base directory. |
| `-s`,<br>`--source`    | `default`                                                      | Name of the theme to clone. |
| `-n`,<br>`--name`      | _(required)_                                                   | Name of the new theme. |
| `-v`,<br>`--version`   | `0.1`                                                          | Theme version. |

The output file is generated at `{directory}/{name}/settings-{version}.css` with the CSS selector updated to the new name.

## Theme Generation Tool

The `tools/bodytheme-css-maker.py` makes standardized CSS files by resolving all `var()` references in the source file, producing a flat CSS file for each color mode. It reads the variable configuration from `{directory}/{name}/settings-{version}.css`.

```bash
python ./bodytheme-css-maker.py

python ./bodytheme-css-maker.py -p <plugin-css-path> -d <themes-directory> -n <theme-name> -v <theme-version>
```

| Option                 | Default value                                                  | Description |
| ---------------------- | -------------------------------------------------------------- | ----------- |
| `-p`,<br>`--plugin`    | `../src/wui-js/plugins/bodytheme/wuiplugin-bodytheme-0.15.css` | Path to the bodytheme plugin CSS source file. |
| `-d`,<br>`--directory` | `../src/wui-js/plugins/bodytheme`                              | Themes base directory. |
| `-n`,<br>`--name`      | `default`                                                      | Theme name. |
| `-v`,<br>`--version`   | `0.12`                                                         | Theme version. |

Output files are generated in `{directory}/{name}/` with the names `light-{version}.css` and `dark-{version}.css`.

## Customizing predefined themes

```css
body.wuiplugin-bodytheme.default {
	--wuiplugin-bodytheme-utilitycolor-hightlight-light: #e91e63;
    --wuiplugin-bodytheme-utilitycolor-hightlight-dark: #f06292;
    --wuiplugin-bodytheme-bgcolor-out-light: #fff8f9;
    --wuiplugin-bodytheme-bgcolor-out-dark: #1a0a0d;
}
```

> [!IMPORTANT]
> For the changes to be applied, it is important to include the root element, in this case `<body>`, with the class `wuiplugin-bodytheme` and the theme name. This way, the definition will have greater specificity and will be applied to the definitions of the specified theme.

> [!TIP]
> To maintain the standard proposed by the WUI/JS library documentation, this customization can be done in the `WUI.css` file.

> [!TIP]
> You can check this working example at the link: [http://docs.wuijs.dev/pages/docs/home/?id=wuijs-demos-plugin-bodytheme-customtheme&lang=en](http://docs.wuijs.dev/pages/docs/home/?id=wuijs-demos-plugin-bodytheme-customtheme&lang=en).

## Customization of your own themes

**Step 1 — Clone an existing theme as a base:**

Run from the `tools/` directory:

```bash
python bodytheme-clone.py -n my-theme
```

This creates `src/wui-js/plugins/bodytheme/my-theme/settings-0.1.css` with the selector updated to `.wuiplugin-bodytheme.my-theme` and all variables from the `default` theme as a starting point.

**Step 2 — Edit the new theme variables:**

Modify `src/wui-js/plugins/bodytheme/my-theme/settings-0.1.css` with the desired values. The file structure is:

```css
.wuiplugin-bodytheme.my-theme {

	/* global */

	--wuiplugin-bodytheme-name: "my-theme";

	/* common */

	--wuiplugin-bodytheme-borderradius-low: 10px;
	--wuiplugin-bodytheme-borderradius-half: 15px;
	--wuiplugin-bodytheme-borderradius-high: 17px;
	--wuiplugin-bodytheme-borderradius-round: 50%;
	--wuiplugin-bodytheme-titlefont: Arial, Helvetica, Verdana, sans-serif;
	--wuiplugin-bodytheme-input-opener-iconsize: 30px;
	--wuiplugin-bodytheme-transition-delay: .4s;

	/* light mode */

	--wuiplugin-bodytheme-graycolor-max-light: #fff;
	--wuiplugin-bodytheme-graycolor-high-light: #ccc;
	--wuiplugin-bodytheme-graycolor-half-light: #888;
	--wuiplugin-bodytheme-graycolor-low-light: #444;
	--wuiplugin-bodytheme-graycolor-min-light: #000;
	--wuiplugin-bodytheme-shadowcolor-high-light: #304d63;
	--wuiplugin-bodytheme-shadowcolor-low-light: #959da5;
	--wuiplugin-bodytheme-bordercolor-max-light: #b5bbc1;
	--wuiplugin-bodytheme-bordercolor-high-light: #d5dce3;
	--wuiplugin-bodytheme-bordercolor-low-light: #f0f0f3;
	--wuiplugin-bodytheme-bgcolor-overlay-light: #010203;
	--wuiplugin-bodytheme-bgcolor-box-light: #efeff6;
	--wuiplugin-bodytheme-bgcolor-out-light: #fdfdfe;
	--wuiplugin-bodytheme-bgcolor-over-light: #f6f6f6;
	--wuiplugin-bodytheme-bgcolor-scroll-light: #353a40;
	--wuiplugin-bodytheme-bgcolor-icon-light: #353a40;
	--wuiplugin-bodytheme-bgcolor-highcontrast-light: #1f2429;
	--wuiplugin-bodytheme-textcolor-title-light: #000;
	--wuiplugin-bodytheme-textcolor-active-light: #2d3a47;
	--wuiplugin-bodytheme-textcolor-focus-light: #1f2937;
	--wuiplugin-bodytheme-utilitycolor-hightlight-light: #1e90ff;
	--wuiplugin-bodytheme-utilitycolor-warning-light: #f44343;
	--wuiplugin-bodytheme-utilitycolor-disabled-light: #d5dce3;
	--wuiplugin-bodytheme-intencitycolor-low-light: mediumaquamarine;
	--wuiplugin-bodytheme-intencitycolor-half-light: darkorange;
	--wuiplugin-bodytheme-intencitycolor-high-light: orangered;

	/* dark mode */

	--wuiplugin-bodytheme-graycolor-max-dark: #000;
	--wuiplugin-bodytheme-graycolor-high-dark: #444;
	--wuiplugin-bodytheme-graycolor-half-dark: #888;
	--wuiplugin-bodytheme-graycolor-low-dark: #ccc;
	--wuiplugin-bodytheme-graycolor-min-dark: #fff;
	--wuiplugin-bodytheme-shadowcolor-high-dark: #2f3a48;
	--wuiplugin-bodytheme-shadowcolor-low-dark: #1f2937;
	--wuiplugin-bodytheme-bordercolor-max-dark: #4b5563;
	--wuiplugin-bodytheme-bordercolor-high-dark: #4b5563;
	--wuiplugin-bodytheme-bordercolor-low-dark: #374151;
	--wuiplugin-bodytheme-bgcolor-overlay-dark: #000;
	--wuiplugin-bodytheme-bgcolor-box-dark: #2f3a48;
	--wuiplugin-bodytheme-bgcolor-out-dark: #1f2937;
	--wuiplugin-bodytheme-bgcolor-over-dark: #374151;
	--wuiplugin-bodytheme-bgcolor-scroll-dark: #9fa8b6;
	--wuiplugin-bodytheme-bgcolor-icon-dark: #d1d5db;
	--wuiplugin-bodytheme-bgcolor-highcontrast-dark: #f9fafb;
	--wuiplugin-bodytheme-textcolor-title-dark: #fff;
	--wuiplugin-bodytheme-textcolor-active-dark: #f3f4f6;
	--wuiplugin-bodytheme-textcolor-focus-dark: #fff;
	--wuiplugin-bodytheme-utilitycolor-hightlight-dark: #1e90ff;
	--wuiplugin-bodytheme-utilitycolor-warning-dark: #f44343;
	--wuiplugin-bodytheme-utilitycolor-disabled-dark: #4b5563;
	--wuiplugin-bodytheme-intencitycolor-low-dark: mediumaquamarine;
	--wuiplugin-bodytheme-intencitycolor-half-dark: darkorange;
	--wuiplugin-bodytheme-intencitycolor-high-dark: orangered;
}
```

**Step 3 — Activate the theme:**

For dynamic mode, activate the theme on the root element and include the configuration file in the HTML head:

```html
<body class="wuiplugin-bodytheme my-theme light">
```

```html
<link type="text/css" rel="stylesheet" href="./libraries/wui-js/plugins/bodytheme/my-theme/settings-0.1.css">
```

**Step 4 — Generate pre-compiled files (static mode):**

Run from the `tools/` directory:

```bash
python bodytheme-css-maker.py -n my-theme
```

The files `light-0.1.css` and `dark-0.1.css` are generated in `src/wui-js/plugins/bodytheme/my-theme/`.
