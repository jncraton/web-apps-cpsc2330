---
reading: '[DOM Scripting](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/DOM_scripting)'
...

# DOM

## What is DOM?

- Stands for Document Object Model
- The DOM represents a web page's structure
- It provides a programming interface for the page

## Page as Objects

- The DOM represents HTML documents as objects
- These objects can then be manipulated by scripting languages
- JavaScript is the primary language used for this purpose

## A Tree Structure

- The DOM organizes all page elements into a tree
- This tree is often called the DOM tree
- Each part of the document becomes a node in this tree

## Node Types

- Different parts of the document are different node types
- These include the document itself, elements, and text
- They all possess specific properties and methods

## Document Node

- The `document` object is the root of the DOM tree
- It represents the entire HTML page
- All other nodes are children or descendants of this node

## Element Nodes

- HTML elements like `<p>`, `<h1>`, or `<div>` are element nodes
- They can have attributes such as `id` or `class`
- Elements often contain other element or text nodes

## Text Nodes

- The actual content inside an element is a text node
- For example, "Hello World!" within `<p>Hello World!</p>`
- Text nodes are typically children of element nodes

---

What are the advantages of representing a web page as a structured, programmatic object that can be manipulated by code?

## JavaScript

- JavaScript uses the DOM to access and modify page content
- It can change the structure, style, and visible content
- This enables web pages to become dynamic and interactive

## Finding Elements

- Before making changes, you must first find the target elements
- The DOM provides several methods to select specific nodes
- We can select by ID, class, tag name, or CSS selectors

## `getElementById()`

- This method selects a single element by its unique `id`
- It returns the element object or `null` if no match is found
- HTML `id` attributes should always be unique per document

## `querySelector()`

- Selects the *first* element that matches a specified CSS selector
- Can select by tag name, class, ID, or more complex patterns
- It offers great flexibility for targeting specific elements

## `querySelectorAll()`

- This method selects *all* elements matching a CSS selector
- It returns a NodeList, which is a collection of elements
- You can then iterate over this list to apply changes to each

## Exercise

```html
<main>
  <p>1</p>
  <p>2</p>
  <p>3</p>
</main>
```

Write a JavaScript line to select the `main` element, and another line to select all `p` elements that are direct children of `main`

## Changing Content

- Once an element is selected, its content can be modified
- The `textContent` property gets or sets the element's text content
- It is a safe way to update text without parsing embedded HTML

## `innerHTML` Property

- This property gets or sets the HTML content *inside* an element
- It allows you to inject new HTML tags and structure
- Using `innerHTML` requires caution due to potential security risks

---

When would you choose to use `textContent` to update an element, rather than `innerHTML`? What are the potential security or performance drawbacks of using `innerHTML` carelessly?

## Managing Attributes

- HTML elements have attributes such as `src`, `href`, or `class`
- `setAttribute()` adds a new attribute or changes an existing one
- `getAttribute()` retrieves the current value of an attribute

## Class List Operations

- The `classList` property allows convenient management of CSS classes
- Methods like `add()`, `remove()`, and `toggle()` are available
- This simplifies changing an element's visual styling dynamically

## Exercise

You have an image element with `id="profile-pic"`. Write JavaScript code to change its `src` attribute to `images/new-avatar.jpg` and then add the CSS class `rounded-corners` to this image element.

## Creating New Elements

- New HTML elements can be dynamically created with JavaScript
- The `document.createElement()` method is used for this purpose
- It takes the tag name of the element as its argument

## Adding Text Content

- To add text to a newly created element, first create a text node
- `document.createTextNode()` generates a new text node
- This text node can then be appended as a child to an element

## Attaching Elements

- Newly created elements exist only in memory initially
- Use `appendChild()` to add them as the last child of an existing element
- `insertBefore()` places them before a specified existing child node

---

What are some practical web development scenarios where dynamically creating and inserting new elements using JavaScript would be more efficient or necessary than pre-defining them in HTML?

## Event Handling

- The DOM allows us to respond to various user interactions
- These interactions are called events, such as clicks or key presses
- Event handling makes web pages highly interactive and responsive

## `addEventListener()`

- This is the primary method for registering event handler functions
- It takes the event type and a function to execute when the event occurs
- You can attach multiple handlers to the same element for the same event

## Common Events

- `click`: fires when an element is clicked with a mouse
- `mouseover`: triggers when the mouse pointer enters an element
- `keydown`: occurs when a keyboard key is pressed down

## Exercise

Create a simple HTML button with the text "Toggle Color". Write a JavaScript snippet that, when this button is clicked, toggles a CSS class named `highlight` on a `div` element with the `id="content-box"`.
