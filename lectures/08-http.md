---
reading: '[Flask Quickstart](https://flask.palletsprojects.com/en/stable/quickstart/), [MDN: HTTP Methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods)'
...

# HTTP

## Web Apps

- Software that runs on a remote server
- Accessed by users through a web browser
- Powers many of the online services we use

## App Components

- A server executes the application's logic
- A database often stores persistent information
- The browser renders the user interface

## Introducing Flask

- A lightweight Python web framework
- Often called a "microframework" for its design
- Provides essential tools to build web applications

## First App Code

- We begin by importing the Flask object
- An instance of the application is then created
- This instance manages how our app behaves

```python
from flask import Flask
app = Flask(__name__)
```

## Running Flask

- The application needs a starting point to run
- This block ensures Flask launches when executed
- It starts a local development server for testing

```python
if __name__ == '__main__':
    app.run(debug=True)
```

## Defining Routes

- Routes map specific URL paths to Python functions
- The `@app.route('/')` decorator links URLs to code
- Functions define what happens at a given path

```python
@app.route('/')
def hello_world():
    return 'Hello, World!'
```

## Hello World

- This function runs when someone visits the root URL
- It simply returns a string as the web response
- This is the simplest possible web application

## Dynamic URLs

- Routes can include variable parts in their paths
- These variables are passed directly to the function
- This allows for flexible and personalized content

```python
@app.route('/user/<username>')
def show_user_profile(username):
    return f'User: {username}'
```

## HTTP Basics

- The protocol browsers use to communicate with servers
- Defines how requests are structured and responses sent
- Fundamental for understanding all web applications

## Request Methods

- HTTP specifies different types of requests
- Each method implies a distinct purpose or action
- Servers use these to process client requests appropriately

## The GET Method

- Used to request data from a specified resource
- It should retrieve information without changing server state
- Think of it as a "read-only" operation

## The POST Method

- Used to submit data to be processed by a resource
- Often used when creating or updating data on the server
- Examples include submitting forms or uploading files

## Exercise

Imagine building a simple blog platform. For each scenario, state whether you would use a `GET` or `POST` request:

1.  Displaying a list of all blog posts
2.  Creating a new blog post via a submission form
3.  Viewing a single blog post by its ID

## Other Methods

- PUT: Replaces a resource with new data, or creates it
- DELETE: Removes a specified resource from the server
- PATCH: Applies partial modifications to a resource

## Method Safety

- A method is "safe" if it causes no server side effects
- `GET` is safe, meaning repeating it doesn't change data
- `POST`, `PUT`, and `DELETE` are generally not considered safe

## Method Idempotence

- An idempotent method produces the same result
- This holds true even if sent multiple times by mistake
- `GET`, `PUT`, `DELETE` are idempotent; `POST` typically is not

---

Why is it important for a web application to differentiate between a `GET` request and a `POST` request, even if both requests target the same URL path?

## Handling Methods

- Flask routes can be configured to accept specific methods
- We pass a list of allowed methods to the decorator
- This helps control how different interactions are managed

```python
from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'Login attempt received'
    else:
        return 'Please provide credentials'
```

## The Request Object

- Flask provides a `request` object for each incoming request
- It contains all details about the current client request
- We can access form data, headers, and query parameters

## Returning HTML

- Flask applications can return full HTML pages
- It separates Python logic from the web presentation

## Flask's Utility

- Excellent for small web APIs or simpler websites
- Highly extensible with many community-contributed packages
- Provides a great foundation for learning web development
