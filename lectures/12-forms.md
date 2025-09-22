---
reading: '[MDN: Forms](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/HTML_forms)'
...

# Building Interactive Forms

## Why Forms?

- Forms are essential tools for interacting with users on the web
- They allow us to collect various types of information from visitors
- This interaction ranges from simple searches to complex data submissions

## User Input

- Think about everyday forms you encounter online
- These could be login screens or contact pages
- They are fundamental to most web applications we use daily

## The Form Element

- All HTML forms begin with the `<form>` element
- This element acts as a container for all your input controls
- It specifies how and where the form data will be sent

## Form Attributes

- The `action` attribute defines the URL where form data is sent
- The `method` attribute determines the HTTP request method
- Common methods are `GET` for retrieval and `POST` for submission

```html
<form action="/submit-data" method="post">
  <!-- Form controls go here -->
</form>
```

## Basic Text Input

- The `<input>` element is a versatile building block for forms
- Its `type` attribute changes its behavior and appearance
- `type="text"` creates a single-line text field for short entries

```html
<input type="text" id="username" name="username">
```

## Input Labels

- Labels are crucial for form accessibility and usability
- The `<label>` element clearly describes the purpose of an input
- It helps users understand what information they need to provide

## Linking Labels

- Connect a `<label>` to its input using the `for` and `id` attributes
- The `for` attribute of the label should match the `id` of the input
- This connection improves accessibility for screen reader users

```html
<label for="name">Your Name:</label>
<input type="text" id="name" name="user_name">
```

---

Think about the last time you abandoned an online form. What made you give up?

## Password Input

- For sensitive information like passwords, use `type="password"`
- This input type visually masks the characters as they are typed
- It helps maintain privacy by obscuring data on the screen

```html
<label for="pass">Password:</label>
<input type="password" id="pass" name="user_password">
```

## Email Input

- The `type="email"` input is designed for email addresses
- It often provides basic client-side validation for email format
- Browsers may also suggest previously entered email addresses

```html
<label for="email">Email:</label>
<input type="email" id="email" name="user_email">
```

## Checkboxes

- Checkboxes allow users to select zero, one, or multiple options
- Each checkbox typically represents a single, independent choice
- They are often used for settings or preferences that can be toggled

```html
<input type="checkbox" id="newsletter" name="subscribe" value="yes">
<label for="newsletter">Sign up for newsletter</label>
```

## Radio Buttons

- Radio buttons are for selecting only one option from a group
- All radio buttons in a group must share the same `name` attribute
- This shared name ensures that only one can be chosen at a time

```html
<input type="radio" id="visa" name="payment_method" value="visa">
<label for="visa">Visa</label>

<input type="radio" id="mastercard" name="payment_method" value="mastercard">
<label for="mastercard">Mastercard</label>
```

## Form Submission

- The `type="submit"` input creates a button to send the form data
- Clicking this button triggers the form's `action` and `method`
- It is the final step in collecting user input through a form

```html
<input type="submit" value="Submit Form">
```

## Exercise

Create an HTML form fragment including a label for "Your Name" linked to a text input, and a separate label for "Are you a student?" linked to a checkbox. Submit the form using a submit button.
