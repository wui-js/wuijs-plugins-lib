> [!WARNING]
> This document has not yet been finalized and is in a preliminary version.

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
└── src/
    └── WUI/
```

| Path                              | Description |
| --------------------------------- | ----------- |
| [imgs](imgs/)                     | Images used in the documentation. |
| [imgs/logo](imgs/logo/)           | Project logo and isotype in SVG and PNG format. |
| [src](src/)                       | Main sources of the latest version. |
| [src/WUIPlugins](src/WUIPlugins/) | WUI JS Plugins Library. |

<a name="install"></a>

## Install

To install the WUIJS Plugins library, must be cloned from the GitHib official distribution repository (`wuijsproject/wuijs-	lib`). Assuming the project where it will be deployed has a download directory: `./downloads`, a `./src` source directory, and within that, a `./src/Libraries` library directory, you must type the following in the terminal:

```bash
cd ./downloads
git clone https://git@github.com/wuijsproject/wuijs-plugins-lib.git
cp -r ./wuijs-plugins-lib/src/WUIPlugins ../src/Libraries/
```

Optionally, it can be downloaded from the same repositories in ZIP format.

```bash
cd ./downloads
wget https://github.com/wuijsproject/wuijs-plugins-lib/archive/refs/heads/main.zip
unzip main.zip
cp -r ./wuijs-plugins-lib-main/src/WUIPlugins ../src/Libraries/
```

> [!TIP]
> It is recommended that the `WUIPlugins` directory be located in the same directory as the `WUI` library.