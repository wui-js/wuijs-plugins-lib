# Registro de Cambios

## [v0.4.0] - 2026-04-09

Características:

> [!NOTE]
> Se cambió el dueño del repositorio oficial de **@wuijsproject** a **@wui-js** con el fin de tener integridad entre las cuentas en GitHub y NPM.

1. Habilitación de instalación vía NPM.
2. Cambio de nombre del directorio fuente de `src/wuiplugins` a `src/wui-js/plugins` para dar soporte a integración con otras librerías del proyecto WUI/JS.
3. Actualización versión clase WUIPluginThemes a 0.3.
	- Se agregó la variable global CSS `--wuiplugin-theme-name` para identificar el tema activo.
	- Se actualizó el método `getTheme()` para que devuelva el valor de la variable global CSS `--wuiplugin-theme-name` del tema activo.

## [v0.3.0] - 2026-03-20

Características:

1. Se renombraron los directorios y archivos fuente a minúscula (ej: `src/WUIPlugin/Themes/WUIPluginTheme-0.1.js` → `src/wuiplugin/themes/wuiplugin-themes-0.2.js`).
2. Se agregó la carpeta `legacy/` con versiones anteriores de los archivos fuente (`WUIPluginThemes-0.1`, `WUIPluginSelector-0.2`).
3. Se renombró el directorio `src/wuiplugin/` (antes `src/WUIPlugins/`) para usar una convención de nombres en minúscula consistente.
4. Se renombró el directorio `legacy/WUIPlugin/` (antes `legacy/WUIPlugins/`) para usar una convención de nombres en singular consistente.
5. Actualización versión clase WUIPluginThemes a 0.2.
	- Se renombró el directorio y archivos a minúscula.
	- Se cambió la opacidad de la variable CSS `--wui-modal-message-box-bgcolor` de `80%` a `100%` en el tema base.
6. Actualización versión clase WUIPluginSelector a 0.3.
	- Se renombró el directorio y archivos a minúscula.

## [v0.1.0] - 2025-10-15

Características:

1. Versión de lanzamiento.