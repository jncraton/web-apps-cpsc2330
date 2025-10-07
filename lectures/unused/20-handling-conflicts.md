---
reading: '[Handling conflicts in CSS](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Handling_conflicts)'
...

# CSS Conflict Resolution

## Why Conflicts Exist?

- Web styling uses Cascading Style Sheets
- "Cascading" means styles can come from many places
- These styles might disagree on how an element should look

---

How does a web browser decide which style to apply when multiple rules target the same element?

## Core Principles

- Browsers have a clear set of rules
- These rules resolve styling conflicts predictably
- Understanding them is key to effective web design

## The Cascade Layers

- Styles come from different origins
- User agent stylesheets (browser defaults)
- Author stylesheets (your CSS code)
- User stylesheets (custom browser settings)

## Priority Order

- Styles are applied in a specific sequence
- Browser defaults are lowest priority
- Your styles typically override defaults
- User styles can sometimes override yours

## Inheritance Basics

- Some CSS properties are inherited by child elements
- Child elements automatically adopt their parent's styles
- This creates a visual hierarchy on the page

## What Inherits?

- Properties like `color`, `font-family`, `text-align`
- These make text styling consistent across elements
- Layout properties like `margin` or `border` do not inherit

## Undoing Inheritance

- You can reset inherited values
- `initial` reverts to the browser's default value
- `unset` resets to inherited or initial value
- `revert` changes to user or user-agent style

```css
p {
  color: initial;
}
```

---

Imagine you have a `<div>` with `font-size: 20px;` and inside it, a `<p>` element. If you don't set a `font-size` for the `<p>`, what will its font size be and why?

## Specificity Matters

- Specificity measures how precise a selector is
- More specific selectors win conflicts
- This is true even if they appear earlier in your code

## Specificity Scores

- Each selector type has a point value
- IDs (`#my-id`) are most specific (100 points)
- Classes (`.my-class`) and attributes (`[type="text"]`) are next (10 points)
- Elements (`p`) and pseudo-elements (`::before`) are least specific (1 point)

## Inline Styles

- Styles directly in HTML `style` attributes
- These have very high specificity (1000 points)
- They typically override all other author styles

```html
<p style="color: blue;">Hello!</p>
```

## Universal Selector

- The universal selector (`*`) has zero specificity
- It applies to all elements but is easily overridden
- Often used for global resets or base styles

## Exercise

Given these CSS rules, which `color` would a `<p>` element become? Explain why.

```css
p { color: red; }
.text-style { color: blue; }
#main-content p { color: green; }
```

## Order of Appearance

- If specificity scores are equal, the last rule wins
- This applies to rules within the same stylesheet
- It also applies to multiple linked stylesheets

---

Why is the order of your CSS files in the `<head>` section of your HTML document important for how styles are applied?

## Link Order

- The order of `<link>` tags in HTML matters
- Stylesheets linked later can override earlier ones
- This is a common way to apply theme changes

## The !important Rule

- `!important` overrides almost everything
- It forcefully applies a style declaration
- This bypasses normal cascade rules

## Using !important

- Add `!important` to the end of a declaration
- `color: purple !important;`
- Generally, avoid using it unless absolutely necessary
- It makes debugging and maintenance difficult

## When to Use !important

- Overriding third-party library styles
- Developer tools for quick testing
- Accessibility features for users with specific needs

## Exercise

Consider this HTML and CSS. What color will the text "Hello" be?

```html
<p id="message" class="info" style="color: orange;">Hello</p>
```

```css
#message { color: red; }
.info { color: blue !important; }
p { color: green; }
```

## Cascade Summary

- Browser determines the final style
- It uses a specific hierarchy of rules
- Understanding this prevents unexpected visual outcomes

## The Cascade Order

- User agent styles (browser defaults)
- User styles (browser/OS settings)
- Author styles (`!important` first, then normal)
- Inline styles (highest author priority)

## Best Practices

- Avoid `!important` whenever possible
- Use well-structured, semantic selectors
- Keep your stylesheets organized and modular
- Test your styles across different browsers
