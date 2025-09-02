---
reading: '[MDN: Lists](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Lists)'
...

# Lists

## Why Use Lists?

- Organize information clearly
- Improve content readability
- Establish visual hierarchy

## Semantic HTML

- Give meaningful context to content
- Assist various screen readers
- Enhance search engine understanding

## List Types

- Unordered lists (`<ul>`)
- Ordered lists (`<ol>`)
- Description lists (`<dl>`)

## Unordered Lists

- Items without a specific order
- Often rendered with bullet points
- Ideal for groups of related items

## UL Syntax

```html
<ul>
  <li>First item</li>
  <li>Second item</li>
  <li>Third item</li>
</ul>
```

## UL Examples

- Shopping list items
- Product feature highlights
- Unsequenced recipe ingredients

---

Why is it important for a list to be semantically correct, rather than just using generic elements with bullet point styling?

## Ordered Lists

- Items with a sequential order
- Often rendered with numbers or letters
- Critical when the order matters

## OL Syntax

```html
<ol>
  <li>Step one</li>
  <li>Step two</li>
  <li>Step three</li>
</ol>
```

## OL Attributes

- `start`: Set the initial number
- `reversed`: Count downwards
- `type`: Change numbering style

## Start Attribute

```html
<ol start="5">
  <li>Item five</li>
  <li>Item six</li>
</ol>
```

## Reversed Order

```html
<ol reversed>
  <li>Last item</li>
  <li>Middle item</li>
  <li>First item</li>
</ol>
```

## Type

- `a` for lowercase letters
- `A` for uppercase letters
- `i` for lowercase Roman numerals
- `I` for uppercase Roman numerals
- `1` for numbers (default)

## Exercise

Create an ordered list of your top five favorite movies, starting from the fifth

## Description Lists

- Terms and their associated descriptions
- Ideal for glossaries or metadata
- Not for general list items

## DL Syntax

```html
<dl>
  <dt>Term</dt>
  <dd>Description of the term</dd>
</dl>
```

## DL Examples

- Explaining acronyms
- Presenting product specifications
- Defining key concepts

## DL Structure

- Each term uses a `<dt>` tag
- Each description uses a `<dd>` tag
- One `<dt>` can have multiple `<dd>`s

```html
<dl>
  <dt>HTML</dt>
  <dd>HyperText Markup Language</dd>
  <dd>A language for web content</dd>
</dl>
```

---

Consider a university course catalog. Would you use an ordered, unordered, or description list to display the course number, title, and a brief description for each course? Justify your choice.

## Nesting Lists

- Creating sub-lists within list items
- Establishes hierarchy and relationships
- Useful for outlines or complex menus

## Nesting Example

```html
<ul>
  <li>Main item one
    <ul>
      <li>Sub-item A</li>
      <li>Sub-item B</li>
    </ul>
  </li>
  <li>Main item two</li>
</ul>
```

## OL Inside UL

- You can mix different list types
- Common for outlines with procedural steps

```html
<ul>
  <li>Project Phases
    <ol>
      <li>Planning</li>
      <li>Execution</li>
      <li>Review</li>
    </ol>
  </li>
</ul>
```

## Exercise

Imagine you are outlining a research paper. Create a nested list structure that includes at least one unordered main section with a nested ordered sub-section.

## Accessibility Impact

- Screen readers interpret list structures
- Proper semantics improve navigation
- Ensures content is understandable

---

What are some potential challenges or considerations when deciding how deeply to nest lists within a complex document structure?

## Exercise

Using any type of list (or a combination), list your three favorite programming languages, and then for each, add a single-item nested list explaining why you like it.
