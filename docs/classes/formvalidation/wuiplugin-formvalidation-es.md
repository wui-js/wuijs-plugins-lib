[English](wuiplugin-formvalidation-en.md) | [Español](wuiplugin-formvalidation-es.md)

[wuijs-plugins-lib](../../README-es.md)

# WUIPluginFormValidation

Versión: `0.3`

Extensión de validación de campos para WUIForm.

## Descripción

WUIPluginFormValidation extiende `WUIForm`, agregando un namespace `validation` a `WUIForm.prototype`. Opera sobre los campos marcados con la clase `.validate`, activando/desactivando el estado `invalid` en el campo y su `.wui-icon` final según resultados de validación externos, y ofrece utilidades para alternar la visibilidad de contraseñas y gestionar el foco.

Los campos de tipo arreglo (`name="...[]"`) se soportan de forma transparente: cada método resuelve cada ocurrencia según su posición entre los inputs que comparten el mismo nombre, en concordancia con el parámetro `position` agregado en `WUIForm` `0.11`.

> [!NOTE]
> La documentación completa de la clase `WUIForm` se encuentra en el proyecto `wuijs-main-lib` en el enlace: [https://github.com/wui-js/wuijs-main-lib/blob/main/docs/classes/form/wui-form-es.md](https://github.com/wui-js/wuijs-main-lib/blob/main/docs/classes/form/wui-form-es.md).

## Dependencias

| Clase     | Versión | Descripción |
| --------- |:-------:| ----------- |
| `WUIForm` | `0.11`  | Clase base extendida por el plugin. Requerida. |

## Fuentes

| Tipo | Archivo |
| ---- | ------- |
| JS   | [src/wui-js/plugins/formvalidation/wuiplugin-formvalidation-0.3.js](https://github.com/wui-js/wuijs-plugins-lib/blob/main/src/wui-js/plugins/formvalidation/wuiplugin-formvalidation-0.3.js) |

## Constructor

No agrega constructor propio; extiende el prototipo de `WUIForm`. Instancia `WUIForm` directamente (`new WUIForm([properties])`).

## Propiedades de la Clase

| Nombre  | Tipo     | Descripción |
| ------- | -------- | ----------- |
| version | `string` | Versión del plugin. |

## Propiedades de la Instancia

No posee propiedades de instancia.

## Métodos

`WUIForm.prototype.validation` es un getter de namespace de solo lectura. Sus métodos se invocan como `form.validation.*` sobre una instancia de `WUIForm`:

| Método            | Return type | Descripción |
| ----------------- | ----------- | ----------- |
| getNames          | `array`     | `validation.getNames()`<br><br>Retorna el atributo `name` de cada input marcado con la clase `.validate` dentro del cuerpo del formulario. |
| getValues         | `object`    | `validation.getValues()`<br><br>Retorna un mapa `{ nombre: valor }` construido a partir de `getNames()` y `getValue(name, position)`. Para inputs de tipo arreglo (`name="...[]"`), el valor en esa clave es un `array` con una entrada por ocurrencia, indexada por posición. |
| prepare           | `void`      | `validation.prepare()`<br><br>Conecta cada input `.validate`: al enfocarse, limpia su estado `invalid` (restableciendo inputs de contraseña y alternando el `.wui-icon` final); para inputs cuyo nombre coincida con `/password/i`, además conecta un evento de clic sobre el ícono final para alternar el `type` del input entre `password` y `text`. |
| clear             | `void`      | `validation.clear()`<br><br>Elimina la clase `invalid` de cada campo `.invalid`. |
| reset             | `void`      | `validation.reset()`<br><br>Elimina la clase `invalid` de cada campo `.invalid` y deja el valor de la entrada de datos vacío. |
| resetAll          | `void`      | `validation.resetAll()`<br><br>Elimina la clase `invalid` de cada campo con entrada de dato `.validate` y deja el valor de la entrada de datos vacío. |
| validate          | `void`      | `validation.validate(validations)`<br><br>Parámetros:<br>**• validations:** `array` de identificadores de error de validación prefijados con el nombre del campo.<br><br>Marca como `invalid` cada campo `.validate` cuyo nombre coincida con una entrada de `validations`, activando el estado de error del `.wui-icon` final (o ajustando el ícono de visibilidad de contraseña). |
| focusFirst        | `void`      | `validation.focusFirst()`<br><br>Enfoca el primer input `.validate` del formulario, si existe. |
| focusFirstInvalid | `void`      | `validation.focusFirstInvalid(validations)`<br><br>Parámetros:<br>**• validations:** `array` de identificadores de error de validación prefijados con el nombre del campo.<br><br>Enfoca el primer input `.validate` cuyo nombre coincida con una entrada de `validations`. |

## Implementación

Cabecera HTML:

```html
<script type="text/javascript" src="./libraries/wui-js/main/form/wui-form-0.11.js"></script>
<script type="text/javascript" src="./libraries/wui-js/plugins/formvalidation/wuiplugin-formvalidation-0.3.js"></script>
```

Código HTML:

```html
<form class="wui-form my-form">
	<div class="field">
		<input type="email" name="email" class="validate">
		<div class="wui-icon error-circle-fill"></div>
	</div>
	<div class="field">
		<input type="password" name="password" class="validate">
		<div class="wui-icon eye-fill"></div>
	</div>
</form>
```

Código JS:

```js
const init = () => {
	const form = new WUIForm({ selector: ".wui-form.my-form" });
	form.init();
	form.validation.prepare();
};

window.addEventListener("DOMContentLoaded", init);
```
