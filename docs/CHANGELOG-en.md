> [!IMPORTANT]
> The GitHub account `@wuiproject` was migrated to `@wui-js` to match the name with the NPM account.

[English](https://github.com/wui-js/wuijs-plugins-lib/blob/main/docs/CHANGELOG-en.md) |
[Español](https://github.com/wui-js/wuijs-plugins-lib/blob/main/docs/CHANGELOG-es.md)
---

# Change Log

## [v0.17.0] - 2026-11-07

Features:

1. Synced the version with `wuijs-main-lib` `0.17.0`.
2. Updated WUIPluginBodyTheme class version to `0.16`.
	- Updated `wuiplugin-themes-0.16.css` file with the updating of the CSS variable values ​​of the `WUIForm` component.
	- Added the `ntapple` `0.1` theme (`ntapple/settings-0.1.css`, `light-0.1.css` and `dark-0.1.css`), inspired by Apple's interface guidelines.
	- Added the `--wuiplugin-bodytheme-textfont`, `--wuiplugin-bodytheme-textsize-(xsmall|small|medium|normal|large|xlarge|xxlarge)` and `--wuiplugin-bodytheme-box-filter` tokens, and the per mode `--wuiplugin-bodytheme-bgcolor-page`, `--wuiplugin-bodytheme-textcolor-onaccent` and `--wuiplugin-bodytheme-utilitycolor-success` tokens.
	- Mapped the new component text size and backdrop filter variables to the `--wuiplugin-bodytheme-textsize-*` scale and the `--wuiplugin-bodytheme-box-filter` token, and `--wui-button-default-shadow`, `--wui-modal-transition-delay`, `--wui-slider-transition-delay`, `--wui-avatarpicker-preview-size`, `--wui-markdown-iframe-bgcolor` and `--wui-markdown-iframe-textcolor`.
	- Text and icons on the accent color (submit/danger and selected buttons, picker selections, WUIForm highlighted message, WUITable selected row and WUIMenubar selected options) use `--wuiplugin-bodytheme-textcolor-onaccent`. In the `default` theme, the WUITable selected row and the WUIMenubar selected options change color (`#fff` in light and `#000` in dark).
	- The WUISwitch activated state uses `--wuiplugin-bodytheme-utilitycolor-highlight`; the `ntapple` theme redefines it with `--wuiplugin-bodytheme-utilitycolor-success`.
	- Renamed the tokens `utilitycolor-hightlight` to `utilitycolor-highlight`, `utilitycolor-warning` to `utilitycolor-danger` and `intencitycolor-*` to `intensitycolor-*`, and the `--wui-button-warning-*` and `--wui-modal-button-warning-textcolor-mobile` mappings to `--wui-button-danger-*` and `--wui-modal-button-danger-textcolor-mobile`.
	- Added the semantic tokens `utilitycolor-warning` and `utilitycolor-info`, and the `bgcolor-field` token, which replaces `bgcolor-over` as the background of the WUIForm, WUISelectpicker, WUIDatepicker and WUITimepicker fields.
	- The text sizes of mobile editable controls (`--wui-form-mobile-textsize` and `--wui-(selectpicker|datepicker|timepicker)-mobile-viewinput-textsize`) have a 16px minimum, to avoid Safari on iOS zooming when they are focused.
	- The `default` theme defines `utilitycolor-success` as `#22c55e`, `utilitycolor-warning` as `#f59e0b` and `utilitycolor-info` as `#1e90ff`, and `utilitycolor-danger` changes from `#f44343` to `#ef4444`; `bgcolor-field` keeps the `bgcolor-over` value.
	- The `ntapple` theme uses the iOS grouped pattern: box background `#f2f2f7`/`#1c1c1e`, field sets `#fff`/`#2c2c2e` (elevated level in dark mode), fields `#e5e5ea`/`#38383a`, hover `#e5e5ea`/`#3a3a3c` and light page background `#f2f2f7`. `graycolor-low` changes to `#636366`/`#aeaeb2` and the WUIDatepicker month title uses `graycolor-low`, for a minimum 4.5:1 contrast.
	- Mapped the new `--wui-modal-footer-justify` and `--wui-button-default-borderradius` variables; in the `default` theme they reproduce the previous look.
	- The `ntapple` theme draws joined buttons (`join`) as a segmented control (field background, continuous outline and separators), the `danger` button as red text on the field background, lists and tables with a soft 10% shadow and the modal footer buttons aligned to the right on desktop. Using it with `fieldMode: "auto"` in WUIForm is recommended.
	- Mapped `--wui-list-shadow` and `--wui-table-shadow` (previously `--wui-list-shadowcolor` and `--wui-table-shadowcolor`) and the new WUIMenubar mobile variables, and `--wui-list-button-bgcolor-danger` to `--wuiplugin-bodytheme-utilitycolor-danger` (in `ntapple` the destructive row action stays a red fill with a white icon, like iOS swipe actions).
	- The `ntapple` theme draws the WUIMenubar mobile bar like the iOS floating tab bar: capsule, capsule buttons, 72% translucent background with the `--wuiplugin-bodytheme-box-filter` filter, and an opaque background without filter with `prefers-reduced-transparency`.
	- Fixed the `bodytheme-css-maker.py` tool: in the `@media` blocks of the settings file, component redefinitions were written twice.
	- Every theme shares the same configuration file structure (same blocks, sections and variables in the same order; only the values change). The 28 theme-dependent component variables (`components` section) are no longer assigned in `wuiplugin-bodytheme-0.16.css` and each theme declares them; the `default` theme does so with the previous values, with no visual change. The `default` theme adds the `@media (prefers-contrast: more)` block, with increased contrast variants of gray, border, active text, accent and success, and the `@media (prefers-reduced-transparency: reduce)` block. Added the `tests/settings-check.py` check, which compares the structure of each theme with `default`.
	- The `wuiview-datalist` variables (`--wuiview-datalist-header-button-width`, `--wuiview-datalist-header-button-height`, `--wuiview-datalist-mobile-header-button-width` and `--wuiview-datalist-mobile-header-button-height`) are assigned, for applications that do not load the `.root.css` files; `--wuiview-datalist-header-button-height` takes the value of `--wui-form-input-height`, to match the search field height. `--wui-form-input-height` changes from `30px` to `32px`, as in WUIForm. The `bodytheme-css-maker.py` tool keeps the `--wuiview-*` variables in the static files.
	- Mapped the normalized margin/padding names (`*-horizontalpadding`, `*-verticalpadding`) of `wui-button`, `wui-menubar`, `wui-selectpicker` and `wui-tree`, and the new `--wui-modal-footer-horizontalmargin` variable in the themes `components` section (`default` `5px`; `ntapple` `20px`, to keep right-aligned buttons off the edge on desktop). In `default`, `utilitycolor-danger-dark` changes from `#ef4444` to `#f15757` (3.06:1 contrast on the dark page background `#374151`, previously 2.74:1).
	- In the `ntapple` theme, the `join` group has a continuous outline in normal state: the border of enabled, `submit`, `danger` and disabled buttons, and the separators, use the soft `bordercolor-low` tone (`#e5e5ea` / `#38383a`), the same over the field and over the page (for example, the `wuiview-datalist` header). On hover/focus, the group's `danger` button keeps the outline with its accent color (`utilitycolor-danger`) and buttons without `submit` or `danger` style take the `bgcolor-over` background. The selected segment uses the accent color (`--wui-button-join-bgcolor-selected` = `utilitycolor-highlight`) and the disabled one keeps the field background (`--wui-button-join-bgcolor-disabled` = `bgcolor-field`), without leaving a gap in the group. In both themes, the separators of a selected segment take the selected border color (`--wui-button-join-separatorcolor-selected` = `--wui-button-default-bordercolor-selected`) and span the full height, so no light line shows next to the segment. Outside a group, `danger` still has no border. In `default`, each variant keeps its own border and background.
	- The `bodytheme-css-maker.py` tool resolves in two passes the overrides that reference other theme overrides.
	- Mapped `--wui-form-button-*` (WUIForm header and body button colors) and `--wui-button-join-*` (buttons joined with the WUIButton `join` property), which replace `--wui-form-joinbuttons-*`. In `default` they point to each WUIButton variant variable and reproduce the previous look; in `ntapple` they keep the joined-button values, which loose header and body form buttons now also take. `--wui-button-join-separator-verticalmargin` (`5px`) is assigned in the core.
	- The plugin file declares every component variable, including those that were previously only in each theme's `components` section (45: `wui-button`, `wui-form`, `wui-switch`, `wui-menubar`, `wui-modal`, `wui-table`, `wui-list` and `wui-datepicker`), with the `default` theme values as the base; each theme still redefines them. Added the `wui-tree`, `wui-avatarpicker`, `wui-markdown` and `wui-codebox` section comments. The wuijs-main-lib `tests/css-root-check.py` script verifies that the plugin declares every `.root.css` variable of main, views, lab, data and plugins, and no nonexistent one.
	- The `ntapple` theme keeps the `danger` button background on hover/focus (`--wui-button-danger-bgcolor-over` = `bgcolor-field`, same as at rest), without the gray hover.
	- In the `ntapple` theme, the `danger` button text and icon on hover/focus use the red at 75% (`--wui-button-danger-textcolor-over`), as a subtle cue without changing the background; contrast 4.16:1 light and 3.39:1 dark.
	- Renamed the `--wuiplugin-bodytheme-token-*` tokens to `--wuiplugin-bodytheme-code-*`. They are mapped to `--wui-codebox-code-*` and applied with the WUICodebox `data-style="theme"` style.
	- The page font and background are applied with the `:where(.wuiplugin-bodytheme)` selector, with zero specificity.
	- Added the `@media (prefers-reduced-motion: reduce)` and `@media (prefers-reduced-transparency: reduce)` blocks.
	- Removed 24 mappings of nonexistent variables: those of the `wuiplugin-selector` plugin and `--wui-selectpicker-box-button-*-(selected|disabled)`.
	- The `default` theme takes the `--wuiplugin-bodytheme-textfont` and `--wuiplugin-bodytheme-bgcolor-page` values from the reference application (SaaSKit) and keeps its colors.
	- The `ntapple` theme adds the macOS and iOS type scale, translucent materials, buttons without shadow, 17px fields on mobile, Xcode style syntax highlighting colors and a `@media (prefers-contrast: more)` block.
	- The static files (`light-*.css` and `dark-*.css`) include the resolved tokens, the theme component overrides, the page font and background rule and the `@media` blocks. Fixed bug: the header copied the whole configuration file into the generated file.
	- Fixed the `bodytheme-css-maker.py` tool (header, component overrides, page rule and `@media` blocks) and the `bodytheme-clone.py` tool (`.wuiplugin-bodytheme` selector, `--source-version` option, header and theme name).
	- Added the `--wuiplugin-bodytheme-textweight` (page font weight; `default` `200`, `ntapple` `300`), `--wuiplugin-bodytheme-bgcolor-fieldset-(light|dark)` (background of the WUIForm field sets) and `--wuiplugin-bodytheme-textcolor-highlight-(light|dark)` (text of the WUIForm highlighted message, which previously used `textcolor-onaccent`) tokens.
	- Mapped `--wui-modal-box-shadow`, `--wui-modal-box-bordercolor`, `--wui-menubar-shadow` (replaces `--wui-menubar-shadowcolor` and `--wui-menubar-shadowopacity`), `--wui-menubar-bar-bordercolor`, `--wui-menubar-mobile-bar-height`, `--wui-menubar-mobile-bar-button-width` and `--wui-form-legend-texttransform` in the `components` section of the themes, and in the plugin file `--wui-form-fieldset-bgcolor`, `--wui-form-fieldset-borderradius`, `--wui-form-message-shadow`, `--wui-menubar-mobile-bar-button-height`, `--wui-selectpicker-box-option-textsize` and `--wui-selectpicker-mobile-box-option-textsize`. In `default` they reproduce the component values, except `--wui-form-legend-texttransform` (`none`). In `ntapple`, the modal, the menu bar, lists and tables use a soft 10% shadow and a 20% border, and the WUIMenubar mobile bar is 46px high with 62px wide buttons.
	- The `ntapple` theme puts the `SanFrancisco` font before the system font stack in `titlefont` and `textfont`, and `utilitycolor-success-light` changes to `#34c759`.
	- The `wui-tree`, `wui-codebox` and `wui-markdown` blocks, graduated to `wuijs-main-lib` `0.17.0`, and the `wui-avatarpicker` block are no longer marked as lab package classes, in the plugin file, the static files and the covered components list.
	- Mapped the renamed mobile variables of WUIModal: `--wui-modal-mobile-button-submit-bgcolor`, `--wui-modal-mobile-button-submit-textcolor` and `--wui-modal-mobile-button-danger-textcolor`.
3. Updated WUIPluginFormValidation class version to `0.4`.
	- JS code normalized: the show/hide password icon is set with `classList.toggle()` from the final type of the field.
4. Updated WUIPluginFormHttp class version to `0.2`.
	- JS code normalized: `typeof` with parentheses.
	- Fixed bug: `submitJson()` sent only the last option of a `<select multiple>`, as a string. It now sends it as an array with all its selected options.

## [v0.16.1] - 2026-10-16

Features:

1. Synced the version with `wuijs-main-lib` `0.16.1`.
2. Updated the `WUIForm` documentation links to its class file in `wuijs-main-lib` (`docs/classes/form/wui-form-en.md`).

## [v0.16.0] - 2026-10-08

Features:

1. Synced the version with `wuijs-main-lib` `0.16.0`.
2. Updated WUIPluginBodyTheme class version to `0.15`.
	- Updated `wuiplugin-themes-0.15.css` file with the updating of the CSS variable values ​​of the `WUISelectpicker` component.

## [v0.15.0] - 2026-09-27

Features:

1. Synced the version with `wuijs-main-lib` `0.15.0`.
2. Updated WUIPluginFormValidation class version to `0.3`.
	- Fixed error in `prepare()` methid.

## [v0.14.1] - 2026-09-08

Features:

1. Synced the version with `wuijs-main-lib` `0.14.1`.
2. Added a `prepare` script to `package.json` so a git-tag install (`npm install github:wui-js/wuijs-plugins-lib#vX.Y.Z`) produces the same flattened file layout as an npm-registry install.

## [v0.14.0] - 2026-09-01

Features:

1. Synced the version with `wuijs-main-lib` `0.14.0`.
2. Updated WUIPluginBodyTheme class version to `0.13`.
	- Updated `wuiplugin-themes-0.13.css` file with the updating of the CSS variable values ​​of the `WUITabs` and `WUIList` components.

## [v0.13.2] - 2026-08-22

Features:

1. Synced the version with `wuijs-main-lib` `0.13.2`.
2. Updated WUIPluginFormValidation class version to `0.2`.
	- Added `reset()` method.
	- Added `resetAll()` method.
	- Added support for array-type inputs (`[name="...[]"]`), matching the `position` parameter added in `WUIForm` `0.11`.

## [v0.13.1] - 2026-07-20

Features:

1. Synced the version with `wuijs-main-lib` `0.13.1`.
2. Updated WUIPluginThemes (ex WUIPluginThemes) class version to `0.12`.
	- Converted class into an extension of the `WUIBody` class from the `wuijs-main-lib` library.
	- Renamed `WUIPluginThemes` class to `WUIPluginBodyThemes`.
	- Renamed `--wuiplugin-theme(s)*`CSS vars prefix to `--wuiplugin-bodytheme*`.
	- Removed `--wui-selectpicker-box-button-textsize` CSS var.
	- Removed `css-theme-maker.py` tool to `bodytheme-css-maker.py`.
	- Removed `clone-theme.py` tool to `bodytheme-clone.py`.
3. Added WUIPluginFormValidation class `0.1` version.
4. Added WUIPluginFormHttp class `0.1` version.
5. Deprecated WUIPluginSelector class.

## [v0.12.0] - 2026-06-24

Features:

1. Synced the version with `wuijs-main-lib` `0.12.0`.
2. Updated WUIPluginThemes class version to `0.11`.
	- Refactored JS code.
	- Added the functionality to add different themes to different elements of the same HTML document.

## [v0.11.0] - 2026-06-12

Features:

1. Synced the version with `wuijs-main-lib` `0.11.0`.
2. WUIPluginThemes version class update to `0.10`.
	- Updated `wuiplugin-themes-0.10.css` file with the updating of the CSS variable values ​​of the `WUITabs`, `WUIMenubar` and `WUIButton` components.

## [v0.10.0] - 2026-06-01

Features:

1. Synced the version with `wuijs-main-lib` `0.10.0`.

## [v0.9.2] - 2026-05-28

Features:

1. Synced the version with `wuijs-main-lib` `0.9.2`.

## [v0.9.1] - 2026-05-28

Features:

1. Synced the version with `wuijs-main-lib` `0.9.1`.

## [v0.9.0] - 2026-05-28

Features:

1. Synced the version with `wuijs-main-lib` `0.9.0`.

> [!IMPORTANT]
> It is suggested to replace the use of `WUIPluginSelector` with the `hidden` mode of `WUISelectpicker`, introduced in version `0.8` of the component and version `0.8.1` of `wuijs-main-lin`.
> The `WUIPluginSelector` plugin will be deprecated in subsequent versions.

## [v0.8.1] - 2026-05-28

Features:

1. Synced the version with `wuijs-main-lib` `0.8.1`.

## [v0.8.0] - 2026-05-26

Features:

1. Synced the version with `wuijs-main-lib` `0.8.0`.
2. WUIPluginThemes version class update to `0.8`.
	- Updated `wuiplugin-themes-0.8.css` file with the update of the default values of the CSS variables of type `scroll`.

## [v0.7.1] - 2026-05-16

Features:

1. Synced the version with `wuijs-main-lib` `0.7.1`.
2. WUIPluginThemes version class update to `0.7`.
	- Updated `wuiplugin-themes-0.7.css` file with default CSS variable values for the `wui-menubar`, `wui-selectpicker`, `wui-datepicker` and `wui-timepicker` components.

## [v0.7.0] - 2026-05-14

Features:

1. Synced the version with `wuijs-main-lib` `0.7.0`.
2. WUIPluginSelector version class update to `0.4`.
	- Added `.root.css` file with CSS default variable values.

## [v0.6.2] - 2026-05-08

Features:

1. Synced the version with `wuijs-main-lib` `0.6.2`.

## [v0.6.1] - 2026-05-06

Features:

1. Synced the version with `wuijs-main-lib` `0.6.1`.
2. Release of the official documentation site for WUI/JS: [https://docs.wuijs.dev](https://docs.wuijs.dev)
3. WUIPluginThemes version class update to `0.6`.
	- Added CSS variables associated with the `wui-codebox` component (lab package).
	- Added CSS variables associated with the `wui-markdown` component (lab package).
	- Synchronized the `default` theme template version with the plugin version.

## [v0.6.0] - 2026-05-01

Features:

1. Synced the version with `wuijs-main-lib` `0.6.0`.
2. WUIPluginThemes version class update to `0.5`.
	- Added `--wui-table-width` CSS var.
	- Added `--wui-table-column-bordercolor-disabled` CSS var.
	- Added `--wui-table-column-bgcolor-disabled` CSS var.
	- Added `--wui-button-default-borderwidth` CSS var.
	- Added `--wui-button-default-horizpadding` CSS var.
	- Added `--wui-button-default-vertpadding` CSS var.
	- Added `--wui-button-mobile-default-minwidth` CSS var.
	- Renamed `--wui-table-column-bordercolor-width` CSS var to `--wui-table-column-borderwidth`.
	- Removed `--wui-switch-bordercolor-invalid` CSS var.

## [v0.5.2] - 2026-04-19

Features:

1. Synchronized the version of the `wuijs-plugins-lib` library with that of `wuijs-main-lib` in order to maintain the integrity of the project and improve the reading of compatibility between libraries.
2. WUIPluginThemes version class update to `0.4`.
	- Added `--wui-modal-mobile-page-box-topmargin` CSS var to improve compatibility with iPhone screens.
	- Added `--wui-modal-mobile-page-box-borderradius-maximized` CSS var to improve compatibility with iPhone screens.
	- Added `--wui-menubar-mobile-bar-horizpadding` CSS var to improve compatibility with iPhone screens.
	- Added `--wui-menubar-mobile-bar-vertpadding` CSS var to improve compatibility with iPhone screens.

## [v0.4.0] - 2026-04-09

Features:

> [!NOTE]
> The owner of the official repository changed from **@wuijsproject** to **@wui-js** in order to have integrity between the GitHub and NPM accounts.

1. Enable installation via NPM.
2. Change of source directory name from `src/wuiplugins` to `src/wui-js/plugins` to support integration with other WUI/JS project libraries.
3. WUIPluginThemes version class update to `0.3`.
	- Added `--wuiplugin-theme-name` global CSS var to identify the active theme.
	- Updated `getTheme()` method to return the value of the global CSS variable `--wuiplugin-theme-name` of the active theme.

## [v0.3.0] - 2026-03-20

Features:

1. Renamed source directories and files to lowercase (e.g. `src/WUIPlugin/Themes/WUIPluginTheme-0.1.js` → `src/wuiplugin/themes/wuiplugin-themes-0.2.js`).
2. Added `legacy/` folder with previous versions of source files (`WUIPluginThemes-0.1`, `WUIPluginSelector-0.2`).
3. Renamed `src/wuiplugin/` directory (previously `src/WUIPlugins/`) to use consistent lowercase naming convention.
4. Renamed `legacy/WUIPlugin/` directory (previously `legacy/WUIPlugins/`) to use consistent singular naming convention.
5. WUIPluginThemes version class update to `0.2`.
	- Renamed the directory and files to lowercase.
	- Changed `--wui-modal-message-box-bgcolor` CSS var opacity from `80%` to `100%` in the base theme.
6. WUIPluginSelector version class update to `0.3`.
	- Renamed the directory and files to lowercase.

## [v0.1.0] - 2025-10-15

Features:

1. Release version.