# Change Log

## [v0.4.0] - 2026-04-09

> [!NOTE]
> The owner of the official repository changed from **@wuijsproject** to **@wui-js** in order to have integrity between the GitHub and NPM accounts.

1. Enable installation via NPM.
2. Change of source directory name from `src/wuiplugins` to `src/wui-js/plugins` to support integration with other WUI/JS project libraries.
3. Update WUIPluginThemes version class to 0.3.
	- Added the global CSS variable `--wuiplugin-theme-name` to identify the active theme.
	- Updated the `getTheme()` method to return the value of the global CSS variable `--wuiplugin-theme-name` of the active theme.

## [v0.3.0] - 2026-03-20

Features:

1. Renamed source directories and files to lowercase (e.g. `src/WUIPlugin/Themes/WUIPluginTheme-0.1.js` → `src/wuiplugin/themes/wuiplugin-themes-0.2.js`).
1. Added `legacy/` folder with previous versions of source files (`WUIPluginThemes-0.1`, `WUIPluginSelector-0.2`).
2. Renamed `src/wuiplugin/` directory (previously `src/WUIPlugins/`) to use consistent lowercase naming convention.
3. Renamed `legacy/WUIPlugin/` directory (previously `legacy/WUIPlugins/`) to use consistent singular naming convention.
4. WUIPluginThemes version class update to 0.2.
	- Renamed the directory and files to lowercase.
	- Changed `--wui-modal-message-box-bgcolor` CSS variable opacity from `80%` to `100%` in the base theme.
5. WUIPluginSelector version class update to 0.3.
	- Renamed the directory and files to lowercase.

## [v0.1.0] - 2025-10-15

Features:

1. Release version.