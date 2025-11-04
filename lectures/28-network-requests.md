---
reading: '[MDN: Network requests](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Network_requests)'
---

# Network requests

## Client/Server Interaction

- The client is typically the browser running your JavaScript code
- A request is sent to a server which hosts the necessary resources
- The server processes the request and sends back a response

## Asynchronous Requirement

- Network requests take an unpredictable amount of time to complete
- Synchronous requests would halt the entire browser interface
- We must use asynchronous methods to keep the user experience smooth

## Early Requests

- The older standard for scripting network requests was `XMLHttpRequest`
- This approach is often verbose and involves complex event handlers
- Modern JavaScript rarely uses this object directly for new development

## Modern Fetching

- The modern and simpler standard is the [`fetch()`](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) API
- It returns a `Promise`, which represents the eventual result of an operation
- Promises make managing asynchronous operations far cleaner

## A Basic Request

- Calling `fetch()` requires one argument: the URL of the resource
- The function immediately returns a `Promise` object
- We use the `.then()` method to define what happens when the Promise resolves

```javascript
fetch('users/data')
  .then(response => {})
```

## Handling the Response

- The first `.then()` receives a `Response` object, not the data itself
- The `Response` object contains status codes and headers
- We need to call another method like `.json()` to extract the body data

## Extracting JSON

- The `.json()` method also returns a new Promise
- This new Promise resolves with the actual JavaScript object data
- Chaining `.then()` allows us to work with the final parsed data

```javascript
.then(response => response.json())
.then(data => console.log(data))
```

## Exercise

Write the JavaScript code necessary to fetch data from the hypothetical URL `/api/items` and print the resulting JavaScript object to the console.

## Connection Errors

- A network failure or inability to reach the URL rejects the Promise
- This type of error prevents the first `.then()` block from running
- The `.catch()` method is used to handle these immediate network failures

## HTTP Status Codes

- The `fetch()` function does not reject the Promise on HTTP error codes
- Responses like 404 Not Found or 500 Server Error still resolve the Promise
- We must manually check the `Response.ok` property or the `Response.status`

---

Describe a practical scenario where a developer would intentionally choose to process a server's response using `Response.text()` instead of `Response.json()`.

## Response Object

- The `Response` object holds metadata about the server's reply
- Properties include `status`, `statusText`, and `headers`
- It is crucial to check these properties before processing the body

## Cleaner Promises

- Writing nested `.then()` calls can sometimes lead to messy code
- The `async` and `await` keywords provide a syntactical sugar
- This makes asynchronous code appear and read more like synchronous code

## `async` Functions

- An `async` function implicitly returns a Promise
- We must define a function with the `async` keyword to use `await` inside
- This pattern helps simplify the flow of asynchronous operations

## `await` Keyword

- `await` can only be used inside an `async` function
- It pauses the function execution until the Promise resolves
- The result of the Promise is then assigned to a variable

```javascript
const response = await fetch(url)
```

## `async` Error Handling

- Since `await` simulates synchronous execution, we use `try...catch`
- If a Promise is rejected, the execution moves into the `catch` block
- This provides a familiar structure for handling errors in modern code

## Exercise

Using `async`/`await` and a `try...catch` block, rewrite the basic fetch request from the previous exercise, logging any errors encountered.

---

How does the inherent asynchronous nature of network requests fundamentally force us to change our programming mindset compared to traditional synchronous code execution?

## Cross-Origin Requests

- Browsers enforce a security policy called the Same-Origin Policy
- Scripts can only request resources from the domain that served the script
- Cross-Origin Resource Sharing (CORS) is a mechanism to override this

## CORS Mechanism

- CORS uses specific HTTP headers sent by the server
- These headers explicitly grant permission to external origins
- Without the correct server headers, the request will likely fail

---

Aside from basic connectivity, what security implications must a developer consider when making cross-origin network requests?

## Exercise

What is the JavaScript code to check if a `Response` object named `res` indicates a successful HTTP status, and what is the typical range for a successful status code?