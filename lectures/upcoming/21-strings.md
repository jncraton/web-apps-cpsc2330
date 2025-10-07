---
reading: '[Working with Text (Strings)](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Strings)'
...

# Strings

## What are Strings?

- A fundamental data type for representing text
- An ordered sequence of characters, symbols, and spaces
- Essential for names, messages, or displaying data

## Creating Strings

- Enclose text content within quotation marks
- Use single quotes (`'...'`) or double quotes (`"..."`)
- Be consistent with your chosen style throughout code

## Template Literals

- Backticks (`` `...` ``) create template literals
- Allow strings to span multiple lines easily
- Enable embedded expressions using `${expression}`

## Escaping Characters

- Use a backslash (`\`) to include special characters
- Like a quote within a same-quoted string: `\'` or `\"`
- Or control characters such as new lines (`\n`) and tabs (`\t`)

---

Considering the different ways to create strings, what are some practical scenarios where using template literals is clearly more advantageous than single or double quotes?

## Joining Strings

- Concatenation combines multiple strings together
- Use the `+` operator to join two or more strings
- The `+=` operator appends a string to an existing one

## Template Concatenation

- Template literals offer a cleaner way to join
- Embed variables or expressions directly within the string
- Makes complex string assembly more readable and concise

```javascript
let name = "Alice";
let greeting = `Hello, ${name}!`;
// greeting is "Hello, Alice!"
```

## Exercise

Given the variables `firstName = "Jane"` and `lastName = "Doe"`, use _both_ `+` concatenation and a template literal to create a variable `fullName` that contains "Jane Doe". Print both results to verify.

```javascript
let firstName = "Jane";
let lastName = "Doe";
// Your code here
```

## String Length

- The `.length` property returns string character count
- It includes all characters, including spaces and symbols
- Useful for validating input sizes or controlling loop iterations

## Accessing Characters

- Strings are ordered, indexed sequences of characters
- Access individual characters using bracket notation `[index]`
- Indices start counting from zero for the very first character

```javascript
let word = "hello";
let firstChar = word[0]; // 'h'
```

## `at()` Method

- The `at()` method also accesses characters by index
- It uniquely supports negative indices for counting from the end
- `str.at(-1)` retrieves the very last character of a string

---

Imagine you're building a feature that processes user input. When would you prefer to use the `at()` method over bracket notation (`[]`) for accessing string characters, and why?

## Case Conversion

- Change the case of all alphabetic characters in a string
- `toLowerCase()` converts all to lowercase letters
- `toUpperCase()` transforms all to uppercase letters

## Finding Substrings

- Determine if a string contains another specific sequence of characters
- `includes()` returns `true` if found, `false` otherwise
- It performs a case-sensitive search by default

## Edge Substrings

- Check if a string begins or ends with specific text
- `startsWith()` verifies the beginning of the string
- `endsWith()` confirms the trailing part of the string

## Exercise

Create a variable `productCode = "AXB-2023-RED"`.

1. Convert `productCode` to all lowercase.
2. Check if the original `productCode` includes "2023".
3. Check if the original `productCode` ends with "RED".

```javascript
let productCode = "AXB-2023-RED";
// Your code here
```

## Replacing Parts

- `replace()` finds a pattern and substitutes it
- It only replaces the *first* occurrence found
- This method returns an entirely new string, leaving the original unchanged

## Replacing All

- `replaceAll()` substitutes *every* instance of a pattern
- Useful when you need a global text replacement
- Also returns a brand new string, leaving the original unchanged

## Trimming Whitespace

- Remove unwanted spaces from string ends
- `trim()` removes whitespace from both start and end
- `trimStart()` and `trimEnd()` target specific sides respectively

---

Consider an application that takes user input from a form. Describe a scenario where `trim()` would be essential, and another where `trimStart()` or `trimEnd()` might be more appropriate.

## Padding Strings

- Extend a string to a target length by adding characters
- `padStart(length, char)` adds characters to the string's beginning
- `padEnd(length, char)` adds characters to the string's end

```javascript
let num = "42";
let paddedNum = num.padStart(5, "0"); // "00042"
```

## Splitting Strings

- `split()` divides a string into an array of substrings
- You specify a delimiter character or string to break on
- For example, splitting a sentence into an array of words

## Extracting Portions

- `slice(start, end)` extracts a part of a string
- `substring(start, end)` also gets a substring
- `slice()` handles negative indices differently for convenience

## Finding Index

- `indexOf()` returns the index of the first matching substring
- `lastIndexOf()` finds the index of the last match
- Both methods return `-1` if the substring is not found

## Exercise

You have a log message: `logMessage = "ERROR: User failed login at 2023-10-26T10:30:00Z"`.

1. Extract the part of the message before the timestamp.
2. Find the index of the word "login".
3. Split the entire message by spaces into an array of words.

```javascript
let logMessage = "ERROR: User failed login at 2023-10-26T10:30:00Z";
// Your code here
```