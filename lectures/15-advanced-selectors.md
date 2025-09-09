---
reading: '[MDN: Attribute Selectors](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Attribute_selectors), [MDN: Pseudo-classes and elements](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Pseudo_classes_and_elements)'
...

# Advanced Selectors

## Why Advanced?

- Target elements based on their unique attributes
- Add decorative content without changing HTML

## Attribute Selectors

- Target elements based on their HTML attributes
- These attributes can have various values
- A flexible way to apply specific styling

## Basic Attribute

- Selects elements that possess a specific attribute no matter what its value might be
- Useful for general styling of form inputs or images

```css
a[title] {
  border-bottom: 1px dotted blue;
}
```

## Exact Value

- Matches elements where an attribute holds an exact value
- Requires a precise match for the entire string
- Ideal for targeting specific input types or data attributes

```css
input[type="text"] {
  background-color: lightyellow;
}
```

## Attribute Substrings 1

- `[attr~="value"]`: Matches a space-separated word list
- `[attr|="value"]`: Matches a hyphen-separated prefix or exact value

```css
[class~="active"] {
  border: 1px solid blue;
}
```

## Attribute Substrings 2

- `[attr^="value"]`: Matches values starting with a string
- `[attr$="value"]`: Matches values ending with a string
- `[attr*="value"]`: Matches values containing a substring

```css
a[href*="example.com"] {
  text-decoration: underline;
}
```

## Case Sensitivity

- By default, attribute selectors are case-sensitive
- Add `i` after the selector to make it case-insensitive
- Ensures broader matching regardless of capitalization

```css
a[href$=".PDF" i] {
  font-weight: bold;
}
```

---

Consider a website with many buttons. How might you use attribute selectors to style "primary" action buttons differently from "cancel" buttons, without adding new classes?

---

## Exercise

Write a CSS rule to highlight all `<div>` elements that have a `data-status` attribute whose value is exactly "pending".

```html
<div data-status="pending">Item 1</div>
<div data-status="complete">Item 2</div>
<div data-status="pending-review">Item 3</div>
```

## Pseudo-classes

- Select elements based on their state or position
- They describe a special state of an element
- Adds dynamic styling without JavaScript

## User Interaction

- Respond to how users interact with elements
- `:hover` for when the mouse is over an element
- `:active` for when an element is clicked
- `:focus` for when an element receives input focus

```css
button:hover {
  background-color: gray;
}
```

---

If you wanted to provide visual feedback for a user filling out a form, when might you use `:focus` differently from `:hover`? What's the main distinction in their purpose?

---

## Structural Order

- Target elements based on their position among siblings
- `:first-child` selects the very first element
- `:last-child` selects the very last element
- `:nth-child(n)` selects based on a numeric pattern

```css
li:nth-child(odd) {
  background-color: lightgray;
}
```

## Unique Elements

- Identify elements that are alone within their parent
- `:only-child` selects an element if it's the sole child
- `:empty` selects elements with no children or text content

```css
div:empty {
  height: 10px;
  background-color: red;
}
```

## Link States

- Style anchor elements based on their visited status
- `:link` targets unvisited hyperlinks
- `:visited` targets previously visited hyperlinks

```css
a:visited {
  color: purple;
}
```

## Form States

- Select form elements based on their current status
- `:checked` for selected checkboxes or radio buttons
- `:disabled` for unusable form controls
- `:enabled` for active and ready form controls

```css
input:disabled {
  opacity: 0.5;
}
```

## Negating Selectors

- Exclude specific elements from a selection
- The `:not()` pseudo-class takes another selector as an argument
- Apply styles to all elements *except* those matching the argument

```css
input:not([type="submit"]) {
  border: 1px solid blue;
}
```

## Exercise

How would you style only the second item in a list to have a red background, and also ensure that any disabled text input fields have a light gray background?

## Pseudo-elements

- Create content or target specific parts of an element
- They generate "fake" elements that aren't in the HTML
- Allow styling of content that doesn't explicitly exist

## Generated Content

- Insert content before or after an element's actual content
- `::before` adds content at the beginning
- `::after` adds content at the end
- Requires the `content` property to display anything

```css
a::after {
  content: " (external)";
  font-size: 0.8em;
}
```

## Text Formatting

- Target specific parts of an element's text
- `::first-letter` styles the initial letter of a block of text
- `::first-line` styles the entire first line of text

```css
p::first-letter {
  font-size: 2em;
  font-weight: bold;
}
```

---

Can you think of a situation where `::before` or `::after` would be a more appropriate choice than adding a `<span>` element directly into your HTML for stylistic purposes? Why?

---

## Text Selection

- Customize the appearance of selected text
- The `::selection` pseudo-element targets highlighted text
- Allows changing background color and text color

```css
::selection {
  background-color: orange;
  color: white;
}
```

## Exercise

Add a small red square `::before` any `<li>` element that has a `data-status="new"` attribute.
