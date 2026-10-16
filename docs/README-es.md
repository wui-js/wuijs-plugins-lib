> [!IMPORTANT]
> La cuenta de GitHub `@wuiproject` se migró a `@wui-js` para que coincidiera con el nombre de la cuenta de NPM.

[English](https://github.com/wui-js/wuijs-plugins-lib/blob/main/docs/README-en.md) |
[Español](https://github.com/wui-js/wuijs-plugins-lib/blob/main/docs/README-es.md)
---

# wuijs-plugins-lib

<p align="center">
	<img src="https://github.com/wui-js/wuijs-plugins-lib/blob/main/imgs/logo/wuijs-plugins-logotype-color.svg" width="220" height="220">
</p>

|                       | |
| --------------------- | --- |
| **Nombre librería**   | `wuijs-plugins-lib` |
| **Versión librería**  | `0.16.1` ([Registro de Cambios](https://github.com/wui-js/wuijs-plugins-lib/blob/main/docs/CHANGELOG-es.md)) |
| **Paquete npm**       | `@wui-js/plugins` ([npm](https://www.npmjs.com/package/@wui-js/plugins)) |
| **Versión documento** | `0.16.1.20261016.0` |
| **Licencia**          | `Licencia Apache 2.0` |
| **Autor**             | `Sergio E. Belmar V. <wuijs.project@gmail.com>` |
| **Repositorio**       | [https://github.com/wui-js/wuijs-plugins-lib](https://github.com/wui-js/wuijs-plugins-lib) |
| **Documentación**     | [https://docs.wuijs.dev](https://docs.wuijs.dev) |
| **Sitio web**         | [https://wuijs.dev](https://wuijs.dev) |

## Índice

*   [Descripción General](#overview)
	*   [Tabla de Clases](#classtable)
*   [Instalación](#install)
*   [Clases](#classes)
	*   [WUIPluginBodyTheme](https://github.com/wui-js/wuijs-plugins-lib/blob/main/docs/classes/bodytheme/wuiplugin-bodytheme-es.md)
	*   [WUIPluginFormValidation](https://github.com/wui-js/wuijs-plugins-lib/blob/main/docs/classes/formvalidation/wuiplugin-formvalidation-es.md)
	*   [WUIPluginFormHttp](https://github.com/wui-js/wuijs-plugins-lib/blob/main/docs/classes/formhttp/wuiplugin-formhttp-es.md)
	*   [WUIPluginSelector](#wuiplugin-selector) (deprecado)
*   [Demos](#demos) (CodeSandbox)

<a name="overview"></a>

## Descripción General

WUI/JS Plugins Lib es una librería JavaScript/CSS de código abierto que proporciona una colección de complementos para las clases de WUI/JS Main Lib, lo que facilita el desarrollo rápido de aplicaciones web.

### Acerca del Proyecto WUI/JS

WUI/JS Plugins Lib es parte del proyecto WUI/JS, que consta actualmente de 4 repositorios:

-	[https://github.com/wui-js/wuijs-main-lib](https://github.com/wui-js/wuijs-main-lib)<br>
	Librería Principal UI.<br><br>
-	[https://github.com/wui-js/wuijs-environment-lib](https://github.com/wui-js/wuijs-environment-lib)<br>
	Librería Puente UI entre entornos web y motores de renderizado web nativos.<br><br>
-	[https://github.com/wui-js/wuijs-plugins-lib](https://github.com/wui-js/wuijs-plugins-lib)<br>
	Librería de Complementos UI.<br><br>
-	[https://github.com/wui-js/wuijs-demos](https://github.com/wui-js/wuijs-demos)<br>
	Repositorio con demos y ejemplos de uso de las librerías del proyecto.<br><br>

<a name="classtable"></a>

### Tabla de Clases

| Nombre Clase                                                                                                                                | Versión | Descripción |
| ------------------------------------------------------------------------------------------------------------------------------------------- |:-------:| ----------- |
| [WUIPluginBodyTheme](https://github.com/wui-js/wuijs-plugins-lib/blob/main/docs/classes/bodytheme/wuiplugin-bodytheme-es.md)                | `0.15`  | Plugin para el manejo de temas prediseñados y modo claro y oscuro. |
| [WUIPluginFormValidation](https://github.com/wui-js/wuijs-plugins-lib/blob/main/docs/classes/formvalidation/wuiplugin-formvalidation-es.md) | `0.3`   | Extensión de validación de campos para WUIForm. |
| [WUIPluginFormHttp](https://github.com/wui-js/wuijs-plugins-lib/blob/main/docs/classes/formhttp/wuiplugin-formhttp-es.md)                   | `0.1`   | Extensión de transporte de datos para WUIForm (envío JSON). |
| [WUIPluginSelector](#wuiplugin-selector) `(deprecado)`                                                                                      | `0.4`   | Selector modal basado en WUIModal. |

### Mapa de Directorios

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

| Ruta                                                                                                  | Descripción |
| ----------------------------------------------------------------------------------------------------- | ----------- |
| [docs](https://github.com/wui-js/wuijs-plugins-lib/tree/main/docs/)                                   | Documentación. |
| [imgs](https://github.com/wui-js/wuijs-plugins-lib/tree/main/imgs/)                                   | Imágenes utilizadas en la documentación. |
| [imgs/logo](https://github.com/wui-js/wuijs-plugins-lib/tree/main/imgs/logo/)                         | Logotipo e isotipo del proyecto en formato SVG y PNG. |
| [legacy](https://github.com/wui-js/wuijs-plugins-lib/tree/main/legacy/)                               | Fuentes obsoletas con versiones anteriores. |
| [legacy/wui-js](https://github.com/wui-js/wuijs-plugins-lib/tree/main/legacy/wui-js/)                 | Directorio del proyecto WUI/JS. |
| [legacy/wui-js/plugins](https://github.com/wui-js/wuijs-plugins-lib/tree/main/legacy/wui-js/plugins/) | Librería WUI/JS Plugins (versiones anteriores). |
| [src](https://github.com/wui-js/wuijs-plugins-lib/tree/main/src/)                                     | Fuentes principales de la última versión. |
| [src/wui-js](https://github.com/wui-js/wuijs-plugins-lib/tree/main/src/wui-js)                        | Directorio del proyecto WUI/JS. |
| [src/wui-js/plugins](https://github.com/wui-js/wuijs-plugins-lib/tree/main/src/wui-js/plugins/)       | Librería WUI/JS Plugins. |
| [tools](https://github.com/wui-js/wuijs-plugins-lib/tree/main/tools/)                                 | Herramientas complementarias. |

<a name="install"></a>

## Instalación

**Opción 1: Instalar desde fuente**

Para instalar la biblioteca WUI/JS Plugins, debe ser clonada desde el repositorio oficial en GitHib (`wui-js/wuijs-plugins-lib`).
Suponiendo que el proyecto donde se implementará tenga un directorio de código fuente `./src` y, dentro de este, un directorio de librerías `./src/libraries`, debe escribir lo siguiente en la terminal:

```bash
git clone --branch v0.16.1 https://git@github.com/wui-js/wuijs-plugins-lib.git
cp -r ./wuijs-plugins-lib/src/wui-js/ ../src/libraries/
```

Opcionalmente puede ser descargada desde los mismos repositorios en formato ZIP.

```bash
wget https://github.com/wui-js/wuijs-plugins-lib/archive/refs/heads/main.zip
unzip main.zip
cp -r ./wuijs-plugins-lib-main/src/wui-js/ ../src/libraries/
```

> [!TIP]
> Es recomendable que el directorio `/plugins` se aloje en el mismo directorio que la biblioteca principal `/main`.

**Opción 2: Instalar vía npm**

Para instalar la librería WUI/JS mediante npm:

```bash
npm i @wui-js/plugins
```

Los recursos quedarán disponibles en la ruta `./node_modules/@wui-js/plugins`.

<a name="classes"></a>

## Clases

La documentación de cada clase está en un documento propio, en el directorio [`docs/classes/`](https://github.com/wui-js/wuijs-plugins-lib/tree/main/docs/classes):

*   <a name="wuiplugin-bodytheme"></a>[WUIPluginBodyTheme](https://github.com/wui-js/wuijs-plugins-lib/blob/main/docs/classes/bodytheme/wuiplugin-bodytheme-es.md)
*   <a name="wuiplugin-formvalidation"></a>[WUIPluginFormValidation](https://github.com/wui-js/wuijs-plugins-lib/blob/main/docs/classes/formvalidation/wuiplugin-formvalidation-es.md)
*   <a name="wuiplugin-formhttp"></a>[WUIPluginFormHttp](https://github.com/wui-js/wuijs-plugins-lib/blob/main/docs/classes/formhttp/wuiplugin-formhttp-es.md)
*   <a name="wuiplugin-selector"></a>WUIPluginSelector `(deprecado)`

> [!WARNING]
> Este plugin está deprecado. Reemplaza su uso por el modo `hidden` de `WUISelectpicker`, introducido en la versión `0.8` del componente y versión `0.8.1` de `wuijs-main-lib`. Ver el [Registro de Cambios](https://github.com/wui-js/wuijs-plugins-lib/blob/main/docs/CHANGELOG-es.md) para más detalles. La documentación de este plugin fue removida; consulta una revisión anterior de este archivo si es necesaria.

<a name="demos"></a>

## Demos

Esta sección recoge los ejemplos de las implementaciones de la documentación y otros demos complementarios, todos disponibles en el repositorio **WUI/JS Demos** [https://github.com/wui-js/wuijs-demos](https://github.com/wui-js/wuijs-demos).

1.	[http://docs.wuijs.dev/pages/docs/home/?id=wuijs-demos-plugin-bodytheme-switchmode&lang=es](http://docs.wuijs.dev/pages/docs/home/?id=wuijs-demos-plugin-bodytheme-switchmode&lang=es)<br>
	Esta demostración muestra el uso de la funcionalidad de cambiar entre modo claro y oscuro de WUIPluginBodyTheme.<br><br>
2.	[http://docs.wuijs.dev/pages/docs/home/?id=wuijs-demos-plugin-bodytheme-customtheme&lang=es](http://docs.wuijs.dev/pages/docs/home/?id=wuijs-demos-plugin-bodytheme-customtheme&lang=es)<br>
	Esta demostración muestra el uso de los temas predefinidos personalizados de WUIPluginBodyTheme.<br><br>

> [!NOTE]
> Todos los demos del repositorio [wuijs-demos](https://github.com/wui-js/wuijs-demos) se pueden revisar en CodeSandbox en el enlace [https://codesandbox.io/p/sandbox/github/wui-js/wuijs-demos/tree/main/demos/wuiplugin](https://codesandbox.io/p/sandbox/github/wui-js/wuijs-demos/tree/main/demos/wuiplugin).
