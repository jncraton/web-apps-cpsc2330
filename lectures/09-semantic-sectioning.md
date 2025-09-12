---
reading: '[MDN: Content Sectioning Elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements#content_sectioning)'
...

Lab questions?

# Structuring Web Content

## Content Sectioning

- Organizing your web pages effectively
- Giving meaning to different parts of content
- Crucial for accessibility and SEO

## The Body Element

- Represents the visible content of a document
- Everything a user sees and interacts with
- Only one `<body>` per HTML document

## Headings: h1-h6

- Establish content hierarchy and importance
- `<h1>` is the most significant heading
- `<h6>` is the least significant heading

---

Consider a webpage without any headings.

How might that impact a user navigating with a screen reader or someone quickly scanning the page for information?

## `<main>`

- Contains the dominant content of the `<body>`
- What the central topic of the document is about
- There should only be one `<main>` per document

## `<article>`

- Independent, self-contained composition
- Makes sense on its own if syndicated
- Examples include blog posts or comments

---

Imagine you are building a blog post. What specific pieces of content would you place inside the `<article>` tag?

## `<section>`

- Generic standalone section of a document
- Often has a heading as its title
- Groups related content thematically

## `<section>` vs `<article>`

- An `<article>` is a complete, distributable unit
- A `<section>` groups related content within a larger context
- You might have `<section>`s inside an `<article>`

---

When creating a page for a university course, where might you use `<section>` elements, and where might an `<article>` element be more appropriate?

## `<nav>`

- The `<nav>` element contains primary navigation links
- Main blocks of links for the entire site
- Often links to other pages or parts of the current page

## `<aside>`

- Represents content indirectly related to the main content
- Often presented as a sidebar or pull-quote
- Think of footnotes or related links

## `<header>`

- Introductory content for its nearest sectioning root
- Can contain headings, navigation, or logos
- Not just for the top of the entire document

## `<footer>`

- Concluding content for its nearest sectioning root
- Can include authorship, copyright, or related links
- Often found at the bottom of a section or page

## Header Examples

- A document-level `<header>` can hold site title and main navigation
- An `<article>` can have its own `<header>` for the article title and author

## Footer Examples

- A document-level `<footer>` contains site-wide copyright info
- An `<article>` can have its own `<footer>` with author details or share buttons

---

If a blog post includes comments, would each comment be an `<article>` or a `<section>`? Justify your choice based on our discussion of semantic elements.

## Address Element

- Provides contact information for the nearest `<article>` or `<body>`
- Author, owner, or other relevant contact details
- Typically renders in italics by default

## Exercise

Write a simple HTML snippet for a `<footer>` that includes a copyright notice and an `<address>` element for a fictional company's contact information.

```html
<footer>
  <!-- Your content here -->
</footer>
```

## Why Semantics Matter

- Improves accessibility for users with disabilities
- Enhances search engine optimization (SEO)
- Makes code easier to read and maintain

## Clearer Codebase

- Developers understand the structure instantly
- Facilitates team collaboration and updates
- Reduces potential for misinterpretation

## Exercise

Create a simple "About Us" page. Use three different HTML content sectioning elements appropriately.
