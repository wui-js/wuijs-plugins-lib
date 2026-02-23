# wuijs-plugins-lib

<div align="center">
	<img src="https://github.com/wuijsproject/wuijs-plugins-lib/blob/main/imgs/logo/wuijs-plugins-logotype-color.svg" width="220" height="220">
</div>

Versión librería: `0.1.0` ([Change Log](./REGISTRODECAMBIO.md))

Versión documentación: `0.1.0.20260121.0`

Licencia: `Apache License 2.0`

Autor: `Sergio E. Belmar V. <wuijs.project@gmail.com>`

> [!NOTE]
> Las dos primeras secciones del número de versión de la biblioteca corresponde a la versión más alta de las clases que componen la biblioteca,
> mientras que la tercera sección corresponde al número de modificación de la versión general.

## Índice

*   [Descripción General](#overview)
*   [Instalación](#install)
*   [Plugins](#plugins)
	*   [WUIPluginThemes](#WUIPluginThemes)
	*   [WUIPluginSelector](#WUIPluginSelector)

<a name="overview"></a>

## Descripción General

WUIJS Plugins Lib es una biblioteca JavaScript/CSS de código abierto que proporciona una colección de complementos para las las clases de WUIJS Lib, lo que facilita el desarrollo rápido de aplicaciones web.

### Tabla de Plugins

| Nombre Plugin                           | Version | Descripción |
| --------------------------------------- | -------:| ----------- |
| [WUIPluginThemes](#WUIPluginThemes)     | `0.1`   | Plugin para el manejo de temas prediseñados y modo claro y oscuro. |
| [WUIPluginSelector](#WUIPluginSelector) | `0.2`   | Modal selector basado en WUIModal. |

### Mapa de Directorios

```bash
wuijs-lib/
├── imgs/
│   └── logo/
└── src/
    └── WUI/
```

| Ruta                              | Descripción |
| --------------------------------- | ----------- |
| [imgs](imgs/)                     | Imágenes utilizadas en la documentación. |
| [imgs/logo](imgs/logo/)           | Logotipo e isotipo del proyecto en formato SVG y PNG. |
| [src](src/)                       | Fuentes principales de la última versión. |
| [src/WUIPlugins](src/WUIPlugins/) | Librería WUI JS Plugins. |

<a name="install"></a>

## Instalación

Para instalar la biblioteca WUIJS Plugins, debe ser clonada desde el repositorio oficial en GitHib (`wuijsproject/wuijs-plugins-lib`). Suponiendo que el proyecto donde se implementará tenga un directorio de descargas: `./downloads`, un directorio de código fuente `./src` y, dentro de este, un directorio de bibliotecas `./src/Libraries`, debe escribir lo siguiente en la terminal:

```bash
cd ./downloads
git clone https://git@github.com/wuijsproject/wuijs-plugins-lib.git
cp -r ./wuijs-plugins-lib/src/WUIPlugins ../src/Libraries/
```

Opcionalmente puede ser descargada desde los mismos repositorios en formato ZIP.

```bash
cd ./downloads
wget https://github.com/wuijsproject/wuijs-plugins-lib/archive/refs/heads/main.zip
unzip main.zip
cp -r ./wuijs-plugins-lib-main/src/WUIPlugins ../src/Libraries/
```

> [!TIP]
> Es recomendable que el directorio `/WUIPlugins` se aloje en el mismo directorio que la biblioteca principal `/WUI`.

<a name="plugins"></a>

## Plugins

<a name="WUIPluginThemes"></a>

### WUIPluginThemes

Versión: `0.1`

Plugin para el manejo de temas prediseñados y modo claro y oscuro.

#### Fuentes

| Tipo | Archivo |
| ---- | ------- |
| CSS  | [src/WUIPlugins/Themes/WUIPluginThemes-0.1.css](https://github.com/wuijsproject/wuijs-plugins-lib/blob/main/src/WUIPlugins/Themes/WUIPluginThemes-0.1.css) |
| JS   | [src/WUIPlugins/Themes/WUIPluginThemes-0.1.js](https://github.com/wuijsproject/wuijs-plugins-lib/blob/main/src/WUIPlugins/Themes/WUIPluginThemes-0.1.js) |
| CSS  | [src/WUIPlugins/Themes/WUIPluginThemes-0.1-theme-1-light.css](https://github.com/wuijsproject/wuijs-plugins-lib/blob/main/src/WUIPlugins/Themes/WUIPluginThemes-0.1-theme-1-light.css) |
| CSS  | [src/WUIPlugins/Themes/WUIPluginThemes-0.1-theme-1-dark.css](https://github.com/wuijsproject/wuijs-plugins-lib/blob/main/src/WUIPlugins/Themes/WUIPluginThemes-0.1-theme-1-dark.css) |

#### Descripción

WUIPluginThemes provee un sistema de temas para aplicaciones web mediante dos capas de variables CSS:

- **Primitivas** (`--wuiplugin-theme-*`): tokens de color, tipografía y espaciado, con variantes explícitas para modo claro (`-light`) y oscuro (`-dark`), además de valores comunes sin sufijo.
- **Componentes** (`--wui-*` y `--wuiplugin-*`): variables consumidas por los componentes de WUIJS Lib, definidas como referencias a las primitivas mediante `var()`.

#### Componentes cubiertos

WUIPluginThemes provee variables de tema para los siguientes componentes de WUIJS Lib:

`wui-scrolly`, `wui-icon`, `wui-loader`, `wui-tooltip`, `wui-modal`, `wui-paging`, `wui-slider`, `wui-tabs`, `wui-menubar`, `wui-list`, `wui-table`, `wui-form`, `wui-selectpicker`, `wui-datepicker`, `wui-timepicker`, `wui-colorpicker`, `wui-switch`, `wui-intensity`, `wui-button`

También provee variables para el plugin `wuiplugin-selector`.

#### Instalación del plugin

**Usando el archivo fuente principal:**

```html
<link rel="stylesheet" href="WUIPluginThemes-0.1.css">
<script src="WUIPluginThemes-0.1.js" defer></script>
```

**Usando archivos pregenerados** (sin encadenamiento de `var()`, mayor compatibilidad):

```html
<link rel="stylesheet" href="WUIPluginThemes-0.1-theme-1-light.css">
<link rel="stylesheet" href="WUIPluginThemes-0.1-theme-1-dark.css">
```

> [!NOTE]
> Al usar archivos pregenerados, ambos archivos pueden cargarse simultáneamente. El modo activo se determina por las clases CSS presentes en el elemento raíz.

#### Configuración

Aplica la clase `wuiplugin-themes` en el elemento raíz de la aplicación (normalmente `<body>`), junto con la clase del tema y la clase del modo de color inicial:

```html
<body class="wuiplugin-themes theme-1 light">
```

#### Clases CSS

**Clase base:**

| Clase | Descripción |
| ----- | ----------- |
| `wuiplugin-themes` | **Obligatoria.** Debe estar presente en el elemento raíz. Activa las variables CSS de los componentes de WUIJS Lib. |

**Clases de tema:**

| Clase | Descripción |
| ----- | ----------- |
| `theme-1` | Tema predeterminado. |
| `theme-default` | Alias de `theme-1`. |

**Clases de modo de color:**

| Clase | `color-scheme` | Descripción |
| ----- | -------------- | ----------- |
| `light` | `light` | Fuerza el modo claro. |
| `dark` | `dark` | Fuerza el modo oscuro. |
| `system` | `light dark` | Modo automático mediante la función CSS `light-dark()`. Se adapta al esquema preferido del sistema operativo. |

> [!NOTE]
> El modo `system` requiere soporte del navegador para la función CSS `light-dark()` (disponible en navegadores modernos a partir de 2024).

**Clase de transición:**

| Clase | Descripción |
| ----- | ----------- |
| `transition` | Activa la transición de fondo durante el cambio de esquema. La agrega y elimina automáticamente el método `setScheme()`. No debe usarse manualmente. |

#### Constructor

```javascript
const themes = new WUIPluginThemes();
```

No requiere argumentos.

#### Propiedades

| Nombre | Tipo | Descripción |
| ------ | ---- | ----------- |
| `WUIPluginThemes.version` | `string` | Versión del plugin. Valor: `"0.1"`. |

#### Métodos Públicos

| Método | Parámetros | Retorno | Descripción |
| ------ | ---------- | ------- | ----------- |
| `getScheme()` | — | `string` | Retorna el valor actual de `color-scheme` del elemento `<html>`. |
| `getCurrentScheme()` | — | `string` | Retorna el esquema de color preferido del sistema operativo. |
| `getTheme()` | — | `string` | Retorna el nombre del tema activo desde las clases de `document.body`. |
| `setScheme(value)` | `value: string` | — | Establece el esquema de color de la aplicación. |

---

**`getScheme()`**

Retorna el valor de la propiedad CSS `color-scheme` definida en el elemento `<html>`.

```javascript
const scheme = themes.getScheme();
```

| Retorno | Tipo | Valores posibles |
| ------- | ---- | ---------------- |
| Esquema de color actual | `string` | `"light"`, `"dark"`, `"light dark"`, `""` |

---

**`getCurrentScheme()`**

Retorna el esquema de color preferido del sistema operativo, independientemente del esquema configurado en la aplicación.

```javascript
const scheme = themes.getCurrentScheme();
```

| Retorno | Tipo | Valores posibles |
| ------- | ---- | ---------------- |
| Esquema preferido del sistema | `string` | `"light"`, `"dark"` |

---

**`getTheme()`**

Retorna el nombre del tema activo según las clases CSS presentes en `document.body`.

```javascript
const theme = themes.getTheme();
```

| Retorno | Tipo | Valores posibles |
| ------- | ---- | ---------------- |
| Nombre del tema activo | `string` | `"theme-1"`, `"theme-default"`, `""` |

---

**`setScheme(value)`**

Establece el esquema de color de la aplicación. Actualiza las clases CSS en `document.body` y el atributo `color-scheme` en el elemento `<html>`. Si el esquema nuevo difiere del actual, activa automáticamente la transición de fondo.

```javascript
themes.setScheme("light");
themes.setScheme("dark");
themes.setScheme("system");
```

| Parámetro | Tipo | Descripción |
| --------- | ---- | ----------- |
| `value` | `string` | Esquema de color deseado. No distingue mayúsculas de minúsculas. |

**Valores aceptados:**

| Valor | Clase aplicada en `<body>` | `color-scheme` en `<html>` |
| ----- | -------------------------- | -------------------------- |
| `"light"` · `"only light"` | `light` | `light` |
| `"dark"` · `"only dark"` | `dark` | `dark` |
| `"system"` · `"light dark"` · `"dark light"` | `system` | `light dark` |

La duración de la transición está controlada por la variable CSS `--wuiplugin-theme-transition-delay` (valor por defecto: `0.4s`).

#### Variables CSS

Las variables primitivas se definen con dos variantes de sufijo: `{variable}-light` para modo claro y `{variable}-dark` para modo oscuro. Los valores sin sufijo son comunes a ambos modos.

**Colores (con variante `-light` y `-dark`):**

| Variable base | Descripción |
| ------------- | ----------- |
| `--wuiplugin-theme-graycolor-max` | Color gris máximo (blanco en claro, negro en oscuro). |
| `--wuiplugin-theme-graycolor-high` | Color gris alto. |
| `--wuiplugin-theme-graycolor-half` | Color gris medio. |
| `--wuiplugin-theme-graycolor-low` | Color gris bajo. |
| `--wuiplugin-theme-graycolor-min` | Color gris mínimo (negro en claro, blanco en oscuro). |
| `--wuiplugin-theme-shadowcolor-high` | Color de sombra fuerte. |
| `--wuiplugin-theme-shadowcolor-low` | Color de sombra suave. |
| `--wuiplugin-theme-bordercolor-max` | Color de borde máximo. |
| `--wuiplugin-theme-bordercolor-high` | Color de borde alto. |
| `--wuiplugin-theme-bordercolor-low` | Color de borde bajo. |
| `--wuiplugin-theme-bgcolor-overlay` | Color de fondo del overlay. |
| `--wuiplugin-theme-bgcolor-box` | Color de fondo de cuadros de diálogo y paneles. |
| `--wuiplugin-theme-bgcolor-out` | Color de fondo en estado normal. |
| `--wuiplugin-theme-bgcolor-over` | Color de fondo en estado hover o seleccionado. |
| `--wuiplugin-theme-bgcolor-scroll` | Color de la barra de desplazamiento. |
| `--wuiplugin-theme-bgcolor-icon` | Color de relleno de íconos. |
| `--wuiplugin-theme-bgcolor-highcontrast` | Color de fondo de alto contraste (tooltips, etc.). |
| `--wuiplugin-theme-textcolor-title` | Color de texto de títulos. |
| `--wuiplugin-theme-textcolor-active` | Color de texto en estado activo. |
| `--wuiplugin-theme-textcolor-focus` | Color de texto en estado de foco. |
| `--wuiplugin-theme-utilitycolor-hightlight` | Color de acento principal (links, botones, selecciones). |
| `--wuiplugin-theme-utilitycolor-warning` | Color de advertencia o error. |
| `--wuiplugin-theme-utilitycolor-disabled` | Color de elementos deshabilitados. |
| `--wuiplugin-theme-intencitycolor-low` | Color de intensidad baja. |
| `--wuiplugin-theme-intencitycolor-half` | Color de intensidad media. |
| `--wuiplugin-theme-intencitycolor-high` | Color de intensidad alta. |

**Tipografía y métricas (comunes, sin variante de modo):**

| Variable | Valor por defecto | Descripción |
| -------- | ----------------- | ----------- |
| `--wuiplugin-theme-borderradius-low` | `10px` | Radio de borde bajo. |
| `--wuiplugin-theme-borderradius-half` | `15px` | Radio de borde medio. |
| `--wuiplugin-theme-borderradius-high` | `17px` | Radio de borde alto. |
| `--wuiplugin-theme-borderradius-round` | `50%` | Radio de borde circular. |
| `--wuiplugin-theme-titlefont` | `Arial, Helvetica, Verdana, sans-serif` | Familia tipográfica para títulos. |
| `--wuiplugin-theme-input-opener-iconsize` | `30px` | Tamaño del ícono de apertura en campos de formulario. |
| `--wuiplugin-theme-transition-delay` | `0.4s` | Duración de la transición de esquema de color. |

#### Personalización de temas

Para crear un tema adicional, define una nueva regla CSS sobreescribiendo las variables primitivas que desees cambiar:

```css
.wuiplugin-themes:is(.theme-2) {
    --wuiplugin-theme-utilitycolor-hightlight-light: #e91e63;
    --wuiplugin-theme-utilitycolor-hightlight-dark: #f06292;
    --wuiplugin-theme-bgcolor-out-light: #fff8f9;
    --wuiplugin-theme-bgcolor-out-dark: #1a0a0d;
}
```

Activa el nuevo tema en el elemento raíz:

```html
<body class="wuiplugin-themes theme-2 light">
```

Para generar los archivos CSS pregenerados del nuevo tema:

```bash
python tools/css-theme-maker.py -t theme-2
```

#### Herramienta de generación de temas

El script `tools/css-theme-maker.py` genera archivos CSS pregenerados resolviendo todas las referencias a `var()` del archivo fuente, produciendo un CSS plano por cada modo de color.

```bash
python tools/css-theme-maker.py

python tools/css-theme-maker.py --css <ruta-css> -o <directorio-salida> -t <nombre-tema>
```

| Opción | Predeterminado | Descripción |
| ------ | -------------- | ----------- |
| `--css` | `../src/WUIPlugins/Themes/WUIPluginThemes-0.1.css` | Ruta al archivo CSS fuente. |
| `-o`, `--out` | `../src/WUIPlugins/Themes/` | Directorio de salida para los archivos generados. |
| `-t`, `--theme` | `theme-1` | Nombre del tema a extraer y resolver. |

Los archivos de salida siguen el patrón `{nombre-base}-{tema}-light.css` y `{nombre-base}-{tema}-dark.css`.