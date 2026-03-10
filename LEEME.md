# wuijs-plugins-lib

<div align="center">
	<img src="https://github.com/wuijsproject/wuijs-plugins-lib/blob/main/imgs/logo/wuijs-plugins-logotype-color.svg" width="220" height="220">
</div>

Versión librería: `0.1.0` ([Change Log](./REGISTRODECAMBIO.md))

Versión documentación: `0.1.0.20260309.0`

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
| [WUIPluginSelector](#WUIPluginSelector) | `0.2`   | Selector modal basado en WUIModal. |

### Mapa de Directorios

```bash
wuijs-lib/
├── imgs/
│   └── logo/
├── src/
│   └── WUI/
└── tools/
```

| Ruta                              | Descripción |
| --------------------------------- | ----------- |
| [imgs](imgs/)                     | Imágenes utilizadas en la documentación. |
| [imgs/logo](imgs/logo/)           | Logotipo e isotipo del proyecto en formato SVG y PNG. |
| [src](src/)                       | Fuentes principales de la última versión. |
| [src/WUIPlugins](src/WUIPlugins/) | Librería WUI JS Plugins. |
| [tools](tools/)                   | Herramientas complementarias. |

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

#### Descripción

WUIPluginThemes provee un sistema de temas para aplicaciones web mediante dos capas de variables CSS:

- **Configuración de tema** (`--wuiplugin-theme-*`): tokens de color, tipografía y espaciado, con variantes explícitas para modo claro (`-light`) y oscuro (`-dark`), además de valores comunes sin sufijo.
- **Variables de componentes** (`--wui-*` y `--wuiplugin-*`): variables consumidas por los componentes de WUIJS Lib, definidas como referencias a las variables de configuración del tema mediante la función `var()`.

#### Componentes cubiertos

WUIPluginThemes provee soporte de temas para los siguientes componentes de WUIJS Lib:

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

También provee soporte de temas para el plugin `wuiplugin-selector`.

#### Fuentes

| Tipo | Archivo |
| ---- | ------- |
| CSS  | [src/WUIPlugins/Themes/WUIPluginThemes-0.1.css](https://github.com/wuijsproject/wuijs-plugins-lib/blob/main/src/WUIPlugins/Themes/WUIPluginThemes-0.1.css) |
| JS   | [src/WUIPlugins/Themes/WUIPluginThemes-0.1.js](https://github.com/wuijsproject/wuijs-plugins-lib/blob/main/src/WUIPlugins/Themes/WUIPluginThemes-0.1.js) |
| CSS  | [src/WUIPlugins/Themes/WUIPluginThemes-0.1-theme-1-light.css](https://github.com/wuijsproject/wuijs-plugins-lib/blob/main/src/WUIPlugins/Themes/WUIPluginThemes-0.1-theme-1-light.css) |
| CSS  | [src/WUIPlugins/Themes/WUIPluginThemes-0.1-theme-1-dark.css](https://github.com/wuijsproject/wuijs-plugins-lib/blob/main/src/WUIPlugins/Themes/WUIPluginThemes-0.1-theme-1-dark.css) |

#### Constructor

| Tipo            | Descripción |
| --------------- | ----------- |
| WUIPluginThemes | `WUIPluginThemes()` |

#### Propiedades de la Clase

| Nombre  | Tipo     | Descripción |
| ------- | -------- | ----------- |
| version | `string` | Versión del plugin. |

#### Propiedades de la Instancia

No posee propiedades de instancia.

#### Métodos

| Método           | Return type | Descripción |
| ---------------- | ----------- | ----------- |
| getScheme        | `string`    | `getScheme()`<br><br>Retorna el valor de la propiedad CSS `color-scheme` definida en el elemento `<html>`. Valores posibles: `"light"`, `"dark"`, `"light dark"`, `""`. |
| getCurrentScheme | `string`    | `getCurrentScheme()`<br><br>Retorna el esquema de color preferido del sistema operativo, independientemente del esquema configurado en la aplicación. Valores posibles: `"light"`, `"dark"`. |
| getTheme         | `string`    | `getTheme()`<br><br>Retorna el nombre del tema activo según las clases CSS presentes en `document.body`. Valores posibles: `"theme-1"`, `"theme-default"`, `""`. |
| setScheme        | `void`      | `setScheme(scheme)`<br><br>Establece el esquema de color de la aplicación. Actualiza las clases CSS en `document.body` y el atributo `color-scheme` en el elemento `<html>`. Si el esquema nuevo difiere del actual, activa automáticamente la transición de fondo. La duración de la transición está controlada por la variable CSS `--wuiplugin-theme-transition-delay` (valor por defecto: `0.4s`). Valores posibles: `"light"`, `"dark"`, `"light dark"`, `"system"`. |

#### Clases CSS

**Clase base:**

| Clase              | Descripción |
| ------------------ | ----------- |
| `wuiplugin-themes` | **Obligatoria.** Debe estar presente en el elemento raíz. Activa las variables CSS de los componentes de WUIJS Lib. |

**Clases de tema:**

| Clase           | Descripción |
| --------------- | ----------- |
| `theme-1`       | Tema predeterminado. |
| `theme-default` | Alias de `theme-1`. |

**Clases de modo de color:**

| Clase    | `color-scheme` | Descripción |
| -------- | -------------- | ----------- |
| `light`  | `light`        | Fuerza el modo claro. |
| `dark`   | `dark`         | Fuerza el modo oscuro. |
| `system` | `light dark`   | Modo automático mediante la función CSS `light-dark()`. Se adapta al esquema preferido del sistema operativo. |

> [!NOTE]
> El modo `system` requiere soporte del navegador para la función CSS `light-dark()` (disponible en navegadores modernos a partir de 2024).

**Clase de transición:**

| Clase        | Descripción |
| ------------ | ----------- |
| `transition` | Activa la transición de fondo durante el cambio de esquema. La agrega y elimina automáticamente el método `setScheme()`. No debe usarse manualmente. |

#### Variables CSS

Las variables de configuración de tema se definen con dos variantes de sufijo: `{variable}-light` para modo claro y `{variable}-dark` para modo oscuro.
Los valores sin sufijo son comunes a ambos modos.

**Colores (con variante por modo de color):**

| Variable base                                             | Descripción |
| --------------------------------------------------------- | ----------- |
| `--wuiplugin-theme-graycolor-max-(light\|dark)`           | Color gris máximo (blanco en claro, negro en oscuro). |
| `--wuiplugin-theme-graycolor-high-(light\|dark)`          | Color gris alto. |
| `--wuiplugin-theme-graycolor-half-(light\|dark)`          | Color gris medio. |
| `--wuiplugin-theme-graycolor-low-(light\|dark)`           | Color gris bajo. |
| `--wuiplugin-theme-graycolor-min-(light\|dark)`           | Color gris mínimo (negro en claro, blanco en oscuro). |
| `--wuiplugin-theme-shadowcolor-high-(light\|dark)`        | Color de sombra fuerte. |
| `--wuiplugin-theme-shadowcolor-low-(light\|dark)`         | Color de sombra suave. |
| `--wuiplugin-theme-bordercolor-max-(light\|dark)`         | Color de borde máximo. |
| `--wuiplugin-theme-bordercolor-high-(light\|dark)`        | Color de borde alto. |
| `--wuiplugin-theme-bordercolor-low-(light\|dark)`         | Color de borde bajo. |
| `--wuiplugin-theme-bgcolor-overlay-(light\|dark)`         | Color de fondo del overlay. |
| `--wuiplugin-theme-bgcolor-box-(light\|dark)`             | Color de fondo de cuadros de diálogo y paneles. |
| `--wuiplugin-theme-bgcolor-out-(light\|dark)`             | Color de fondo en estado normal. |
| `--wuiplugin-theme-bgcolor-over-(light\|dark)`            | Color de fondo en estado hover o seleccionado. |
| `--wuiplugin-theme-bgcolor-scroll-(light\|dark)`          | Color de la barra de desplazamiento. |
| `--wuiplugin-theme-bgcolor-icon-(light\|dark)`            | Color de relleno de íconos. |
| `--wuiplugin-theme-bgcolor-highcontrast-(light\|dark)`	| Color de fondo de alto contraste (tooltips, etc.). |
| `--wuiplugin-theme-textcolor-title-(light\|dark)`         | Color de texto de títulos. |
| `--wuiplugin-theme-textcolor-active-(light\|dark)`        | Color de texto en estado activo. |
| `--wuiplugin-theme-textcolor-focus-(light\|dark)`         | Color de texto en estado de foco. |
| `--wuiplugin-theme-utilitycolor-hightlight-(light\|dark)` | Color de acento principal (links, botones, selecciones). |
| `--wuiplugin-theme-utilitycolor-warning-(light\|dark)`    | Color de advertencia o error. |
| `--wuiplugin-theme-utilitycolor-disabled-(light\|dark)`   | Color de elementos deshabilitados. |
| `--wuiplugin-theme-intencitycolor-low-(light\|dark)`      | Color de intensidad baja. |
| `--wuiplugin-theme-intencitycolor-half-(light\|dark)`     | Color de intensidad media. |
| `--wuiplugin-theme-intencitycolor-high-(light\|dark)`     | Color de intensidad alta. |

**Tipografía y métricas (comunes, sin variante por modo de color):**

| Variable                                  | Valor por defecto                       | Descripción |
| ----------------------------------------- | --------------------------------------- | ----------- |
| `--wuiplugin-theme-borderradius-low`      | `10px`                                  | Radio de borde bajo. |
| `--wuiplugin-theme-borderradius-half`     | `15px`                                  | Radio de borde medio. |
| `--wuiplugin-theme-borderradius-high`     | `17px`                                  | Radio de borde alto. |
| `--wuiplugin-theme-borderradius-round`    | `50%`                                   | Radio de borde circular. |
| `--wuiplugin-theme-titlefont`             | `Arial, Helvetica, Verdana, sans-serif` | Familia tipográfica para títulos. |
| `--wuiplugin-theme-input-opener-iconsize` | `30px`                                  | Tamaño del ícono de apertura en campos de formulario. |
| `--wuiplugin-theme-transition-delay`      | `0.4s`                                  | Duración de la transición de esquema de color. |

#### Herramienta de generación de temas

El script `tools/css-theme-maker.py` crea archivos SVG estandarizados resolviendo todas las referencias a `var()` del archivo fuente, produciendo un CSS plano por cada modo de color.

```bash
python tools/css-theme-maker.py

python tools/css-theme-maker.py -c <ruta-css-fuente> -s <ruta-css-settings> -o <directorio-salida> -t <nombre-tema>
```

| Opción                | Predeterminado                                             | Descripción |
| --------------------- | ---------------------------------------------------------- | ----------- |
| `-c`,<br>`--source`   | `../src/WUIPlugins/Themes/WUIPluginThemes-0.1.css`         | Ruta al archivo CSS fuente. |
| `-s`,<br>`--settings` | `../src/WUIPlugins/Themes/WUIPluginThemes-0.1-theme-1.css` | Ruta al archivo CSS de configuración. |
| `-o`,<br>`--out`      | `../src/WUIPlugins/Themes/`                                | Directorio de salida para los archivos generados. |
| `-t`,<br>`--theme`    | `theme-1`                                                  | Nombre del tema a extraer y resolver. |

Los archivos de salida siguen el patrón `{nombre-base}-{tema}-light.css` y `{nombre-base}-{tema}-dark.css`.

#### Implementación

Existen dos modos de implementación:

**Usando archivos pregenerados:**
Utiliza únicamente los archivos CSS predefinidos (`WUIPluginThemes-0.1-theme-*-[light|dark].css`).
Recomendado si no se requiere cambiar entre modos claro y oscuro dinámicamente.

Cabecera HTML:

```html
<link rel="stylesheet" href="WUIPluginThemes-0.1-theme-1-light.css">
```

Código HTML:

```html
<body class="wuiplugin-themes theme-1 light"></body>
```

**Usando el archivo fuente principal:**
Requiere la implementación de la clase JS `WUIPluginThemes` y el archivo CSS fuente (`WUIPluginThemes-0.1.css`).
Adicionalmente el visualizador donde se despliegue debe tener soporte par la fiunción CSS `light-dark()` [https://www.w3schools.com/cssref/func_light-dark.php](https://www.w3schools.com/cssref/func_light-dark.php)

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
<link rel="stylesheet" href="./Libraries/WUI/Switch/WUISwitch-0.3.css">
<link rel="stylesheet" href="./Libraries/WUIPlugins/Themes/WUIPluginThemes-0.1.css">
<link rel="stylesheet" href="./Libraries/WUIPlugins/Themes/WUIPluginThemes-0.1-theme-1.css">
<script type="text/javascript" src="./Libraries/WUI/Switch/WUISwitch-0.3.js"></script>
<script type="text/javascript" src="./Libraries/WUIPlugins/Themes/WUIPluginThemes-0.1.js"></script>
```

Código HTML:

```html
<body class="wuiplugin-themes theme-1 light">
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
	const themes = new WUIPluginThemes();
	const switchbox = new WUISwitch({
		selector: ".wui-switch.my-switch",
		value: "1",
		activated: false,
		onChange: (value, activated) => {
			themes.setScheme(activated ? "dark" : "light");
		}
	});
	switchbox.init();
}

window.addEventListener("DOMContentLoaded", init);
```

> [!TIP]
> Puede revisar este ejemplo funcional en CodeSandbox en el enlace: [https://codesandbox.io/p/sandbox/github/wuijsproject/wuijs-plugins-lib/tree/main/demos/WUIPluginsThemes-switchmode](https://codesandbox.io/p/sandbox/github/wuijsproject/wuijs-plugins-lib/tree/main/demos/WUIPluginsThemes-switchmode).

#### Personalización de temas

Para crear un tema adicional, se debe definir una nueva regla CSS con todas las variables de configuración de tema:

```css
.wuiplugin-themes.my-theme {
    
	/* light mode */

	/* ... */

	/* dark mode */

	/* ... */

	/* common */

	/* ... */
}
```

Activa el nuevo tema en el elemento raíz:

```html
<body class="wuiplugin-themes my-theme light">
```

Para generar los archivos CSS pregenerados del nuevo tema:

```bash
python tools/css-theme-maker.py --settings ./my-theme.css --theme my-theme --out ./
```

La ejecución de esta herramienta crea los archivos `WUIPluginThemes-0.1-theme-my-theme-light.css` y `WUIPluginThemes-0.1-theme-my-theme-dark.css` en el directorio actual.

<a name="WUIPluginSelector"></a>

### WUIPluginSelector

Versión: `0.2`

Selector modal de lista de opciones basado en WUIModal.

#### Descripción

WUIPluginSelector extiende `WUIModal` e implementa un selector de lista de opciones de tipo modal.
Está optimizado para entornos móviles e intercepta el evento táctil sobre elementos `<select>` nativos para reemplazar el selector del sistema por un panel de selección personalizado.
También puede utilizarse de forma programática independientemente de un input nativo `<select>` en entornos responsivos.

> [!NOTE]
> La documentación completa de `WUIModal` se encuentra en el proyecto wuijs-lib en el enlace: [https://github.com/wuijsproject/wuijs-lib/blob/main/README.md#WUIModal](https://github.com/wuijsproject/wuijs-lib/blob/main/README.md#WUIModal).

#### Dependencias

| Clase       | Versión | Descripción |
| ----------- | :-----: | ----------- |
| `WUIModal`  | `0.2`   | Clase base del modal. Requerida. |
| `WUIButton` | `0.2`   | Utilizada internamente para los botones de aceptar y cancelar. Requerida. |
| `WUIIcon`   | `0.1`   | Requerida para el ícono de las opciones seleccionadas. |

#### Fuentes

| Tipo | Archivo |
| ---- | ------- |
| CSS  | [src/WUIPlugins/Selector/WUIPluginSelector-0.2.css](https://github.com/wuijsproject/wuijs-plugins-lib/blob/main/src/WUIPlugins/Selector/WUIPluginSelector-0.2.css) |
| JS   | [src/WUIPlugins/Selector/WUIPluginSelector-0.2.js](https://github.com/wuijsproject/wuijs-plugins-lib/blob/main/src/WUIPlugins/Selector/WUIPluginSelector-0.2.js) |

#### Constructor

| Tipo              | Descripción |
| ----------------- | ----------- |
| WUIPluginSelector | `WUIPluginSelector([properties])`<br><br>Parámetros:<br>**• properties:** `object` *opcional* |

#### Propiedades de la Clase

| Nombre  | Tipo     | Descripción |
| ------- | -------- | ----------- |
| version | `string` | Versión del plugin. |

#### Propiedades de la Instancia

| Propiedad       | Tipo             | Valor predeterminado | Descripción |
| --------------- | ---------------- | -------------------- | ----------- |
| value           | `string`         | `""`                 | (get/set)<br>Valor actual seleccionado. En selección múltiple, los valores se unen con `separatorValue`. |
| options         | `array`          | `[]`                 | (get/set)<br>Array de objetos de opción. Ver estructura en la sección de implementación. |
| multiple        | `boolean`        | `false`              | (get/set)<br>Indica si la selección es múltiple. Afecta cómo se actualizan las opciones del `<select>` vinculado al aceptar. |
| separatorValue  | `string`         | `","`                | (get/set)<br>Separador usado para unir los valores seleccionados en la propiedad `value` y en el parámetro `values` del callback `acceptOnClick`. |
| separatorText   | `string`         | `", "`               | (get/set)<br>Separador usado para unir los textos seleccionados en el parámetro `texts` del callback `acceptOnClick`. |
| emptyText       | `string`         | `""`                 | (get/set)<br>Texto alternativo para opciones con `value` vacío. |
| selecteableText | `boolean`        | `false`              | (get/set)<br>Si es `true`, permite al usuario seleccionar y copiar el texto de las opciones. Se aplica únicamente a las opciones seleccionadas. |
| acceptButton    | `WUIButton`      | `null`               | (get/set)<br>Instancia del botón de aceptar. Se asigna automáticamente en `init()`. El setter solo acepta instancias de `WUIButton`. |
| acceptVisible   | `boolean`        | `true`               | (get/set)<br>Indica si el botón de aceptar es visible. Se restablece a `true` al cerrar el selector. |
| acceptData      | `object`         | `{}`                 | (get/set)<br>Atributos `data-*` a aplicar en el botón de aceptar (por ejemplo `{ key: "buttons.accept" }` para WUILanguage). |
| acceptText      | `string`         | `""`                 | (get/set)<br>Texto del botón de aceptar. |
| acceptOnClick   | `function\|null` | `null`               | (get/set)<br>Función ejecutada al pulsar el botón de aceptar. Firma: `acceptOnClick(indexes, values, texts)`. Se restablece a `null` al cerrar el selector. |
| cancelButton    | `WUIButton`      | `null`               | (get/set)<br>Instancia del botón de cancelar. Se asigna automáticamente en `init()`. El setter solo acepta instancias de `WUIButton`. |
| cancelVisible   | `boolean`        | `true`               | (get/set)<br>Indica si el botón de cancelar es visible. Se restablece a `true` al cerrar el selector. |
| cancelData      | `object`         | `{}`                 | (get/set)<br>Atributos `data-*` a aplicar en el botón de cancelar. |
| cancelText      | `string`         | `""`                 | (get/set)<br>Texto del botón de cancelar. |
| cancelOnClick   | `function\|null` | `null`               | (get/set)<br>Función ejecutada al pulsar el botón de cancelar. Se restablece a `null` al cerrar el selector. |
| onSelect        | `function\|null` | `null`               | (get/set)<br>Función ejecutada al pulsar una opción de la lista. Firma: `onSelect(value, index)`. Se restablece a `null` al cerrar el selector. |

Además, hereda todas las propiedades de `WUIModal` (`selector`, `openDelay`, `onStartOpen`, `onOpen`, `onScrolling`, `onStartClose`, `onClose`, etc.).

#### Métodos

| Método         | Return type | Descripción |
| -------------- | ----------- | ----------- |
| init           | `void`      | `init()`<br><br>Construye la estructura HTML interna del selector si no existe (o la carga si ya existe en el DOM), inicializa el modal base e instancia los botones de aceptar y cancelar. |
| prepareInput   | `void`      | `prepareInput(input[, options])`<br><br>Vincula el selector a un elemento `<select>` nativo para reemplazar su comportamiento en pantallas móviles. Parámetros:<br>**• input:** `HTMLSelectElement`. Elemento a vincular.<br>**• options:** `object` *opcional*. Opciones de configuración:<br>&nbsp;&nbsp;&nbsp;**- emptyText:** `string` *(predeterminado: `this.emptyText`)* – Texto para opciones de valor vacío.<br>&nbsp;&nbsp;&nbsp;**- direction:** `"ltr"\|"rtl"` *(predeterminado: `"ltr"`)* – Dirección del texto del input.<br>&nbsp;&nbsp;&nbsp;**- force:** `boolean` *(predeterminado: `false`)* – Si `true`, activa el selector en todos los tamaños de pantalla, no solo en móvil (≤767px).<br><br>Al abrirse, puebla automáticamente `this.options` con los `<option>` del `<select>` y establece la selección actual. Al aceptar, actualiza el valor del `<select>` y dispara su evento `change`. |
| open           | `void`      | `open()`<br><br>Abre el selector. Renderiza la lista de opciones desde `this.options` y desplaza la vista hasta la primera opción seleccionada. Muestra u oculta los botones según `acceptVisible` y `cancelVisible`. |
| close          | `void`      | `close()`<br><br>Cierra el selector y restaura las opciones del `<select>` vinculado si existe. Restablece `acceptVisible`, `cancelVisible`, `acceptOnClick`, `cancelOnClick`, `onOpen`, `onClose` y `onSelect` a sus valores predeterminados, y desvincula el input. |
| destroy        | `void`      | `destroy()`<br><br>Destructor. Elimina todos los elementos HTML internos y libera las propiedades del objeto. |

Los métodos de instancia de `WUIModal` (`getElement()`, `getBox()`, `getFooter()`, `getStatus()`, `isOpen()`, `responsive()`) también están disponibles.

#### Clases CSS

| Clase                | Elemento     | Descripción |
| -------------------- | ------------ | ----------- |
| `wuiplugin-selector` | `.wui-modal` | Clase principal del plugin. Identifica el componente. |
| `mobile`             | `.wui-modal` | Activa la presentación modal de tipo móvil en WUIModal. Agregada automáticamente por `init()`. |
| `priority`           | `.wui-modal` | Asigna prioridad de apilamiento (z-index) al modal. Agregada automáticamente por `init()`. |

#### Variables CSS

| Variable                                         | Descripción |
| ------------------------------------------------ | ----------- |
| `--wuiplugin-selector-box-width`                 | Ancho de la caja del selector. |
| `--wuiplugin-selector-box-bgcolor`               | Color de fondo de la caja del selector. |
| `--wuiplugin-selector-option-bordercolor-out`    | Color de borde de la opción en estado normal. |
| `--wuiplugin-selector-option-bordercolor-over`   | Color de borde de la opción en estado hover. |
| `--wuiplugin-selector-option-bgcolor-out`        | Color de fondo de la opción en estado normal. |
| `--wuiplugin-selector-option-bgcolor-over`       | Color de fondo de la opción en estado hover. |
| `--wuiplugin-selector-option-iconcolor-out`      | Color del ícono de la opción en estado normal. |
| `--wuiplugin-selector-option-iconcolor-over`     | Color del ícono de la opción en estado hover. |
| `--wuiplugin-selector-option-iconcolor-disabled` | Color del ícono de la opción deshabilitada. |
| `--wuiplugin-selector-option-textcolor-out`      | Color del texto de la opción en estado normal. |
| `--wuiplugin-selector-option-textcolor-over`     | Color del texto de la opción en estado hover. |
| `--wuiplugin-selector-option-textcolor-selected` | Color del texto de la opción seleccionada (solo cuando `selecteableText = true`). |
| `--wuiplugin-selector-option-textcolor-disabled` | Color del texto de la opción deshabilitada. |
| `--wuiplugin-selector-button-bordercolor`        | Color del borde del pie de botones en modo móvil. |

> [!NOTE]
> Los valores predeterminados de estas variables también estan soportados por WUIPluginThemes. Ver sección [WUIPluginThemes](#WUIPluginThemes).

#### Estructura HTML

El elemento contenedor debe ser un `<div>` con la clase `wui-modal wuiplugin-selector`. La estructura interna es construida automáticamente por `init()`:

```html
<div class="wui-modal wuiplugin-selector mobile priority">
	<div class="box">
		<div class="options">
			<div class="option [selected] [disabled]">
				<div class="icon wui-icon check-line"></div>
				<div class="text [selecteable]">Texto de la opción</div>
			</div>
		</div>
		<div class="footer">
			<button class="wui-button cancel flat wui-language"></button>
			<button class="wui-button submit wui-language"></button>
		</div>
	</div>
</div>
```

#### Implementación

Cabecera HTML:

```html
<link type="text/css" rel="stylesheet" href="./Libraries/WUI/Icon/WUIIcon-0.1.css">
<link type="text/css" rel="stylesheet" href="./Libraries/WUI/Modal/WUIModal-0.2.css">
<link type="text/css" rel="stylesheet" href="./Libraries/WUI/Button/WUIButton-0.2.css">
<link type="text/css" rel="stylesheet" href="./Libraries/WUIPlugins/Selector/WUIPluginSelector-0.2.css">
<script type="text/javascript" src="./Libraries/WUI/Modal/WUIModal-0.2.js"></script>
<script type="text/javascript" src="./Libraries/WUI/Button/WUIButton-0.2.js"></script>
<script type="text/javascript" src="./Libraries/WUIPlugins/Selector/WUIPluginSelector-0.2.js"></script>
```

**Uso programático:**

Código HTML:

```html
<div class="wui-modal wuiplugin-selector my-selector"></div>
```

Código JS:

```js
const init = () => {
	const selector = new WUIPluginSelector({
		selector: ".wui-modal.my-selector",
		acceptText: "Aceptar",
		cancelText: "Cancelar"
	});
	selector.init();
	selector.options = [
		{ icon: null, text: "Opción 1", value: "1", selected: false },
		{ icon: null, text: "Opción 2", value: "2", selected: true },
		{ icon: null, text: "Opción 3", value: "3", selected: false, enabled: false }
	];
	selector.acceptOnClick = (indexes, values, texts) => {
		console.log(values);
	};
	selector.open();
};

window.addEventListener("DOMContentLoaded", init);
```

**Vinculado a un `<select>` nativo (`prepareInput`):**

Código HTML:

```html
<select class="my-select">
	<option value="">— Selecciona —</option>
	<option value="1">Opción 1</option>
	<option value="2">Opción 2</option>
	<option value="3">Opción 3</option>
</select>

<div class="wui-modal wuiplugin-selector my-selector"></div>
```

Código JS:

```js
const init = () => {
	const selector = new WUIPluginSelector({
		selector: ".wui-modal.my-selector",
		acceptText: "aceptar",
		cancelText: "cancelar",
		emptyText: "— selecciona —"
	});
	selector.init();
	selector.prepareInput(document.querySelector(".my-select"), {
		force: false
	});
};

window.addEventListener("DOMContentLoaded", init);
```

> [!NOTE]
> `prepareInput` intercepta el `<select>` únicamente en pantallas móviles (≤767px) salvo que `force` sea `true`. En escritorio, el `<select>` conserva su comportamiento nativo.
