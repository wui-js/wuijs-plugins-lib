[English](wuiplugin-bodytheme-en.md) | [Español](wuiplugin-bodytheme-es.md)

[wuijs-plugins-lib](../../README-en.md)

# WUIPluginBodyTheme

Version: `0.16`

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
- `wui-tree`
- `wui-list`
- `wui-table`
- `wui-form`
- `wui-selectpicker`
- `wui-datepicker`
- `wui-timepicker`
- `wui-colorpicker`
- `wui-avatarpicker`
- `wui-switch`
- `wui-intensity`
- `wui-button`
- `wui-codebox`
- `wui-markdown`
- `wuiview-datalist` (views package): `--wuiview-datalist-header-button-width`, `--wuiview-datalist-header-button-height`, `--wuiview-datalist-mobile-header-button-width` and `--wuiview-datalist-mobile-header-button-height`

## Sources

| Type | File |
| ---- | ---- |
| CSS  | [src/wui-js/plugins/bodytheme/wuiplugin-bodytheme-0.16.css](https://github.com/wui-js/wuijs-plugins-lib/blob/main/src/wui-js/plugins/bodytheme/wuiplugin-bodytheme-0.16.css) |
| JS   | [src/wui-js/plugins/bodytheme/wuiplugin-bodytheme-0.16.js](https://github.com/wui-js/wuijs-plugins-lib/blob/main/src/wui-js/plugins/bodytheme/wuiplugin-bodytheme-0.16.js) |
| CSS  | [src/wui-js/plugins/bodytheme/default/settings-0.16.css](https://github.com/wui-js/wuijs-plugins-lib/blob/main/src/wui-js/plugins/bodytheme/default/settings-0.16.css) |
| CSS  | [src/wui-js/plugins/bodytheme/default/light-0.16.css](https://github.com/wui-js/wuijs-plugins-lib/blob/main/src/wui-js/plugins/bodytheme/default/light-0.16.css) |
| CSS  | [src/wui-js/plugins/bodytheme/default/dark-0.16.css](https://github.com/wui-js/wuijs-plugins-lib/blob/main/src/wui-js/plugins/bodytheme/default/dark-0.16.css) |
| CSS  | [src/wui-js/plugins/bodytheme/ntapple/settings-0.1.css](https://github.com/wui-js/wuijs-plugins-lib/blob/main/src/wui-js/plugins/bodytheme/ntapple/settings-0.1.css) |
| CSS  | [src/wui-js/plugins/bodytheme/ntapple/light-0.1.css](https://github.com/wui-js/wuijs-plugins-lib/blob/main/src/wui-js/plugins/bodytheme/ntapple/light-0.1.css) |
| CSS  | [src/wui-js/plugins/bodytheme/ntapple/dark-0.1.css](https://github.com/wui-js/wuijs-plugins-lib/blob/main/src/wui-js/plugins/bodytheme/ntapple/dark-0.1.css) |

## Dependencies

| Class     | Version | Description |
| --------- |:-------:| ----------- |
| `WUIBody` | `0.10`  | Base class extended by the plugin. Required. |

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
| `ntapple` | Theme inspired by Apple's interface guidelines (version `0.1`): system font, macOS (13px) and iOS (17px) type scale, neutral surfaces, a single blue accent, green for the activated state, translucent materials and increased contrast variants. Using it with `fieldMode: "auto"` in WUIForm is recommended, so that on desktop the label sits to the left of the field, as in iOS and macOS cells. Files in `src/wui-js/plugins/bodytheme/ntapple/` with the `-0.1` suffix. Form header and body buttons, and joined buttons (`join` of WUIButton), use a soft outline (`bordercolor-low`); on hover/focus, the text over `bgcolor-over` stays below 4.5:1 (4.43 light, 3.76 dark) as a transient state, like the `danger` button. |

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
| `--wuiplugin-bodytheme-bgcolor-page-(light\|dark)`            | Page (`<body>`) background color. |
| `--wuiplugin-bodytheme-bgcolor-overlay-(light\|dark)`         | Overlay background color. |
| `--wuiplugin-bodytheme-bgcolor-box-(light\|dark)`             | Dialog and panel background color. |
| `--wuiplugin-bodytheme-bgcolor-out-(light\|dark)`             | Background color in normal state. |
| `--wuiplugin-bodytheme-bgcolor-over-(light\|dark)`            | Background color in hover or selected state. |
| `--wuiplugin-bodytheme-bgcolor-fieldset-(light\|dark)`        | Background color of the `wui-form` field sets (`--wui-form-fieldset-bgcolor`). |
| `--wuiplugin-bodytheme-bgcolor-field-(light\|dark)`           | Background color of editable fields (`wui-form`, `wui-selectpicker`, `wui-datepicker`, `wui-timepicker`). |
| `--wuiplugin-bodytheme-bgcolor-scroll-(light\|dark)`          | Scrollbar color. |
| `--wuiplugin-bodytheme-bgcolor-icon-(light\|dark)`            | Icon fill color. |
| `--wuiplugin-bodytheme-bgcolor-highcontrast-(light\|dark)`    | High-contrast background color (tooltips, etc.). |
| `--wuiplugin-bodytheme-textcolor-title-(light\|dark)`         | Title text color. |
| `--wuiplugin-bodytheme-textcolor-active-(light\|dark)`        | Active state text color. |
| `--wuiplugin-bodytheme-textcolor-focus-(light\|dark)`         | Focused state text color. |
| `--wuiplugin-bodytheme-textcolor-onaccent-(light\|dark)`      | Text and icon color on the accent color (buttons, selections). |
| `--wuiplugin-bodytheme-textcolor-highlight-(light\|dark)`     | Text color of the `wui-form` highlighted message (`--wui-form-message-highlight-textcolor`). |
| `--wuiplugin-bodytheme-utilitycolor-highlight-(light\|dark)`  | Main highlight color (links, buttons, selections, activated `wui-switch`). |
| `--wuiplugin-bodytheme-utilitycolor-success-(light\|dark)`    | Success semantic color. |
| `--wuiplugin-bodytheme-utilitycolor-warning-(light\|dark)`    | Warning semantic color. |
| `--wuiplugin-bodytheme-utilitycolor-danger-(light\|dark)`     | Danger or error semantic color (`danger` button, invalid field, `wui-menubar` bubble). |
| `--wuiplugin-bodytheme-utilitycolor-info-(light\|dark)`       | Information semantic color. |
| `--wuiplugin-bodytheme-utilitycolor-disabled-(light\|dark)`   | Disabled element color. |
| `--wuiplugin-bodytheme-intensitycolor-low-(light\|dark)`      | Low intensity color. |
| `--wuiplugin-bodytheme-intensitycolor-half-(light\|dark)`     | Medium intensity color. |
| `--wuiplugin-bodytheme-intensitycolor-high-(light\|dark)`     | High intensity color. |
| `--wuiplugin-bodytheme-code-{name}-(light\|dark)`             | `wui-codebox` syntax highlighting colors (`data-style="theme"`). `{name}`: `command`, `comment`, `string`, `keyword`, `number`, `tag`, `attr`, `selector`, `property`, `function`, `operator`, `variable`, `constant`, `decorator`, `type`, `builtin`, `color` or `regex`. |

**Typography and metrics (common, no color mode variant):**

| Variable                                      | Default value                           | Description |
| --------------------------------------------- | --------------------------------------- | ----------- |
| `--wuiplugin-bodytheme-borderradius-low`      | `10px`                                  | Low border radius. |
| `--wuiplugin-bodytheme-borderradius-half`     | `15px`                                  | Medium border radius. |
| `--wuiplugin-bodytheme-borderradius-high`     | `17px`                                  | High border radius. |
| `--wuiplugin-bodytheme-borderradius-round`    | `50%`                                   | Circular border radius. |
| `--wuiplugin-bodytheme-titlefont`             | `Arial, Helvetica, Verdana, sans-serif` | Font family for titles. |
| `--wuiplugin-bodytheme-textfont`              | `Arial, Helvetica, Verdana, sans-serif` | Font family for the page text. |
| `--wuiplugin-bodytheme-textweight`            | `200`                                   | Font weight of the page text. |
| `--wuiplugin-bodytheme-textsize-xsmall`       | `10px`                                  | Text size scale step. |
| `--wuiplugin-bodytheme-textsize-small`        | `12px`                                  | Text size scale step. |
| `--wuiplugin-bodytheme-textsize-medium`       | `13px`                                  | Text size scale step. |
| `--wuiplugin-bodytheme-textsize-normal`       | `14px`                                  | Text size scale step. |
| `--wuiplugin-bodytheme-textsize-large`        | `15px`                                  | Text size scale step. |
| `--wuiplugin-bodytheme-textsize-xlarge`       | `17px`                                  | Text size scale step. |
| `--wuiplugin-bodytheme-textsize-xxlarge`      | `20px`                                  | Text size scale step. |
| `--wuiplugin-bodytheme-input-opener-iconsize` | `30px`                                  | Opener icon size for form fields. |
| `--wuiplugin-bodytheme-transition-delay`      | `0.4s`                                  | Color scheme transition duration. |
| `--wuiplugin-bodytheme-box-filter`            | `blur(10px)`                            | Backdrop filter (`backdrop-filter`) of the floating boxes: modal and pickers. |

> [!NOTE]
> The plugin maps each component text size variable (`--wui-*-textsize`) to a step of the `--wuiplugin-bodytheme-textsize-*` scale.

## Configuration file structure

Every theme shares the same configuration file structure: the same blocks, in the same order, with the same variables; only the values change.

| Block                                           | Content |
| ----------------------------------------------- | ------- |
| `.wuiplugin-bodytheme.{theme}`                  | Theme tokens (`global`, `common`, `light mode` and `dark mode` sections) and the `components` section with the theme-dependent component variables. |
| `@media (prefers-contrast: more)`               | Increased contrast variants of the gray, border, active text and accent tokens (and success in dark mode). |
| `@media (prefers-reduced-transparency: reduce)` | Background and filter of the `wui-menubar` mobile bar. |

The plugin file declares every component variable (those of each `.root.css` in main, views, lab, data and plugins), with the `default` theme values as the base. The `components` section of each theme redefines them with its own values; the `.wuiplugin-bodytheme.{theme}` selector is more specific than `.wuiplugin-bodytheme`, so the theme value wins regardless of load order. The wuijs-main-lib `tests/css-root-check.py` script verifies that the plugin declares every `.root.css` variable and no nonexistent one.

| Component        | Variable                                       | `default` | `ntapple` |
| ---------------- | ---------------------------------------------- | --------- | --------- |
| `wui-modal`      | `--wui-modal-box-shadow`                       | `rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px` | `rgb(from var(--wuiplugin-bodytheme-shadowcolor-low) r g b / 10%) 0px 4px 12px` |
| `wui-modal`      | `--wui-modal-box-bordercolor`                  | `var(--wuiplugin-bodytheme-bordercolor-high)` | `rgb(from var(--wuiplugin-bodytheme-bordercolor-high) r g b / 20%)` |
| `wui-modal`      | `--wui-modal-footer-justify`                   | `center` | `flex-end` |
| `wui-modal`      | `--wui-modal-footer-horizontalmargin`          | `5px` | `20px` |
| `wui-menubar`    | `--wui-menubar-shadow`                         | `rgb(from var(--wuiplugin-bodytheme-shadowcolor-low) r g b / 40%) 0px 4px 12px` | `rgb(from var(--wuiplugin-bodytheme-shadowcolor-low) r g b / 10%) 0px 4px 12px` |
| `wui-menubar`    | `--wui-menubar-bar-bordercolor`                | `var(--wuiplugin-bodytheme-bordercolor-high)` | `rgb(from var(--wuiplugin-bodytheme-bordercolor-high) r g b / 20%)` |
| `wui-menubar`    | `--wui-menubar-mobile-bar-height`              | `50px` | `46px` |
| `wui-menubar`    | `--wui-menubar-mobile-bar-bgcolor-top`         | `var(--wuiplugin-bodytheme-bordercolor-low)` | `rgb(from var(--wuiplugin-bodytheme-bgcolor-out) r g b / 72%)` |
| `wui-menubar`    | `--wui-menubar-mobile-bar-bgcolor-bottom`      | `var(--wuiplugin-bodytheme-bordercolor-low)` | `rgb(from var(--wuiplugin-bodytheme-bgcolor-out) r g b / 72%)` |
| `wui-menubar`    | `--wui-menubar-mobile-bar-borderradius`        | `var(--wuiplugin-bodytheme-borderradius-low)` | `9999px` |
| `wui-menubar`    | `--wui-menubar-mobile-bar-button-width`        | `36px` | `62px` |
| `wui-menubar`    | `--wui-menubar-mobile-bar-button-borderradius` | `9999px` | `9999px` |
| `wui-menubar`    | `--wui-menubar-mobile-bar-filter`              | `none` | `var(--wuiplugin-bodytheme-box-filter)` |
| `wui-list`       | `--wui-list-shadow`                            | `rgb(from var(--wuiplugin-bodytheme-shadowcolor-low) r g b / 40%) 0px 4px 12px` | `rgb(from var(--wuiplugin-bodytheme-shadowcolor-low) r g b / 10%) 0px 4px 12px` |
| `wui-table`      | `--wui-table-shadow`                           | `rgb(from var(--wuiplugin-bodytheme-shadowcolor-low) r g b / 40%) 0px 4px 12px` | `rgb(from var(--wuiplugin-bodytheme-shadowcolor-low) r g b / 10%) 0px 4px 12px` |
| `wui-form`       | `--wui-form-legend-texttransform`              | `none` | `none` |
| `wui-form`       | `--wui-form-button-bordercolor-out`            | `var(--wui-button-default-bordercolor-out)` | `var(--wuiplugin-bodytheme-bordercolor-low)` |
| `wui-form`       | `--wui-form-button-bordercolor-disabled`       | `var(--wui-button-default-bordercolor-disabled)` | `var(--wuiplugin-bodytheme-bordercolor-low)` |
| `wui-form`       | `--wui-form-button-bordercolor-submit-out`     | `var(--wui-button-submit-bordercolor-out)` | `var(--wuiplugin-bodytheme-bordercolor-low)` |
| `wui-form`       | `--wui-form-button-bordercolor-danger-out`     | `var(--wui-button-danger-bordercolor-out)` | `var(--wuiplugin-bodytheme-bordercolor-low)` |
| `wui-form`       | `--wui-form-button-bordercolor-danger-over`    | `var(--wui-button-danger-bordercolor-over)` | `var(--wuiplugin-bodytheme-utilitycolor-danger)` |
| `wui-form`       | `--wui-form-button-bgcolor-out`                | `var(--wui-button-default-bgcolor-out)` | `var(--wuiplugin-bodytheme-bgcolor-field)` |
| `wui-form`       | `--wui-form-button-bgcolor-over`               | `var(--wui-button-default-bgcolor-over)` | `var(--wuiplugin-bodytheme-bgcolor-over)` |
| `wui-form`       | `--wui-form-mobile-textsize`                   | `max(16px, var(--wuiplugin-bodytheme-textsize-large))` | `var(--wuiplugin-bodytheme-textsize-xlarge)` |
| `wui-form`       | `--wui-form-mobile-input-height`               | `32px` | `44px` |
| `wui-datepicker` | `--wui-datepicker-box-month-titlecolor`        | `var(--wuiplugin-bodytheme-graycolor-half)` | `var(--wuiplugin-bodytheme-graycolor-low)` |
| `wui-switch`     | `--wui-switch-bordercolor-activated`           | `var(--wuiplugin-bodytheme-utilitycolor-highlight)` | `var(--wuiplugin-bodytheme-utilitycolor-success)` |
| `wui-switch`     | `--wui-switch-bgcolor-activated`               | `var(--wuiplugin-bodytheme-utilitycolor-highlight)` | `var(--wuiplugin-bodytheme-utilitycolor-success)` |
| `wui-switch`     | `--wui-switch-button-bordercolor-activated`    | `var(--wuiplugin-bodytheme-utilitycolor-highlight)` | `var(--wuiplugin-bodytheme-utilitycolor-success)` |
| `wui-switch`     | `--wui-switch-button-bgcolor-out`              | `var(--wuiplugin-bodytheme-bgcolor-over)` | `#fff` |
| `wui-switch`     | `--wui-switch-button-bgcolor-activated`        | `var(--wuiplugin-bodytheme-bgcolor-over)` | `#fff` |
| `wui-button`     | `--wui-button-default-shadow`                  | `rgba(50, 50, 93, .25) 0px 13px 27px -5px, rgba(0, 0, 0, 0.3) 0px 8px 16px -8px` | `none` |
| `wui-button`     | `--wui-button-danger-bordercolor-out`          | `rgb(from var(--wuiplugin-bodytheme-utilitycolor-danger) r g b / 25%)` | `transparent` |
| `wui-button`     | `--wui-button-danger-bordercolor-over`         | `var(--wuiplugin-bodytheme-utilitycolor-danger)` | `transparent` |
| `wui-button`     | `--wui-button-danger-bgcolor-out`              | `var(--wuiplugin-bodytheme-utilitycolor-danger)` | `var(--wuiplugin-bodytheme-bgcolor-field)` |
| `wui-button`     | `--wui-button-danger-bgcolor-over`             | `var(--wuiplugin-bodytheme-utilitycolor-danger)` | `var(--wuiplugin-bodytheme-bgcolor-field)` |
| `wui-button`     | `--wui-button-danger-textcolor-out`            | `var(--wuiplugin-bodytheme-textcolor-onaccent)` | `var(--wuiplugin-bodytheme-utilitycolor-danger)` |
| `wui-button`     | `--wui-button-danger-textcolor-over`           | `var(--wuiplugin-bodytheme-textcolor-onaccent)` | `rgb(from var(--wuiplugin-bodytheme-utilitycolor-danger) r g b / 75%)` |
| `wui-button`     | `--wui-button-join-bordercolor-out`            | `var(--wui-button-default-bordercolor-out)` | `var(--wuiplugin-bodytheme-bordercolor-low)` |
| `wui-button`     | `--wui-button-join-bordercolor-disabled`       | `var(--wui-button-default-bordercolor-disabled)` | `var(--wuiplugin-bodytheme-bordercolor-low)` |
| `wui-button`     | `--wui-button-join-bordercolor-submit-out`     | `var(--wui-button-submit-bordercolor-out)` | `var(--wuiplugin-bodytheme-bordercolor-low)` |
| `wui-button`     | `--wui-button-join-bordercolor-danger-out`     | `var(--wui-button-danger-bordercolor-out)` | `var(--wuiplugin-bodytheme-bordercolor-low)` |
| `wui-button`     | `--wui-button-join-bordercolor-danger-over`    | `var(--wui-button-danger-bordercolor-over)` | `var(--wuiplugin-bodytheme-utilitycolor-danger)` |
| `wui-button`     | `--wui-button-join-bgcolor-out`                | `var(--wui-button-default-bgcolor-out)` | `var(--wuiplugin-bodytheme-bgcolor-field)` |
| `wui-button`     | `--wui-button-join-bgcolor-over`               | `var(--wui-button-default-bgcolor-over)` | `var(--wuiplugin-bodytheme-bgcolor-over)` |
| `wui-button`     | `--wui-button-join-bgcolor-selected`           | `var(--wui-button-default-bgcolor-selected)` | `var(--wuiplugin-bodytheme-utilitycolor-highlight)` |
| `wui-button`     | `--wui-button-join-bgcolor-disabled`           | `var(--wui-button-default-bgcolor-disabled)` | `var(--wuiplugin-bodytheme-bgcolor-field)` |
| `wui-button`     | `--wui-button-join-separatorcolor-out`         | `var(--wui-button-default-bordercolor-out)` | `var(--wui-button-default-bordercolor-out)` |
| `wui-button`     | `--wui-button-join-separatorcolor-over`        | `var(--wui-button-default-bordercolor-over)` | `var(--wui-button-default-bordercolor-over)` |
| `wui-button`     | `--wui-button-join-separatorcolor-selected`    | `var(--wui-button-default-bordercolor-selected)` | `var(--wui-button-default-bordercolor-selected)` |
| `wui-button`     | `--wui-button-join-separatorcolor-disabled`    | `var(--wui-button-default-bordercolor-disabled)` | `var(--wui-button-default-bordercolor-disabled)` |
| `wui-button`     | `--wui-button-mobile-default-height`           | `40px` | `44px` |
| `wui-button`     | `--wui-button-mobile-submit-height`            | `40px` | `44px` |

> [!NOTE]
> The `tests/settings-check.py` script compares the structure of each theme with the `default` theme and fails if the blocks, sections or the set or order of variables differ.

## Page font and background

The plugin applies `--wuiplugin-bodytheme-textfont` and `--wuiplugin-bodytheme-bgcolor-page` to the element with the `wuiplugin-bodytheme` class through the `:where(.wuiplugin-bodytheme)` selector, with zero specificity: any application rule on `body` takes precedence.

## Accessibility preferences

| Query                                           | Effect |
| ----------------------------------------------- | ------ |
| `@media (prefers-reduced-motion: reduce)`       | Removes the modal, paging, slider and color scheme transitions. |
| `@media (prefers-reduced-transparency: reduce)` | Removes the backdrop filter of the floating boxes and makes the `wui-timepicker` and `wui-colorpicker` boxes opaque. Each theme also defines, in its configuration file, the background and filter of the `wui-menubar` mobile bar. |
| `@media (prefers-contrast: more)`               | Defined by each theme in its configuration file (`default` and `ntapple`), with higher contrast variants of its colors. |

## Implementation

There are two implementation modes:

**Using generated CSS files**:

Use only the generated CSS files (`[light|dark]-{version}.css`) located in the theme directory (`src/wui-js/plugins/bodytheme/{name}/`).
Recommended if dynamic switching between light and dark modes is not required.

HTML head:

```html
<link type="text/css" rel="stylesheet" href="./libraries/wui-js/plugins/bodytheme/default/dark-0.16.css">
```

HTML code:

```html
<body class="wuiplugin-bodytheme default dark"></body>
```

**Using JS class instantiation:**

It requires the implementation of the JS class `WUIBody`, the plugin JS/CSS files `wuiplugin-bodytheme-0.16.{js,css}` and the theme settings CSS file `wui-js/plugins/bodytheme/{name}/settings-{version}.css`.
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
<link type="text/css" rel="stylesheet" href="./libraries/wui-js/main/switch/wui-switch-0.10.css">
<link type="text/css" rel="stylesheet" href="./libraries/wui-js/plugins/bodytheme/wuiplugin-bodytheme-0.16.css">
<link type="text/css" rel="stylesheet" href="./libraries/wui-js/plugins/bodytheme/default/settings-0.16.css">
<script type="text/javascript" src="./libraries/wui-js/main/body/wui-body-0.11.js"></script>
<script type="text/javascript" src="./libraries/wui-js/main/switch/wui-switch-0.10.js"></script>
<script type="text/javascript" src="./libraries/wui-js/plugins/bodytheme/wuiplugin-bodytheme-0.16.js"></script>
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

The `tools/bodytheme-clone.py` script creates a new theme by copying the configuration file of an existing theme: it replaces its CSS selector (also inside `@media` blocks), the `@file`, `@theme` and `@version` header fields and the `--wuiplugin-bodytheme-name` value. It is the recommended starting point before running `bodytheme-css-maker.py`.

```bash
python ./bodytheme-clone.py -n <new-theme-name>

python ./bodytheme-clone.py -d <themes-directory> -s <source-theme> -S <source-theme-version> -n <new-theme-name> -v <theme-version>
```

| Option                      | Default value                     | Description |
| --------------------------- | --------------------------------- | ----------- |
| `-d`,<br>`--directory`      | `../src/wui-js/plugins/bodytheme` | Themes base directory. |
| `-s`,<br>`--source`         | `default`                         | Name of the theme to clone. |
| `-S`,<br>`--source-version` | `0.16`                            | Version of the theme to clone. |
| `-n`,<br>`--name`           | _(required)_                      | Name of the new theme. |
| `-v`,<br>`--version`        | `0.1`                             | Version of the new theme. |

The output file is generated at `{directory}/{name}/settings-{version}.css` with the CSS selector, the header and the theme name updated, and with the same structure as the source theme. When editing it, change only the values; `tests/settings-check.py {name}` checks the structure.

## Theme Generation Tool

The `tools/bodytheme-css-maker.py` makes standardized CSS files by resolving all `var()` references in the source file, producing a flat CSS file for each color mode. It reads the variable configuration from `{directory}/{name}/settings-{version}.css`.

Each generated file includes the resolved theme tokens, the component variables (with the `--wui-*` overrides of the configuration file, resolving `light-dark()` by mode), the page font and background rule, the plugin accessibility preference `@media` blocks and the configuration file `@media` blocks, with only the values that change.

```bash
python ./bodytheme-css-maker.py

python ./bodytheme-css-maker.py -p <plugin-css-path> -d <themes-directory> -n <theme-name> -v <theme-version>
```

| Option                 | Default value                                                  | Description |
| ---------------------- | -------------------------------------------------------------- | ----------- |
| `-p`,<br>`--plugin`    | `../src/wui-js/plugins/bodytheme/wuiplugin-bodytheme-0.16.css` | Path to the bodytheme plugin CSS source file. |
| `-d`,<br>`--directory` | `../src/wui-js/plugins/bodytheme`                              | Themes base directory. |
| `-n`,<br>`--name`      | `default`                                                      | Theme name. |
| `-v`,<br>`--version`   | `0.16`                                                         | Theme version. |

Output files are generated in `{directory}/{name}/` with the names `light-{version}.css` and `dark-{version}.css`.

## Customizing predefined themes

```css
body.wuiplugin-bodytheme.default {
	--wuiplugin-bodytheme-utilitycolor-highlight-light: #e91e63;
    --wuiplugin-bodytheme-utilitycolor-highlight-dark: #f06292;
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
	--wuiplugin-bodytheme-textfont: Arial, Helvetica, Verdana, sans-serif;
	--wuiplugin-bodytheme-textweight: 200;
	--wuiplugin-bodytheme-textsize-xsmall: 10px;
	--wuiplugin-bodytheme-textsize-small: 12px;
	--wuiplugin-bodytheme-textsize-medium: 13px;
	--wuiplugin-bodytheme-textsize-normal: 14px;
	--wuiplugin-bodytheme-textsize-large: 15px;
	--wuiplugin-bodytheme-textsize-xlarge: 17px;
	--wuiplugin-bodytheme-textsize-xxlarge: 20px;
	--wuiplugin-bodytheme-input-opener-iconsize: 30px;
	--wuiplugin-bodytheme-transition-delay: .4s;
	--wuiplugin-bodytheme-box-filter: blur(10px);

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
	--wuiplugin-bodytheme-bgcolor-page-light: #f8fafb;
	--wuiplugin-bodytheme-bgcolor-overlay-light: #010203;
	--wuiplugin-bodytheme-bgcolor-box-light: #efeff6;
	--wuiplugin-bodytheme-bgcolor-out-light: #fdfdfe;
	--wuiplugin-bodytheme-bgcolor-over-light: #f6f6f6;
	--wuiplugin-bodytheme-bgcolor-fieldset-light: #fdfdfe;
	--wuiplugin-bodytheme-bgcolor-field-light: #f6f6f6;
	--wuiplugin-bodytheme-bgcolor-scroll-light: #353a40;
	--wuiplugin-bodytheme-bgcolor-icon-light: #353a40;
	--wuiplugin-bodytheme-bgcolor-highcontrast-light: #1f2429;
	--wuiplugin-bodytheme-textcolor-title-light: #000;
	--wuiplugin-bodytheme-textcolor-active-light: #2d3a47;
	--wuiplugin-bodytheme-textcolor-focus-light: #1f2937;
	--wuiplugin-bodytheme-textcolor-onaccent-light: #fff;
	--wuiplugin-bodytheme-textcolor-highlight-light: #fff;
	--wuiplugin-bodytheme-utilitycolor-highlight-light: #1e90ff;
	--wuiplugin-bodytheme-utilitycolor-success-light: #22c55e;
	--wuiplugin-bodytheme-utilitycolor-warning-light: #f59e0b;
	--wuiplugin-bodytheme-utilitycolor-danger-light: #ef4444;
	--wuiplugin-bodytheme-utilitycolor-info-light: #1e90ff;
	--wuiplugin-bodytheme-utilitycolor-disabled-light: #d5dce3;
	--wuiplugin-bodytheme-intensitycolor-low-light: mediumaquamarine;
	--wuiplugin-bodytheme-intensitycolor-half-light: darkorange;
	--wuiplugin-bodytheme-intensitycolor-high-light: orangered;
	--wuiplugin-bodytheme-code-command-light: #3e999f;
	--wuiplugin-bodytheme-code-comment-light: #8e908c;
	--wuiplugin-bodytheme-code-string-light: #718c00;
	--wuiplugin-bodytheme-code-keyword-light: #8959a8;
	--wuiplugin-bodytheme-code-number-light: #f5871f;
	--wuiplugin-bodytheme-code-tag-light: #c82829;
	--wuiplugin-bodytheme-code-attr-light: #3e999f;
	--wuiplugin-bodytheme-code-selector-light: #8959a8;
	--wuiplugin-bodytheme-code-property-light: #4271ae;
	--wuiplugin-bodytheme-code-function-light: #eab700;
	--wuiplugin-bodytheme-code-operator-light: #4d4d4c;
	--wuiplugin-bodytheme-code-variable-light: #4271ae;
	--wuiplugin-bodytheme-code-constant-light: #f5871f;
	--wuiplugin-bodytheme-code-decorator-light: #f5871f;
	--wuiplugin-bodytheme-code-type-light: #3e999f;
	--wuiplugin-bodytheme-code-builtin-light: #3e999f;
	--wuiplugin-bodytheme-code-color-light: #4271ae;
	--wuiplugin-bodytheme-code-regex-light: #3e999f;

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
	--wuiplugin-bodytheme-bgcolor-page-dark: #374151;
	--wuiplugin-bodytheme-bgcolor-overlay-dark: #000;
	--wuiplugin-bodytheme-bgcolor-box-dark: #2f3a48;
	--wuiplugin-bodytheme-bgcolor-out-dark: #1f2937;
	--wuiplugin-bodytheme-bgcolor-over-dark: #374151;
	--wuiplugin-bodytheme-bgcolor-fieldset-dark: #1f2937;
	--wuiplugin-bodytheme-bgcolor-field-dark: #374151;
	--wuiplugin-bodytheme-bgcolor-scroll-dark: #9fa8b6;
	--wuiplugin-bodytheme-bgcolor-icon-dark: #d1d5db;
	--wuiplugin-bodytheme-bgcolor-highcontrast-dark: #f9fafb;
	--wuiplugin-bodytheme-textcolor-title-dark: #fff;
	--wuiplugin-bodytheme-textcolor-active-dark: #f3f4f6;
	--wuiplugin-bodytheme-textcolor-focus-dark: #fff;
	--wuiplugin-bodytheme-textcolor-onaccent-dark: #000;
	--wuiplugin-bodytheme-textcolor-highlight-dark: #00000099;
	--wuiplugin-bodytheme-utilitycolor-highlight-dark: #1e90ff;
	--wuiplugin-bodytheme-utilitycolor-success-dark: #22c55e;
	--wuiplugin-bodytheme-utilitycolor-warning-dark: #f59e0b;
	--wuiplugin-bodytheme-utilitycolor-danger-dark: #f15757;
	--wuiplugin-bodytheme-utilitycolor-info-dark: #1e90ff;
	--wuiplugin-bodytheme-utilitycolor-disabled-dark: #4b5563;
	--wuiplugin-bodytheme-intensitycolor-low-dark: mediumaquamarine;
	--wuiplugin-bodytheme-intensitycolor-half-dark: darkorange;
	--wuiplugin-bodytheme-intensitycolor-high-dark: orangered;
	--wuiplugin-bodytheme-code-command-dark: #8abeb7;
	--wuiplugin-bodytheme-code-comment-dark: #969896;
	--wuiplugin-bodytheme-code-string-dark: #b5bd68;
	--wuiplugin-bodytheme-code-keyword-dark: #b294bb;
	--wuiplugin-bodytheme-code-number-dark: #de935f;
	--wuiplugin-bodytheme-code-tag-dark: #cc6666;
	--wuiplugin-bodytheme-code-attr-dark: #8abeb7;
	--wuiplugin-bodytheme-code-selector-dark: #b294bb;
	--wuiplugin-bodytheme-code-property-dark: #81a2be;
	--wuiplugin-bodytheme-code-function-dark: #f0c674;
	--wuiplugin-bodytheme-code-operator-dark: #c5c8c6;
	--wuiplugin-bodytheme-code-variable-dark: #81a2be;
	--wuiplugin-bodytheme-code-constant-dark: #de935f;
	--wuiplugin-bodytheme-code-decorator-dark: #de935f;
	--wuiplugin-bodytheme-code-type-dark: #8abeb7;
	--wuiplugin-bodytheme-code-builtin-dark: #8abeb7;
	--wuiplugin-bodytheme-code-color-dark: #81a2be;
	--wuiplugin-bodytheme-code-regex-dark: #8abeb7;

	/* components */

	--wui-modal-box-shadow: rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px;
	--wui-modal-box-bordercolor: var(--wuiplugin-bodytheme-bordercolor-high);
	--wui-modal-footer-justify: center;
	--wui-modal-footer-horizontalmargin: 5px;
	--wui-menubar-shadow: rgb(from var(--wuiplugin-bodytheme-shadowcolor-low) r g b / 40%) 0px 4px 12px;
	--wui-menubar-bar-bordercolor: var(--wuiplugin-bodytheme-bordercolor-high);
	--wui-menubar-mobile-bar-height: 50px;
	--wui-menubar-mobile-bar-bgcolor-top: var(--wuiplugin-bodytheme-bordercolor-low);
	--wui-menubar-mobile-bar-bgcolor-bottom: var(--wuiplugin-bodytheme-bordercolor-low);
	--wui-menubar-mobile-bar-borderradius: var(--wuiplugin-bodytheme-borderradius-low);
	--wui-menubar-mobile-bar-button-width: 36px;
	--wui-menubar-mobile-bar-button-borderradius: 9999px;
	--wui-menubar-mobile-bar-filter: none;
	--wui-list-shadow: rgb(from var(--wuiplugin-bodytheme-shadowcolor-low) r g b / 40%) 0px 4px 12px;
	--wui-table-shadow: rgb(from var(--wuiplugin-bodytheme-shadowcolor-low) r g b / 40%) 0px 4px 12px;
	--wui-form-legend-texttransform: none;
	--wui-form-button-bordercolor-out: var(--wui-button-default-bordercolor-out);
	--wui-form-button-bordercolor-disabled: var(--wui-button-default-bordercolor-disabled);
	--wui-form-button-bordercolor-submit-out: var(--wui-button-submit-bordercolor-out);
	--wui-form-button-bordercolor-danger-out: var(--wui-button-danger-bordercolor-out);
	--wui-form-button-bordercolor-danger-over: var(--wui-button-danger-bordercolor-over);
	--wui-form-button-bgcolor-out: var(--wui-button-default-bgcolor-out);
	--wui-form-button-bgcolor-over: var(--wui-button-default-bgcolor-over);
	--wui-form-mobile-textsize: max(16px, var(--wuiplugin-bodytheme-textsize-large));
	--wui-form-mobile-input-height: 32px;
	--wui-datepicker-box-month-titlecolor: var(--wuiplugin-bodytheme-graycolor-half);
	--wui-switch-bordercolor-activated: var(--wuiplugin-bodytheme-utilitycolor-highlight);
	--wui-switch-bgcolor-activated: var(--wuiplugin-bodytheme-utilitycolor-highlight);
	--wui-switch-button-bordercolor-activated: var(--wuiplugin-bodytheme-utilitycolor-highlight);
	--wui-switch-button-bgcolor-out: var(--wuiplugin-bodytheme-bgcolor-over);
	--wui-switch-button-bgcolor-activated: var(--wuiplugin-bodytheme-bgcolor-over);
	--wui-button-default-shadow: rgba(50, 50, 93, .25) 0px 13px 27px -5px, rgba(0, 0, 0, 0.3) 0px 8px 16px -8px;
	--wui-button-danger-bordercolor-out: rgb(from var(--wuiplugin-bodytheme-utilitycolor-danger) r g b / 25%);
	--wui-button-danger-bordercolor-over: var(--wuiplugin-bodytheme-utilitycolor-danger);
	--wui-button-danger-bgcolor-out: var(--wuiplugin-bodytheme-utilitycolor-danger);
	--wui-button-danger-bgcolor-over: var(--wuiplugin-bodytheme-utilitycolor-danger);
	--wui-button-danger-textcolor-out: var(--wuiplugin-bodytheme-textcolor-onaccent);
	--wui-button-danger-textcolor-over: var(--wuiplugin-bodytheme-textcolor-onaccent);
	--wui-button-join-bordercolor-out: var(--wui-button-default-bordercolor-out);
	--wui-button-join-bordercolor-disabled: var(--wui-button-default-bordercolor-disabled);
	--wui-button-join-bordercolor-submit-out: var(--wui-button-submit-bordercolor-out);
	--wui-button-join-bordercolor-danger-out: var(--wui-button-danger-bordercolor-out);
	--wui-button-join-bordercolor-danger-over: var(--wui-button-danger-bordercolor-over);
	--wui-button-join-bgcolor-out: var(--wui-button-default-bgcolor-out);
	--wui-button-join-bgcolor-over: var(--wui-button-default-bgcolor-over);
	--wui-button-join-bgcolor-selected: var(--wui-button-default-bgcolor-selected);
	--wui-button-join-bgcolor-disabled: var(--wui-button-default-bgcolor-disabled);
	--wui-button-join-separatorcolor-out: var(--wui-button-default-bordercolor-out);
	--wui-button-join-separatorcolor-over: var(--wui-button-default-bordercolor-over);
	--wui-button-join-separatorcolor-selected: var(--wui-button-default-bordercolor-selected);
	--wui-button-join-separatorcolor-disabled: var(--wui-button-default-bordercolor-disabled);
	--wui-button-mobile-default-height: 40px;
	--wui-button-mobile-submit-height: 40px;
}

@media (prefers-contrast: more) {

	.wuiplugin-bodytheme.default {

		/* light mode */

		--wuiplugin-bodytheme-graycolor-half-light: #6b6b6b;
		--wuiplugin-bodytheme-graycolor-low-light: #2b2b2b;
		--wuiplugin-bodytheme-bordercolor-max-light: #6b7680;
		--wuiplugin-bodytheme-bordercolor-high-light: #8a949e;
		--wuiplugin-bodytheme-bordercolor-low-light: #f0f0f3;
		--wuiplugin-bodytheme-textcolor-active-light: #141c24;
		--wuiplugin-bodytheme-utilitycolor-highlight-light: #0063d1;

		/* dark mode */

		--wuiplugin-bodytheme-graycolor-half-dark: #a8a8a8;
		--wuiplugin-bodytheme-graycolor-low-dark: #e6e6e6;
		--wuiplugin-bodytheme-bordercolor-max-dark: #8b95a3;
		--wuiplugin-bodytheme-bordercolor-high-dark: #6b7684;
		--wuiplugin-bodytheme-bordercolor-low-dark: #374151;
		--wuiplugin-bodytheme-textcolor-active-dark: #fff;
		--wuiplugin-bodytheme-utilitycolor-highlight-dark: #5aaeff;
		--wuiplugin-bodytheme-utilitycolor-success-dark: #4ade80;
	}
}

@media (prefers-reduced-transparency: reduce) {

	.wuiplugin-bodytheme.default {
		--wui-menubar-mobile-bar-bgcolor-top: var(--wuiplugin-bodytheme-bordercolor-low);
		--wui-menubar-mobile-bar-bgcolor-bottom: var(--wuiplugin-bodytheme-bordercolor-low);
		--wui-menubar-mobile-bar-filter: none;
	}
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
