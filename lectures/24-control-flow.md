---
reading: '[Conditionals and Loops in JavaScript](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Conditionals) and [Loops in JavaScript](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Loops)'
...

# Controlling Program Flow

## Why Control Flow?

- Most programs require the ability to make decisions and repeat actions
- We need mechanisms to execute certain code blocks only if conditions are met
- This structure allows programs to respond dynamically to user input or data changes

## Conditional Structures

- The fundamental structure is the `if` statement
- It evaluates a boolean expression to determine execution path
- Code inside the curly braces runs only if the expression resolves to true

```javascript
if (condition) {
  // run this code
}
```

## Comparison Operators

- These operators determine truthiness by comparing two values
- Use `===` for strict equality, checking both value and type
- Use `!==` for strict inequality, confirming values are different

---

If you have a function that checks user age, why is using `==` (loose equality) instead of `===` (strict equality) a potential security or logic risk?

## The `else` Block

- We can specify an alternative action when the primary condition is false
- The `else` block provides a default path for the program to follow
- This ensures that one of two distinct paths is always taken

```javascript
if (userValid) {
  // access granted
} else {
  // access denied
}
```

## Exercise

Write a small `if...else` block that checks if a variable named `score` is greater than 90, logging "A Grade" or "Review Needed" appropriately.

## Complex Decisions

- We can chain multiple conditions using `else if`
- The interpreter checks conditions sequentially until one is true
- Once a true condition is found, subsequent `else if` and `else` blocks are skipped

## Logical Operators

- Combining multiple conditions requires logical operators
- The AND operator (`&&`) requires both sides to be true
- The OR operator (`||`) requires at least one side to be true
- The NOT operator (`!`) inverts the truthiness of a condition

## Multi-Way Branches

- The `switch` statement handles complex equality checks efficiently
- It evaluates an expression against multiple predefined `case` values
- We must remember to use `break` to exit the structure after a match is found

```javascript
switch (day) {
  case 'Mon':
    // code
    break;
}
```

---

When might a `switch` statement be cleaner and more readable than a long chain of `if...else if` statements?

## Repetition

- Loops automate repetitive tasks without rewriting code
- They are crucial for iterating over data collections like arrays
- Loops save time and reduce errors in long sequences of instructions

## The `for` Loop

- A common structure for definite iteration
- It clearly defines three parts: initialization, stopping condition, and iteration step

```javascript
for (init; condition; step) {
  // code to repeat
}
```

## Exercise

A variable `limit` is set to 10. Write a `for` loop that prints numbers starting from 1 up to and including `limit`.

## Different Loop Types

- The `while` loop executes as long as its condition remains true
- The condition is checked *before* each iteration runs
- This type is useful when the exact number of repetitions is unknown beforehand

## Guaranteed Execution

- The `do...while` loop checks the condition *after* the first iteration
- This means the code block is guaranteed to run at least once
- This structure is less common but useful for input prompts

```javascript
do {
  // runs at least once
} while (condition);
```

## Controlling Iteration

- Sometimes we need to adjust the flow within a running loop
- We use keywords to skip iterations or completely stop the loop execution
- This allows us to handle exceptions or optimization mid-cycle

## Stopping Early: `break`

- The `break` keyword immediately halts the current loop
- Program execution moves to the code immediately following the loop body
- This is essential when the required result is found early in a search

## Skipping: `continue`

- The `continue` keyword skips the rest of the current loop iteration
- It immediately proceeds to the next iteration's evaluation step
- This is useful for ignoring certain values, such as negative numbers in a calculation

## Infinite Loops

- A loop where the stopping condition is never met is an infinite loop
- This causes the program to hang and consume resources indefinitely
- Always ensure the iteration step moves the loop toward the condition being false

---

If a developer accidentally creates an infinite loop, what are the most common mistakes they likely made in setting up the loop condition or iteration step?

## Exercise

Using a `for` loop, iterate through numbers 1 to 15. Use the `continue` keyword to skip printing the number 13, and print all other numbers.
