# JavaScript — Components

Rules for the component classes of a WUIJS library: each file `{prefix}-{component}-{version}.js` defines one class
`{Prefix}{Component}` (e.g. `wui-button-0.1.js` defines `WUIButton`). They extend `js-0.1.md` and never repeat it.

## 1. Header

Every component file starts with a JSDoc header:

```js
/*
 * @file {prefix}-{component}-{version}.js
 * @class {Prefix}{Component}
 * @version {version}
 * @author {author} ({email})
 * @copyright {author} ({email})
 */
```

- `@file` is the exact file name and `@version` matches the version in it and the `static version` field.
- `@class` is the exact class name.

---

## 2. Property reads through getters

In methods that are neither getters nor setters, properties are read through their public getter (`this.hidden`), not
from `this.#properties.hidden`.

- It applies to properties with getter and setter and to getter-only properties.
- Writes to a getter-only property go to `#properties` directly (`this.#properties.sceneIndex = i`), since there is no
  setter to delegate to.
- Exception: when the getter computes a value instead of returning the stored one (e.g. `get value()` reads it from a
  native `<select>`), `this.#properties.value` is used where the stored value is needed.

```js
// correct
const hidden = this.hidden;
box.className = `box ${this.boxAlign} ${this.openDirection}`;
if (this.sceneIndex !== null) {
	section.animate(this.sceneStep, this.sceneProgress);
}
this.#properties.sceneIndex = i;

// incorrect
const hidden = this.#properties.hidden;
box.className = `box ${this.#properties.boxAlign} ${this.#properties.openDirection}`;
```

---

## 3. Type validation in setters

A setter validates the type of the received value before assigning it to `#properties`. It never assumes the type.

```js
set hidden(value) {
	if (typeof (value) === "boolean") {
		this.#properties.hidden = value;
	}
}
```

Optional callbacks accept a function or `null`:

```js
set onChange(value) {
	if (typeof (value) === "function" || value === null) {
		this.#properties.onChange = value;
	}
}
```

---

## 4. Instance check before DOM operations

Before using properties or methods of an HTML element, check that it is the expected instance with `instanceof`.

```js
// correct
if (input instanceof HTMLSelectElement) {
	input.setAttribute("multiple", "true");
}

// incorrect
if (input) {
	input.setAttribute("multiple", "true");
}
```

---

## 5. Preloading `#htmlElement`

When a method uses `this.#htmlElement` more than once, it assigns it to a local constant at the start of the method.
There are no exceptions, including `#buildHtml()`.

```js
// correct
const htmlElement = this.#htmlElement;
if (htmlElement instanceof HTMLDivElement) {
	htmlElement.classList.add("disabled");
}

// incorrect
if (this.#htmlElement instanceof HTMLDivElement) {
	this.#htmlElement.classList.add("disabled");
}
```

---

## 6. Preloading `#htmlElements`

A method that uses two or more keys of `#htmlElements`, or one key more than once, preloads them with destructuring at
the start of the method.

```js
// correct
const { overlay, box } = this.#htmlElements;
overlay.classList.remove("hidden");
box.className = "box";

// incorrect
this.#htmlElements.overlay.classList.remove("hidden");
this.#htmlElements.box.className = "box";
```

The only exception is the conditional creation inside `#buildHtml()` (§7 [8]): each key is read and written once in its
own `if` block (`if (!this.#htmlElements.box) { this.#htmlElements.box = ...; }`), so it keeps direct access. The
exception does not exempt `#buildHtml()` from §5.

---

## 7. Class structure

Canonical order of the members of a component class, in two spans: first what the class offers to be used (data,
accessors, HTML construction, and the reading `get*` and writing `set*` methods), then its lifecycle from `init()`, in
order of execution. It is the same criterion as `js-fragments` §3. Members that a component does not need are omitted;
the relative order of the rest is kept.

```
[header]
class {Prefix}{Component} {

	[1]  static data fields

	[2]  private instance fields

	[3]  static { }

	[4]  constructor()

	[5]  getters
	[6]  setters

	[7]  #loadHtml()
	[8]  #buildHtml()
	[9]  #initHtml()

	[10] public element access methods (getElement(), getBox(), ...)
	[11] private computation methods (#getSelectedOptions(), #getValue(), ..., #setValue())
	[12] setOptions()
	[13] #setStyle()
	[14] init()
	[15] #prepare()
	[16] #refreshView()
	[17] addOption(), #addSelectOption(), #addHtmlOption()
	[18] #loadBox()
	[19] clearOptions()
	[20] open(), close()
	[21] toggle(), cancel(), accept()
	[22] isOpen(), isEmpty(), isValid()
	[23] private observer methods (#addColorSchemeObserver(), ...)
	[24] destroy()
}
```

### [1] Static data fields

In this order:
- `static version`: the component version as a string.
- `static #defaults`: the default values of every public property, in the order of the getters.
- Other immutable static data (`static #icons`, `static #texts`, ...).
- Shared static state (`static #active`, ...).

```js
static version = "0.1";
static #defaults = { ... };
static #icons = { ... };
static #active = null;
```

### [2] Private instance fields

In this order:
- `#properties = {}`: flat store of every instance property.
- `#htmlElement`: the root element of the component.
- `#htmlElements = { ... }`: the relevant child elements, every key initialized to `null`, in DOM order.
- Other private state (`#targetValue`, `#cancelValue`, `#colorScheme`, ...).

```js
#properties = {};
#htmlElement;
#htmlElements = {
	input: null,
	opener: null,
	box: null
};
#targetValue;
```

### [3] `static { }`

Optional static initialization block. It registers class-level listeners (`document.addEventListener(...)`) or builds
structures derived from other static fields. It runs once, when the class is evaluated.

- It replaces any public or "protected by convention" initializer called by hand after the class
  (`{Prefix}{Component}._initClass()`).
- Every static field it uses is declared before it, since static blocks run in textual order.

```js
static {
	document.addEventListener("keydown", event => { ... });
}
```

### [4] `constructor(properties = {})`

- Clones `#defaults` with `structuredClone()`.
- Assigns every property through its setter (`this[name] = ...`), taking the received value when present.
- Initializes the private state.
- Calls `#initHtml()` last. The constructor is the only caller of `#initHtml()`.

```js
constructor(properties = {}) {
	const defaults = structuredClone({Prefix}{Component}.#defaults);
	Object.entries(defaults).forEach(([name, value]) => {
		this[name] = name in properties ? properties[name] : value;
	});
	this.#targetValue = null;
	this.#initHtml();
}
```

### [5] Getters

One getter per public property, in the order of `#defaults`. They return the value from `#properties`.

### [6] Setters

One setter per public property, in the order of `#defaults`. They validate the type (§3) and may update the DOM.

### [7] `#loadHtml()`

Reads the existing DOM and fills `#htmlElement` and `#htmlElements`. It neither creates elements nor registers events.
`#htmlElements` is assigned as a complete object literal, so every key is reassigned together.

```js
#loadHtml() {
	const selector = this.selector;
	this.#htmlElement = document.querySelector(selector);
	this.#htmlElements = {
		input: document.querySelector(`${selector} > input`),
		opener: document.querySelector(`${selector} > .opener`),
		box: document.querySelector(`${selector} > .box`)
	};
}
```

### [8] `#buildHtml()`

Creates the elements that do not exist yet, checking each one first (`if (!this.#htmlElements.box)`), and appends them.
It neither reads the DOM to find elements nor registers events.

```js
#buildHtml() {
	const htmlElement = this.#htmlElement;
	if (htmlElement instanceof HTMLDivElement) {
		if (!this.#htmlElements.box) {
			this.#htmlElements.box = document.createElement("div");
			htmlElement.appendChild(this.#htmlElements.box);
		}
	}
}
```

When the number of elements depends on children already in the DOM (one indicator per existing `.slide`), it iterates
those children instead of checking keys, and empties the container first with `innerHTML = ""` when needed.

### [9] `#initHtml()`

Calls `#loadHtml()` and then `#buildHtml()`, with no other logic. A component with nothing to create omits
`#buildHtml()`, and `#initHtml()` calls only `#loadHtml()`.

### [10] Public element access methods

Return references to the root or internal elements (`getElement()`, `getBox()`, `getInput()`). No side effects.

### [11] Private computation methods

Computations over the internal state, without DOM changes (`#getSelectedOptions()`, `#getValue()`, `#getText()`), plus
low-level internal writes such as `#setValue()`.

### [12] `setOptions()`

Replaces the whole set of options: clears, assigns and rebuilds, then calls `#refreshView()` and `close()`.

### [13] `#setStyle()`

Syncs the CSS classes of the root element with the current state (e.g. `disabled`). Called from setters and from the
color scheme listener.

### [14] `init()`

Entry point of the component life cycle: registers the instance listeners, applies the initial state to the DOM and
enables interaction. It is called once per instance and never calls `#initHtml()`.

### [15] `#prepare()`

Syncs the transient state before opening (`#targetValue`, `#cancelValue`, button texts) and calls `#refreshView()`.

### [16] `#refreshView()`

Updates the visible view (text, icon) from the current value and properties. Called from setters, `setOptions()` and
`#prepare()`.

### [17] `addOption()`, `#addSelectOption()`, `#addHtmlOption()`

`addOption()` is the public entry point; it delegates to the private methods that update the native element and the
visual DOM.

### [18] `#loadBox()`

Syncs the visual state of the options with the selection of the native element. Called from `open()`.

### [19] `clearOptions()`

Empties the options and clears the native element and the visual DOM.

### [20] `open()`, `close()`

Control the visibility of the box. `open()` calls `#prepare()` and `#loadBox()`; `close()` clears the focus state.

### [21] `toggle()`, `cancel()`, `accept()`

- `toggle()`: opens when closed, closes when open.
- `cancel()`: restores the value from the moment of opening and closes.
- `accept()`: fires `onChange` with the current value and closes.

### [22] `isOpen()`, `isEmpty()`, `isValid()`

Public predicates. They return a `boolean` and have no side effects.

### [23] Private observer methods

Set up system observers or media queries (`#addColorSchemeObserver()`) and keep their cleanup in a private field for
`destroy()`.

### [24] `destroy()`

Releases every resource: closes the component, disconnects observers, removes its DOM elements and clears `#properties`.

---

## 8. Console messages

The console method follows the severity:

- `console.error()`: a serious error that prevents finishing the process or producing a result.
- `console.warn()`: the process finished and produced a result, but something must be reported.
- `console.log()`: debug output only, conditioned on the `debug` property of the class.

No other console method is used (`console.info()`, `console.debug()`, ...).

Format, for the three methods: `WUIJS - {ClassName}: {description}`.

- `{ClassName}` is the exact class name.
- The description is lowercase, except acronyms (`JSON`, `CSS`, `URL`) and proper names.
- A useful value (URL, name, identifier, status) is referenced with `${value}` in a template literal. The message is a
  single string, with no extra arguments.

```js
// correct
console.error(`WUIJS - WUILanguage: JSON file ${url} could not be parsed: ${error}`);
console.warn(`WUIJS - WUIIcon: style sheet ${sheet.href} could not be read: ${error.message}`);
if (this.debug) {
	console.log(`WUIJS - WUIScrolly: section ${section.selector} initialized, height ${height}`);
}

// incorrect
console.error("WUICookie error:", detail);
console.warn(`The style sheet could not be read: ${sheet.href}`, error);
console.log("ui import htm:", id, element);
```

Exceptions:

- A library resource loader is not a class: its format is `WUIJS: {description}` (``console.error(`WUIJS:
  ${error.message}`)``).
- A class that reports an HTTP status to its caller throws the status number (`throw response.status`). It is flow
  control for the caller, not a console message, and does not follow this format.

---

## Verification

Empty output means no violations, except where a comment says the output is a list for review.

```bash
# §2 — reads from #properties (review: valid only inside getters and setters, and for §2 writes and exceptions)
grep -rnE "this\.#properties\." {scope} --include="*.js"

# §3 — setters (review: each one validates the type before assigning)
grep -rnE $'^\tset [[:alnum:]_]+\(value\)' {scope} --include="*.js"

# §5 — files with two or more this.#htmlElement (review: within the same method without a local constant)
grep -rcE "this\.#htmlElement([^[:alnum:]_]|$)" {scope} --include="*.js" | awk -F: '$2 >= 2'

# §6 — direct access to #htmlElements keys (review: outside the #buildHtml() creation pattern)
grep -rnE "this\.#htmlElements\.[[:alnum:]_]+" {scope} --include="*.js"

# §7 — structure method names with uppercase acronyms (js-0.1.md §3.1)
grep -rnE "#(load|build|init)HTML\(|#add(HTML|SRC)[[:alnum:]_]*\(" {scope} --include="*.js"

# §8 — console messages out of format
grep -rnE "console\.(log|warn|error|info|debug)\(" {scope} --include="*.js" | grep -vE "console\.(log|warn|error)\(\`WUIJS( - [A-Z][[:alnum:]_]+)?: "
```

## Manual review

- §1: the header matches the file name, the class name and `static version`.
- §2, §3, §5, §6: the listed occurrences are violations only in the cases each rule describes.
- §4: every operation on an HTML element is preceded by its `instanceof` check.
- §7: members follow the canonical order; `#initHtml()` is called only from the constructor and `init()` only once.
- §8: each `console.log()` is conditioned on `debug`, and `error`/`warn` match the severity.
