> [!IMPORTANT]
> La cuenta de GitHub `@wuiproject` se migró a `@wui-js` para que coincidiera con el nombre de la cuenta de NPM.

[English](https://github.com/wui-js/wuijs-plugins-lib/blob/main/docs/CHANGELOG-en.md) |
[Español](https://github.com/wui-js/wuijs-plugins-lib/blob/main/docs/CHANGELOG-es.md)
---

# Registro de Cambios

## [v0.17.0] - 2026-11-07

Características:

1. Se sincronizó la versión con `wuijs-main-lib` `0.17.0`.
2. Se actualizó versión clase WUIPluginBodyTheme a `0.16`.
	- Se actualizó el archivo `wuiplugin-themes-0.16.css` con la actualización de los valores de las variables CSS del componente `WUIForm`.
	- Se agregó el tema `ntapple` `0.1` (`ntapple/settings-0.1.css`, `light-0.1.css` y `dark-0.1.css`), inspirado en las guías de interfaz de Apple.
	- Se agregaron los tokens `--wuiplugin-bodytheme-textfont`, `--wuiplugin-bodytheme-textsize-(xsmall|small|medium|normal|large|xlarge|xxlarge)` y `--wuiplugin-bodytheme-box-filter`, y los tokens por modo `--wuiplugin-bodytheme-bgcolor-page`, `--wuiplugin-bodytheme-textcolor-onaccent` y `--wuiplugin-bodytheme-utilitycolor-success`.
	- Se mapearon las variables nuevas de tamaño de texto y de filtro de fondo de los componentes a la escala `--wuiplugin-bodytheme-textsize-*` y al token `--wuiplugin-bodytheme-box-filter`, y `--wui-button-default-shadow`, `--wui-modal-transition-delay`, `--wui-slider-transition-delay`, `--wui-avatarpicker-preview-size`, `--wui-markdown-iframe-bgcolor` y `--wui-markdown-iframe-textcolor`.
	- El texto y los íconos sobre el color de acento (botones submit/danger y seleccionados, selecciones de los selectores, mensaje destacado de WUIForm, fila seleccionada de WUITable y opciones seleccionadas de WUIMenubar) usan `--wuiplugin-bodytheme-textcolor-onaccent`. En el tema `default` cambian de color la fila seleccionada de WUITable y las opciones seleccionadas de WUIMenubar (`#fff` en claro y `#000` en oscuro).
	- El estado activado de WUISwitch usa `--wuiplugin-bodytheme-utilitycolor-highlight`; el tema `ntapple` lo redefine con `--wuiplugin-bodytheme-utilitycolor-success`.
	- Se renombraron los tokens `utilitycolor-hightlight` a `utilitycolor-highlight`, `utilitycolor-warning` a `utilitycolor-danger` e `intencitycolor-*` a `intensitycolor-*`, y los mapeos `--wui-button-warning-*` y `--wui-modal-button-warning-textcolor-mobile` a `--wui-button-danger-*` y `--wui-modal-button-danger-textcolor-mobile`.
	- Se agregaron los tokens semánticos `utilitycolor-warning` (advertencia) y `utilitycolor-info`, y el token `bgcolor-field`, que reemplaza a `bgcolor-over` en el fondo de los campos de WUIForm, WUISelectpicker, WUIDatepicker y WUITimepicker.
	- Los tamaños de texto de los controles editables en móvil (`--wui-form-mobile-textsize` y `--wui-(selectpicker|datepicker|timepicker)-mobile-viewinput-textsize`) tienen un mínimo de 16px, para evitar la ampliación de Safari en iOS al enfocarlos.
	- El tema `default` define `utilitycolor-success` en `#22c55e`, `utilitycolor-warning` en `#f59e0b` y `utilitycolor-info` en `#1e90ff`, y `utilitycolor-danger` cambia de `#f44343` a `#ef4444`; `bgcolor-field` conserva el valor de `bgcolor-over`.
	- El tema `ntapple` usa el patrón agrupado de iOS: fondo de cuadros `#f2f2f7`/`#1c1c1e`, conjuntos de campos `#fff`/`#2c2c2e` (nivel elevado en modo oscuro), campos `#e5e5ea`/`#38383a`, hover `#e5e5ea`/`#3a3a3c` y fondo de página claro `#f2f2f7`. `graycolor-low` cambia a `#636366`/`#aeaeb2` y el título del mes de WUIDatepicker usa `graycolor-low`, para un contraste mínimo de 4,5:1.
	- Se mapearon las variables nuevas `--wui-modal-footer-justify` y `--wui-button-default-borderradius`; en el tema `default` reproducen el aspecto anterior.
	- El tema `ntapple` dibuja los botones unidos (`join`) como un control segmentado (fondo de campo, contorno continuo y separadores), el botón `danger` como texto rojo sobre el fondo de campo, las listas y tablas con sombra suave al 10% y los botones del pie del modal alineados a la derecha en escritorio. Se recomienda usarlo con `fieldMode: "auto"` en WUIForm.
	- Se mapearon `--wui-list-shadow` y `--wui-table-shadow` (antes `--wui-list-shadowcolor` y `--wui-table-shadowcolor`) y las variables móviles nuevas de WUIMenubar, y `--wui-list-button-bgcolor-danger` a `--wuiplugin-bodytheme-utilitycolor-danger` (en `ntapple` la acción destructiva de fila queda en relleno rojo con ícono blanco, como las acciones de deslizamiento de iOS).
	- El tema `ntapple` dibuja la barra móvil de WUIMenubar como la barra de pestañas flotante de iOS: cápsula, botones en cápsula, fondo translúcido al 72% con el filtro `--wuiplugin-bodytheme-box-filter`, y fondo opaco sin filtro con `prefers-reduced-transparency`.
	- Se corrigió la herramienta `bodytheme-css-maker.py`: en los bloques `@media` del archivo de configuración, las redefiniciones de componentes se escribían dos veces.
	- Todos los temas comparten la misma estructura de archivo de configuración (mismos bloques, secciones y variables en el mismo orden; solo cambian los valores). Las 28 variables de componentes que dependen del tema (sección `components`) dejan de asignarse en `wuiplugin-bodytheme-0.16.css` y cada tema las declara; el tema `default` lo hace con los valores anteriores, sin cambio visual. El tema `default` agrega los bloques `@media (prefers-contrast: more)`, con variantes de contraste aumentado de gris, borde, texto activo, acento y éxito, y `@media (prefers-reduced-transparency: reduce)`. Se agregó la verificación `tests/settings-check.py`, que compara la estructura de cada tema con la de `default`.
	- Se asignan las variables de `wuiview-datalist` (`--wuiview-datalist-header-button-width`, `--wuiview-datalist-header-button-height`, `--wuiview-datalist-mobile-header-button-width` y `--wuiview-datalist-mobile-header-button-height`), para las aplicaciones que no cargan los archivos `.root.css`; `--wuiview-datalist-header-button-height` toma el valor de `--wui-form-input-height`, para igualar el alto del campo de búsqueda. `--wui-form-input-height` cambia de `30px` a `32px`, como en WUIForm. La herramienta `bodytheme-css-maker.py` conserva en los archivos estáticos las variables `--wuiview-*`.
	- Se mapearon los nombres normalizados de margin/padding (`*-horizontalpadding`, `*-verticalpadding`) de `wui-button`, `wui-menubar`, `wui-selectpicker` y `wui-tree`, y la variable nueva `--wui-modal-footer-horizontalmargin` en la sección `components` de los temas (`default` `5px`; `ntapple` `20px`, para separar del borde los botones alineados a la derecha en escritorio). En `default`, `utilitycolor-danger-dark` cambia de `#ef4444` a `#f15757` (contraste 3,06:1 sobre el fondo de página oscuro `#374151`, antes 2,74:1).
	- En el tema `ntapple`, el grupo `join` tiene un contorno continuo en estado normal: el borde de los botones habilitados, `submit`, `danger` y deshabilitados, y los separadores, usan el tono suave `bordercolor-low` (`#e5e5ea` / `#38383a`), igual sobre el campo y sobre la página (por ejemplo, la cabecera de `wuiview-datalist`). En hover/focus, el botón `danger` del grupo mantiene el contorno con su color de acento (`utilitycolor-danger`) y los botones sin estilo `submit` ni `danger` toman el fondo `bgcolor-over`. El segmento seleccionado usa el color de acento (`--wui-button-join-bgcolor-selected` = `utilitycolor-highlight`) y el deshabilitado conserva el fondo de campo (`--wui-button-join-bgcolor-disabled` = `bgcolor-field`), sin dejar un hueco en el grupo. En los dos temas, los separadores de un segmento seleccionado toman el color de borde seleccionado (`--wui-button-join-separatorcolor-selected` = `--wui-button-default-bordercolor-selected`) y ocupan todo el alto, para que no se vea una línea clara junto al segmento. Fuera de un grupo, `danger` sigue sin borde. En `default`, cada variante conserva su borde y fondo.
	- La herramienta `bodytheme-css-maker.py` resuelve en dos pasadas las redefiniciones que referencian otras redefiniciones del tema.
	- Se mapearon `--wui-form-button-*` (colores de los botones de la cabecera y el cuerpo de WUIForm) y `--wui-button-join-*` (botones unidos con la propiedad `join` de WUIButton), que reemplazan `--wui-form-joinbuttons-*`. En `default` apuntan a las variables de cada variante de WUIButton y reproducen el aspecto anterior; en `ntapple` conservan los valores de los botones unidos, que ahora también toman los botones sueltos de la cabecera y el cuerpo de los formularios. `--wui-button-join-separator-verticalmargin` (`5px`) se asigna en el núcleo.
	- El archivo del plugin declara todas las variables de los componentes, también las que antes solo estaban en la sección `components` de cada tema (45: `wui-button`, `wui-form`, `wui-switch`, `wui-menubar`, `wui-modal`, `wui-table`, `wui-list` y `wui-datepicker`), con los valores del tema `default` como base; cada tema las sigue redefiniendo. Se agregaron los comentarios de sección de `wui-tree`, `wui-avatarpicker`, `wui-markdown` y `wui-codebox`. El script `tests/css-root-check.py` de wuijs-main-lib verifica que el plugin declare todas las variables de los `.root.css` de main, views, lab, data y plugins, y ninguna inexistente.
	- El tema `ntapple` mantiene el fondo del botón `danger` en hover/focus (`--wui-button-danger-bgcolor-over` = `bgcolor-field`, igual que en reposo), sin el gris de hover.
	- En el tema `ntapple`, el texto y el ícono del botón `danger` en hover/focus usan el rojo al 75% (`--wui-button-danger-textcolor-over`), como señal sutil sin cambiar el fondo; contraste 4,16:1 en claro y 3,39:1 en oscuro.
	- Se renombraron los tokens `--wuiplugin-bodytheme-token-*` a `--wuiplugin-bodytheme-code-*`. Se mapean a `--wui-codebox-code-*` y se aplican con el estilo `data-style="theme"` de WUICodebox.
	- La fuente y el fondo de la página se aplican con el selector `:where(.wuiplugin-bodytheme)`, de especificidad cero.
	- Se agregaron los bloques `@media (prefers-reduced-motion: reduce)` y `@media (prefers-reduced-transparency: reduce)`.
	- Se eliminaron 24 mapeos de variables inexistentes: las del plugin `wuiplugin-selector` y `--wui-selectpicker-box-button-*-(selected|disabled)`.
	- El tema `default` toma de la aplicación de referencia (SaaSKit) los valores de `--wuiplugin-bodytheme-textfont` y `--wuiplugin-bodytheme-bgcolor-page`, y conserva sus colores.
	- El tema `ntapple` agrega la escala tipográfica de macOS e iOS, materiales translúcidos, botones sin sombra, campos de 17px en móvil, colores de resaltado de sintaxis del estilo Xcode y un bloque `@media (prefers-contrast: more)`.
	- Los archivos estáticos (`light-*.css` y `dark-*.css`) incluyen los tokens resueltos, las redefiniciones de componentes del tema, la regla de fuente y fondo de página y los bloques `@media`. Se corrigió error: la cabecera copiaba el archivo de configuración completo dentro del archivo generado.
	- Se corrigió la herramienta `bodytheme-css-maker.py` (cabecera, redefiniciones de componentes, regla de página y bloques `@media`) y la herramienta `bodytheme-clone.py` (selector `.wuiplugin-bodytheme`, opción `--source-version`, cabecera y nombre del tema).
	- Se agregaron los tokens `--wuiplugin-bodytheme-textweight` (grosor de fuente de la página; `default` `200`, `ntapple` `300`), `--wuiplugin-bodytheme-bgcolor-fieldset-(light|dark)` (fondo de los conjuntos de campos de WUIForm) y `--wuiplugin-bodytheme-textcolor-highlight-(light|dark)` (texto del mensaje destacado de WUIForm, que antes usaba `textcolor-onaccent`).
	- Se mapearon `--wui-modal-box-shadow`, `--wui-modal-box-bordercolor`, `--wui-menubar-shadow` (reemplaza a `--wui-menubar-shadowcolor` y `--wui-menubar-shadowopacity`), `--wui-menubar-bar-bordercolor`, `--wui-menubar-mobile-bar-height`, `--wui-menubar-mobile-bar-button-width` y `--wui-form-legend-texttransform` en la sección `components` de los temas, y en el archivo del plugin `--wui-form-fieldset-bgcolor`, `--wui-form-fieldset-borderradius`, `--wui-form-message-shadow`, `--wui-menubar-mobile-bar-button-height`, `--wui-selectpicker-box-option-textsize` y `--wui-selectpicker-mobile-box-option-textsize`. En `default` reproducen los valores de los componentes, salvo `--wui-form-legend-texttransform` (`none`). En `ntapple`, el modal, la barra de menú, las listas y las tablas usan sombra suave al 10% y borde al 20%, y la barra móvil de WUIMenubar mide 46px con botones de 62px de ancho.
	- El tema `ntapple` antepone la fuente `SanFrancisco` a la pila de fuentes del sistema en `titlefont` y `textfont`, y `utilitycolor-success-light` cambia a `#34c759`.
	- Los bloques de `wui-tree`, `wui-codebox` y `wui-markdown`, graduadas hacia `wuijs-main-lib` `0.17.0`, y el de `wui-avatarpicker` dejan de marcarse como clases del paquete lab, en el archivo del plugin, en los archivos estáticos y en la lista de componentes cubiertos.
	- Se mapearon las variables móviles renombradas de WUIModal: `--wui-modal-mobile-button-submit-bgcolor`, `--wui-modal-mobile-button-submit-textcolor` y `--wui-modal-mobile-button-danger-textcolor`.
3. Se actualizó versión clase WUIPluginFormValidation a `0.4`.
	- Se normalizó el código JS: el ícono de mostrar u ocultar contraseña se asigna con `classList.toggle()` según el tipo final del campo.
4. Se actualizó versión clase WUIPluginFormHttp a `0.2`.
	- Se normalizó el código JS: `typeof` con paréntesis.
	- Se corrigió error: `submitJson()` enviaba solo la última opción de un `<select multiple>`, como string. Ahora lo envía como arreglo con todas sus opciones seleccionadas.

## [v0.16.1] - 2026-10-16

Características:

1. Se sincronizó la versión con `wuijs-main-lib` `0.16.1`.
2. Se actualizaron los enlaces a la documentación de `WUIForm` hacia su archivo de clase en `wuijs-main-lib` (`docs/classes/form/wui-form-es.md`).

## [v0.16.0] - 2026-10-08

Características:

1. Se sincronizó la versión con `wuijs-main-lib` `0.16.0`.
2. Se actualizó versión clase WUIPluginBodyTheme a `0.15`.
	- Se actualizó el archivo `wuiplugin-themes-0.15.css` con la actualización de los valores de las variables CSS del componente `WUISelectpicker`.

## [v0.15.0] - 2026-09-27

Características:

1. Se sincronizó la versión con `wuijs-main-lib` `0.15.0`.
2. Se actualizó versión clase WUIPluginFormValidation a `0.3`.
	- Se corriguó error en método `prepare()`.

## [v0.14.1] - 2026-09-08

Características:

1. Se sincronizó la versión con `wuijs-main-lib` `0.14.1`.
2. Se agregó el script `prepare` a `package.json` para que una instalación vía tag de git (`npm install github:wui-js/wuijs-plugins-lib#vX.Y.Z`) produzca la misma estructura de archivos aplanada que una instalación desde el registro de npm.

## [v0.14.0] - 2026-09-01

Características:

1. Se sincronizó la versión con `wuijs-main-lib` `0.14.0`.
2. Se actualizó versión clase WUIPluginBodyTheme a `0.13`.
	- Se actualizó el archivo `wuiplugin-themes-0.13.css` con la actualización de los valores de las variables CSS de los componentes `WUITabs` y `WUIList`.

## [v0.13.2] - 2026-08-22

Características:

1. Se sincronizó la versión con `wuijs-main-lib` `0.13.2`.
2. Se actualizó versión clase WUIPluginFormValidation a `0.2`.
	- Se agregó método `reset()`.
	- Se agregó método `resetAll()`.
	- Se agregó soporte para entradas de datos de tipo arreglo (`[name="...[]"]`), en concordancia con el parámetro `position` agregado en `WUIForm` `0.11`.

## [v0.13.1] - 2026-07-20

Características:

1. Se sincronizó la versión con `wuijs-main-lib` `0.13.1`.
2. Se actualizó versión clase WUIPluginBodyThemes (ex WUIPluginThemes) a `0.12`.
	- Se convirtió la clase en una extensión de la clase `WUIBody` de la librería `wuijs-main-lib`.
	- Se renombró la clase de `WUIPluginThemes` a `WUIPluginBodyThemes`.
	- Se renombró los prefijos de las variables CSS de `--wuiplugin-theme(s)*` a `--wuiplugin-bodytheme*`.
	- Se eliminó la variable CSS `--wui-selectpicker-box-button-textsize`.
	- Se renombró la herramienta `css-theme-maker.py` a `bodytheme-css-maker.py`.
	- Se renombró la herramienta `clone-theme.py` a `bodytheme-clone.py`.
3. Se agregó classe WUIPluginFormValidation versión `0.1`.
4. Se agregó clase WUIPluginFormHttp versión `0.1`.
5. Se deprecó clase WUIPluginSelector.

## [v0.12.0] - 2026-06-24

Características:

1. Se sincronizó la versión con `wuijs-main-lib` `0.12.0`.
2. Se actualizó versión clase WUIPluginThemes a `0.11`.
	- Se refactorizó el código JS.
	- Se agregó la funcionalidad de agregar distintos temas en distintos elementos de un mismo documento HTML.

## [v0.11.0] - 2026-06-12

Características:

1. Se sincronizó la versión con `wuijs-main-lib` `0.11.0`.
2. Se actualizó versión clase WUIPluginThemes a `0.10`.
	- Se actualizó el archivo `wuiplugin-themes-0.10.css` con la actualización de los valores de las variables CSS de los componentes `WUITabs`, `WUIMenubar` y `WUIButton`.

## [v0.10.0] - 2026-06-01

Características:

1. Se sincronizó la versión con `wuijs-main-lib` `0.10.0`.

## [v0.9.2] - 2026-05-28

Características:

1. Se sincronizó la versión con `wuijs-main-lib` `0.9.2`.

## [v0.9.1] - 2026-05-28

Características:

1. Se sincronizó la versión con `wuijs-main-lib` `0.9.1`.

## [v0.9.0] - 2026-05-28

Características:

1. Se sincronizó la versión con `wuijs-main-lib` `0.9.0`.

> [!IMPORTANT]
> Se sugiere reemplazar el uso de `WUIPluginSelector` por em modo `hidden` de `WUISelectpicker` introducido en la versión `0.8` del componente y versión `0.8.1` de `wuijs-main-lin`.
> El plugin `WUIPluginSelector` será deprecado en las seguientes versiones.

## [v0.8.1] - 2026-05-28

Características:

1. Se sincronizó la versión con `wuijs-main-lib` `0.8.1`.

## [v0.8.0] - 2026-05-26

Características:

1. Se sincronizó la versión con `wuijs-main-lib` `0.8.0`.
2. Se actualizó versión clase WUIPluginThemes a `0.8`.
	- Se actualizó el archivo `wuiplugin-themes-0.8.css` con la actualización de los valores de las variables CSS de tipo `scroll`.

## [v0.7.1] - 2026-05-16

Características:

1. Se sincronizó la versión con `wuijs-main-lib` `0.7.1`.
2. Se actualizó versión clase WUIPluginThemes a `0.7`.
	- Se actualizó el archivo `wuiplugin-themes-0.7.css` con los valores por defecto de las variables CSS de los componentes `wui-menubar`, `wui-selectpicker`, `wui-datepicker` y `wui-timepicker`.

## [v0.7.0] - 2026-05-14

Características:

1. Se sincronizó la versión con `wuijs-main-lib` `0.7.0`.
2. Se actualizó versión clase WUIPluginSelector a `0.4`.
	- Se agregó archivo `.root.css` con los valores por defecto de las variables CSS.

## [v0.6.2] - 2026-05-08

Características:

1. Se sincronizó la versión con `wuijs-main-lib` `0.6.2`.

## [v0.6.1] - 2026-05-06

Características:

1. Se sincronizó la versión con `wuijs-main-lib` `0.6.1`.
2. Liberación del sitio oficial de documentación de WUI/JS: [https://docs.wuijs.dev](https://docs.wuijs.dev)
3. Se actualizó versión clase WUIPluginThemes a `0.6`.
	- Se agregó la variable CSS asociadas al componente `wui-codebox` (paquete lab).
	- Se agregó la variable CSS asociadas al componente `wui-markdown` (paquete lab).
	- Se sincronizó la versión del template `default` con el de la versión del plugin.

## [v0.6.0] - 2026-05-01

Características:

1. Se sincronizó la versión con `wuijs-main-lib` `0.6.0`.
2. Se actualizó versión clase WUIPluginThemes a `0.5`.
	- Se agregó la variable CSS `--wui-table-width`.
	- Se agregó la variable CSS `--wui-table-column-bordercolor-disabled`.
	- Se agregó la variable CSS `--wui-table-column-bgcolor-disabled`.
	- Se agregó la variable CSS `--wui-button-default-borderwidth`.
	- Se agregó la variable CSS `--wui-button-default-horizpadding`.
	- Se agregó la variable CSS `--wui-button-default-vertpadding`.
	- Se agregó la variable CSS `--wui-button-mobile-default-minwidth`.
	- Se renombró la variable CSS `--wui-table-column-bordercolor-width` a `--wui-table-column-borderwidth`.
	- Se eliminó la variable CSS `--wui-switch-bordercolor-invalid`.

## [v0.5.2] - 2026-04-19

Características:

1. Se sincronizó la versión de la librería `wuijs-plugins-lib` con la de `wuijs-main-lib` con el fin de mantener la integridad del proyecto y mejorar la lectura de compatibilidad entre librerías.
2. Se actualizó versión clase WUIPluginThemes a `0.4`.
	- Se agregó la variable CSS `--wui-modal-mobile-page-box-topmargin` para mejorar compatibilidad con pantallas iPhone.
	- Se agregó la variable CSS `--wui-modal-mobile-page-box-borderradius-maximized` para mejorar compatibilidad con pantallas iPhone.
	- Se agregó la variable CSS `--wui-menubar-mobile-bar-horizpadding` para mejorar compatibilidad con pantallas iPhone.
	- Se agregó la variable CSS `--wui-menubar-mobile-bar-vertpadding` para mejorar compatibilidad con pantallas iPhone.

## [v0.4.0] - 2026-04-09

Características:

> [!NOTE]
> Se cambió el dueño del repositorio oficial de **@wuijsproject** a **@wui-js** con el fin de tener integridad entre las cuentas en GitHub y NPM.

1. Habilitación de instalación vía NPM.
2. Cambio de nombre del directorio fuente de `src/wuiplugins` a `src/wui-js/plugins` para dar soporte a integración con otras librerías del proyecto WUI/JS.
3. Se actualizó versión clase WUIPluginThemes a `0.3`.
	- Se agregó la variable global CSS `--wuiplugin-theme-name` para identificar el tema activo.
	- Se actualizó el método `getTheme()` para que devuelva el valor de la variable global CSS `--wuiplugin-theme-name` del tema activo.

## [v0.3.0] - 2026-03-20

Características:

1. Se renombraron los directorios y archivos fuente a minúscula (ej: `src/WUIPlugin/Themes/WUIPluginTheme-0.1.js` → `src/wuiplugin/themes/wuiplugin-themes-0.2.js`).
2. Se agregó la carpeta `legacy/` con versiones anteriores de los archivos fuente (`WUIPluginThemes-0.1`, `WUIPluginSelector-0.2`).
3. Se renombró el directorio `src/wuiplugin/` (antes `src/WUIPlugins/`) para usar una convención de nombres en minúscula consistente.
4. Se renombró el directorio `legacy/WUIPlugin/` (antes `legacy/WUIPlugins/`) para usar una convención de nombres en singular consistente.
5. Se actualizó versión clase WUIPluginThemes a `0.2`.
	- Se renombró el directorio y archivos a minúscula.
	- Se cambió la opacidad de la variable CSS `--wui-modal-message-box-bgcolor` de `80%` a `100%` en el tema base.
6. Se actualizó versión clase WUIPluginSelector a `0.3`.
	- Se renombró el directorio y archivos a minúscula.

## [v0.1.0] - 2025-10-15

Características:

1. Versión de lanzamiento.