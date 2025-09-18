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

- Access data from forms submitted with `POST` or `PUT`
- Use the `request.form` attribute to get key-value pairs
- `request.form['username']` will raise a `KeyError` if not found

## Handling Missing Data

- If a key doesn't exist, a `KeyError` is raised
- Flask will automatically display a 400 Bad Request error
- This is often fine, as it lets you avoid boilerplate code

## The `args` Attribute

- This attribute is for accessing URL parameters
- The URL would look like `?key=value`
- You can access these with `request.args.get('key')`

---

What are the benefits of using `request.args.get()` rather than directly accessing `request.args['key']`?

## Exercise

Write a simple Flask route for `/greet` that takes a `name` from a form parameter and returns "Hello, [name]!".

## File Uploads

- Files are accessed through the `request.files` attribute
- The HTML form must have `enctype="multipart/form-data"`
- Each file behaves like a standard Python file object

## `save()` Method

- The uploaded file object has a built-in `save()` method
- It can be used to store the file on the server's filesystem
- For example: `f.save('/path/to/uploads/filename.txt')`

## Filenames

- You can get the original filename with `file.filename`
- **NEVER** trust this value directly
- It can be easily forged by a malicious user

## `secure_filename()`

- The `secure_filename()` function sanitizes the filename
- This helps prevent security vulnerabilities, like directory traversal

## Exercise

Using the Flask quickstart documentation and your knowledge of forms, what HTML would you write to submit a file to your server?

---

Why is it so important to sanitize data that is submitted by a user?
