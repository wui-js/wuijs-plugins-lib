[English](wuiplugin-bodytheme-en.md) | [Español](wuiplugin-bodytheme-es.md)

[wuijs-plugins-lib](../../README-es.md)

# WUIPluginBodyTheme

Versión: `0.15`

Plugin para el manejo de temas prediseñados y modo claro y oscuro.

## Descripción

WUIPluginBodyTheme provee un sistema de temas para aplicaciones web mediante dos capas de variables CSS.
A diferencia de un plugin independiente, extiende la clase `WUIBody` de `wuijs-main-lib`: al cargarse, añade un namespace `theme` a `WUIBody.prototype`, exponiendo `getScheme`, `getCurrentScheme`, `getTheme` y `setScheme` en cualquier instancia de `WUIBody` como `body.theme.*`.

## Componentes cubiertos

WUIPluginBodyTheme provee soporte de temas para los siguientes componentes de WUI/JS Main Lib:

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
- `wui-codebox` (paquete lab)
- `wui-markdown` (paquete lab)
- `wui-tree` (paquete lab)

## Fuentes

| Tipo | Archivo |
| ---- | ------- |
| CSS  | [src/wui-js/plugins/bodytheme/wuiplugin-bodytheme-0.15.css](https://github.com/wui-js/wuijs-plugins-lib/blob/main/src/wui-js/plugins/bodytheme/wuiplugin-bodytheme-0.15.css) |
| JS   | [src/wui-js/plugins/bodytheme/wuiplugin-bodytheme-0.15.js](https://github.com/wui-js/wuijs-plugins-lib/blob/main/src/wui-js/plugins/bodytheme/wuiplugin-bodytheme-0.15.js) |
| CSS  | [src/wui-js/plugins/bodytheme/default/settings-0.15.css](https://github.com/wui-js/wuijs-plugins-lib/blob/main/src/wui-js/plugins/bodytheme/default/settings-0.15.css) |
| CSS  | [src/wui-js/plugins/bodytheme/default/light-0.15.css](https://github.com/wui-js/wuijs-plugins-lib/blob/main/src/wui-js/plugins/bodytheme/default/light-0.15.css) |
| CSS  | [src/wui-js/plugins/bodytheme/default/dark-0.15.css](https://github.com/wui-js/wuijs-plugins-lib/blob/main/src/wui-js/plugins/bodytheme/default/dark-0.15.css) |

## Dependencias

| Clase     | Versión | Descripción |
| --------- | :-----: | ----------- |
| `WUIBody` | `0.5`   | Clase base extendida por el plugin. Requerida. |

## Constructor

No agrega constructor propio; extiende el prototipo de `WUIBody`. Instancia `WUIBody` directamente (`new WUIBody([properties])`).

## Propiedades de la Clase

| Nombre  | Tipo     | Descripción |
| ------- | -------- | ----------- |
| version | `string` | Versión del plugin. |

## Propiedades de la Instancia

No posee propiedades de instancia.

## Métodos

`WUIBody.prototype.theme` es un getter de namespace de solo lectura. Sus métodos se invocan como `body.theme.*` sobre una instancia de `WUIBody`:

| Método           | Return type | Descripción |
| ---------------- | ----------- | ----------- |
| getScheme        | `string`    | `theme.getScheme()`<br><br>Retorna el valor de la propiedad CSS `color-scheme` definida en el elemento `<html>`. Valores posibles: `"light"`, `"dark"`, `"light dark"`, `""`. |
| getCurrentScheme | `string`    | `theme.getCurrentScheme()`<br><br>Retorna el esquema de color preferido del sistema operativo, independientemente del esquema configurado en la aplicación. Valores posibles: `"light"`, `"dark"`. |
| getTheme         | `string`    | `theme.getTheme()`<br><br>Retorna el nombre del tema activo según las clases CSS presentes en `document.body`. |
| setScheme        | `void`      | `theme.setScheme(scheme)`<br><br>Establece el esquema de color de la aplicación. Actualiza las clases CSS en `document.body` y el atributo `color-scheme` en el elemento `<html>`. Si el esquema nuevo difiere del actual, activa automáticamente la transición de fondo. La duración de la transición está controlada por la variable CSS `--wuiplugin-bodytheme-transition-delay` (valor por defecto: `0.4s`). Valores posibles: `"light"`, `"dark"`, `"light dark"`, `"system"`. |

## Temas Predefinidos

| Nombre    | Descripción |
| --------- | ----------- |
| `default` | Tema predeterminado. |

## Variables CSS

Las variables de configuración de tema se definen en el archivo `src/wui-js/plugins/bodytheme/{theme-name}/{version}.css` y se organizan en dos variantes de sufijo: `{variable}-light` para modo claro y `{variable}-dark` para modo oscuro.
Los valores sin sufijo son comunes a ambos modos.

**Colores (con variante por modo de color):**

| Variable base                                                 | Descripción |
| --------------------------------------------------------------| ----------- |
| `--wuiplugin-bodytheme-graycolor-max-(light\|dark)`           | Color gris máximo (blanco en claro, negro en oscuro). |
| `--wuiplugin-bodytheme-graycolor-high-(light\|dark)`          | Color gris alto. |
| `--wuiplugin-bodytheme-graycolor-half-(light\|dark)`          | Color gris medio. |
| `--wuiplugin-bodytheme-graycolor-low-(light\|dark)`           | Color gris bajo. |
| `--wuiplugin-bodytheme-graycolor-min-(light\|dark)`           | Color gris mínimo (negro en claro, blanco en oscuro). |
| `--wuiplugin-bodytheme-shadowcolor-high-(light\|dark)`        | Color de sombra fuerte. |
| `--wuiplugin-bodytheme-shadowcolor-low-(light\|dark)`         | Color de sombra suave. |
| `--wuiplugin-bodytheme-bordercolor-max-(light\|dark)`         | Color de borde máximo. |
| `--wuiplugin-bodytheme-bordercolor-high-(light\|dark)`        | Color de borde alto. |
| `--wuiplugin-bodytheme-bordercolor-low-(light\|dark)`         | Color de borde bajo. |
| `--wuiplugin-bodytheme-bgcolor-overlay-(light\|dark)`         | Color de fondo del overlay. |
| `--wuiplugin-bodytheme-bgcolor-box-(light\|dark)`             | Color de fondo de cuadros de diálogo y paneles. |
| `--wuiplugin-bodytheme-bgcolor-out-(light\|dark)`             | Color de fondo en estado normal. |
| `--wuiplugin-bodytheme-bgcolor-over-(light\|dark)`            | Color de fondo en estado hover o seleccionado. |
| `--wuiplugin-bodytheme-bgcolor-scroll-(light\|dark)`          | Color de la barra de desplazamiento. |
| `--wuiplugin-bodytheme-bgcolor-icon-(light\|dark)`            | Color de relleno de íconos. |
| `--wuiplugin-bodytheme-bgcolor-highcontrast-(light\|dark)`	| Color de fondo de alto contraste (tooltips, etc.). |
| `--wuiplugin-bodytheme-textcolor-title-(light\|dark)`         | Color de texto de títulos. |
| `--wuiplugin-bodytheme-textcolor-active-(light\|dark)`        | Color de texto en estado activo. |
| `--wuiplugin-bodytheme-textcolor-focus-(light\|dark)`         | Color de texto en estado de foco. |
| `--wuiplugin-bodytheme-utilitycolor-hightlight-(light\|dark)` | Color de acento principal (links, botones, selecciones). |
| `--wuiplugin-bodytheme-utilitycolor-warning-(light\|dark)`    | Color de advertencia o error. |
| `--wuiplugin-bodytheme-utilitycolor-disabled-(light\|dark)`   | Color de elementos deshabilitados. |
| `--wuiplugin-bodytheme-intencitycolor-low-(light\|dark)`      | Color de intensidad baja. |
| `--wuiplugin-bodytheme-intencitycolor-half-(light\|dark)`     | Color de intensidad media. |
| `--wuiplugin-bodytheme-intencitycolor-high-(light\|dark)`     | Color de intensidad alta. |

**Tipografía y métricas (comunes, sin variante por modo de color):**

| Variable                                      | Valor por defecto                       | Descripción |
| --------------------------------------------- | --------------------------------------- | ----------- |
| `--wuiplugin-bodytheme-borderradius-low`      | `10px`                                  | Radio de borde bajo. |
| `--wuiplugin-bodytheme-borderradius-half`     | `15px`                                  | Radio de borde medio. |
| `--wuiplugin-bodytheme-borderradius-high`     | `17px`                                  | Radio de borde alto. |
| `--wuiplugin-bodytheme-borderradius-round`    | `50%`                                   | Radio de borde circular. |
| `--wuiplugin-bodytheme-titlefont`             | `Arial, Helvetica, Verdana, sans-serif` | Familia tipográfica para títulos. |
| `--wuiplugin-bodytheme-input-opener-iconsize` | `30px`                                  | Tamaño del ícono de apertura en campos de formulario. |
| `--wuiplugin-bodytheme-transition-delay`      | `0.4s`                                  | Duración de la transición de esquema de color. |

## Implementación

Existen dos modos de implementación:

**Usando archivos CSS generados:**

Utiliza únicamente los archivos CSS generados (`[light|dark]-{versión}.css`) ubicados en el directorio del tema (`src/wui-js/plugins/bodytheme/{nombre}/`).
Recomendado si no se requiere cambiar entre modos claro y oscuro dinámicamente.

Cabecera HTML:

```html
<link type="text/css" rel="stylesheet" href="./libraries/wui-js/plugins/bodytheme/default/dark-0.15.css">
```

Código HTML:

```html
<body class="wuiplugin-bodytheme default dark"></body>
```

**Usando instanciamiento de la clase JS:**

Requiere la implementación de la clase JS `WUIBody`, los archivos JS/CSS del plugin `wuiplugin-bodytheme-0.15.{js,css}` y el archivo CSS de configuración del tema `wui-js/plugins/bodytheme/{nombre}/settings-{versión}.css`.
Adicionalmente el visualizador donde se despliegue debe tener soporte para la función CSS `light-dark()` [https://www.w3schools.com/cssref/func_light-dark.php](https://www.w3schools.com/cssref/func_light-dark.php)

Código CSS:

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

Cabecera HTML:

```html
<link type="text/css" rel="stylesheet" href="./libraries/wui-js/main/switch/wui-switch-0.7.css">
<link type="text/css" rel="stylesheet" href="./libraries/wui-js/plugins/bodytheme/wuiplugin-bodytheme-0.15.css">
<link type="text/css" rel="stylesheet" href="./libraries/wui-js/plugins/bodytheme/default/settings-0.15.css">
<script type="text/javascript" src="./libraries/wui-js/main/body/wui-body-0.5.js"></script>
<script type="text/javascript" src="./libraries/wui-js/main/switch/wui-switch-0.7.js"></script>
<script type="text/javascript" src="./libraries/wui-js/plugins/bodytheme/wuiplugin-bodytheme-0.15.js"></script>
```

> [!TIP]
> Al utilizar el plugin no es necesario cargar los archivos `.root.css` de los componentes.

Código HTML:

```html
<body class="wuiplugin-bodytheme default light">
	<nav>
		<div class="wui-switch my-switch">
			<input type="checkbox" name="mySwitch">
		</div>
	</nav>
</body>
```

Código JS:

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
> Puede revisar este ejemplo funcional en el enlace: [http://docs.wuijs.dev/pages/docs/home/?id=wuijs-demos-plugin-bodytheme-switchmode&lang=es](http://docs.wuijs.dev/pages/docs/home/?id=wuijs-demos-plugin-bodytheme-switchmode&lang=es).

## Herramienta de clonación de temas

El script `tools/bodytheme-clone.py` crea un nuevo tema copiando el archivo de configuración de un tema existente y reemplazando su selector CSS. Es el punto de partida recomendado antes de ejecutar `bodytheme-css-maker.py`.

```bash
python ./bodytheme-clone.py -n <nombre-nuevo-tema>

python ./bodytheme-clone.py -d <directorio-temas> -s <tema-origen> -n <nombre-nuevo-tema> -v <versión-tema>
```

| Opción                 | Predeterminado                                                 | Descripción |
| ---------------------- | -------------------------------------------------------------- | ----------- |
| `-p`,<br>`--plugin`    | `../src/wui-js/plugins/bodytheme/wuiplugin-bodytheme-0.15.css` | Ruta al archivo CSS fuente del plugin bodytheme. |
| `-d`,<br>`--directory` | `../src/wui-js/plugins/bodytheme`                              | Directorio base de temas. |
| `-s`,<br>`--source`    | `default`                                                      | Nombre del tema a clonar. |
| `-n`,<br>`--name`      | _(requerido)_                                                  | Nombre del nuevo tema. |
| `-v`,<br>`--version`   | `0.1`                                                          | Versión del tema. |

El archivo de salida se genera en `{directorio}/{nombre}/settings-{versión}.css` con el selector CSS actualizado al nuevo nombre.

## Herramienta de generación de temas

El script `tools/bodytheme-css-maker.py` crea archivos CSS estandarizados resolviendo todas las referencias a `var()` del archivo fuente, produciendo un CSS plano por cada modo de color. Lee la configuración de variables desde el archivo `{directorio}/{nombre}/settings-{versión}.css`.

```bash
python ./bodytheme-css-maker.py

python ./bodytheme-css-maker.py -p <ruta-css-plugin> -d <directorio-temas> -n <nombre-tema> -v <versión-tema>
```

| Opción                 | Predeterminado                                                 | Descripción |
| ---------------------- | -------------------------------------------------------------- | ----------- |
| `-p`,<br>`--plugin`    | `../src/wui-js/plugins/bodytheme/wuiplugin-bodytheme-0.15.css` | Ruta al archivo CSS fuente del plugin bodytheme. |
| `-d`,<br>`--directory` | `../src/wui-js/plugins/bodytheme`                              | Directorio base de temas. |
| `-n`,<br>`--name`      | `default`                                                      | Nombre del tema. |
| `-v`,<br>`--version`   | `0.12`                                                         | Versión del tema. |

Los archivos de salida se generan en `{directorio}/{nombre}/` con los nombres `light-{versión}.css` y `dark-{versión}.css`.

## Personalización de temas predefinidos

```css
body.wuiplugin-bodytheme.default {
	--wuiplugin-bodytheme-utilitycolor-hightlight-light: #e91e63;
    --wuiplugin-bodytheme-utilitycolor-hightlight-dark: #f06292;
    --wuiplugin-bodytheme-bgcolor-out-light: #fff8f9;
    --wuiplugin-bodytheme-bgcolor-out-dark: #1a0a0d;
}
```

> [!IMPORTANT]
> Para que los cambios sean aplicados es importante incluir el elemento raíz, en este caso `<body>`, con la clase `wuiplugin-bodytheme` y el nombre del tema, de esta manera la definición tendrá mayor especificidad y se aplicará sobre las definiciones del tema especificado.

> [!TIP]
> Para mantener el estándar propuesto por la documentación de la librería WUI/JS, esta personalización puede realizarse en el archivo `WUI.css`.

> [!TIP]
> Puede revisar este ejemplo funcional en el enlace: [http://docs.wuijs.dev/pages/docs/home/?id=wuijs-demos-plugin-bodytheme-customtheme&lang=es](http://docs.wuijs.dev/pages/docs/home/?id=wuijs-demos-plugin-bodytheme-customtheme&lang=es).

## Personalización de temas propios

**Paso 1 — Clonar un tema existente como base:**

Ejecuta desde el directorio `tools/`:

```bash
python bodytheme-clone.py -n my-theme
```

Esto crea `src/wui-js/plugins/bodytheme/my-theme/settings-0.1.css` con el selector actualizado a `.wuiplugin-bodytheme.my-theme` y todas las variables del tema `default` como punto de partida.

**Paso 2 — Editar las variables del nuevo tema:**

Modifica `src/wui-js/plugins/bodytheme/my-theme/settings-0.1.css` con los valores deseados. La estructura del archivo es:

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

**Paso 3 — Activar el tema:**

Para el modo dinámico, activa el tema en el elemento raíz e incluye el archivo de configuración en la cabecera HTML:

```html
<body class="wuiplugin-bodytheme my-theme light">
```

```html
<link type="text/css" rel="stylesheet" href="./libraries/wui-js/plugins/bodytheme/my-theme/settings-0.1.css">
```

**Paso 4 — Generar archivos pregenerados (modo estático):**

Ejecuta desde el directorio `tools/`:

```bash
python bodytheme-css-maker.py -n my-theme
```

Los archivos `light-0.1.css` y `dark-0.1.css` se generan en `src/wui-js/plugins/bodytheme/my-theme/`.
