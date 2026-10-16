[English](wuiplugin-formvalidation-en.md) | [Español](wuiplugin-formvalidation-es.md)

[wuijs-plugins-lib](../../README-en.md)

# WUIPluginFormValidation

Version: `0.3`

Input validation extension for WUIForm.

## Description

WUIPluginFormValidation extends `WUIForm`, attaching a `validation` namespace to `WUIForm.prototype`. It operates on form fields marked with the `.validate` class, toggling an `invalid` state on the field and its trailing `.wui-icon` based on external validation results, and provides helpers for password visibility toggling and focus management.

Array-type inputs (`name="...[]"`) are supported transparently: every method resolves each occurrence by its position among inputs sharing the same name, matching the `position` parameter added in `WUIForm` `0.11`.

> [!NOTE]
> The complete documentation for the `WUIForm` class can be found in the `wuijs-main-lib` project at the following link: [https://github.com/wui-js/wuijs-main-lib/blob/main/docs/classes/form/wui-form-en.md](https://github.com/wui-js/wuijs-main-lib/blob/main/docs/classes/form/wui-form-en.md).

## Dependencies

| Class     | Version | Description |
| --------- |:-------:| ----------- |
| `WUIForm` | `0.11`  | Base class extended by the plugin. Required. |

## Sources

| Type | File |
| ---- | ---- |
| JS   | [src/wui-js/plugins/formvalidation/wuiplugin-formvalidation-0.3.js](https://github.com/wui-js/wuijs-plugins-lib/blob/main/src/wui-js/plugins/formvalidation/wuiplugin-formvalidation-0.3.js) |

## Constructor

It does not add a constructor; it extends the `WUIForm` prototype. Instantiate `WUIForm` directly (`new WUIForm([properties])`).

## Class Properties

| Name    | Type     | Description |
| ------- | -------- | ----------- |
| version | `string` | Plugin version. |

## Instance Properties

It does not have instance properties.

## Methods

`WUIForm.prototype.validation` is a read-only namespace getter. Its methods are called as `form.validation.*` on a `WUIForm` instance:

| Method            | Return type | Description |
| ----------------- | ----------- | ----------- |
| getNames          | `array`     | `validation.getNames()`<br><br>Returns the `name` attribute of every input marked with the `.validate` class within the form body. |
| getValues         | `object`    | `validation.getValues()`<br><br>Returns a `{ name: value }` map built from `getNames()` and `getValue(name, position)`. For array-type inputs (`name="...[]"`), the value at that key is an `array` holding one entry per occurrence, indexed by position. |
| prepare           | `void`      | `validation.prepare()`<br><br>Wires each `.validate` input: on `focus`, clears its `invalid` state (resetting password inputs and toggling the trailing `.wui-icon`); for inputs whose name matches `/password/i`, also wires a click handler on the trailing icon to toggle the input's `type` between `password` and `text`. |
| clear             | `void`      | `validation.clear()`<br><br>Removes the `invalid` class from every `.invalid` field. |
| reset             | `void`      | `validation.reset()`<br><br>Removes the `invalid` class from every `.invalid` field and leave the input value empty. |
| resetAll          | `void`      | `validation.resetAll()`<br><br>Removes the `invalid` class from each field with `.validate` data input. and leave the input value empty. |
| validate          | `void`      | `validation.validate(validations)`<br><br>Parameters:<br>**• validations:** `array` of field-name prefixed validation error identifiers.<br><br>Marks each `.validate` field whose name matches an entry in `validations` as `invalid`, activating the trailing `.wui-icon` error state (or adjusting the password visibility icon). |
| focusFirst        | `void`      | `validation.focusFirst()`<br><br>Focuses the first `.validate` input in the form, if any. |
| focusFirstInvalid | `void`      | `validation.focusFirstInvalid(validations)`<br><br>Parameters:<br>**• validations:** `array` of field-name prefixed validation error identifiers.<br><br>Focuses the first `.validate` input whose name matches an entry in `validations`. |

## Implementation

HTML head:

```html
<script type="text/javascript" src="./libraries/wui-js/main/form/wui-form-0.11.js"></script>
<script type="text/javascript" src="./libraries/wui-js/plugins/formvalidation/wuiplugin-formvalidation-0.3.js"></script>
```

HTML code:

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

JS code:

```js
const init = () => {
	const form = new WUIForm({ selector: ".wui-form.my-form" });
	form.init();
	form.validation.prepare();
};

window.addEventListener("DOMContentLoaded", init);
```
