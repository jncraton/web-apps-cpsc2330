# Structuring Web Content

-----

## What is HTML?

  - A markup language
  - Not a programming language

## Elements and Tags

  - Everything in HTML is an element
  - Elements are represented by tags

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

-----

What's the purpose of HTML? What is a markup language?

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

-----

How would you describe the difference between proper and improper nesting?

## What are Attributes?

  - Extra information for an element
  - They do not appear in the content

## Anatomy of an Attribute

  - An attribute has a name and a value
  - The value is in quotes

## Example Attribute

```html
<a href="https://example.com">
  Example Link
</a>
```

## Exercise

Add an attribute to the `<img>` tag to make it display the image "sunset.jpg".

```html
<img src="">
```

## Void Elements

  - A few elements have no content
  - They don't need a closing tag

## Void Element Examples

  - `<img>` for images
  - `<input>` for forms
  - `<br>` for line breaks

-----

How does using attributes make HTML elements more powerful and flexible?

## Case Sensitivity

  - Tags are not case-sensitive
  - But lowercase is a best practice

## Best Practices

  - Always use lowercase for tags and attributes
  - Always use quotes around attribute values

## Final Exercise

Look at the following HTML. Identify the element, attribute, and content, then explain why the nesting is incorrect.

```html
<p>
  This is <strong>text.</p></strong>
```
