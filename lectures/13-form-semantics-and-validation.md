---
reading: '[MDN: Forms](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/HTML_forms)'
...

# Form Semantics and Validation

## Grouping Controls

- The `<fieldset>` element is used to group related form controls
- It provides a visual and semantic grouping for better organization
- This structure improves the readability and understanding of complex forms

## Fieldset Legend

- A `<legend>` element gives a title or caption to a `<fieldset>`
- It clearly describes the purpose of the grouped controls within the fieldset
- This enhances accessibility by providing context to users

```html
<fieldset>
  <legend>Contact Information</legend>
  <!-- Inputs for name, email, etc. -->
</fieldset>
```

## Multiline Text

- For longer text inputs, use the `<textarea>` element
- It allows users to enter multiple lines of text
- You can specify its initial size using `rows` and `cols` attributes

```html
<label for="message">Your Message:</label>
<textarea id="message" name="user_message" rows="5" cols="30"></textarea>
```

---

When would a `<textarea>` be more appropriate than a `type="text"` input?

## Dropdown Selects

- The `<select>` element creates a dropdown list of options
- Users can choose one or multiple items from a predefined list
- Each option is defined by an `<option>` element within the select

```html
<label for="country">Country:</label>
<select id="country" name="user_country">
  <option value="us">United States</option>
  <option value="ca">Canada</option>
</select>
```

## Option Groups

- For better organization, use `<optgroup>` within `<select>`
- It allows you to group related options under a common label
- This feature is useful for long lists of choices, making them easier to navigate

## Optgroup Example

```html
<select id="continent" name="user_country">
  <optgroup label="North America">
    <option value="us">USA</option>
    <option value="ca">Canada</option>
  </optgroup>
  <optgroup label="Europe">
    <option value="de">Germany</option>
    <option value="fr">France</option>
  </optgroup>
</select>
```

## Validation Basics

- HTML5 provides built-in client-side form validation
- Attributes like `required` prevent submission if a field is empty
- This helps guide users to provide necessary information

```html
<input type="text" id="name" name="user_name" required>
```

## Min and Max Length

- Control text input length with `minlength` and `maxlength` attributes
- These ensure that user input meets specific character count requirements
- This is useful for fields like passwords or short messages

```html
<input type="password" minlength="8" maxlength="20" required>
```

## Exercise

Add the `minlength="5"` and `required` attributes to the "Your Name" text input from our previous discussion, ensuring a minimum length and mandating input.

---

Describe a situation where client-side validation would be sufficient and one where server-side validation is absolutely necessary.

## `pattern` Attribute

  - Specifirs a regular expression against which the input value is checked
  - Allows you to enforce a specific format
  - If input doesn't match the defined pattern, the form will not submit, and a validation message is displayed to the user

```html
<label for="zip-code">Zip Code (e.g., 12345):</label>
<input type="text" id="zip-code" name="zip_code" pattern="\d{5}" required>
```

## `placeholder` Attribute

  - Provides a short hint or example
  - The hint is displayed inside the input field itself and disappears on input
  - Not a replacement for `<label>`

```html
<label for="search">Search:</label>
<input type="search" id="search" name="search" placeholder="Enter keywords here">
```
