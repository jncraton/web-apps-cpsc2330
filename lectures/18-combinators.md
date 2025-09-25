---
reading: '[CSS Combinators](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Combinators)'
...

# CSS Combinators

## Powerful Selectors

- CSS selectors target specific elements on a webpage
- Combinators help refine this targeting based on relationships
- They connect two or more simple selectors to form complex rules

## Context Matters

- We select not just *what* an element is, but *where* it is
- Think about elements as having parent, child, or sibling relationships
- This allows for highly precise and flexible styling rules

## Descendant Selectors

- This is the most frequently used combinator
- It selects an element that is located *anywhere inside* another element
- A simple space character is used between the two selectors

## Ancestor Descendant

- The selector `article p` targets all `<p>` elements
- As long as they are nested inside an `<article>` element
- This works regardless of how many levels deep the paragraph is

## Descendant Example

```html
<article>
  <p>Paragraph one.</p>
  <div>
    <p>Paragraph two.</p>
  </div>
</article>
```

## Styling All Children

```css
article p {
  color: blue;
}
```

- Both "Paragraph one" and "Paragraph two" would appear in blue
- The selector looks for any paragraph that is a descendant
- This is a broad and incredibly useful targeting tool

---

How can combining selectors make your CSS more maintainable and easier to read?

## Exercise

Write a CSS rule to make all list items (`<li>`) *inside an unordered list (`<ul>`)* have a green background.

## Child Selectors

- This combinator offers more specificity than descendant selectors
- It selects an element that is a *direct child* of another element
- The `>` character is used to indicate this direct relationship

## Direct Relationship

- The selector `ul > li` targets only `<li>` elements
- Which are immediately and directly inside a `<ul>` element
- It does not apply to any deeply nested `<li>` elements

## Child Example

```html
<nav>
  <ul>
    <li>Item 1</li>
    <li>
      <span>Sub-item container</span>
      <ul>
        <li>Sub-item 1</li>
      </ul>
    </li>
  </ul>
</nav>
```

## What Gets Styled?

```css
ul > li {
  border: 1px solid red;
}
```

---

What are the practical implications of using `article p` versus `article > p` in a complex webpage layout?

## Adjacent Siblings

- This combinator selects an element that is immediately preceded by another
- The two elements must share the exact same parent element
- The `+` character is used to represent this adjacent sibling relationship

## Next Door Neighbors

- The selector `h2 + p` targets a `<p>` element
- Only if it comes immediately after an `<h2>` element
- And both the `h2` and `p` share a common parent

## Adjacent Example

```html
<div>
  <h2>Title</h2>
  <p>Intro paragraph.</p>
  <p>More content.</p>
</div>
```

## Specific Pairing

```css
h2 + p {
  margin-top: 0;
}
```

- Only "Intro paragraph." would have its `margin-top` set to 0
- "More content." is not immediately preceded by an `<h2>`
- It is instead preceded by another `<p>` element

## General Siblings

- This combinator selects an element that is preceded by another
- They must share the same parent element, but not necessarily be immediate
- The `~` character is used for this general sibling relationship

## All Following Siblings

- The selector `h2 ~ p` targets all `<p>` elements
- That come *after* an `<h2>` element in the document flow
- And are at the same level in the document tree

## General Example

```html
<div>
  <h2>Title</h2>
  <p>Paragraph A.</p>
  <span>Span Element</span>
  <p>Paragraph B.</p>
</div>
```

## All Siblings Styled

```css
h2 ~ p {
  color: purple;
}
```

- Both "Paragraph A." and "Paragraph B." would be styled purple
- They both follow an `<h2>` and are siblings in the `div`
- The `<span>` element in between them does not stop the selection

---

Think about a blog post structure. When would you use `h2 + p` versus `h2 ~ p` for styling?

## Exercise

Consider the HTML: `<section><p>A</p><span>B</span><p>C</p></section>`.

Write a CSS rule using a combinator to style *only* paragraph "C" red.

## Combining Combinators

- You have the flexibility to use multiple combinators in one selector
- This enables even more precise and powerful element targeting
- You can build complex relationships like `nav ul > li + li`

## Complex Selectors

- This allows for incredibly fine-grained control over styling
- It can reduce the need for adding extra classes or IDs to HTML
- This approach makes your CSS cleaner and more semantic

## Reviewing Relationships

- Space: Targets any descendant element
- `>`: Targets a direct child element
- `+`: Targets an immediate adjacent sibling element
- `~`: Targets any following sibling element
