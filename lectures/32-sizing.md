---
reading: '[MDN: Sizing](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Sizing)'
...

# CSS Sizing Fundamentals

## The CSS Box Model

- Every HTML element is a rectangular box
- This box has content, padding, border, and margin
- Sizing properties control the dimensions of this box 

## Width and Height

- The primary properties for sizing are `width` and `height`
- They set the dimensions of the content area
- They do not include padding, border, or margin by default 

## Exercise

Draw a simple box and label the four parts of the CSS Box Model.

## Box Sizing

- The `box-sizing` property changes how `width` and `height` are calculated
- Default value is `content-box`
- This means `width` and `height` apply only to the content 

## Border-Box

- Setting `box-sizing: border-box` is often preferred
- `width` and `height` then include padding and border
- This makes layout calculations much easier 

---

Why is `box-sizing: border-box` considered a best practice for modern CSS layouts?

## Min and Max Sizes

- `min-width` and `max-width` set limits on the element's width
- `min-height` and `max-height` set limits on the element's height 

## Responsive Design

- Min/max properties are crucial for responsive design
- They prevent elements from becoming too small or too large
- This ensures readability on different screen sizes 

## Exercise

Write a CSS rule that ensures a main content area is never wider than 1200 pixels.

## Length Units

- CSS uses various units for sizing
- Units are categorized as absolute or relative 

## Absolute Units

- Absolute units are fixed and do not change
- Examples: `px` (pixels), `cm` (centimeters), `in` (inches)
- `px` is the most common absolute unit for web design 

## Relative Units

- Relative units are based on another length
- They scale depending on the context
- This is key for flexible and responsive layouts 

## Viewport Units

- Viewport units are relative to the browser window size
- `vw` (viewport width): 1% of the viewport width
- `vh` (viewport height): 1% of the viewport height 

## Font Relative Units

- `em`: Relative to the font size of the element's parent
- `rem`: Relative to the font size of the root element (HTML) 

---

When would you choose to use `em` over `rem` for sizing an element's padding?

## Percentage Units

- `%` is relative to the size of the element's containing block
- For `width`, it is relative to the container's width
- For `height`, it is relative to the container's height 

## Intrinsic Sizing

- Intrinsic sizing is based on the content itself
- The browser determines the size based on what is inside
- This is the default behavior for many elements 

## Intrinsic Keywords

- Keywords like `max-content` and `min-content` control intrinsic sizing
- `max-content`: The element takes up the maximum possible width without wrapping
- `min-content`: The element takes up the minimum possible width 

## Flow Layout

- Block elements (like `div`) take up 100% of the available width by default
- Inline elements (like `span`) only take up the width of their content 

## Exercise

If a parent `div` has a width of 500 pixels, what is the calculated width of a child `div` with `width: 50%`?

## Aspect Ratio

- The `aspect-ratio` property maintains a proportional size
- It takes a ratio like `16 / 9` or `1 / 1`
- This is useful for images and video embeds 

## Aspect Ratio Example

```css
.video-container {
  width: 100%;
  aspect-ratio: 16 / 9;
}
```

- The height will automatically adjust to maintain the 16:9 ratio 

---

How does the `aspect-ratio` property simplify the process of embedding responsive video content?

## Sizing Images

- Images should often be sized using relative units
- Setting `max-width: 100%` is a common technique
- This prevents images from overflowing their container 

## Sizing with Flexbox

- Flexbox introduces new sizing concepts
- `flex-basis` sets the initial size of a flex item
- `flex-grow` and `flex-shrink` control how items distribute space 

## Sizing with Grid

- CSS Grid uses the `fr` (fractional unit)
- `1fr` represents one fraction of the available space
- This allows for easy distribution of space across columns and rows 

## Exercise

What is the difference between the `em` and `rem` units, and which is generally better for global layout consistency?
