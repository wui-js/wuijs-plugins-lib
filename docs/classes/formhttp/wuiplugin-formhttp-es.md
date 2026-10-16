[English](wuiplugin-formhttp-en.md) | [Español](wuiplugin-formhttp-es.md)

[wuijs-plugins-lib](../../README-es.md)

# WUIPluginFormHttp

Versión: `0.1`

Extensión de transporte de datos para WUIForm (envío JSON).

## Descripción

WUIPluginFormHttp extiende `WUIForm`, agregando un namespace `http` a `WUIForm.prototype`. Está pensado para crecer con más operaciones de intercambio de datos del formulario (p. ej. descarga de archivos, manejo de response), comenzando con el envío JSON.

> [!NOTE]
> El namespace es `http`, no `submit`, ya que `WUIForm` ya expone una propiedad `submit` (booleana, get/set) que controla el envío nativo del formulario.

> [!NOTE]
> La documentación completa de la clase `WUIForm` se encuentra en el proyecto `wuijs-main-lib` en el enlace: [https://github.com/wui-js/wuijs-main-lib/blob/main/docs/classes/form/wui-form-es.md](https://github.com/wui-js/wuijs-main-lib/blob/main/docs/classes/form/wui-form-es.md).

## Dependencias

| Clase     | Versión | Descripción |
| --------- |:-------:| ----------- |
| `WUIForm` | `0.11`  | Clase base extendida por el plugin. Requerida. |

## Fuentes

| Tipo | Archivo |
| ---- | ------- |
| JS   | [src/wui-js/plugins/formhttp/wuiplugin-formhttp-0.1.js](https://github.com/wui-js/wuijs-plugins-lib/blob/main/src/wui-js/plugins/formhttp/wuiplugin-formhttp-0.1.js) |

## Constructor

No agrega constructor propio; extiende el prototipo de `WUIForm`. Instancia `WUIForm` directamente (`new WUIForm([properties])`).

## Propiedades de la Clase

| Nombre  | Tipo     | Descripción |
| ------- | -------- | ----------- |
| version | `string` | Versión del plugin. |

## Propiedades de la Instancia

No posee propiedades de instancia.

## Métodos

`WUIForm.prototype.http` es un getter de namespace de solo lectura. Sus métodos se invocan como `form.http.*` sobre una instancia de `WUIForm`:

| Método        | Return type         | Descripción |
| ------------- | ------------------- | ----------- |
| submitJson    | `Promise<object>` | `http.submitJson(options)`<br><br>Parámetros:<br>**• options:** `object`. Opciones de envío, con las mismas propiedades aceptadas por `fetch()`.<br>&nbsp;&nbsp;- **url:** `string`. Endpoint de destino.<br>&nbsp;&nbsp;- **token:** `string` *opcional*. Si se entrega, se envía como cabecera `Authorization: Bearer {token}`.<br><br>Envía los datos del formulario en formato JSON vía `POST`, construyendo el cuerpo desde `getFormData()`. Si la respuesta no es `ok`, retorna `{ status: "error" }`. Si lo es, intenta parsear el cuerpo como JSON y lo retorna tal cual (se espera que incluya su propia clave `status`); si el parseo falla, retorna `{ status: "error", content: <texto de la respuesta> }`. |

> [!TIP]
> Usa `form.closeKeyboard()` (disponible directamente en `WUIForm` desde la versión `0.10` de `wuijs-main-lib`) para cerrar el teclado en pantalla en dispositivos móviles antes o después del envío.

## Implementación

Cabecera HTML:

```html
<script type="text/javascript" src="./libraries/wui-js/main/form/wui-form-0.11.js"></script>
<script type="text/javascript" src="./libraries/wui-js/plugins/formhttp/wuiplugin-formhttp-0.1.js"></script>
```

Código JS:

```js
const init = () => {
	const form = new WUIForm({ selector: ".wui-form.my-form" });
	form.init();
	form.closeKeyboard();
	form.http.submitJson({ url: "/api/login", token: miTokenAuth});
};

window.addEventListener("DOMContentLoaded", init);
```
