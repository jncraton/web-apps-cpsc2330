---
reading: '[MDN: Grid](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Grids)'
...

# Grid Layout

## Why Use Grid?

- Grid is a powerful two-dimensional layout system
- It enables precise control over both rows and columns simultaneously
- It simplifies organizing content into complex, structured interfaces

## Grid vs Flexbox

- Flexbox is designed for one-dimensional layouts, either a single row or a single column
- Grid manages content in two dimensions, defining a full container structure
- They often work well when nested, with Grid for the main layout

## The Grid Container

- To activate the grid layout, apply `display: grid` to the parent element
- Only the direct children of the container become grid items
- This is the essential first step for any grid design

```css
.container {
  display: grid;
}
```

---

![Grid Layout](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Grids/grid.png){height=400px}

## Tracks and Lines

- A track is the space between two grid lines and defines a row or a column
- Grid lines are the dividing lines, which are implicitly numbered starting at 1
- Tracks are created and sized explicitly using template properties

## Sizing Grid Tracks

- We define the size of columns and rows using `grid-template-columns` and `grid-template-rows`
- These properties accept standard length units like `px`, `%`, or the flexible `fr` unit

```css
.container {
  grid-template-columns: 200px auto 1fr;
}
```

## The `fr` Unit

- The `fr` unit, or "fractional unit," represents a share of the available space
- It makes distributing remaining space between tracks simple and responsive
- For example, `1fr 1fr` creates two columns of equal width after fixed-size tracks are accounted for

## Exercise

If a grid container is 1000px wide, and you set `grid-template-columns: 100px 1fr 3fr`, what is the final width of the column defined by `3fr`?

## Placing Items

- By default, grid items are placed automatically in order, filling the grid tracks
- We can explicitly position items based on the numerical grid lines
- This allows items to be placed anywhere in the defined structure

## Explicit Placement

- To place an item, specify its start line for the row and/or column
- Use properties like `grid-column-start` and `grid-row-start` to assign a line number
- The item will occupy only one track unless a span is defined

## Spanning Tracks

- We can make an item cover multiple tracks using the `span` keyword
- Set the end position to `span` followed by the number of tracks the item should cover

```css
.item-a {
  grid-column-end: span 3;
}
```

## Grid Template Areas

- This method allows you to name sections of your grid layout
- Names provide a semantic way to build complex, magazine-style layouts
- It makes the overall layout structure immediately clear in the CSS

## Defining Areas

- The `grid-template-areas` property is applied to the container
- The layout is mapped visually using strings of area names
- A dot (`.`) signifies an empty cell within the grid

```css
.container {
  grid-template-areas:
    "head head"
    "nav main";
}
```

## Assigning Items to Areas

- Once the areas are defined, assign an item to a named area
- Use the `grid-area` property on the specific grid item

```css
.navigation {
  grid-area: nav;
}
```

## Alignment Control

- The `justify-items` property aligns content along the row axis within the cells
- The `align-items` property aligns content along the column axis within the cells
- These are set on the grid container to apply to all children

## Implicit Grid

- The implicit grid forms when items are placed outside the explicitly defined tracks
- The grid creates new tracks automatically to accommodate the misplaced items
- You can control the size of these automatic tracks using `grid-auto-rows` or `grid-auto-columns`

---

In what scenarios would you choose to use the implicit grid functionality rather than explicitly defining all your rows and columns?

## Exercise

Using the `grid-template-areas` property, define a 2x2 grid where the top-left is `logo`, the top-right is `header`, the bottom-left is an `aside`, and the bottom-right is `content`.
