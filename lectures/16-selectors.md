---
reading: '[MDN: Selectors](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Basic_selectors)'
...

# Styling Elements

## Targeting CSS

- CSS allows us to visually style web pages
- We need precise methods to select which elements to modify
- This selection mechanism is fundamental to CSS

## What are Selectors?

- Selectors are patterns that match one or more elements
- They point to the specific HTML elements to be styled
- They form the crucial first part of any CSS rule

## Type Selectors

- These selectors target elements by their HTML tag name
- They apply styles to *all* instances of a given element type
- For example, `p` selects every paragraph element on the page

## Type Example

```css
p {
  color: blue;
  font-family: sans-serif;
}
```

```html
<p>This paragraph is blue</p>
<p>So is this one</p>
```

## ID Selectors

- IDs provide a unique identifier for a single element
- An element's ID *must* be unique across the entire page
- In CSS, you reference an ID using the `#` symbol

## ID Example

```css
#main-banner {
  background-color: navy;
  color: white;
}
```

```html
<header id="main-banner">
  <h1>Site Title</h1>
</header>
```

## Class Selectors

- Classes group multiple elements for shared styling
- Many elements can share the same class name
- In CSS, you reference a class using the `.` symbol

## Class Example

```css
.card-item {
  border: 1px solid gray;
  padding: 15px;
}
```

```html
<div class="card-item">Product A</div>
<div class="card-item">Product B</div>
<article>Normal Content</article>
```

## Exercise

Create two HTML paragraphs. Give one paragraph an `id` of `intro-text` and both paragraphs a `class` of `dark-mode`. Write CSS to give `intro-text` a larger font size and `dark-mode` a black background with white text.

## Selector Lists

- Individual selectors can be combined so that the rule is applied to all of the individual selectors

```html
h1, .special {
  color: blue;
}
```

## Universal Selection

- `*` selector selects all elements
- Useful for clarity and resetting all properties
