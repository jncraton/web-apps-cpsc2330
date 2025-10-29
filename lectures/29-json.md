---
reading: '[MDN: JSON](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/JSON)'
...

# JSON

## What Is JSON?

- JSON stands for JavaScript Object Notation
- It is a lightweight format for exchanging data
- It is easy for humans to read and write
- It is completely language independent for use across systems

## Key JSON Structure

- Data is organized into key/value pairs
- The structure is based on two universal structures
- A collection of key/value pairs, like an object
- An ordered list of values, like an array

## JSON Data Types

- Values can only be one of six primitive types
- The allowed types are strings, numbers, and boolean values
- Objects, arrays, and `null` are also valid value types

## Type: String Example

- JSON strings must be enclosed in double quotes
- This rule applies to all property keys as well
- The structure closely resembles JavaScript string syntax

```json
{
  "name": "Prof Smith"
}
```

## Type: Number Example

- JSON numbers follow standard JavaScript number rules
- They can include decimal points or be integers
- Octal and hexadecimal formats are not supported in JSON

```json
{
  "score": 95,
  "pi": 3.14159
}
```

## Exercise

Create a valid JSON object representing a book that includes a `title` (string) and an `pages` (number) property.

```json
/* Write your JSON here */
```

## JSON vs JavaScript

- JSON syntax is a strict subset of JavaScript object literal syntax
- JSON is *data only* and cannot contain executable code
- You cannot include functions, dates, or `undefined` values

## JSON.parse()

- This is the standard method for reading JSON data
- It takes a JSON string and converts it into a JavaScript object
- This is essential when receiving data from a web server

## Parsing Example

- We store the result into a new JavaScript variable
- This variable can then be used like any other object

```javascript
const jsonText = '{"id": 42}'
const data = JSON.parse(jsonText)
console.log(data.id)
```

---

Why is it critical that JSON is "completely language independent" when dealing with modern, distributed web services?

## JSON.stringify()

- This method converts a JavaScript value into a JSON string
- It is essential when preparing data to send to a server
- It is also used for writing data to local storage

## Stringify Example

- The method takes an object and converts it to a string
- Note that functions are automatically stripped out of the result

```javascript
const obj = {user: "alex"}
const jsonString = JSON.stringify(obj)
console.log(jsonString)
```

## Arrays in JSON

- JSON arrays are ordered lists of values
- They follow the same structure as JavaScript arrays
- Each element must be a valid JSON value or object

```json
{
  "colors": ["red", "green", "blue"]
}
```

## Nested Objects

- Objects and arrays can be nested within each other
- This allows for the representation of complex, hierarchical data structures
- This ability is key for modeling real-world entities

```json
{
  "profile": {
    "city": "Boston"
  }
}
```

---

What would happen if a web server accidentally returned a JSON string that contained a JavaScript function definition?

## Deep Cloning

- We can achieve a quick deep clone using JSON methods
- This involves stringifying the object, then parsing the resulting string
- The new object is completely separate from the original

## Cloning Caveats

- This method will silently fail on objects containing functions or `undefined`
- It is a fast method, but it is not universally applicable
- It is best used for simple data objects that require deep copies

## Error Handling

- The `JSON.parse()` method will throw a `SyntaxError` if the string is not valid JSON
- It is crucial to wrap parsing calls in a `try...catch` block
- This prevents your application from crashing due to malformed input data

## Reviver Function

- The `JSON.parse()` method accepts an optional second argument
- This is a "reviver" function that processes each key/value pair
- It can be used to transform or filter data during the parsing process

## Exercise

Describe a scenario where a `SyntaxError` from `JSON.parse()` would indicate a failure in the communication layer, not just a malformed object.

## Exercise

Write the JavaScript required to convert a variable named `userProfile` into a JSON string suitable for sending to a server, storing the result in a variable named `payload`.