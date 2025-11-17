---
reading: '[MDN: Flexbox](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Flexbox)'
...

# Mastering Flexible Layout

## Why Flexbox Matters

- Flexbox is the Flexible Box Layout module, a modern CSS standard
- It is a powerful one-dimensional layout method for arranging items
- Its primary goal is distributing space and aligning items efficiently
- This approach provides predictable positioning across different screens

## Container and Items

- Flexbox operates on a distinct parent-child relationship model
- The parent HTML element is designated as the **flex container**
- All of the container's direct children automatically become **flex items**

## Making a Container

- To activate the flex context, use the `display` property in CSS
- Setting `display: flex` creates a block-level flex container
- Using `display: inline-flex` creates an inline flow container

## The Two Axes

- Flexbox uses two primary axes for all positioning calculations
- The **main axis** runs in the direction specified by `flex-direction`
- The **cross axis** always runs perpendicular to the main axis

## Defining Main Axis

- The `flex-direction` property explicitly sets the main axis
- Common values include `row` (the default) or `column`
- Reverse values like `row-reverse` change the starting point of the flow

## Justifying Content

- The `justify-content` property aligns items along the main axis
- Key alignment values are `flex-start`, `center`, and `flex-end`
- Distribution values like `space-around` add space between items and at ends

## Aligning Items

- The `align-items` property aligns items along the cross axis
- Use `align-items: center` to center items vertically in a row layout
- The default `stretch` value makes items fill the entire cross dimension

## Exercise

Write the CSS to make all flex items in a container center perfectly, both along the main axis and the cross axis, assuming `flex-direction: row`.

## Handling Overflow

- By default, flex items are forced onto a single line, causing overflow
- Use `flex-wrap: wrap` to allow items to drop onto new lines when necessary
- The `flex-flow` property is a useful shorthand for direction and wrapping

## Multi-line Control

- The `align-content` property controls the spacing between multiple flex lines
- This property only takes effect when `flex-wrap` is set to `wrap`
- It functions similarly to `justify-content` but acts on the cross axis

## Item Control

- Flex items can be individually manipulated to override container rules
- Key item properties include `order`, `align-self`, and the `flex` shorthand
- These properties allow for precise, granular control over item behavior

## Changing Display Order

- The `order` property dictates the visual order of items in the container
- It accepts an integer value, with all items defaulting to `0`
- Items with lower numerical values appear earlier in the flow

## Defining Growth

- `flex-grow` determines how much an item expands to fill available space
- It is a unitless ratio defining the proportion of space the item should take
- A value of `1` ensures the item takes one part of the total remaining space

## Defining Shrink

- `flex-shrink` determines how an item will contract if space is limited
- It is also a unitless ratio, with the standard default being `1`
- Setting it to `0` prevents the item from getting smaller than its `flex-basis` size

## Defining Basis

- `flex-basis` sets the initial, ideal size of a flex item before growth or shrinking
- It can take standard length values, like `150px` or `33%`
- If set to `auto`, the item's content size is used as the initial basis

## The Flex Property

- `flex` is a powerful shorthand for three core item sizing properties
- These are `flex-grow`, `flex-shrink`, and `flex-basis`
- This shorthand is commonly used to assign responsive sizing rules

---

Explain the critical difference between setting a flex item's size using `flex-basis` versus setting its size using a standard `width` or `height` property

## Individual Alignment

- `align-self` allows a single flex item to override the container's `align-items`
- This is useful for placing one or two items differently on the cross axis
- The available values are identical to those used for `align-items`

## Exercise

Write the single CSS declaration using the `flex` shorthand that ensures an item has an initial size of `200px`, can grow if necessary, but is prevented from shrinking.
