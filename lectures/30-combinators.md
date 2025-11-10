---
reading: '[MDN: Combinators](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Combinators)'
...

# Combining Selectors

## What Are Combinators?

- Combinators are special syntax used to combine simple selectors
- They allow us to create more complex and targeted CSS rules
- These tools specify the relationship between two selectors

## Why We Combine

- Combining selectors increases the specificity of your styles
- This precision helps avoid unintended styling in large projects
- They allow you to select elements based on their position in the document structure

## Descendant Selectors

- The descendant combinator is a simple space between selectors
- It targets an element nested anywhere inside another element
- The elements do not need to be direct children of the parent element

## Descendant Example

- To style all `p` elements inside an `article` element:

```css
article p {
  color: midnightblue
}
```

- This rule will apply to deeply nested paragraphs as well

---

How might a poorly chosen descendant selector cause issues with component reuse in a large web application?

## Child Selectors

- The child combinator uses the greater-than symbol `>`
- It only targets elements that are direct children of the preceding element
- This creates a much more constrained selection compared to the space

## Child Example

- We can use this to style only the top-level list items in a menu:

```css
nav > ul > li {
  font-weight: bold
}
```

- Any list items nested deeper in a submenu will be ignored

## Exercise

Given the HTML structure below, write a CSS rule using the child combinator to make only the word "Direct" red, but not the word "Nested":

```html
<div>
  <p>Direct</p>
  <span>
    <p>Nested</p>
  </span>
</div>
```

## Sibling Relationship

- Combinators can also select elements that share a common parent element
- We call these elements "siblings" within the document tree
- Sibling combinators only look *forward* from the first selector

## Adjacent Sibling

- The adjacent sibling combinator uses the plus symbol `+`
- It selects an element that is immediately preceded by the first selector
- This relationship must be directly sequential in the HTML source

## Adjacent Example

- A common use is styling the first paragraph after a heading:

```css
h2 + p {
  margin-top: 0
}
```

- Only the very next paragraph after the `h2` will receive this style

---

When would using the adjacent sibling combinator is more robust than using a simple class on the intended element?

## General Sibling

- The general sibling combinator uses the tilde symbol `~`
- It selects *all* elements that share the same parent and follow the first selector
- The elements do not need to be immediately next to each other

## General Example

- This rule styles every paragraph that follows an introduction element:

```css
.intro ~ p {
  text-indent: 1em
}
```

- Other elements can exist between `.intro` and the targeted paragraphs

## Combining Combinators

- You can chain combinators together to create very specific selection paths
- This allows you to select elements based on complex structural requirements
- The selectors are processed from left to right to narrow the selection

## Chaining Example

- This rule styles only the adjacent paragraph that follows a strong element inside an article:

```css
article strong + p {
  margin-left: 20px
}
```

---

## Reviewing the Four

- Space: Descendant, selects anything inside the parent
- `>`: Child, selects only direct descendants
- `+`: Adjacent Sibling, selects the *next* sibling
- `~`: General Sibling, selects *all* following siblings

## Selectors List

- The comma `,` is also critical for grouping selectors
- It is not a combinator, but it applies the same styles to multiple, independent targets
- This helps keep your stylesheets concise and manageable

## Exercise

Write a single CSS selector that achieves the following:

1. Selects all `a` tags inside a header.
2. Selects all direct child `li` elements of an unordered list with the class `.menu`.
3. Selects all `p` elements that follow a `blockquote` element.
