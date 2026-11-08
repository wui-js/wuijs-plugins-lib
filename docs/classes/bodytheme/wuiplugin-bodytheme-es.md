[English](wuiplugin-bodytheme-en.md) | [Español](wuiplugin-bodytheme-es.md)

[wuijs-plugins-lib](../../README-es.md)

# WUIPluginBodyTheme

Versión: `0.16`

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
- `wuiview-datalist` (paquete views): `--wuiview-datalist-header-button-width`, `--wuiview-datalist-header-button-height`, `--wuiview-datalist-mobile-header-button-width` y `--wuiview-datalist-mobile-header-button-height`

## Fuentes

| Tipo | Archivo |
| ---- | ------- |
| CSS  | [src/wui-js/plugins/bodytheme/wuiplugin-bodytheme-0.16.css](https://github.com/wui-js/wuijs-plugins-lib/blob/main/src/wui-js/plugins/bodytheme/wuiplugin-bodytheme-0.16.css) |
| JS   | [src/wui-js/plugins/bodytheme/wuiplugin-bodytheme-0.16.js](https://github.com/wui-js/wuijs-plugins-lib/blob/main/src/wui-js/plugins/bodytheme/wuiplugin-bodytheme-0.16.js) |
| CSS  | [src/wui-js/plugins/bodytheme/default/settings-0.16.css](https://github.com/wui-js/wuijs-plugins-lib/blob/main/src/wui-js/plugins/bodytheme/default/settings-0.16.css) |
| CSS  | [src/wui-js/plugins/bodytheme/default/light-0.16.css](https://github.com/wui-js/wuijs-plugins-lib/blob/main/src/wui-js/plugins/bodytheme/default/light-0.16.css) |
| CSS  | [src/wui-js/plugins/bodytheme/default/dark-0.16.css](https://github.com/wui-js/wuijs-plugins-lib/blob/main/src/wui-js/plugins/bodytheme/default/dark-0.16.css) |
| CSS  | [src/wui-js/plugins/bodytheme/ntapple/settings-0.1.css](https://github.com/wui-js/wuijs-plugins-lib/blob/main/src/wui-js/plugins/bodytheme/ntapple/settings-0.1.css) |
| CSS  | [src/wui-js/plugins/bodytheme/ntapple/light-0.1.css](https://github.com/wui-js/wuijs-plugins-lib/blob/main/src/wui-js/plugins/bodytheme/ntapple/light-0.1.css) |
| CSS  | [src/wui-js/plugins/bodytheme/ntapple/dark-0.1.css](https://github.com/wui-js/wuijs-plugins-lib/blob/main/src/wui-js/plugins/bodytheme/ntapple/dark-0.1.css) |

## Dependencias

| Clase     | Versión | Descripción |
| --------- | :-----: | ----------- |
| `WUIBody` | `0.10`  | Clase base extendida por el plugin. Requerida. |

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
| `ntapple` | Tema inspirado en las guías de interfaz de Apple (versión `0.1`): fuente del sistema, escala tipográfica de macOS (13px) e iOS (17px), superficies neutras, acento azul único, verde para el estado activado, materiales translúcidos y variantes de contraste aumentado. Se recomienda usarlo con `fieldMode: "auto"` en WUIForm, para que en escritorio la etiqueta quede a la izquierda del campo, como en las celdas de iOS y macOS. Archivos en `src/wui-js/plugins/bodytheme/ntapple/` con sufijo `-0.1`. Los botones de la cabecera y el cuerpo de los formularios, y los botones unidos (`join` de WUIButton), usan un contorno suave (`bordercolor-low`); en hover/focus, el texto sobre `bgcolor-over` queda bajo 4,5:1 (4,43 en claro, 3,76 en oscuro) como estado transitorio, igual que el botón `danger`. |

## Variables CSS

Las variables de configuración de tema se definen en el archivo `src/wui-js/plugins/bodytheme/{theme-name}/{version}.css` y se organizan en dos variantes de sufijo: `{variable}-light` para modo claro y `{variable}-dark` para modo oscuro.
Los valores sin sufijo son comunes a ambos modos.

**Colores (con variante por modo de color):**

| Variable base                                                 | Descripción |
| ------------------------------------------------------------- | ----------- |
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
| `--wuiplugin-bodytheme-bgcolor-page-(light\|dark)`            | Color de fondo de la página (`<body>`). |
| `--wuiplugin-bodytheme-bgcolor-overlay-(light\|dark)`         | Color de fondo del overlay. |
| `--wuiplugin-bodytheme-bgcolor-box-(light\|dark)`             | Color de fondo de cuadros de diálogo y paneles. |
| `--wuiplugin-bodytheme-bgcolor-out-(light\|dark)`             | Color de fondo en estado normal. |
| `--wuiplugin-bodytheme-bgcolor-over-(light\|dark)`            | Color de fondo en estado hover o seleccionado. |
| `--wuiplugin-bodytheme-bgcolor-fieldset-(light\|dark)`        | Color de fondo de los conjuntos de campos de `wui-form` (`--wui-form-fieldset-bgcolor`). |
| `--wuiplugin-bodytheme-bgcolor-field-(light\|dark)`           | Color de fondo de los campos editables (`wui-form`, `wui-selectpicker`, `wui-datepicker`, `wui-timepicker`). |
| `--wuiplugin-bodytheme-bgcolor-scroll-(light\|dark)`          | Color de la barra de desplazamiento. |
| `--wuiplugin-bodytheme-bgcolor-icon-(light\|dark)`            | Color de relleno de íconos. |
| `--wuiplugin-bodytheme-bgcolor-highcontrast-(light\|dark)`    | Color de fondo de alto contraste (tooltips, etc.). |
| `--wuiplugin-bodytheme-textcolor-title-(light\|dark)`         | Color de texto de títulos. |
| `--wuiplugin-bodytheme-textcolor-active-(light\|dark)`        | Color de texto en estado activo. |
| `--wuiplugin-bodytheme-textcolor-focus-(light\|dark)`         | Color de texto en estado de foco. |
| `--wuiplugin-bodytheme-textcolor-onaccent-(light\|dark)`      | Color de texto e íconos sobre el color de acento (botones, selecciones). |
| `--wuiplugin-bodytheme-textcolor-highlight-(light\|dark)`     | Color de texto del mensaje destacado de `wui-form` (`--wui-form-message-highlight-textcolor`). |
| `--wuiplugin-bodytheme-utilitycolor-highlight-(light\|dark)`  | Color de realce principal (links, botones, selecciones, `wui-switch` activado). |
| `--wuiplugin-bodytheme-utilitycolor-success-(light\|dark)`    | Color semántico de éxito. |
| `--wuiplugin-bodytheme-utilitycolor-warning-(light\|dark)`    | Color semántico de advertencia. |
| `--wuiplugin-bodytheme-utilitycolor-danger-(light\|dark)`     | Color semántico de peligro o error (botón `danger`, campo inválido, burbuja de `wui-menubar`). |
| `--wuiplugin-bodytheme-utilitycolor-info-(light\|dark)`       | Color semántico de información. |
| `--wuiplugin-bodytheme-utilitycolor-disabled-(light\|dark)`   | Color de elementos deshabilitados. |
| `--wuiplugin-bodytheme-intensitycolor-low-(light\|dark)`      | Color de intensidad baja. |
| `--wuiplugin-bodytheme-intensitycolor-half-(light\|dark)`     | Color de intensidad media. |
| `--wuiplugin-bodytheme-intensitycolor-high-(light\|dark)`     | Color de intensidad alta. |
| `--wuiplugin-bodytheme-code-{name}-(light\|dark)`             | Colores de resaltado de sintaxis de `wui-codebox` (`data-style="theme"`). `{name}`: `command`, `comment`, `string`, `keyword`, `number`, `tag`, `attr`, `selector`, `property`, `function`, `operator`, `variable`, `constant`, `decorator`, `type`, `builtin`, `color` o `regex`. |

**Tipografía y métricas (comunes, sin variante por modo de color):**

| Variable                                      | Valor por defecto                       | Descripción |
| --------------------------------------------- | --------------------------------------- | ----------- |
| `--wuiplugin-bodytheme-borderradius-low`      | `10px`                                  | Radio de borde bajo. |
| `--wuiplugin-bodytheme-borderradius-half`     | `15px`                                  | Radio de borde medio. |
| `--wuiplugin-bodytheme-borderradius-high`     | `17px`                                  | Radio de borde alto. |
| `--wuiplugin-bodytheme-borderradius-round`    | `50%`                                   | Radio de borde circular. |
| `--wuiplugin-bodytheme-titlefont`             | `Arial, Helvetica, Verdana, sans-serif` | Familia tipográfica para títulos. |
| `--wuiplugin-bodytheme-textfont`              | `Arial, Helvetica, Verdana, sans-serif` | Familia tipográfica del texto de la página. |
| `--wuiplugin-bodytheme-textweight`            | `200`                                   | Grosor de fuente del texto de la página. |
| `--wuiplugin-bodytheme-textsize-xsmall`       | `10px`                                  | Escalón de la escala de tamaños de texto. |
| `--wuiplugin-bodytheme-textsize-small`        | `12px`                                  | Escalón de la escala de tamaños de texto. |
| `--wuiplugin-bodytheme-textsize-medium`       | `13px`                                  | Escalón de la escala de tamaños de texto. |
| `--wuiplugin-bodytheme-textsize-normal`       | `14px`                                  | Escalón de la escala de tamaños de texto. |
| `--wuiplugin-bodytheme-textsize-large`        | `15px`                                  | Escalón de la escala de tamaños de texto. |
| `--wuiplugin-bodytheme-textsize-xlarge`       | `17px`                                  | Escalón de la escala de tamaños de texto. |
| `--wuiplugin-bodytheme-textsize-xxlarge`      | `20px`                                  | Escalón de la escala de tamaños de texto. |
| `--wuiplugin-bodytheme-input-opener-iconsize` | `30px`                                  | Tamaño del ícono de apertura en campos de formulario. |
| `--wuiplugin-bodytheme-transition-delay`      | `0.4s`                                  | Duración de la transición de esquema de color. |
| `--wuiplugin-bodytheme-box-filter`            | `blur(10px)`                            | Filtro de fondo (`backdrop-filter`) de las cajas flotantes: modal y selectores. |

> [!NOTE]
> El plugin asocia cada variable de tamaño de texto de los componentes (`--wui-*-textsize`) a un escalón de la escala `--wuiplugin-bodytheme-textsize-*`.

## Estructura del archivo de configuración

Todos los temas comparten la misma estructura de archivo de configuración: los mismos bloques, en el mismo orden, con las mismas variables; solo cambian los valores.

| Bloque                                          | Contenido |
| ----------------------------------------------- | --------- |
| `.wuiplugin-bodytheme.{tema}`                   | Tokens del tema (secciones `global`, `common`, `light mode` y `dark mode`) y la sección `components` con las variables de componentes que dependen del tema. |
| `@media (prefers-contrast: more)`               | Variantes de contraste aumentado de los tokens de gris, borde, texto activo y acento (y éxito en modo oscuro). |
| `@media (prefers-reduced-transparency: reduce)` | Fondo y filtro de la barra móvil de `wui-menubar`. |

El archivo del plugin declara todas las variables de los componentes (las de cada `.root.css` de main, views, lab, data y plugins), con los valores del tema `default` como base. La sección `components` de cada tema las redefine con sus propios valores; el selector `.wuiplugin-bodytheme.{tema}` es más específico que `.wuiplugin-bodytheme`, por lo que el valor del tema prevalece sin depender del orden de carga. El script `tests/css-root-check.py` de wuijs-main-lib verifica que el plugin declare todas las variables de los `.root.css` y ninguna inexistente.

| Componente       | Variable                                       | `default` | `ntapple` |
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
> El script `tests/settings-check.py` compara la estructura de cada tema con la del tema `default` y falla si difieren los bloques, las secciones o el conjunto u orden de las variables.

## Fuente y fondo de página

El plugin aplica `--wuiplugin-bodytheme-textfont` y `--wuiplugin-bodytheme-bgcolor-page` al elemento con la clase `wuiplugin-bodytheme` mediante el selector `:where(.wuiplugin-bodytheme)`, de especificidad cero: cualquier regla de la aplicación sobre `body` tiene precedencia.

## Preferencias de accesibilidad

| Consulta                                        | Efecto |
| ----------------------------------------------- | ------ |
| `@media (prefers-reduced-motion: reduce)`       | Anula las transiciones de modal, paginado, slider y cambio de esquema de color. |
| `@media (prefers-reduced-transparency: reduce)` | Quita el filtro de fondo de las cajas flotantes y vuelve opacas las cajas de `wui-timepicker` y `wui-colorpicker`. Cada tema define además, en su archivo de configuración, el fondo y el filtro de la barra móvil de `wui-menubar`. |
| `@media (prefers-contrast: more)`               | Definida por cada tema en su archivo de configuración (`default` y `ntapple`), con variantes de mayor contraste de sus colores. |

## Implementación

Existen dos modos de implementación:

**Usando archivos CSS generados:**

Utiliza únicamente los archivos CSS generados (`[light|dark]-{versión}.css`) ubicados en el directorio del tema (`src/wui-js/plugins/bodytheme/{nombre}/`).
Recomendado si no se requiere cambiar entre modos claro y oscuro dinámicamente.

Cabecera HTML:

```html
<link type="text/css" rel="stylesheet" href="./libraries/wui-js/plugins/bodytheme/default/dark-0.16.css">
```

Código HTML:

```html
<body class="wuiplugin-bodytheme default dark"></body>
```

**Usando instanciamiento de la clase JS:**

Requiere la implementación de la clase JS `WUIBody`, los archivos JS/CSS del plugin `wuiplugin-bodytheme-0.16.{js,css}` y el archivo CSS de configuración del tema `wui-js/plugins/bodytheme/{nombre}/settings-{versión}.css`.
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
<link type="text/css" rel="stylesheet" href="./libraries/wui-js/main/switch/wui-switch-0.10.css">
<link type="text/css" rel="stylesheet" href="./libraries/wui-js/plugins/bodytheme/wuiplugin-bodytheme-0.16.css">
<link type="text/css" rel="stylesheet" href="./libraries/wui-js/plugins/bodytheme/default/settings-0.16.css">
<script type="text/javascript" src="./libraries/wui-js/main/body/wui-body-0.11.js"></script>
<script type="text/javascript" src="./libraries/wui-js/main/switch/wui-switch-0.10.js"></script>
<script type="text/javascript" src="./libraries/wui-js/plugins/bodytheme/wuiplugin-bodytheme-0.16.js"></script>
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

El script `tools/bodytheme-clone.py` crea un nuevo tema copiando el archivo de configuración de un tema existente: reemplaza su selector CSS (también dentro de los bloques `@media`), los campos `@file`, `@theme` y `@version` de la cabecera y el valor de `--wuiplugin-bodytheme-name`. Es el punto de partida recomendado antes de ejecutar `bodytheme-css-maker.py`.

```bash
python ./bodytheme-clone.py -n <nombre-nuevo-tema>

python ./bodytheme-clone.py -d <directorio-temas> -s <tema-origen> -S <versión-tema-origen> -n <nombre-nuevo-tema> -v <versión-tema>
```

| Opción                      | Predeterminado                    | Descripción |
| --------------------------- | --------------------------------- | ----------- |
| `-d`,<br>`--directory`      | `../src/wui-js/plugins/bodytheme` | Directorio base de temas. |
| `-s`,<br>`--source`         | `default`                         | Nombre del tema a clonar. |
| `-S`,<br>`--source-version` | `0.16`                            | Versión del tema a clonar. |
| `-n`,<br>`--name`           | _(requerido)_                     | Nombre del nuevo tema. |
| `-v`,<br>`--version`        | `0.1`                             | Versión del nuevo tema. |

El archivo de salida se genera en `{directorio}/{nombre}/settings-{versión}.css` con el selector CSS, la cabecera y el nombre del tema actualizados, y con la misma estructura del tema de origen. Al editarlo, cambie solo los valores; `tests/settings-check.py {nombre}` verifica la estructura.

## Herramienta de generación de temas

El script `tools/bodytheme-css-maker.py` crea archivos CSS estandarizados resolviendo todas las referencias a `var()` del archivo fuente, produciendo un CSS plano por cada modo de color. Lee la configuración de variables desde el archivo `{directorio}/{nombre}/settings-{versión}.css`.

Cada archivo generado incluye los tokens del tema resueltos, las variables de los componentes (con las redefiniciones `--wui-*` del archivo de configuración, resolviendo `light-dark()` según el modo), la regla de fuente y fondo de página, los bloques `@media` de preferencias de accesibilidad del plugin y los bloques `@media` del archivo de configuración, con solo los valores que cambian.

```bash
python ./bodytheme-css-maker.py

python ./bodytheme-css-maker.py -p <ruta-css-plugin> -d <directorio-temas> -n <nombre-tema> -v <versión-tema>
```

| Opción                 | Predeterminado                                                 | Descripción |
| ---------------------- | -------------------------------------------------------------- | ----------- |
| `-p`,<br>`--plugin`    | `../src/wui-js/plugins/bodytheme/wuiplugin-bodytheme-0.16.css` | Ruta al archivo CSS fuente del plugin bodytheme. |
| `-d`,<br>`--directory` | `../src/wui-js/plugins/bodytheme`                              | Directorio base de temas. |
| `-n`,<br>`--name`      | `default`                                                      | Nombre del tema. |
| `-v`,<br>`--version`   | `0.16`                                                         | Versión del tema. |

Los archivos de salida se generan en `{directorio}/{nombre}/` con los nombres `light-{versión}.css` y `dark-{versión}.css`.

## Personalización de temas predefinidos

```css
body.wuiplugin-bodytheme.default {
	--wuiplugin-bodytheme-utilitycolor-highlight-light: #e91e63;
    --wuiplugin-bodytheme-utilitycolor-highlight-dark: #f06292;
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
