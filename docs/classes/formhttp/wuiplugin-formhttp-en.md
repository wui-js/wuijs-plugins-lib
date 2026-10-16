[English](wuiplugin-formhttp-en.md) | [Español](wuiplugin-formhttp-es.md)

[wuijs-plugins-lib](../../README-en.md)

# WUIPluginFormHttp

Version: `0.1`

Data transport extension for WUIForm (JSON submission).

## Description

WUIPluginFormHttp extends `WUIForm`, attaching an `http` namespace to `WUIForm.prototype`. It is meant to grow with additional data-exchange operations for the form (e.g. file downloads, response handling), starting with JSON submission.

> [!NOTE]
> The namespace is `http`, not `submit`, since `WUIForm` already exposes a `submit` property (boolean, get/set) that controls native form submission.

> [!NOTE]
> The complete documentation for the `WUIForm` class can be found in the `wuijs-main-lib` project at the following link: [https://github.com/wui-js/wuijs-main-lib/blob/main/docs/classes/form/wui-form-en.md](https://github.com/wui-js/wuijs-main-lib/blob/main/docs/classes/form/wui-form-en.md).

## Dependencies

| Class     | Version | Description |
| --------- |:-------:| ----------- |
| `WUIForm` | `0.11`  | Base class extended by the plugin. Required. |

## Sources

| Type | File |
| ---- | ---- |
| JS   | [src/wui-js/plugins/formhttp/wuiplugin-formhttp-0.1.js](https://github.com/wui-js/wuijs-plugins-lib/blob/main/src/wui-js/plugins/formhttp/wuiplugin-formhttp-0.1.js) |

## Constructor

It does not add a constructor; it extends the `WUIForm` prototype. Instantiate `WUIForm` directly (`new WUIForm([properties])`).

## Class Properties

| Name    | Type     | Description |
| ------- | -------- | ----------- |
| version | `string` | Plugin version. |

## Instance Properties

It does not have instance properties.

## Methods

`WUIForm.prototype.http` is a read-only namespace getter. Its methods are called as `form.http.*` on a `WUIForm` instance:

| Method     | Return type.        | Description |
| ---------- | ------------------- | ----------- |
| submitJson | `Promise<object>` | `http.submitJson(options)`<br><br>Parameters:<br>**• options:** `object`. Submission options, sharing the same properties accepted by `fetch()`.<br>&nbsp;&nbsp;- **url:** `string`. Endpoint to submit to.<br>&nbsp;&nbsp;- **token:** `string` *optional*. When provided, sent as `Authorization: Bearer {token}` header.<br><br>Sends the form data as JSON via `POST`, building the body from `getFormData()`. If the response is not `ok`, returns `{ status: "error" }`. If it is, attempts to parse the body as JSON and returns it as-is (expected to carry its own `status` key); on parse failure, returns `{ status: "error", content: <response text> }`. |

> [!TIP]
> Use `form.closeKeyboard()` (available directly on `WUIForm` since version `0.10` of `wuijs-main-lib`) to close the on-screen keyboard on mobile devices before or after submitting.

## Implementation

HTML head:

```html
<script type="text/javascript" src="./libraries/wui-js/main/form/wui-form-0.11.js"></script>
<script type="text/javascript" src="./libraries/wui-js/plugins/formhttp/wuiplugin-formhttp-0.1.js"></script>
```

JS code:

```js
const init = () => {
	const form = new WUIForm({ selector: ".wui-form.my-form" });
	form.init();
	form.closeKeyboard();
	form.http.submitJson({ url: "/api/login", token: miTokenAuth});
};

window.addEventListener("DOMContentLoaded", init);
```
