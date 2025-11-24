---
reading: '[htmx Documentation](https://htmx.org/docs/)'
...

# Frameworks

## Traditional Web Problem

- Modern web applications often involve writing excessive JavaScript
- We ended up rebuilding many browser capabilities like form submission
- This leads to complex client-side state management

## What htmx Offers

- htmx allows you to access AJAX, CSS Transitions, WebSockets, and Server Sent Events
- This access is directly available within your HTML structure
- It extends HTML naturally instead of replacing it with client-side frameworks

## The Core Attributes

- The four core attributes are `hx-get`, `hx-post`, `hx-put`, and `hx-delete`
- These attributes specify which HTTP verb and URL to use for a request
- They turn any element into an AJAX request trigger

## Example Get Request

- To load new content into a `div`, add the `hx-get` attribute
- Clicking the button sends a GET request to `/items`

```html
<button hx-get="/items">Load Items</button>
```

## Controlling Where Content Goes

- The `hx-target` attribute specifies where the server response should be loaded
- This target can be an element's ID, a CSS selector, or keywords
- By default, htmx targets the element that triggered the request

## How Content Is Replaced

- The `hx-swap` attribute defines how the new content replaces the old content
- Common values include `innerHTML`, `outerHTML`, or `afterend`
- This gives fine-grained control over DOM manipulation

## Request Target Example

- The following code targets the element with the ID `parent-div`
- It replaces the content *inside* that element with the response

```html
<button hx-get="/clicked" 
        hx-target="#parent-div" 
        hx-swap="innerHTML">
  Click Me
</button>
```

---

If htmx encourages you to return full HTML snippets from your server, what are the architectural implications for the backend code?

## Customizing The Trigger

- By default, requests trigger on the "natural" event, like a click or change
- The `hx-trigger` attribute lets you specify different events
- You can use standard DOM events, custom events, or delay them

## Trigger Modifiers

- Modifiers allow for more precise control over when events fire
- Examples include `once` to fire only a single time
- The `delay:` modifier waits a specific duration before firing the request

## Exercise

Write the HTML for a button that posts to the URL `/contact/submit` and only triggers the request the first time it is clicked.

## Showing Load States

- The `htmx-request` class is added to the element during a request
- This lets you use CSS to show a loading spinner or change button text
- The `hx-indicator` attribute can target a different element to show the loading state

## Enhancing Navigation

- The `hx-boost` attribute allows you to upgrade standard HTML anchors and forms
- This makes them issue AJAX requests instead of full page loads
- It's a simple way to achieve faster navigation without changing server code

## Progressive Enhancement Benefit

- Since htmx uses standard HTML elements and attributes, it enhances existing functionality
- If htmx fails to load or is disabled, the page still functions normally
- This results in a robust and accessible user experience

---

How does htmx's approach of returning HTML snippets instead of JSON affect the ability to reuse data in different client-side contexts?

## HTTP Headers Sent

- htmx automatically includes special headers with every request
- The `HX-Request: true` header lets the server know it's an htmx request
- This allows the server to return only the necessary HTML fragment, not a full page layout

## The Server's Role

- The server's main job is simply to respond with HTML
- There is no need for complex JSON API serialization or CORS configuration
- This simplifies the entire web development stack dramatically

---

If you were building a mobile-first application, what are the tradeoffs of relying on htmx versus building a native mobile API that returns JSON data?

## Server-Side Headers

- The server can respond with specific headers to direct the client
- `HX-Redirect` tells the client to do a client-side redirect
- `HX-Refresh` forces a full page refresh on the client

## Exercise

A developer wants to load the response from `/users/1` into a list, appending the new content *after* the existing list items. What is the combination of the `hx-get` and `hx-swap` attributes they should use?

## Hypermedia Architecture

- htmx embraces the Hypertext As The Engine Of Application State (HATEOAS) principle
- The client receives instructions on what to do next embedded within the hypermedia
- HTML becomes the mechanism for state transitions, not a simple display layer

## Interacting With JavaScript

- htmx provides custom DOM events for lifecycle hooks
- You can listen for `htmx:beforeRequest` or `htmx:afterSwap` using standard JavaScript
- This allows you to integrate htmx with existing client-side logic when necessary

---

If htmx makes many single-page application features possible without complex JavaScript, is this a return to simpler web development or an embrace of a different kind of complexity?

## Exercise

If you wanted a text input field to send a GET request to `/search` every time the user types a character, what should the `hx-trigger` attribute be?
