---
reading: '[MDN: Getting started with CSS](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Getting_started)'
...

# Styling Basics

## What is CSS?

- CSS stands for Cascading Style Sheets
- It describes how HTML elements look on screen
- This includes colors, fonts, layout, and spacing

## Why Use CSS?

- It separates presentation from content
- This makes websites easier to maintain and update
- It allows for consistent branding across many pages

## HTML and CSS

- HTML provides the structure of your content
- CSS provides the visual styling and presentation
- They work together to create a complete webpage

## CSS Rulesets

- A CSS ruleset is the basic building block
- It consists of a selector and a declaration block
- Rulesets tell the browser what to style and how

## Declarations

- Inside a ruleset, declarations define style
- Each declaration has a property and a value
- Properties control an aspect, values set the appearance

## Selectors

- Selectors target specific HTML elements
- They tell CSS which parts of the page to style
- Common selectors include element names or classes

## Example Rule

```css
p {
  color: blue;
  font-size: 16px;
}
```

- This rule targets all `<p>` (paragraph) elements
- It sets their text color to blue
- It also sets their font size to 16 pixels

---

Imagine you're designing a complex website with hundreds of pages. Why might keeping your styling separate from your content be a significant advantage for your team?

## External Styles

- The most common and recommended way to use CSS
- Styles are written in a separate `.css` file
- This file is then linked to your HTML document

## Link Tag

- HTML uses the `<link>` element for external stylesheets
- It's placed within the `<head>` section of your HTML
- The `href` attribute points to your `.css` file

## Benefits

- Styles can be reused across multiple HTML pages
- Browsers can cache the CSS file for faster loading
- It keeps your HTML clean and easy to read

## Exercise

1.  Create two files: `index.html` and `style.css`
2.  In `index.html`, add a paragraph `<p>` element and link `style.css`
3.  In `style.css`, write a rule to make the paragraph text `green`

## Internal Styles

- CSS can be written directly within the HTML file
- You use a `<style>` element inside the `<head>` section
- This approach applies styles only to that specific page

## When to Use?

- Useful for single-page applications or quick demos
- Can be convenient for very small, isolated style blocks
- Generally less flexible than external stylesheets

---

When might an internal stylesheet be a more practical choice than an external one, even if it's not the "best practice" for large projects?

## Inline Styles

- Styles are applied directly to an HTML element
- You use the `style` attribute on the element itself
- This gives style to only that single element

## Why Avoid?

- It mixes presentation directly with content
- Difficult to maintain or update styles globally
- Makes HTML files much larger and less readable

## When to Use?

- Occasionally used for dynamic styles controlled by JavaScript
- Can be helpful for quick, one-off overrides during development
- Often seen in email templates for broad compatibility

## Order of Styles

- CSS rules can come from multiple sources
- Browsers decide which rule to apply based on specific criteria
- This process is called "cascading" and follows specific rules

## Specificity

- Specificity is a weighting given to CSS selectors
- It determines which rule applies if multiple rules target an element
- More specific rules override less specific ones

---

If you have a paragraph of text, and one CSS rule makes it blue while another makes it red, how do you think the browser decides which color to display? What factors might influence this decision?

## Exercise

1.  Using your `index.html` from the previous exercise, add an *inline* style to your paragraph element
2.  Set its `color` to `orange` using the `style` attribute
3.  Observe what color the text becomes in the browser

## Inheritance

- Some CSS properties are inherited by child elements
- For example, `color` set on a `<body>` might affect paragraphs inside it
- This helps propagate styles efficiently

## Common Properties

- `color` controls text color
- `font-family` sets the typeface
- `margin` and `padding` manage spacing around elements

## The Box Model

- Every HTML element is essentially a rectangular box
- CSS helps control the size, padding, borders, and margins of this box
- Understanding this model is fundamental to layout

---

![Box Model](https://upload.wikimedia.org/wikipedia/commons/7/7a/Boxmodell-detail.png)

## Exercise

In your `style.css` file, add a rule that targets your paragraph `<p>` and sets its `font-size` to `20px` and its `font-family` to `monospace`.
