---
reading: '[MDN: Box Model](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Box_model)'
...

# Elements as Boxes

## The Core Idea

- Every single HTML element is conceptually treated as a rectangular box
- This fundamental model defines exactly how elements take up space and relate to others

## Box Components

- The box model is composed of four distinct and measurable layers
- These layers stack outwards in the order of content, padding, border, and margin

## Content Layer

- This is the innermost area where the actual text and images reside
- The `width` and `height` properties usually set the dimensions of this specific area

## Padding Layer

- Padding is the buffer of space that sits immediately outside the content area
- It is a transparent layer that creates distance between the content and the element's edge

## Border Layer

- The border wraps directly around the padding and the content layers
- It is a visible line that separates the element from its surrounding space

## Margin Layer

- The margin is the outermost transparent layer of the box model
- It dictates the minimum amount of external space between the box and any adjacent elements

---

![Box Model](https://upload.wikimedia.org/wikipedia/commons/7/7a/Boxmodell-detail.png){height=540px}

---

Why is understanding the margin and padding distinction crucial for building professional, responsive web layouts?

## Controlling Dimensions

- We can specify the size of an element's area with `width` and `height` properties
- However, the definition of what constitutes that specified width depends on the box model used

## Setting Padding

- The `padding` shorthand allows you to set all four sides of the internal space at once
- You can target individual sides for precise control using properties like `padding-right`

## Setting Margin

- Margins can be set using the `margin` shorthand in the same manner as padding
- The value `margin: auto` is commonly used to horizontally center a block-level element

## Margin Collapsing

- Vertical margins between two block elements can sometimes collapse into a single space
- The resulting margin is the size of the *largest* of the two original margins, not the sum

## Exercise

Using your browser's developer tools, inspect a heading element and a paragraph element on a live webpage and note the default top and bottom margin values for each.

## Display Types

- Elements are fundamentally categorized as either `block` boxes or `inline` boxes
- The display type significantly dictates how the box behaves within the flow of the document

## Block Boxes

- A block box always begins on a new line and automatically extends to use all available horizontal space
- Examples include structural elements like `<div>`, `<p>`, and various heading tags

## Inline Boxes

- An inline box only occupies exactly as much width as its content requires
- Elements like `<a>` for links or `<span>` for text emphasis are typically inline

---

What issues might arise if you try to apply a `width` or `height` property to a standard inline element?

## Hybrid Boxes

- The `display: inline-block` value creates a useful combination of the two types
- It allows the box to flow horizontally like an inline element but still respects `width` and `height` properties

## Standard Sizing

- The default browser model is explicitly named the `content-box` model
- Under this rule, the set `width` property only applies to the element's content area

## Sizing Calculations

- The total width of the element equals the `width` property plus padding and plus border
- This default calculation can often lead to layout elements overflowing their intended container

## Alternative Sizing

- The `border-box` model fundamentally changes the dimension calculation process
- The specified `width` property now includes the space taken up by the padding and the border

## Preferred Sizing

- Some developers prefer using `border-box` universally
- This can be achieved using the universal selector and including pseudo-elements:

  ```css
  *,
  *::before,
  *::after {
    box-sizing: border-box
  }
  ```

---

If you set an element to have a `width` of `50%` and a `border-box` model, what part of the surrounding container does that `50%` measurement refer to?

## Exercise

A box has `width: 200px`, `padding: 10px`, and `border: 5px solid`. Calculate the total rendered width under both the `content-box` and `border-box` models.

## Box Model Summary

- The box model is truly the fundamental bedrock for all visual layout on the web
- Mastery of its components and the various sizing rules is essential for responsive design

## Exercise

Write a CSS rule to give a `div` element 15 pixels of internal space on the left and right, and 20 pixels of external space on the top and bottom.