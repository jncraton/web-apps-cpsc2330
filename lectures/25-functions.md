---
reading: '[MDN: Functions](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Functions)'
...

# Functions

## What Are Functions?

- Reusable blocks of code that perform
- A specific, often repeated task
- Crucial for structured programming

## Why Use Functions?

- Prevent repetitive code (DRY principle)
- Improve code organization and readability
- Make programs easier to debug

## Function Structure

- Begin with the `function` keyword
- Give it a descriptive name
- Use parentheses for parameters

## Simple Example

```javascript
function greet() {
  console.log('Hello')
}
```

## Calling Functions

- To execute the code inside a function
- Use its name followed by parentheses
- This triggers its defined actions

## Example Call

```javascript
greet()
```

## Exercise

Write a function called `sayGoodbye` that logs "Goodbye" to the console, and then call it.

## Parameters

- Placeholders for data
- Defined in the function signature
- Essential for custom behavior

## Arguments

- The actual values supplied
- Passed when calling the function

## Function with Parameter

```javascript
function greetName(name) {
  console.log('Hello, ' + name)
}
```

## Calling with Argument

```javascript
greetName('Alice')
greetName('Bob')
```

## Multiple Parameters

- Functions can accept many arguments
- Separate each parameter with a comma

## Return Values

- Functions can produce a result
- Use the `return` keyword
- This stops execution and sends data back

## Example Return

```javascript
function add(a, b) {
  return a + b
}
const sum = add(5, 3); // sum is 8
```

---

How does returning a value make a function more flexible than just logging output?

## Function Expressions

- Assign an anonymous function to a constant or variable
- The variable then holds the function

## Expression Example

```javascript
const multiply = function(x, y) {
  return x * y
}
const product = multiply(4, 2) // product is 8
```

## Arrow Functions

- A modern, concise syntax for writing function expressions
- Often used for shorter functions

## Arrow Function Syntax

```javascript
const square = num => num * num;
const result = square(7) // result is 49
```

---

When might using an arrow function be more readable or efficient than a traditional function?

## Exercise

Write a function called `calculateArea` that takes `width` and `height` as parameters, returns their product, and then log the area of a rectangle with width 10 and height 5.
