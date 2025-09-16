---
reading: '[MDN: Tables](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/HTML_table_basics)'
...

# HTML Tables

## Purpose of Tables

- Organize and display tabular data
- Present information clearly and structured
- Essential for data-driven web content

## Not For Layout

- Tables are for data, not page design
- Use CSS for visual layout and positioning
- Avoid tables for non-tabular content

## Table Tag

- The `<table>` element defines an HTML table
- It acts as a container for all table content
- All other table-related elements reside inside it

## Table Rows

- The `<tr>` element defines a table row
- Each `<tr>` holds one row of data or headers
- It groups related cells horizontally

## Data Cells

- The `<td>` element defines a standard data cell
- This is where your actual table data goes
- Each `<td>` must be inside a `<tr>` element

## Header Cells

- The `<th>` element defines a table header cell
- These cells provide context for columns or rows
- Browsers often display `<th>` text as bold and centered

## Exercise

Create a simple HTML table with two rows and two columns. Make the first row contain header cells and the second row contain data cells.

---

What is the primary benefit of using `<th>` over just styling a `<td>` to look like a header?

## Grouping Content

- HTML provides elements to group table content
- These elements enhance structure and meaning
- They help define semantic sections of a table

## Table Head

- The `<thead>` element groups the header content
- It contains one or more `<tr>` elements with `<th>`
- It clearly identifies the table's column headings

## Table Body

- The `<tbody>` element groups the main body content
- It contains one or more `<tr>` elements with `<td>`
- This section holds the actual data rows of the table

## Table Foot

- The `<tfoot>` element groups summary content
- It typically contains sums, averages, or totals
- Often placed after `<tbody>` but appears at the bottom

## Exercise

Take your previous 2x2 table and wrap the header row in `<thead>` and the data row in `<tbody>`.

## Table Caption

- The `<caption>` element provides a title for the table
- It describes the table's content in a concise way
- This improves accessibility for all users

## Caption Placement

- The `<caption>` tag must be the first child of `<table>`
- It is placed immediately after the `<table>` opening tag
- This ensures its semantic association with the table

## Spanning Cells

- `colspan` allows a cell to span multiple columns
- `rowspan` allows a cell to span multiple rows
- These attributes merge cells horizontally or vertically

## Colspan Example

- A single cell stretching across several columns
- Useful for grouping sub-headers or combined data
- `<td>` or `<th>` elements use the `colspan` attribute

```html
<th colspan="2">Details</th>
```

## Rowspan Example

- A single cell stretching across several rows
- Useful for shared labels or categorizations
- `<td>` or `<th>` elements use the `rowspan` attribute

```html
<td rowspan="2">Category A</td>
```

---

When might using `colspan` or `rowspan` make a table *less* accessible or harder to understand?

## Accessibility

- Semantic HTML is crucial for screen readers
- Well-structured tables are easier to navigate
- Ensure every user can understand your data

## Scope Attribute

- The `scope` attribute explicitly defines header direction
- `scope="col"` identifies a column header
- `scope="row"` identifies a row header

## How Scope Helps

- Guides screen readers to associate data with headers
- Clarifies the relationship between cells
- Enhances understanding of complex tables

## Best Practices

- Use tables only for tabular data
- Always include `<thead>`, `<tbody>`, and `<caption>`
- Use `<th>` with `scope` for headers
