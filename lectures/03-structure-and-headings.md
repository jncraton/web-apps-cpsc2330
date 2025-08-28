---
reading: '[MDN: Structuring Documents](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Structuring_documents), [MDN: Headings and Paragraphs](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Headings_and_paragraphs)'
...

# HTML Structure

## Complete HTML Documents

- Include HTML version
- Include a title
- Should specify human language
- Should specify charset

## HTML Version

- Currently 5
- Specified using `<!doctype html>` as the first characters
- Avoids rendering in quirks mode

## Title

- Provides a title for a page
- Commonly shown in browser tab
- Lives within the `<head>` element

## head

- Includes global page data
- May include `<meta>` elements holding page metadata
- Often includes style information
- Not rendered by the user agent

## charset

- Used to specify document character encoding
- Commonly `<meta charset="utf-8">`
- Defined in `<head>` element

## body

- Hold visible content elements

## Optional

- `<html>`, `<head>`, and `<body>` are optional
- They will be inferred if omitted
- Documents may be clearer if included
- Google style guide [suggests considering omission](https://google.github.io/styleguide/htmlcssguide.html#Optional_Tags)

## Content Structure

What are some examples of structured content you encounter daily?

## Why is it important?

- Improves readability for human users
- Helps with SEO for search engines
- Enhances accessibility for screen readers

## Headings

- Organize document with hierarchy
- Use `<h1>` for main title
- Use `<h2>`, `<h3>`, etc. for subheadings

## Heading levels

- Six heading levels available
- `<h1>` is the most important
- `<h6>` is the least important

## Don't skip levels

- Do not jump from `<h1>` to `<h3>`
- Follow a logical sequence
- This creates an outline for the document

-----

How might a screen reader use headings to help a user navigate a webpage?

## Exercise

Using a text editor, create a document with an `<h1>` and two `<h2>` headings.

## Paragraphs

- Used for blocks of text
- The element is `<p>`
- Each block of text should have its own `<p>` element

## Semantics

- Use elements for their intended purpose
- `<p>` is for paragraphs
- Headings are for headings

## What not to do

- Do not use headings for styling text
- Do not use `<p>` for a single line break
- Do not use empty `<p>` elements

## Why avoid empty elements?

- Screen readers may announce them
- They create unnecessary clutter
- Can cause unexpected rendering issues

## Accessibility

- Proper structure is key
- Screen readers create an outline
- Visually impaired users can find content

## Exercise

Open a website you frequent and inspect the headings. Do they follow a logical order?

-----

What are the benefits of proper HTML structure for search engine optimization?

## A simple example

```html
<h1>Main Title</h1>
<p>This is the first paragraph of text.</p>
<h2>Subheading One</h2>
<p>A paragraph under a subheading.</p>
<h2>Subheading Two</h2>
<p>A second paragraph under a different subheading.</p>
```

-----

Consider a news article. How would you use headings and paragraphs to structure its content?

## Exercise

Write a short summary of a favorite movie using `<h1>`, `<h2>`, and `<p>` tags.
