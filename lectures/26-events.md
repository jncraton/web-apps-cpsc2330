```
---
reading: '[MDN: Events](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Events)'
...

# Responding to Users

## What Are Events?

- Actions or occurrences happening in the browser
- Your code can listen for and react to them
- They make web pages interactive

## User-Triggered Events

- Clicking a mouse button
- Pressing a key on the keyboard
- Moving the mouse pointer over an element

## Browser-Triggered Events

- Finishing the loading of a page
- A video has finished playing
- An error occurs when fetching data

## Handling Events

- We write functions called "event handlers"
- These functions run when a specific event occurs on a specific element

## Three Attachment Methods

- Inline event handlers (old, bad practice)
- Event handler properties (simple, but limited)
- `addEventListener()` (modern, flexible, and preferred)

## Inline Handlers

This method mixes JavaScript directly into your HTML.

```html
<button onclick="alert('Hello!');">
  Click Me
</button>
```

## Please Don't

- This mixes your structure (HTML) and behavior (JS)
- It makes code much harder to read and maintain

## Handler Properties

- DOM elements have properties for handling events
- We can assign a function directly to these properties

## Property Example

```javascript
const btn = document.querySelector('button');

btn.onclick = function() {
  alert('Hello again!')
};
```

## Property Limitations

- The biggest drawback is you can only have one handler
- Assigning a new function overwrites the old one

## Exercise

Given an HTML button with `id="color-changer"`, write JavaScript to change the background color of the page to blue when the button is clicked, using an event handler property.

## The Modern Way

- Use the `addEventListener()` method
- It's the most flexible and powerful approach

## `addEventListener()` Syntax

```javascript
element.addEventListener('event-type', functionToRun)
```
- The event type is a string, like `'click'` or `'keydown'`

## `addEventListener()` Benefits

- You can add multiple handlers for the same event
- It provides finer control over the event-firing process
- It works on any event target, not just HTML elements

## Removing Handlers

- You can also remove listeners you've added
- This is done using `removeEventListener()`

## The Event Object

- Your handler function is automatically passed an argument
- This "event object" contains details about the event

## Using The Object

It's common to name this object `event`, `evt`, or `e`.

```javascript
btn.addEventListener('click', function(e) {
  console.log(e);
});
```

## Target

- The `event.target` property is very useful
- It gives you a reference to the specific element that triggered the event

## Event Propagation

- Events "travel" through the DOM tree
- This allows different elements to respond to the same event

## Event Bubbling

- The default behavior is "bubbling"
- The event fires on the target, then its parent, and so on up to the root

---

Can you think of a situation where you might want to stop an event from bubbling up to its parent elements?

## A Common Problem

What if you have 100 list items and want each to be clickable? Adding 100 listeners is inefficient.

## Event Delegation

- This pattern provides an elegant solution
- Place a single event listener on the common parent element

## How It Works

- An event on a child element will bubble up to the parent
- We use `event.target` to figure out which child was clicked

## Delegation Benefits

- Uses less memory and improves performance
- Automatically works for new child elements added later

## Exercise

Imagine an HTML `<ul>` with the id `shopping-list`. Write a single event listener on the `<ul>` that logs the text content of any `<li>` element that is clicked inside of it.
```