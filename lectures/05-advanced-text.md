---
reading: '[MDN: Advanced Text Features](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Advanced_text_features)'
...

# Semantic Text Markup

## Why Semantic HTML?

- Describe content's meaning
- Not just its appearance
- Improves accessibility
- Enhances search engines
- Makes code clearer

---

How might semantic HTML specifically benefit users who rely on screen readers?

## Block Quotes

- For longer block quotations
- Use `<blockquote>` tag
- Optional `cite` attribute
- Links to source URL

## Inline Quotes

- For short inline quotes
- Use `<q>` tag
- Browser adds quotation marks
- Optional `cite` attribute

## Citation Elements

- Use `<cite>` tag
- For title of a creative work
- E.g., book, song, film
- Not the author's name

## Quote Example

```html
<blockquote cite="https://www.w3.org/TR/html/text-level-semantics.html#the-blockquote-element">
  <p>The blockquote element represents content that is quoted from another source...</p>
</blockquote>
<p>As <cite>HTML Specification</cite> states, <q>inline quotes use the q element</q>.</p>
```

## Exercise

Write HTML to quote and cite Genesis 1:1 from BibleGateway.

## Abbreviations

- Use `<abbr>` tag
- For abbreviations or acronyms
- `title` attribute provides full text
- Helpful for clarity and SEO

## Address Elements

- Use `<address>` tag
- For contact information
- For nearest `<body>` or `article` parent
- Often includes name, address, email

## Abbr/Address Example

```html
<p>The <abbr title="World Wide Web Consortium">W3C</abbr> sets web standards.</p>
<address>
  <p>Anderson Univerity</p>
  <p>1100 E. 5th St.</p>
  <p>Anderson, IN</p>
</address>
```

---

When would you use an `<abbr>` tag versus simply writing the abbreviation directly?

## Superscript Text

- Use `<sup>` tag
- For text above baseline
- Common for footnotes or mathematical powers

## Subscript Text

- Use `<sub>` tag
- For text below baseline
- Common for chemical formulas or mathematical indices

## Sup/Sub Example

```html
<p>H<sub>2</sub>O is the chemical formula for water.</p>
<p>In algebra, x<sup>2</sup> means x squared.</p>
```

## Code Representation

- `<code>`: Inline code snippet
- `<pre>`: Preformatted text block
- Preserves whitespace and line breaks
- Often used with `<code>` inside

## Variable Elements

- Use `<var>` tag
- To represent a variable in programming or math
- Often italicized by default

## Keyboard Input

- Use `<kbd>` tag
- For user keyboard input
- Often monospace by default

## Sample Output

- Use `<samp>` tag
- For program output or a system message
- Often monospace by default

## Code Elements Example

```html
<p>To start the server, type <kbd>npm start</kbd> in your terminal.</p>
<pre><code>
function hello() {
  console.log("Hello, World!");
}
</code></pre>
<p>Output: <samp>Hello, World!</samp></p>
```

---

From an accessibility perspective, how do these various code-related elements enhance understanding for diverse users?

## Time Elements

- Use `<time>` tag
- For dates, times, durations
- `datetime` attribute for machine-readable format
- Improves search engine understanding

## Time Example

```html
<p>Our class begins on <time datetime="2024-09-04T10:00">September 4th at 10 AM</time>.</p>
<p>The report was published <time datetime="2023-11-01">November 1, 2023</time>.</p>
```

## Exercise

Using semantic HTML, mark up the following text: "The event is on October 26th, 2024. It will last for 3 hours. The formula for the speed of light is E = mc²."
