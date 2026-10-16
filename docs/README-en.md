> [!IMPORTANT]
> The GitHub account `@wuiproject` was migrated to `@wui-js` to match the name with the NPM account.

[English](https://github.com/wui-js/wuijs-plugins-lib/blob/main/docs/README-en.md) |
[Español](https://github.com/wui-js/wuijs-plugins-lib/blob/main/docs/README-es.md)
---

# wuijs-plugins-lib

<p align="center">
	<img src="https://github.com/wui-js/wuijs-plugins-lib/blob/main/imgs/logo/wuijs-plugins-logotype-color.svg" width="220" height="220">
</p>

|                      | |
| -------------------- | --- |
| **Library name**     | `wuijs-plugins-lib` |
| **Library version**  | `0.16.1` ([Change Log](https://github.com/wui-js/wuijs-plugins-lib/blob/main/docs/CHANGELOG-en.md)) |
| **NPM package**      | `@wui-js/plugins` ([npm](https://www.npmjs.com/package/@wui-js/plugins)) |
| **Document version** | `0.16.1.20261016.0` |
| **License**          | `Apache License 2.0` |
| **Author**           | `Sergio E. Belmar V. <wuijs.project@gmail.com>` |
| **Repository**       | [https://github.com/wui-js/wuijs-plugins-lib](https://github.com/wui-js/wuijs-plugins-lib) |
| **Documentation**    | [https://docs.wuijs.dev](https://docs.wuijs.dev) |
| **Website**          | [https://wuijs.dev](https://wuijs.dev) |

## Index

*   [Overview](#overview)
	*   [Classes Table](#classtable)
*   [Installation](#install)
*   [Classes](#classes)
	*   [WUIPluginBodyTheme](https://github.com/wui-js/wuijs-plugins-lib/blob/main/docs/classes/bodytheme/wuiplugin-bodytheme-en.md)
	*   [WUIPluginFormValidation](https://github.com/wui-js/wuijs-plugins-lib/blob/main/docs/classes/formvalidation/wuiplugin-formvalidation-en.md)
	*   [WUIPluginFormHttp](https://github.com/wui-js/wuijs-plugins-lib/blob/main/docs/classes/formhttp/wuiplugin-formhttp-en.md)
	*   [WUIPluginSelector](#wuiplugin-selector) (deprecated)
*   [Demos](#demos) (CodeSandbox)

<a name="overview"></a>

## Overview

WUI/JS Plugins Lib is an open-source JavaScript/CSS library that provides a collection of plugins for WUI/JS Main Lib classes, making it easier to quickly develop web applications.

### About the WUI/JS Project

WUI/JS Plugins Lib is part of the WUI/JS project, which currently consists of 4 repositories:

-	[https://github.com/wui-js/wuijs-main-lib](https://github.com/wui-js/wuijs-main-lib)<br>
	UI Main library.<br><br>
-	[https://github.com/wui-js/wuijs-environment-lib](https://github.com/wui-js/wuijs-environment-lib)<br>
	UI Bridge library between a web environments and native web rendering engines.<br><br>
-	[https://github.com/wui-js/wuijs-plugins-lib](https://github.com/wui-js/wuijs-plugins-lib)<br>
	UI Plugins library.<br><br>
-	[https://github.com/wui-js/wuijs-demos](https://github.com/wui-js/wuijs-demos)<br>
	Repository with demos and usage examples for the project libraries.<br><br>

<a name="classtable"></a>

### Classes Table

| Class Name                                                                                                                                  | Version | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------- |:-------:| ----------- |
| [WUIPluginBodyTheme](https://github.com/wui-js/wuijs-plugins-lib/blob/main/docs/classes/bodytheme/wuiplugin-bodytheme-en.md)                | `0.15`  | Plugin for managing pre-designed themes and light and dark modes. |
| [WUIPluginFormValidation](https://github.com/wui-js/wuijs-plugins-lib/blob/main/docs/classes/formvalidation/wuiplugin-formvalidation-en.md) | `0.3`   | Input validation extension for WUIForm. |
| [WUIPluginFormHttp](https://github.com/wui-js/wuijs-plugins-lib/blob/main/docs/classes/formhttp/wuiplugin-formhttp-en.md)                   | `0.1`   | Data transport extension for WUIForm (JSON submission). |
| [WUIPluginSelector](#wuiplugin-selector) `(deprecated)`                                                                                     | `0.4`   | Modal selector based on WUIModal. |

### Directory Map

```bash
wuijs-lib/
├── docs/
├── imgs/
│   └── logo/
├── legacy/
│   └── wui-js/
│       └── plugins/
├── src/
│   └── wui-js/
│       └── plugins/
└── tools/
```

| Path                                                                                                  | Description |
| ----------------------------------------------------------------------------------------------------- | ----------- |
| [docs](https://github.com/wui-js/wuijs-plugins-lib/tree/main/docs/)                                   | Documentation. |
| [imgs](https://github.com/wui-js/wuijs-plugins-lib/tree/main/imgs/)                                   | Images used in the documentation. |
| [imgs/logo](https://github.com/wui-js/wuijs-plugins-lib/tree/main/imgs/logo/)                         | Project logo and isotype in SVG and PNG format. |
| [legacy](https://github.com/wui-js/wuijs-plugins-lib/tree/main/legacy/)                               | Deprecated sources with previous versions. |
| [legacy/wui-js](https://github.com/wui-js/wuijs-plugins-lib/tree/main/legacy/wui-js/)                 | WUI/JS Project directory. |
| [legacy/wui-js/plugins](https://github.com/wui-js/wuijs-plugins-lib/tree/main/legacy/wui-js/plugins/) | WUI/JS Plugins library (previous versions). |
| [src](https://github.com/wui-js/wuijs-plugins-lib/tree/main/src/)                                     | Main sources of the latest version. |
| [src/wui-js](https://github.com/wui-js/wuijs-plugins-lib/tree/main/src/wui-js)                        | WUI/JS Project directory. |
| [src/wui-js/plugins](https://github.com/wui-js/wuijs-plugins-lib/tree/main/src/wui-js/plugins/)       | WUI/JS Plugins library. |
| [tools](https://github.com/wui-js/wuijs-plugins-lib/tree/main/tools/)                                 | Complementary tools. |

<a name="install"></a>

## Install

**Option 1: Install from source**

To install the WUI/JS Plugins library, it must be cloned from the official GitHub repository (`wui-js/wuijs-plugins-lib`).
Assuming the project where it will be deployed has a source directory: `./src` and within that, a `./src/libraries` library directory, you must type the following in the terminal:

```bash
git clone --branch v0.16.1 https://git@github.com/wui-js/wuijs-plugins-lib.git
cp -r ./wuijs-plugins-lib/src/wui-js/ ../src/libraries/
```

Optionally, it can be downloaded from the same repository in ZIP format.

```bash
wget https://github.com/wui-js/wuijs-plugins-lib/archive/refs/heads/main.zip
unzip main.zip
cp -r ./wuijs-plugins-lib/src/wui-js/ ../src/libraries/
```

> [!TIP]
> It is recommended that the `/plugins` directory be located in the same directory as the main library `/main`.

**Option 2: Install via npm**

To install the WUI/JS library via npm:

```bash
npm i @wui-js/plugins
```

The resources will be available in the `./node_modules/@wui-js/plugins` directory.

<a name="classes"></a>

## Classes

The documentation of each class is in its own document, in the [`docs/classes/`](https://github.com/wui-js/wuijs-plugins-lib/tree/main/docs/classes) directory:

*   <a name="wuiplugin-bodytheme"></a>[WUIPluginBodyTheme](https://github.com/wui-js/wuijs-plugins-lib/blob/main/docs/classes/bodytheme/wuiplugin-bodytheme-en.md)
*   <a name="wuiplugin-formvalidation"></a>[WUIPluginFormValidation](https://github.com/wui-js/wuijs-plugins-lib/blob/main/docs/classes/formvalidation/wuiplugin-formvalidation-en.md)
*   <a name="wuiplugin-formhttp"></a>[WUIPluginFormHttp](https://github.com/wui-js/wuijs-plugins-lib/blob/main/docs/classes/formhttp/wuiplugin-formhttp-en.md)
*   <a name="wuiplugin-selector"></a>WUIPluginSelector `(deprecated)`

> [!WARNING]
> This plugin is deprecated. Replace its usage with the `hidden` mode of `WUISelectpicker`, introduced in version `0.8` of the component and version `0.8.1` of `wuijs-main-lib`. See the [Change Log](https://github.com/wui-js/wuijs-plugins-lib/blob/main/docs/CHANGELOG-en.md) for details. Documentation for this plugin has been removed; refer to an earlier revision of this file if needed.

<a name="demos"></a>

## Demos

This section contains examples of the implementations from the documentation and other complementary demos, all available in the **WUI/JS Demos** repository [https://github.com/wui-js/wuijs-demos](https://github.com/wui-js/wuijs-demos).

1.	[http://docs.wuijs.dev/pages/docs/home/?id=wuijs-demos-plugin-bodytheme-switchmode&lang=en](http://docs.wuijs.dev/pages/docs/home/?id=wuijs-demos-plugin-bodytheme-switchmode&lang=en)<br>
	This demo shows the use of WUIPluginBodyTheme's switch light and dark mode functionality.<br><br>
2.	[http://docs.wuijs.dev/pages/docs/home/?id=wuijs-demos-plugin-bodytheme-customtheme&lang=en](http://docs.wuijs.dev/pages/docs/home/?id=wuijs-demos-plugin-bodytheme-customtheme&lang=en)<br>
	This demo shows the use of WUIPluginBodyTheme's custom predefined themes.<br><br>

> [!NOTE]
> All demos from the [wuijs-demos](https://github.com/wui-js/wuijs-demos) repository can be reviewed on CodeSandbox at the following link [https://codesandbox.io/p/sandbox/github/wui-js/wuijs-demos/tree/main/demos/wuiplugin](https://codesandbox.io/p/sandbox/github/wui-js/wuijs-demos/tree/main/demos/wuiplugin).
