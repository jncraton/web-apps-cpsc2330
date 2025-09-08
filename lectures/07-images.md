---
reading: '[MDN: Images](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/HTML_images)'
...

# HTML Images

## Displaying Images

- Images are a fundamental part of modern web design
- They effectively break up text, attract attention, and convey information
- HTML uses the `<img>` element to embed them into documents

## The img Element

- The `<img>` element is an "empty" or "void" element
- This means it does not have a closing tag
- Its behavior and content are determined solely by its attributes

## Image Source

- The `src` attribute is absolutely essential for every `<img>` element
- It specifies the file path or URL to the image you want to display
- This path can be relative to your project or an absolute web address

## Alt Text

- The `alt` attribute provides "alternative text" for an image
- This text describes the image content to users who cannot see it
- It's a cornerstone of web accessibility for images

## Why Alt Text?

- Screen readers announce the `alt` text, allowing visually impaired users to understand images
- It displays on the page if the image fails to load for any reason
- Search engines also use `alt` text to understand and rank your content

---

How does `alt` text improve the experience for *all* users, not just those with visual impairments?

---

## Exercise

Write an `<img>` tag for an image of a "[sunset over mountains](https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/%D0%9D%D0%B0%D1%80%D1%86%D0%B8%D1%81%D0%B8_%D0%B2_%D0%9C%D0%B0%D1%80%D0%BC%D0%B0%D1%80%D0%BE%D1%81%D0%B0%D1%85.jpg/960px-%D0%9D%D0%B0%D1%80%D1%86%D0%B8%D1%81%D0%B8_%D0%B2_%D0%9C%D0%B0%D1%80%D0%BC%D0%B0%D1%80%D0%BE%D1%81%D0%B0%D1%85.jpg)" named sunset.jpg. Include descriptive `alt` text.

## Image Dimensions

- The `width` and `height` attributes define the image's size
- Values are specified in pixels, like `width="400"`
- Using these attributes helps the browser reserve space before image load

## Aspect Ratio

- Specifying only one dimension, like `width`, can preserve the aspect ratio
- The browser automatically calculates the other dimension to prevent distortion
- This ensures your images always look proportional

## CSS vs. HTML

- HTML `width` and `height` attributes are for initial rendering and performance
- CSS properties are generally preferred for styling and responsive control

## The Title Attribute

- The `title` attribute provides supplementary advisory information
- It typically appears as a tooltip when a user hovers over the image
- This information is not usually critical for understanding the image content

## Title Caution

- The `title` attribute is less accessible than `alt` text
- Screen readers do not consistently support or announce `title` text
- For images, it's generally discouraged in favor of `figcaption` or `alt`

## Figure Element

- The `<figure>` element semantically groups self-contained content
- It's commonly used for images, diagrams, code examples, or quotes
- This element helps associate content with its caption

## Figcaption Element

- The `<figcaption>` element provides a descriptive caption for the content within a `<figure>`
- It clearly explains or labels the associated image or media
- This improves both accessibility and overall content clarity

## Exercise

Create an `<img>` tag for a [key opening a lock](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Pin_tumbler_with_key.svg/576px-Pin_tumbler_with_key.svg.png) wrap it in a `<figure>` element and add a `<figcaption>` that labels it.

---

What are some situations where you might choose to *not* include an image on a webpage, even if you have one available?

---

## Responsive Images

- Images must adapt gracefully to various screen sizes and device capabilities
- Serving large images on small screens wastes bandwidth and loads slowly
- Displaying small images on large screens can result in blurry or pixelated visuals

## Srcset Attribute

- The `srcset` attribute allows you to provide a list of different image sources
- The browser intelligently chooses the most appropriate image from this list
- This choice is based on factors like the device's pixel density or viewport width

## Example

```html
<picture>
  <source
    srcset="
      https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Saturn_during_Equinox.jpg/2560px-Saturn_during_Equinox.jpg 2560w,
      https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Saturn_during_Equinox.jpg/1024px-Saturn_during_Equinox.jpg 1024w,
      https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Saturn_during_Equinox.jpg/330px-Saturn_during_Equinox.jpg 330w"
    sizes="(max-width: 330px) 330px, (max-width: 1024px) 1024px, 2560px">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Saturn_during_Equinox.jpg/960px-Saturn_during_Equinox.jpg" alt="Saturn during equinox">
</picture>
```


## Sizes Attribute

- The `sizes` attribute complements `srcset` by describing the image's intended display width
- It uses media conditions to tell the browser how much space the image will occupy
- This helps the browser make an informed decision when selecting an image from `srcset`

## The Picture Element

- The `<picture>` element offers more explicit control over responsive images
- It contains multiple `<source>` elements and one `<img>` element
- This allows for "art direction" by changing the image source based on media queries

## Art Direction

- Art direction involves serving completely different image crops or versions
- This ensures visual fidelity and effective messaging across diverse screen sizes
- It's not just about scaling, but about presenting the best visual representation

## Image Formats

- Not all user agents support all images formats
- The `<picture>` element provides a way list images in multiple formats (`jpg`, `webp`, etc)
- User agents pick the format they can display based on user preferences

---

In what scenarios would the `srcset` attribute be more appropriate than the `picture` element, and vice-versa?

---

## Accessibility Recap

- Always prioritize the `alt` attribute for all meaningful images
- Use `figcaption` within `<figure>` for extended image descriptions
- Consider `aria-hidden="true"` for purely decorative images

## Performance Tips

- Optimize image file sizes without sacrificing quality
- Use modern image formats like WebP or AVIF when possible
- Implement lazy loading for images that are not immediately visible

## Semantic HTML

- Use `<img>` for embedding standalone images
- Wrap images with captions in `<figure>` and `<figcaption>`
- Choose the right element for the meaning, not just the appearance
