---
reading: '[Flask Quickstart: Accessing Request Data](https://flask.palletsprojects.com/en/stable/quickstart/#accessing-request-data)'
...

# Handling Requests

## The `request` Object

- A global object that provides access to client data
- It holds all the information sent from the browser
- This includes form data, URL parameters, and file uploads

---

What makes the Flask `request` object "global" yet still "threadsafe"?

## Context Locals

- A special kind of global object
- They are a proxy to an object specific to a context
- In Flask, the context is usually the handling thread

## How It Works

- A request comes in and a new thread is spawned
- Flask binds the `request` object to that specific thread
- This makes the object available everywhere in your code

## Accessing Data

- The `request` object must be imported from the `flask` module
- It provides different attributes for different data types
- You'll use these attributes to get data from forms or URLs

## Form Data

- Access data from forms submitted with `POST`
- Use the `request.form` attribute to get key-value pairs
- `request.form['username']` will raise a `KeyError` if not found

## Handling Missing Data

- If a key doesn't exist, a `KeyError` is raised
- Flask will automatically display a 400 Bad Request error
- This is often fine, as it lets you avoid boilerplate code

## The `args` Attribute

- This attribute is for accessing URL (GET) parameters
- The URL would look like `?key=value`
- You can access these with `request.args.get('key')`

---

What are the benefits of using `request.args.get()` rather than directly accessing `request.args['key']`?

## Exercise

Write a simple Flask route for `/greet` that takes a `name` from a form parameter and returns "Hello, [name]!".

---

Why is it important to sanitize data that is submitted by a user?

## Sanitizing User Input

- Consider carefully how user input will be display, stored, or used
- Safely quote or escape user input

## Escaping HTML

```python
from html import escape

print(escape('<p>Hello, world</p>'))
```

## Libraries

- Most libraries will handle this for you if used properly
- They must be used properly
- For flask, this means always using the built-in template system
