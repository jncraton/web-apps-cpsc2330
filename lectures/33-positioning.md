---
reading: '[CSS Layout Fundamentals](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Introduction), [CSS Positioning](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Positioning)'
...

# Structuring Web Content

## Understanding Normal Flow

- Normal flow is the default way elements are laid out in the browser
- Elements are placed sequentially based on their order in the source code
- This flow forms the baseline for all subsequent CSS layout modifications

## Block and Inline

- **Block** elements take up the full available width and stack vertically
- **Inline** elements only take up the necessary content width and flow horizontally

## The Box Model

- Every element is conceptually wrapped in a rectangular box structure
- This box includes content, padding, border, and margin areas
- The model determines how space is consumed and how elements interact

## Modern Layout Tools

- Traditional float and table-based layouts are now generally deprecated
- **Flexbox** is designed for one-dimensional linear content alignment
- **Grid** is designed for complex, two-dimensional page structures

---

If the "normal flow" is purely determined by the source code, why is CSS necessary to create complex visual hierarchies?

## Why Positioning Matters

- Positioning allows us to move elements out of the default normal flow
- It is essential for layering content or fixing elements to the viewport
- It fundamentally changes how the element interacts with its neighbors

## Static Positioning

- This is the default position value for every HTML element
- The `top`, `bottom`, `left`, or `right` properties have absolutely no effect here

## Relative Positioning

- The element is moved relative to its original, normal flow location
- The space it originally occupied in the flow is preserved by the browser

## Exercise

Create a css ruleset that would shift an element 30 pixels down and 15 pixels to the right of its original location

## Absolute Positioning

- The element is entirely removed from the normal document flow
- Its position is calculated relative to its nearest *positioned* ancestor

## The Absolute Anchor

- If no ancestor has a position value other than `static`, the viewport is used
- This often means the element is positioned relative to the `<body>` element

## Fixed Positioning

- The element is fixed relative to the viewport, not the document
- It stays in the exact same place even when the user scrolls the page

## Fixed Use Cases

- Ideal for navigation bars that must always remain visible at the top
- Common for persistent status notifications or chat buttons on mobile

## Sticky Positioning

- A hybrid that begins as `relative` until a defined scroll threshold is met
- Once the threshold is met, it then behaves as `fixed`

## Sticky Thresholds

- Requires a value for `top`, `right`, `bottom`, or `left` to activate the fixed behavior
- Without a threshold offset, the element simply behaves as `relative`

## Exercise

You need a small, persistent "Help" button that hovers over *all* other page content. What CSS `position` value is the best choice and why?

## Stacking Context

- Positioning elements introduces the third dimension, which is depth or the Z-axis
- The `z-index` property controls which elements are drawn on top of others

## Z-Index Requirements

- The `z-index` property only works on elements that are not `position: static`
- Higher numerical values mean the element is closer to the user in the viewport

---

A website designer is using `position: absolute` everywhere to achieve a complex layout. What potential maintenance problems will this approach create over time?

## Managing Overlap

- Over-reliance on positioning often leads to visual bugs and inaccessible content
- Prioritize using Flexbox or Grid before resorting to explicit positioning methods

## Exercise

Write the CSS rule for an element to make it stick to the top of the viewport once the user scrolls it within 10 pixels of the top.
