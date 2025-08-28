---
reading: '[MDN: Basic HTML Syntax](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Basic_HTML_syntax)'
...

# Structuring Web Content

---

![Web and Internet](https://upload.wikimedia.org/wikipedia/commons/c/c4/IP_stack_connections.svg){height=540px}

---

## What is HTML?

- A markup language
- Not a programming language

## Elements and Tags

- Elements are represented by tags
- An element is everything from the start tag to the end tag

## Opening and Closing Tags

- A tag pair consists of `<tag>` and `</tag>`
- The content goes between the tags

## Example Paragraph

```html
<p>
  This is a paragraph.
</p>
```

## Anatomy of an Element

- Opening tag
- Content
- Closing tag

## Exercise

Identify the opening tag, closing tag, and content in the following example:

```html
<p>
  This is some text.
</p>
```

## Nesting Elements

- You can put elements inside other elements
- This creates the structure of a page

## Example Nesting

```html
<p>
  This is a paragraph with <strong>bold text</strong>.
</p>
```

## Proper Nesting

- Nested elements must be closed in the correct order
- The last opened must be the first closed

## Improper Nesting

- Overlapping tags can cause errors
- Tags must be fully contained
