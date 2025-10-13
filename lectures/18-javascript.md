---
reading: '[What is JavaScript](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/What_is_JavaScript)'
...

# JavaScript

## What is JavaScript?

- The third pillar of modern web development
- Adds interactivity and dynamic behavior
- Makes web pages responsive and engaging

## Browser Interaction

- Runs directly within your web browser
- Interpreted by the browser's JavaScript engine
- Different browsers use unique engines, like V8 or SpiderMonkey

## HTML, CSS, JS

- HTML provides the fundamental structure and content
- CSS defines the presentation and visual styling
- JavaScript introduces functionality and dynamic action

## Client-Side Scripting

- Most commonly executed on the client side
- Code runs directly on the user's computer
- Enhances user experience without server interaction

## Server-Side Too

- Can also operate on the server with Node.js
- Used for building backends, APIs, and databases
- Enables full-stack JavaScript application development

## Adding JS: Inline

- Directly embedded within HTML tags
- Uses event handler attributes like `onclick`
- Generally discouraged for maintainability and separation of concerns

## Adding JS: Internal

- Placed inside `<script>` tags within an HTML file
- Often located in the `<head>` or `<body>` section
- Suitable for small, specific scripts unique to that page

## Adding JS: External

- Linked from a separate `.js` file via `src` attribute
- `<script src="my-script.js"></script>` is the syntax
- Best practice for organization, caching, and reusability

---

How does separating JavaScript into its own file benefit large web projects?

## Core Capabilities

- Updates content without reloading the entire page
- Handles user input and form interactions
- Controls multimedia playback and device features

## Dynamic Content

- Manipulates the Document Object Model (DOM)
- Adds, removes, or changes HTML elements
- Dynamically alters CSS styles based on conditions

## Interactivity

- Responds to user actions such as clicks or hovers
- Creates animations and sophisticated visual effects
- Validates form submissions before data is sent

## Browser APIs

- Built-in functionalities provided by the web browser
- Allow JavaScript to interact with the environment
- Examples include the DOM, Geolocation, and Web Storage

## Third-Party APIs

- External services integrated via JavaScript
- Add features like maps, social media feeds, or payment processing
- Often require an internet connection for data exchange

## Interpreted Language

- Code is read and executed line by line by the engine
- Does not require a separate compilation step before execution
- Leads to faster development and testing cycles

## High-Level Language

- Abstracts away complex, low-level computer details
- Easier for developers to read, write, and understand
- Focuses on program logic rather than memory management

## Dynamically Typed

- Variable types are determined at runtime
- You do not declare a variable's type explicitly
- Offers flexibility but demands careful type handling

## Multi-Paradigm

- Supports various programming styles and approaches
- Includes object-oriented, imperative, and functional paradigms
- Provides developers with diverse problem-solving tools

## JavaScript Ecosystem

- A vast collection of tools, libraries, and frameworks
- Popular frameworks include React, Angular, and Vue.js
- Libraries address specific tasks, like data fetching or UI components

## Node.js

- Extends JavaScript beyond the traditional browser environment
- Enables server-side development and command-line tools
- Used to build powerful, scalable network applications

## Exercise

Identify whether the following actions are primarily handled by JavaScript, HTML, or CSS.

- Defining the structure of a navigation menu
- Changing a button's color when hovered over
- Submitting a form and showing a "Success!" message
- Playing an audio file when a user clicks a link

## Exercise

Open your browser's developer console (F12 or right-click -> Inspect, then 'Console' tab). Type `alert('Hello, Class!');` and press Enter. Describe what happens.
