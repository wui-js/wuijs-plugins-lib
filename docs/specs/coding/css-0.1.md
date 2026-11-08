# CSS

General rules for CSS. They apply to every `.css` file in the project scope. A `css-{use}` spec extends or restricts
them for one kind of file; the file header, the naming of library or application variables, and the layers where they
are declared are defined by the use specs.

## 1. Indentation

Indentation uses the tab character `\t`.

---

## 2. Line breaks

- The separator is **a single blank line, never two or more in a row**, anywhere in the file.
- A blank line after the header, when the file has one.
- A blank line between rules.
- A blank line at the start of every `@` block (`@supports`, `@media`, `@keyframes`, ...).
- No blank lines inside a rule, except the line before and the line after a comment inside the rule.

```css
/* correct */
.example-main {
	display: flex;
	position: absolute;
}

@media screen and (max-width: 767px) {

	.example-main {
		width: 100%;
	}
}

@keyframes example-spin {

	0% {
		transform: rotate(0deg);
	}

	100% {
		transform: rotate(360deg);
	}
}
```

---

## 3. Rule naming

Class names, keyframe names and custom properties are in English and in kebab-case.

Exception: a rule tied directly to a DOM id (`#exampleForm`) keeps the id as written; the id does not follow the
kebab-case convention of the rest of the rules.

---

## 4. Rule order

Rules follow the structure of the HTML they style: first the rule of the root element, then its children in the order in
which they appear in the HTML. Rules with the universal selector `*` come before explicit rules that share the same
parent.

`@supports` and `@media` blocks go at the end of the rules that share their context, in the same order as those rules.
When there is more than one `@media`, they go from the smallest to the largest screen: `max-width` before `min-width`.

A multiple selector puts each selector on its own line, with no blank lines between them.

```css
/* correct */
.example-banner,
.example-banner * {
	box-sizing: border-box;
}

.example-banner {
	display: flex;
	position: absolute;
}

.example-banner > .content {
	display: flex;
	flex-direction: column;
}

@media screen and (max-width: 767px) {

	.example-banner {
		display: none;
	}
}

@media screen and (min-width: 768px) {

	.example-banner {
		width: 50%;
	}
}
```

---

## 5. Declaration order inside a rule

### 5.1. Local variables

Local variables go first: custom properties that apply only inside the rule or its descendants, and whose name does not
belong to a library or application prefix (those are defined by the use specs).

```css
/* correct */
.example-button {
	--button-radius: calc(var(--example-button-height) / 2);
	display: flex;
}
```

### 5.2. Properties

Properties go from the outermost to the innermost, in the following groups and, inside each group, in the listed order.
A property that is not listed goes next to the listed property of its family.

#### 5.2.1. Content generation

`content`, `quotes`, `counter-reset`, `counter-increment`.

#### 5.2.2. Element position

`position`, `z-index`, `top`, `left`, `right`, `bottom`, `float`, `clear`, `display`.

#### 5.2.3. Box model

Sides in the order `top → left → right → bottom`:

`width`, `min-width`, `max-width`, `height`, `min-height`, `max-height`, `shape-outside`, `shape-margin`,
`aspect-ratio`, `box-sizing`, `box-shadow`, `margin`, `margin-top`, `margin-left`, `margin-right`, `margin-bottom`,
`outline`, `outline-width`, `outline-style`, `outline-offset`, `outline-color`, `border`, `border-top`, `border-left`,
`border-right`, `border-bottom`, `border-width`, `border-top-width`, `border-left-width`, `border-right-width`,
`border-bottom-width`, `border-style`, `border-top-style`, `border-left-style`, `border-right-style`,
`border-bottom-style`, `border-color`, `border-top-color`, `border-left-color`, `border-right-color`,
`border-bottom-color`, `border-radius`, `border-top-left-radius`, `border-top-right-radius`,
`border-bottom-left-radius`, `border-bottom-right-radius`, `border-collapse`, `border-spacing`, `background`,
`background-color`, `background-image`, `background-position`, `background-size`, `background-repeat`,
`background-attachment`, `background-origin`, `background-clip`, `backdrop-filter`, `padding`, `padding-top`,
`padding-left`, `padding-right`, `padding-bottom`, `object-fit`, `object-position`.

#### 5.2.4. Content behavior

`color-scheme`, `cursor`, `pointer-events`, `accent-color`, `appearance`, `isolation`, `mix-blend-mode`,
`-webkit-touch-callout`, `user-select`, `touch-action`, `-webkit-tap-highlight-color`, `overflow`, `overflow-x`,
`overflow-y`, `overflow-anchor`, `overscroll-behavior`, `scrollbar-width`, `scrollbar-color`, `scroll-behavior`,
`scroll-snap-type`, `scroll-snap-align`, `resize`, `clip`, `clip-path`, `mask`, `mask-image`, `mask-position`,
`mask-repeat`, `visibility`, `opacity`, `filter`, `transition`, `transition-property`, `transition-duration`,
`transition-timing-function`, `transition-delay`, `animation`, `animation-name`, `animation-duration`,
`animation-timing-function`, `animation-delay`, `animation-iteration-count`, `animation-direction`,
`animation-fill-mode`, `animation-play-state`, `transform`, `transform-origin`, `transform-style`, `perspective`,
`will-change`, `caret-color`.

#### 5.2.5. Content layout

`flex`, `-webkit-box-orient`, `flex-direction`, `flex-wrap`, `flex-flow`, `flex-grow`, `flex-shrink`, `flex-basis`,
`align-content`, `align-items`, `align-self`, `justify-content`, `justify-items`, `justify-self`, `place-content`,
`place-items`, `place-self`, `gap`, `row-gap`, `column-gap`, `order`, `grid`, `grid-column`, `grid-row`, `grid-area`,
`grid-template-columns`, `grid-template-rows`, `grid-template-areas`, `grid-template`, `grid-auto-columns`,
`grid-auto-rows`, `grid-auto-flow`, `columns`, `column-count`, `column-rule`, `column-span`, `column-width`,
`list-style`, `list-style-type`, `list-style-position`, `list-style-image`, `table-layout`, `vertical-align`,
`caption-side`, `empty-cells`.

#### 5.2.6. Typography and text

`line-height`, `line-clamp`, `letter-spacing`, `word-spacing`, `word-break`, `word-wrap`, `overflow-wrap`,
`white-space`, `writing-mode`, `direction`, `unicode-bidi`, `tab-size`, `text-align`, `text-align-last`, `text-justify`,
`text-indent`, `text-decoration`, `text-decoration-line`, `text-decoration-style`, `text-decoration-color`,
`text-decoration-thickness`, `text-underline-offset`, `text-transform`, `text-overflow`, `text-shadow`, `text-wrap`,
`font`, `font-family`, `font-size`, `font-size-adjust`, `font-weight`, `font-style`, `font-variant`, `font-stretch`,
`font-feature-settings`, `font-kerning`, `color`.

`line-clamp` always goes with `-webkit-line-clamp` (§6).

---

## 6. Vendor prefixes

A vendor prefix (`-webkit-`, `-moz-`, `-o-`, `-ms-`) is not written when the standard property has enough support; if
one is found, it is removed.

When a property still needs its prefix, the prefixed declaration goes immediately before the standard one. A prefixed
property without a standard equivalent (`-webkit-tap-highlight-color`) takes its place in §5.2.

The prefixed properties without a standard equivalent are `-webkit-tap-highlight-color`, `-webkit-touch-callout` and
`-webkit-box-orient`, and `-webkit-line-clamp` with `display: -webkit-box`. A vendor-prefixed pseudo-element
(`::-webkit-scrollbar`, `::-moz-range-thumb`) is a selector, not a property, and this rule does not apply to it.

```css
/* correct: prefix still needed, before the standard property */
-webkit-line-clamp: 3;
line-clamp: 3;

/* incorrect: linear-gradient has full standard support */
background-image: -webkit-linear-gradient(...);
background-image: -moz-linear-gradient(...);
background-image: linear-gradient(...);
```

---

## 7. Comments

Comments follow `specs-0.1.md` §8. The only form is a single line that names a rule, a section or a set of related
rules.

```css
/* correct */
/* global */
/* light dark modes */
/* example-button default */

/* incorrect: more than one line */
/*
 * This rule controls the background of the panel
 * when it is disabled.
 */
```

When normalizing a file, single-line comments in the format are kept, single-line comments out of the format are
removed, and multi-line comments are removed from the code.

---

## Verification

```bash
# §1 — indentation with spaces
grep -rnE "^( {2}| {4})" {scope} --include="*.css"

# §2 — two or more consecutive blank lines
find {scope} -name "*.css" | xargs awk 'FNR==1{b=0} /^[ \t]*$/{if(b){print FILENAME":"FNR}; b=1; next} {b=0}'

# §6 — prefixed property not immediately followed by its standard property, or prefixed value
find {scope} -name "*.css" | xargs awk 'FNR==1{if(w!="")print w; w=""} {if(w!=""){if($0 !~ "^[[:space:]]*" s "[[:space:]]*:")print w; w=""}} match($0,/^[[:space:]]*-(webkit|moz|o|ms)-[a-z-]+[[:space:]]*:/){d=substr($0,RSTART,RLENGTH); gsub(/[[:space:]:]/,"",d); if(d !~ /^-webkit-(tap-highlight-color|touch-callout|box-orient|line-clamp)$/){s=d; sub(/^-[a-z]+-/,"",s); w=FILENAME":"FNR}; next} /:[^;{]*[[:space:](]-(webkit|moz|o|ms)-/ && !/display:[[:space:]]*-webkit-box/{print FILENAME":"FNR} END{if(w!="")print w}'

# §7 — multi-line comments
find {scope} -name "*.css" | xargs awk 'FNR==1{h=($0 ~ /^\/\*/)} h{if($0 ~ /\*\//)h=0; next} /\/\*/ && !/\*\//{print FILENAME":"FNR}'
```

## Manual review

- §3: names in English and kebab-case.
- §4: rule order against the HTML structure, and `@media` order.
- §5: declaration order inside each rule.
- §6: whether each prefixed property that precedes its standard one is still needed by the supported browsers; if not,
  it is removed.
- §7: each single-line comment names what it heads.
