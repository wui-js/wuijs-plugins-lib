> [!NOTE]
> For the English version of this document, see [README.md](./README.md).

# wuijs-plugins-lib

<div align="center">
	<img src="https://github.com/wui-js/wuijs-plugins-lib/blob/main/imgs/logo/wuijs-plugins-logotype-color.svg" width="220" height="220">
</div>

Versión librería: `0.4.0` ([Change Log](./REGISTRODECAMBIO.md))

Versión documentación: `0.4.0.20260409.0`

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
*   [Demos](#demos) (CodeSandbox)

<a name="overview"></a>

## Descripción General

WUI/JS Plugins Lib es una librería JavaScript/CSS de código abierto que proporciona una colección de complementos para las clases de WUI/JS Lib, lo que facilita el desarrollo rápido de aplicaciones web.

### Tabla de Plugins

| Nombre Plugin                           | Versión | Descripción |
| --------------------------------------- | -------:| ----------- |
| [WUIPluginThemes](#WUIPluginThemes)     | `0.3`   | Plugin para el manejo de temas prediseñados y modo claro y oscuro. |
| [WUIPluginSelector](#WUIPluginSelector) | `0.3`   | Selector modal basado en WUIModal. |

### Mapa de Directorios

```bash
wuijs-plugins-lib/
├── imgs/
│   └── logo/
├── legacy/
│   └── wuiplugin/
└── src/
    └── wui-js/
        └── plugins/
```

| Ruta                                      | Descripción |
| ----------------------------------------- | ----------- |
| [imgs](imgs/)                             | Imágenes utilizadas en la documentación. |
| [imgs/logo](imgs/logo/)                   | Logotipo e isotipo del proyecto en formato SVG y PNG. |
| [legacy](legacy/)                         | Fuentes obsoletas con versiones anteriores. |
| [legacy/wuiplugin](legacy/wuiplugin/)     | Librería WUI/JS Plugins. |
| [src](src/)                               | Fuentes principales de la última versión. |
| [src/wui-js](src/wui-js)                  | Directorio del proyecto WUI/JS. |
| [src/wui-js/plugins](src/wui-js/plugins/) | Librería de plugins WUI/JS. |

<a name="install"></a>

## Instalación

**Opción 1: Instalar desde fuente**

Para instalar la biblioteca WUI/JS Plugins, debe ser clonada desde el repositorio oficial en GitHib (`wui-js/wuijs-plugins-lib`).
Suponiendo que el proyecto donde se implementará tenga un directorio de código fuente `./src` y, dentro de este, un directorio de librerías `./src/libraries`, debe escribir lo siguiente en la terminal:

```bash
git clone https://git@github.com/wui-js/wuijs-plugins-lib.git
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

<a name="plugins"></a>

## Plugins

<a name="WUIPluginThemes"></a>

### WUIPluginThemes

Versión: `0.3`

Plugin para el manejo de temas prediseñados y modo claro y oscuro.

#### Descripción

WUIPluginThemes provee un sistema de temas para aplicaciones web mediante dos capas de variables CSS:

- **Configuración de tema** (`--wuiplugin-theme-*`): tokens de color, tipografía y espaciado, con variantes explícitas para modo claro (`-light`) y oscuro (`-dark`), además de valores comunes sin sufijo.
- **Variables de componentes** (`--wui-*` y `--wuiplugin-*`): variables consumidas por los componentes de WUI/JS Lib, definidas como referencias a las variables de configuración del tema mediante la función `var()`.

#### Componentes cubiertos

WUIPluginThemes provee soporte de temas para los siguientes componentes de WUI/JS Lib:

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

> [!NOTE]
> Los archivos de temas (CSS pregenerados y configuración) se distribuyen como paquete independiente: [wuijs-themes-lib](https://github.com/wui-js/wuijs-themes-lib). Instálalo con `npm i @wui-js/themes`.

#### Fuentes

| Tipo | Archivo |
| ---- | ------- |
| CSS  | [src/wui-js/plugins/themes/wuiplugin-themes-0.3.css](https://github.com/wui-js/wuijs-plugins-lib/blob/main/src/wui-js/plugins/themes/wuiplugin-themes-0.3.css) |
| JS   | [src/wui-js/plugins/themes/wuiplugin-themes-0.3.js](https://github.com/wui-js/wuijs-plugins-lib/blob/main/src/wui-js/plugins/themes/wuiplugin-themes-0.3.js) |

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
| getTheme         | `string`    | `getTheme()`<br><br>Retorna el nombre del tema activo según las clases CSS presentes en `document.body`. |
| setScheme        | `void`      | `setScheme(scheme)`<br><br>Establece el esquema de color de la aplicación. Actualiza las clases CSS en `document.body` y el atributo `color-scheme` en el elemento `<html>`. Si el esquema nuevo difiere del actual, activa automáticamente la transición de fondo. La duración de la transición está controlada por la variable CSS `--wuiplugin-theme-transition-delay` (valor por defecto: `0.4s`). Valores posibles: `"light"`, `"dark"`, `"light dark"`, `"system"`. |

#### Implementación

Existen dos modos de implementación:

**Usando archivos CSS pregenerados:**

Utiliza únicamente los archivos CSS predefinidos (`[light|dark]-{versión}.css`) de [wuijs-themes-lib](https://github.com/wui-js/wuijs-themes-lib), ubicados en `node_modules/@wui-js/themes/{nombre}/` o en `src/wui-js/themes/{nombre}/` si se instaló desde fuente.
Recomendado si no se requiere cambiar entre modos claro y oscuro dinámicamente.

Cabecera HTML:

```html
<link rel="stylesheet" href="./libreries/wui-js/themes/default/light-0.2.css">
```

Código HTML:

```html
<body class="wuiplugin-themes default light"></body>
```

**Usando instanciamiento de la clase JS:**

Requiere la implementación de la clase JS `WUIPluginThemes`, el archivo CSS fuente `wuiplugin-themes-0.3.css` y el archivo CSS de configuración del tema `theme-{versión}.css` de [wuijs-themes-lib](https://github.com/wui-js/wuijs-themes-lib).
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
<link rel="stylesheet" href="./libraries/wui-js/main/switch/wui-switch-0.4.css">
<link rel="stylesheet" href="./libraries/wui-js/plugins/themes/wuiplugin-themes-0.3.css">
<link rel="stylesheet" href="./libraries/wui-js/themes/default/theme-0.2.css">
<script type="text/javascript" src="./libraries/wui-js/main/switch/wui-switch-0.4.js"></script>
<script type="text/javascript" src="./libraries/wui-js/plugins/themes/wuiplugin-themes-0.3.js"></script>
```

Código HTML:

```html
<body class="wuiplugin-themes default light">
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
> Puede revisar este ejemplo funcional en CodeSandbox en el enlace: [https://codesandbox.io/p/sandbox/github/wui-js/wuijs-lab/tree/main/demos/plugin/themes/switchmode](https://codesandbox.io/p/sandbox/github/wui-js/wuijs-lab/tree/main/demos/plugin/themes/switchmode).

#### Personalización de temas predefinidos

```css
body.wuiplugin-themes.default {
	--wuiplugin-theme-utilitycolor-hightlight-light: #e91e63;
    --wuiplugin-theme-utilitycolor-hightlight-dark: #f06292;
    --wuiplugin-theme-bgcolor-out-light: #fff8f9;
    --wuiplugin-theme-bgcolor-out-dark: #1a0a0d;
}
```

> [!IMPORTANT]
> Para que los cambios sean aplicados es importante incluir el elemento raíz, en este caso `<body>`, con la clase `wuiplugin-themes` y el nombre del tema, de esta manera la definición tendrá mayor especificidad y se aplicará sobre las definiciones del tema especificado.

> [!TIP]
> Para mantener el estándar propuesto por la documentación de la librería WUI/JS, esta personalización puede realizarse en el archivo `WUI.css`.

> [!TIP]
> Puede revisar este ejemplo funcional en CodeSandbox en el enlace: [https://codesandbox.io/p/sandbox/github/wui-js/wuijs-lab/tree/main/demos/plugin/themes/customtheme](https://codesandbox.io/p/sandbox/github/wui-js/wuijs-lab/tree/main/demos/plugin/themes/customtheme).

```html
<body class="wuiplugin-themes default light"></body>
```

<a name="WUIPluginSelector"></a>

### WUIPluginSelector

Versión: `0.3`

Selector modal de lista de opciones basado en WUIModal.

#### Descripción

WUIPluginSelector extiende `WUIModal` e implementa un selector de lista de opciones de tipo modal.
Está optimizado para entornos móviles e intercepta el evento táctil sobre elementos `<select>` nativos para reemplazar el selector del sistema por un panel de selección personalizado.
También puede utilizarse de forma programática independientemente de un input nativo `<select>` en entornos responsivos.

> [!NOTE]
> La documentación completa de `WUIModal` se encuentra en el proyecto wuijs-lib en el enlace: [https://github.com/wui-js/wuijs-lib/blob/main/README.md#WUIModal](https://github.com/wui-js/wuijs-lib/blob/main/README.md#WUIModal).

#### Dependencias

| Clase       | Versión | Descripción |
| ----------- | :-----: | ----------- |
| `WUIModal`  | `0.3`   | Clase base del modal. Requerida. |
| `WUIButton` | `0.3`   | Utilizada internamente para los botones de aceptar y cancelar. Requerida. |
| `WUIIcon`   | `0.2`   | Requerida para el ícono de las opciones seleccionadas. |

#### Fuentes

| Tipo | Archivo |
| ---- | ------- |
| CSS  | [src/wui-js/plugins/selector/wuiplugin-selector-0.3.css](https://github.com/wui-js/wuijs-plugins-lib/blob/main/src/wui-js/plugins/selector/wuiplugin-selector-0.3.css) |
| JS   | [src/wui-js/plugins/selector/wuiplugin-selector-0.3.js](https://github.com/wui-js/wuijs-plugins-lib/blob/main/src/wui-js/plugins/selector/wuiplugin-selector-0.3.js) |

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
<link type="text/css" rel="stylesheet" href="./libraries/wui/icon/wui-icon-0.2.css">
<link type="text/css" rel="stylesheet" href="./libraries/wui/modal/wui-modal-0.3.css">
<link type="text/css" rel="stylesheet" href="./libraries/wui/button/wui-button-0.3.css">
<link type="text/css" rel="stylesheet" href="./libraries/wuiplugin/selector/wuiplugin-selector-0.3.css">
<script type="text/javascript" src="./libraries/wui/modal/wui-modal-0.3.js"></script>
<script type="text/javascript" src="./libraries/wui/button/wui-button-0.3.js"></script>
<script type="text/javascript" src="./libraries/wuiplugin/selector/wuiplugin-selector-0.3.js"></script>
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
		acceptText: "aceptar",
		cancelText: "cancelar"
	});
	selector.init();
	selector.options = [
		{ icon: null, text: "opción 1", value: "1", selected: false },
		{ icon: null, text: "opción 2", value: "2", selected: true },
		{ icon: null, text: "opción 3", value: "3", selected: false, enabled: false }
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
	<option value="">— selecciona —</option>
	<option value="1">opción 1</option>
	<option value="2">opción 2</option>
	<option value="3">opción 3</option>
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

<a name="demos"></a>

## Demos

Esta sección recoge los ejemplos de las implementaciones de la documentación y otros demos complementarios, todos disponibles en el repositorio **WUI/JS Lab** [https://github.com/wui-js/wuijs-lab](https://github.com/wui-js/wuijs-lab).

1.	[https://codesandbox.io/p/sandbox/github/wui-js/wuijs-lab/tree/main/demos/plugin/themes/switchmode](https://codesandbox.io/p/sandbox/github/wui-js/wuijs-lab/tree/main/demos/plugin/themes/switchmode)<br>
	Esta demostración muestra el uso de la funcionalidad de cambiar entre modo claro y oscuro de WUIPluginThemes.<br><br>
2.	[https://codesandbox.io/p/sandbox/github/wui-js/wuijs-lab/tree/main/demos/plugin/themes/customtheme](https://codesandbox.io/p/sandbox/github/wui-js/wuijs-lab/tree/main/demos/plugin/themes/customtheme)<br>
	Esta demostración muestra el uso de los temas predefinidos personalizados de WUIPluginThemes.<br><br>

> [!NOTE]
> Todos los demos del repositorio [wuijs-lab](https://github.com/wui-js/wuijs-lab) se pueden revisar en CodeSandbox en el enlace [https://codesandbox.io/p/sandbox/github/wui-js/wuijs-lab/tree/main/demos/wuiplugin](https://codesandbox.io/p/sandbox/github/wui-js/wuijs-lab/tree/main/demos/wuiplugin).
