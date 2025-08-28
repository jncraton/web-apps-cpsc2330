---
reading: '[MDN: Creating Links](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Creating_links)'
...

# Navigating the Web

---

## What are Links?

- The fundamental building blocks of the web
- Connect documents across the internet
- Allow users to move seamlessly

---

## The `<a>` Element

- Stands for "anchor"
- Defines a hyperlink
- Turns text or other content into a clickable element

---

## `href` Attribute

- Hypertext Reference
- Specifies the destination URL
- The required attribute for any functional link

---

## Link Text

- The visible, clickable part
- Should be descriptive and concise
- Provides context to the user

---

How do you decide what text to make clickable?

---

## Enhancing Links

- Provide additional context
- Improve accessibility for users
- Offer a better user experience

---

## `title` Attribute

- Offers supplementary information
- Displays on hover as a tooltip
- Explains the link's purpose further

---

## `title` Example

```html
<a href="https://example.com" title="Visit the Example Website">Example Site</a>
```

- Displays "Visit the Example Website" on hover

---

## Exercise

Create a simple link to a favorite website, including a descriptive `title` attribute.

---

## Types of URLs

- Absolute URLs
- Relative URLs
- Different uses for different scenarios

---

## Absolute URLs

- Complete web address
- Includes protocol, domain, path
- Links to any external resource

---

## Relative URLs

- Path from the current page
- Points to resources within the same site
- More concise for internal links

---

## Relative Examples

- `images/logo.png` to find an image
- `../index.html` to navigate up a directory
- `./about.html` for a sibling page

---

Consider a large website with hundreds of pages. What might be the advantages and disadvantages of using only absolute URLs for internal navigation?

---

## Linking Within Pages

- Jump to specific sections
- Useful for long documents
- Improves navigation efficiency

---

## Document Fragments

- Use `#` followed by an ID
- Targets elements on the same page
- Requires an `id` on the target element

---

## Creating an Anchor

- Add an `id` attribute to the element you want to link to
- `<h2 id="intro">Introduction</h2>`

---

## Linking to Anchor

- Reference the `id` in the `href`
- `<a href="#intro">Jump to Intro</a>`
- Works even if the URL is different

---

## Exercise

Imagine you have a long blog post. Create a link that jumps to a section with the ID `conclusion`.

---

## Special Link Types

- Go beyond standard web pages
- Interact with user systems
- Facilitate downloads or emails

---

## Download Links

- `download` attribute
- Prompts a file download instead of opening in the browser

---

## `download` Example

```html
<a href="document.pdf" download="my-report.pdf">Download Report</a>
```

- Downloads `document.pdf` as `my-report.pdf`

---

## Email Links

- `mailto:` protocol
- Opens the user's email client
- Pre-fills recipient information

---

## `mailto:` Details

- Can include subject, body, CC, BCC
- Uses URL query parameters
- `mailto:name@example.com?subject=Hello`

---

How do you think web developers should balance user convenience with privacy when designing email links that pre-fill information?

---

## Good Link Hygiene

- Always test your links
- Ensure all links lead somewhere useful
- Regularly check for broken links

---

## Exercise

Create an email link to `your.email@example.com` that pre-fills the subject line with "Website Feedback" and the body with "I noticed...".
