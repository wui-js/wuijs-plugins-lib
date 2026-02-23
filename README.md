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
- `wuiplugin-selector`

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

#### Theme Generation Tool

The `tools/css-theme-maker.py` make standardized SVG files by resolving all `var()` references in the source file, producing a flat CSS file for each color mode.

```bash
python tools/css-theme-maker.py

python tools/css-theme-maker.py --css <css-path> -o <output-directory> -t <theme-name>
```

| Option             | Default value                                      | Description |
| ------------------ | -------------------------------------------------- | ----------- |
| `--css`            | `../src/WUIPlugins/Themes/WUIPluginThemes-0.1.css` | Path to the source CSS file. |
| `-o`,<br>`--out`   | `../src/WUIPlugins/Themes/`                        | Output directory for generated files. |
| `-t`,<br>`--theme` | `theme-1`                                          | Name of the theme to extract and resolve. |

Output files follow the pattern `{base-name}-{theme}-light.css` and `{base-name}-{theme}-dark.css`.

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

<a name="WUIPluginSelector"></a>

### WUIPluginSelector

Version: `0.2`

Modal list selector based on WUIModal.

#### Description

WUIPluginSelector extends `WUIModal` and implements a modal list selector.
It is optimized for mobile environments and intercepts touch events on native `<select>` elements to replace the system picker with a custom selection panel.
It can also be used programmatically, independently of a native input `<select>` in responsive environments.

#### Dependencies

| Class       | Version | Description |
| ----------- | :-----: | ----------- |
| `WUIModal`  | `0.2`   | Base modal class. Required. |
| `WUIButton` | `0.2`   | Used internally for the accept and cancel buttons. Required. |
| `WUIIcon`   | `0.1`   | Required for the selected option checkmark icon. |

#### Sources

| Type | File |
| ---- | ---- |
| CSS  | [src/WUIPlugins/Selector/WUIPluginSelector-0.2.css](https://github.com/wuijsproject/wuijs-plugins-lib/blob/main/src/WUIPlugins/Selector/WUIPluginSelector-0.2.css) |
| JS   | [src/WUIPlugins/Selector/WUIPluginSelector-0.2.js](https://github.com/wuijsproject/wuijs-plugins-lib/blob/main/src/WUIPlugins/Selector/WUIPluginSelector-0.2.js) |

#### Constructor

| Type              | Description |
| ----------------- | ----------- |
| WUIPluginSelector | `WUIPluginSelector([properties])`<br><br>Parameters:<br>**• properties:** `object` *optional* |

#### Class Properties

| Name    | Type     | Description |
| ------- | -------- | ----------- |
| version | `string` | Plugin version. |

#### Instance Properties

| Property        | Type             | Default value | Description |
| --------------- | ---------------- | ------------- | ----------- |
| value           | `string`         | `""`          | (get/set)<br>Current selected value. In multiple selection mode, values are joined with `separatorValue`. |
| options         | `array`          | `[]`          | (get/set)<br>Array of option objects. See structure in the implementation section. |
| multiple        | `boolean`        | `false`       | (get/set)<br>Indicates whether multiple selection is enabled. Affects how the linked `<select>` options are updated on accept. |
| separatorValue  | `string`         | `","`         | (get/set)<br>Separator used to join selected values in the `value` property and in the `values` parameter of the `acceptOnClick` callback. |
| separatorText   | `string`         | `", "`        | (get/set)<br>Separator used to join selected texts in the `texts` parameter of the `acceptOnClick` callback. |
| emptyText       | `string`         | `""`          | (get/set)<br>Fallback text for options with an empty `value`. |
| selecteableText | `boolean`        | `false`       | (get/set)<br>If `true`, allows the user to select and copy option text. Applies only to selected options. |
| acceptButton    | `WUIButton`      | `null`        | (get/set)<br>Accept button instance. Assigned automatically by `init()`. The setter only accepts `WUIButton` instances. |
| acceptVisible   | `boolean`        | `true`        | (get/set)<br>Indicates whether the accept button is visible. Reset to `true` when the selector closes. |
| acceptData      | `object`         | `{}`          | (get/set)<br>`data-*` attributes to apply to the accept button (e.g. `{ key: "buttons.accept" }` for WUILanguage). |
| acceptText      | `string`         | `""`          | (get/set)<br>Accept button label. |
| acceptOnClick   | `function\|null` | `null`        | (get/set)<br>Function executed when the accept button is pressed. Signature: `acceptOnClick(indexes, values, texts)`. Reset to `null` when the selector closes. |
| cancelButton    | `WUIButton`      | `null`        | (get/set)<br>Cancel button instance. Assigned automatically by `init()`. The setter only accepts `WUIButton` instances. |
| cancelVisible   | `boolean`        | `true`        | (get/set)<br>Indicates whether the cancel button is visible. Reset to `true` when the selector closes. |
| cancelData      | `object`         | `{}`          | (get/set)<br>`data-*` attributes to apply to the cancel button. |
| cancelText      | `string`         | `""`          | (get/set)<br>Cancel button label. |
| cancelOnClick   | `function\|null` | `null`        | (get/set)<br>Function executed when the cancel button is pressed. Reset to `null` when the selector closes. |
| onSelect        | `function\|null` | `null`        | (get/set)<br>Function executed when an option is tapped. Signature: `onSelect(value, index)`. Reset to `null` when the selector closes. |

All `WUIModal` properties (`selector`, `openDelay`, `onStartOpen`, `onOpen`, `onScrolling`, `onStartClose`, `onClose`, etc.) are also inherited.

#### Methods

| Method       | Return type | Description |
| ------------ | ----------- | ----------- |
| init         | `void`      | `init()`<br><br>Builds the internal HTML structure of the selector if it does not exist (or loads it if already present in the DOM), initializes the base modal, and instantiates the accept and cancel buttons. |
| prepareInput | `void`      | `prepareInput(input[, options])`<br><br>Links the selector to a native `<select>` element to replace its behavior on mobile screens. Parameters:<br>**• input:** `HTMLSelectElement`. The element to link.<br>**• options:** `object` *optional*. Configuration options:<br>&nbsp;&nbsp;&nbsp;**- emptyText:** `string` *(default: `this.emptyText`)* – Text for empty-value options.<br>&nbsp;&nbsp;&nbsp;**- direction:** `"ltr"\|"rtl"` *(default: `"ltr"`)* – Text direction attribute for the input.<br>&nbsp;&nbsp;&nbsp;**- force:** `boolean` *(default: `false`)* – If `true`, activates the selector on all screen sizes, not only mobile (≤767px).<br><br>On open, automatically populates `this.options` from the `<select>` `<option>` elements and sets the current selection. On accept, updates the `<select>` value and dispatches its `change` event. |
| open         | `void`      | `open()`<br><br>Opens the selector. Renders the option list from `this.options` and scrolls to the first selected option. Shows or hides buttons based on `acceptVisible` and `cancelVisible`. |
| close        | `void`      | `close()`<br><br>Closes the selector and restores the linked `<select>` options if one exists. Resets `acceptVisible`, `cancelVisible`, `acceptOnClick`, `cancelOnClick`, `onOpen`, `onClose`, and `onSelect` to their default values, and unlinks the input. |
| destroy      | `void`      | `destroy()`<br><br>Destructor. Removes all internal HTML elements and releases the object's properties. |

The `WUIModal` instance methods (`getElement()`, `getBox()`, `getFooter()`, `getStatus()`, `isOpen()`, `responsive()`) are also available.

#### CSS Classes

| Class                | Element      | Description |
| -------------------- | ------------ | ----------- |
| `wuiplugin-selector` | `.wui-modal` | Main plugin class. Identifies the component. |
| `mobile`             | `.wui-modal` | Activates the mobile-style modal presentation in WUIModal. Added automatically by `init()`. |
| `priority`           | `.wui-modal` | Assigns stack priority (z-index) to the modal. Added automatically by `init()`. |

#### CSS Variables

| Variable                                         | Description |
| ------------------------------------------------ | ----------- |
| `--wuiplugin-selector-box-width`                 | Width of the selector box. |
| `--wuiplugin-selector-box-bgcolor`               | Background color of the selector box. |
| `--wuiplugin-selector-option-bordercolor-out`    | Option border color in normal state. |
| `--wuiplugin-selector-option-bordercolor-over`   | Option border color in hover state. |
| `--wuiplugin-selector-option-bgcolor-out`        | Option background color in normal state. |
| `--wuiplugin-selector-option-bgcolor-over`       | Option background color in hover state. |
| `--wuiplugin-selector-option-iconcolor-out`      | Option icon color in normal state. |
| `--wuiplugin-selector-option-iconcolor-over`     | Option icon color in hover state. |
| `--wuiplugin-selector-option-iconcolor-disabled` | Disabled option icon color. |
| `--wuiplugin-selector-option-textcolor-out`      | Option text color in normal state. |
| `--wuiplugin-selector-option-textcolor-over`     | Option text color in hover state. |
| `--wuiplugin-selector-option-textcolor-selected` | Selected option text color (only when `selecteableText = true`). |
| `--wuiplugin-selector-option-textcolor-disabled` | Disabled option text color. |
| `--wuiplugin-selector-button-bordercolor`        | Button footer border color in mobile mode. |

> [!NOTE]
> Default values for these variables are also supported by WUIPluginThemes. See the [WUIPluginThemes](#WUIPluginThemes) section.

#### HTML Structure

The container element must be a `<div>` with the class `wui-modal wuiplugin-selector`. The internal structure is built automatically by `init()`:

```html
<div class="wui-modal wuiplugin-selector mobile priority">
	<div class="box">
		<div class="options">
			<div class="option [selected] [disabled]">
				<div class="icon wui-icon check-line"></div>
				<div class="text [selecteable]">Option text</div>
			</div>
		</div>
		<div class="footer">
			<button class="wui-button cancel flat wui-language"></button>
			<button class="wui-button submit wui-language"></button>
		</div>
	</div>
</div>
```

#### Implementation

HTML head:

```html
<link type="text/css" rel="stylesheet" href="./Libraries/WUI/Icon/WUIIcon-0.1.css">
<link type="text/css" rel="stylesheet" href="./Libraries/WUI/Modal/WUIModal-0.2.css">
<link type="text/css" rel="stylesheet" href="./Libraries/WUI/Button/WUIButton-0.2.css">
<link type="text/css" rel="stylesheet" href="./Libraries/WUIPlugins/Selector/WUIPluginSelector-0.2.css">
<script type="text/javascript" src="./Libraries/WUI/Modal/WUIModal-0.2.js"></script>
<script type="text/javascript" src="./Libraries/WUI/Button/WUIButton-0.2.js"></script>
<script type="text/javascript" src="./Libraries/WUIPlugins/Selector/WUIPluginSelector-0.2.js"></script>
```

**Programmatic use:**

HTML code:

```html
<div class="wui-modal wuiplugin-selector my-selector"></div>
```

JS code:

```js
const init = () => {
	const selector = new WUIPluginSelector({
		selector: ".wui-modal.my-selector",
		acceptText: "Accept",
		cancelText: "Cancel"
	});
	selector.init();
	selector.options = [
		{ icon: null, text: "Option 1", value: "1", selected: false },
		{ icon: null, text: "Option 2", value: "2", selected: true },
		{ icon: null, text: "Option 3", value: "3", selected: false, enabled: false }
	];
	selector.acceptOnClick = (indexes, values, texts) => {
		console.log(values);
	};
	selector.open();
};

window.addEventListener("DOMContentLoaded", init);
```

**Linked to a native `<select>` (`prepareInput`):**

HTML code:

```html
<select class="my-select">
	<option value="">— Select —</option>
	<option value="1">Option 1</option>
	<option value="2">Option 2</option>
	<option value="3">Option 3</option>
</select>

<div class="wui-modal wuiplugin-selector my-selector"></div>
```

JS code:

```js
const init = () => {
	const selector = new WUIPluginSelector({
		selector: ".wui-modal.my-selector",
		acceptText: "Accept",
		cancelText: "Cancel",
		emptyText: "— Select —"
	});
	selector.init();
	selector.prepareInput(document.querySelector(".my-select"), {
		force: false
	});
};

window.addEventListener("DOMContentLoaded", init);
```

> [!NOTE]
> `prepareInput` intercepts the `<select>` only on mobile screens (≤767px) unless `force` is `true`. On desktop, the `<select>` retains its native behavior.
