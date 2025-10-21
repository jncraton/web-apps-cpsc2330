---
reading: '[Arrays in JavaScript](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Arrays)'
...

# Arrays

## What Are Arrays?

- Arrays are ordered lists of data
- They allow you to store multiple items within a single variable

## Why Use Arrays?

- Organize related data efficiently
- Handle collections of information
- Simplify operations on many values

## Creating Arrays

- The most common method uses square brackets
- This is called an array literal
- Example: `let colors = ['red', 'green', 'blue']`

## `Array()` Constructor

- Less common approach
- Uses the `Array()` constructor function
- Example: `let numbers = new Array(10, 20, 30)`

---

Why might it be better to store a list of items like `['monday', 'tuesday', 'wednesday']` in an array rather than in three separate variables `day1`, `day2`, `day3`?

## Accessing Items

- Retrieve items using their numeric index
- Indexing always starts at zero
- Example: `colors[0]` would give `'red'`

## Array Length

- The `length` property tells you the total count
- It's useful for iterating or checking size
- Example: `colors.length` would be `3`

## Changing Items

- Modify an item by assigning a new value
- Use the item's index for this assignment
- Example: `colors[1] = 'yellow'`

## Exercise

Create an array named `favoriteFoods` with three foods. Then, change the second food in your array to a different dish.

## Adding Items

- Use the `push()` method to add an item
- It appends the new item to the end
- Example: `colors.push('purple')`

## Adding to Start

- The `unshift()` method adds to the beginning
- All existing items shift their indexes
- Example: `colors.unshift('orange')`

## Removing Items

- The `pop()` method removes the last item
- It also returns the item that was removed
- Example: `colors.pop()`

## Removing from Start

- The `shift()` method removes the first item
- It also returns the item that was removed
- Example: `colors.shift()`

## Finding Items

- `indexOf()` finds the first matching item's index
- It returns `-1` if the item is not found
- Example: `colors.indexOf('green')`

## Checking Presence

- The `includes()` method checks for an item's existence
- It returns a simple `true` or `false` value
- Example: `colors.includes('blue')`

## Exercise

Given `let inventory = ['hammer', 'screwdriver', 'wrench']`. Add 'drill' to the end. Then, check if 'screwdriver' is in the `inventory` array.

## Looping Arrays

- Iterating over each item is a common task
- Different methods offer distinct advantages
- Essential for processing array data

## `for...of` Loop

- Provides a clean way to access each item's value
- No need to manage indexes manually
- Example: `for (let color of colors) { console.log(color) }`

## `forEach()` Method

- A functional approach to iteration
- Takes a callback function for each item
- Example: `colors.forEach(color => console.log(color))`

## Traditional `for`

- Offers precise control over indexing
- Useful for specific index-based logic
- Example: `for (let i = 0; i < colors.length; i++) { console.log(colors[i]) }`

---

When would you choose a traditional `for` loop over `for...of` or `forEach()` when iterating through an array in your code?

## `splice()` Method

- Highly versatile for adding, removing, or replacing
- Specify a start index, delete count, and new items
- Example: `colors.splice(1, 1, 'cyan', 'magenta')`

## Multi-dimensional Arrays

- Arrays can contain other arrays as their items
- Useful for representing grids or matrices
- Example: `let board = [['X', 'O'], ['O', 'X']]`

## Accessing 2D Arrays

- Use multiple sets of square brackets
- The first index is for the outer array (row)
- The second index is for the inner array (column)
- Example: `board[0][1]` would give `'O'`

## Exercise

Given `let students = ['Alice', 'Bob', 'Charlie']`, use `splice()` to remove 'Bob' and add 'Eve' and 'Mallory' in his place.
