# CSS — Components

Rules for the style sheets of the component classes of a WUIJS library: `{prefix}-{component}-{version}.css`,
`{prefix}-{component}-{version}.root.css` and the complementary sheets of a component. They extend `css-0.1.md` and
never repeat it.

## 1. Header

Every component style sheet starts with a CSSDoc header, without asterisks at the start of each line:

```css
/*
@file {prefix}-{component}-{version}.css
@class {Prefix}{Component}
@version {version}
@author {author} ({email})
@copyright {author} ({email})
*/
```

- `@file` is the exact file name, `@class` the class the sheet belongs to, and `@version` the version in the file name.
- A header in any other format (JSDoc asterisks, missing tags) is replaced by this one.

---

## 2. Files of a component

| File                                        | Content                                                                                                                                                  |
| ------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `{prefix}-{component}-{version}.css`        | The rules of the component.                                                                                                                              |
| `{prefix}-{component}-{version}.root.css`   | Only a `:root { }` block that declares the library variables of the component (§5) with their default values.                                            |
| `{prefix}-{component}-{version}.{name}.css` | Optional complementary sheet loaded together with the base sheet (e.g. `.styles.css` with alternative color styles, `.texts.css` with translated texts). |

- The three kinds share the component version.
- A component without styles has no sheets.

---

## 3. Selectors anchored to the component

Every selector of a component sheet includes the root class of the component, `.{prefix}-{component}`, in the compound
that selects the root (`.wui-button`, `button.wui-button`, `div[data-value="low"].wui-intensity`). The selector may only
be preceded by a context on `html` or `body` (`body.dark pre.wui-codebox`). A component never styles elements outside
its root.

```css
/* correct */
.wui-markdown iframe {
	max-width: 100%;
}

pre.wui-codebox[data-style="github"] {
	color-scheme: light;
}

/* incorrect */
iframe {
	max-width: 100%;
}
```

---

## 4. Rule order

The structure that `css-0.1.md` §4 follows is the HTML structure of the component: the root element, then its children
in the order the class builds them (the order of its `#htmlElements`).

The `.root.css` sheet is exempt from rule order, since it holds a single `:root` block.

---

## 5. Library variables

The values a project may customize are library variables, declared in the component `.root.css`:

```
--{prefix}-{component}[-mobile][-{element}]-{property}[-{state}]
```

- `{prefix}` and `{component}` are the ones of the file name (`--wui-button-*`, `--wuiview-datalist-*`).
- `-mobile` marks the variant for narrow screens and goes right after the component
  (`--wui-modal-mobile-back-textsize`). It applies inside `@media screen and (max-width: 767px)`.
- `{element}` names the child element or variant, from outer to inner, one lowercase word per level (`box-option`,
  `button-submit`). It is omitted when the variable belongs to the root.
- `{property}` is the CSS property in one lowercase word without hyphens (`bordercolor`, `borderradius`, `minwidth`,
  `horizontalpadding`), with these established names:

| `{property}`                           | CSS property                         |
| -------------------------------------- | ------------------------------------ |
| `bgcolor`                              | `background-color`                   |
| `textcolor`                            | `color` of text                      |
| `textsize`                             | `font-size`                          |
| `textfont`                             | `font-family`                        |
| `textweight`                           | `font-weight`                        |
| `iconcolor`, `iconsize`, `iconopacity` | color, size and opacity of an icon   |
| `src`                                  | an image or icon source (`url(...)`) |

- `{state}` is the interaction state, when the value changes with it: `out` (rest), `over` (hover or focus), `focus`,
  `selected`, `activated`, `disabled`, `invalid`, `empty`, `notempty`.

```css
:root {
	--wui-button-default-height: 34px;
	--wui-button-default-bordercolor-out: #d5dce3;
	--wui-button-default-bordercolor-over: #b8c2cc;
	--wui-modal-mobile-back-textsize: 17px;
}
```

- Every library variable used in the component sheets is declared in its `.root.css`, also when the class sets its value
  at run time.
- Every variable declared in `.root.css` is used by the component sheets or by the class.
- A component never redefines its own library variables inside its rules; a theme or a project overrides them in its own
  sheets.
- A component that contains another component may redefine the library variables of the contained one, scoped to its own
  selector (a form adapting the pickers inside it).

---

## 6. Local variables

A local variable is a custom property whose name has no library prefix (`--button-radius`). It is declared inside a rule
as the first declaration (`css-0.1.md` §5.1) and serves only that rule and its descendants.

- Its name is kebab-case and starts with a word of the component (`--button-radius`, `--box-filter`).
- A value that a project should be able to customize is a library variable (§5), not a local one.

```css
/* correct */
button.wui-button {
	--button-radius: calc(var(--wui-button-default-height) / 2);
	border-radius: var(--button-radius);
}

/* incorrect — a local variable with a library prefix */
button.wui-button {
	--wui-button-radius: calc(var(--wui-button-default-height) / 2);
}
```

---

## Verification

Empty output means no violations, except where a comment says the output is a list for review.

```bash
# §1 — sheets without a header in CSSDoc format (no asterisks)
grep -rL "^@file " {scope} --include="*.css"

# §2 — .root.css with content outside :root (review: only the header and one :root block)
grep -rLz ":root {" {scope} --include="*.root.css"

# §3 — top-level selectors without a component root class
grep -rnE "^[^[:space:]@/*}:][^{]*[{,]$" {scope} --include="*.css" | grep -vE "\.[a-z]+-[a-z]+|:[0-9]+::?root"

# §5 — mobile variables with the -mobile suffix at the end instead of after the component
grep -rnoE -e "--[a-z]+-[a-z0-9-]+-mobile:" {scope} --include="*.root.css"

# §5, §6 — library variables declared inside rules (review: valid only for the variables of a contained component)
grep -rnE "^\t--[a-z]+-[a-z]+-[a-z0-9-]+:" {scope} --include="*.css" | grep -v "\.root\.css:"
```

## Manual review

- §1: the header tags match the file name and the class.
- §4: rules follow the HTML structure the class builds.
- §5: each variable name follows the pattern; every variable used is declared in `.root.css`, and every declared one is
  used.
- §5: a component does not redefine its own library variables in its rules.
- §6: values meant to be customized are not local variables.
