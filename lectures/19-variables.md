---
reading: '[Variables](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Variables)'
...

# Variables

## What Are Variables?

- Named containers for storing values
- Essential building blocks for any program
- Allow data to be referenced and manipulated

## Why Use Variables?

- Hold information that changes over time
- Make code more readable by giving meaning to values
- Prevent repetition by storing a value once

## Declaring Variables

- You must tell JavaScript you're creating one
- Keywords `var`, `let`, and `const` are used

## The `var` Keyword

- The original way to declare variables in JavaScript
- Should generally be avoided
- Known for its *unique* scope and hoisting behaviors

## `var` Scope

- `var` variables are function-scoped
- They are accessible throughout the entire function
- Ignores block-level scope, such as `if` or `for` blocks

---

If `var` variables can be redeclared and are function-scoped, what potential issues might this introduce in large projects with many developers?

## `let` for Flexibility

- A modern and preferred way to declare variables
- Provides block-scoping, which is more intuitive
- Allows its value to be reassigned later

## `let` Scope

- `let` variables are block-scoped
- Their existence is limited to the specific block they are defined in
- This prevents accidental variable overwrites

## `const` for Immutability

- Used for values that should not change after initialization
- Ensures a variable's reference remains constant
- Promotes more robust and predictable code

## `const` Rules

- Must be initialized with a value upon declaration
- Cannot be reassigned to a new value later
- Important for values that are truly constant

## `const` and Objects

- The *binding* to the object is constant, not its internal content
- You can freely modify properties within a `const` object or array

## Exercise

- Declare a variable `userName` using `const` and assign it your full name
- On the next line, try to reassign `userName` to a nickname. What error message do you receive?
- Now, declare an object `userProfile` using `const` with properties `name` and `age`. Can you change `userProfile.age`?

## Naming Variables

- Choose clear, descriptive names for your variables
- Enhances code readability and maintainability significantly
- Variable names are case-sensitive, like `myVar` and `myvar`

## Naming Rules

- Must start with a letter, underscore (`_`), or dollar sign (`$`)
- Cannot begin with a number or contain spaces
- Avoid using JavaScript reserved keywords as names

## Naming Conventions

- `camelCase` is the standard for JavaScript variables (`firstName`, `totalAmount`)
- `PascalCase` for class names, `SCREAMING_SNAKE_CASE` for global constants

---

Imagine working on a team project. How might inconsistent variable naming, or lack of descriptive names, hinder collaboration and debugging efforts?

## Dynamic Typing

- JavaScript is dynamically typed, meaning variable types are not fixed
- A variable can hold a number, then later a string or an object
- The type is determined by the value it currently contains

## Type Flexibility

- Allows for quick prototyping and flexible data handling
- Requires developers to be mindful of current data types
- Type errors can occur if operations expect a different type

## Variable Hoisting

- A JavaScript mechanism where variable declarations are processed
- They are conceptually moved to the top of their containing scope
- This occurs before any code is actually executed

## Hoisting Behavior

- `var` declarations are hoisted and assigned `undefined`
- `let` and `const` are hoisted, but remain uninitialized

## Exercise

- Without running the code, predict the output for each `console.log`:
    ```javascript
    console.log(greeting);
    var greeting = "Hello";
    console.log(farewell);
    let farewell = "Goodbye";
    ```
- Explain the reasoning behind each prediction based on hoisting rules