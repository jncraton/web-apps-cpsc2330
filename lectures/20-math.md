---
reading: '[MDN: Math](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Math)'
...

# JavaScript Math

## The Math Object

- A built-in JavaScript object for mathematical constants and functions
- It does not have a constructor
- All properties and methods are static, used directly through `Math`

## Math Constants

- `Math.PI` represents the ratio of a circle's circumference to its diameter
- `Math.E` represents Euler's number, the base of natural logarithms

---

Why might JavaScript's `Math` object be designed without a constructor, making all its methods static?

## Rounding Values

- `Math.round()` rounds a number to the nearest whole integer
- Standard rounding rules apply, where `.5` rounds the number up
- Useful for formatting numerical data for display or calculations

## Flooring Numbers

- `Math.floor()` always rounds a number down to the nearest integer
- It truncates towards negative infinity, discarding any fractional part

## Ceiling Numbers

- `Math.ceil()` always rounds a number up to the nearest integer
- Rounds towards positive infinity

## Truncating Numbers

- `Math.trunc()` simply removes the decimal part of a number
- It lops off any digits after the decimal point without any rounding

## Exercise

What will `Math.round(4.4)`, `Math.floor(4.9)`, `Math.ceil(4.1)`, and `Math.trunc(4.9)` each return?

## Random Numbers

- `Math.random()` returns a floating-point number
- It's a pseudo-random number between 0 (inclusive) and 1 (exclusive)
- Frequently used for games, simulations, or unique identifiers

## Random Range

- To get a random number within a specific range, you scale `Math.random()`
- `Math.floor(Math.random() * (max - min + 1)) + min` generates integers
- This formula is a common pattern for many practical applications

## Extremes

- `Math.min()` returns the smallest number from a list of arguments
- `Math.max()` returns the largest number from a list of arguments
- These functions can take multiple numerical arguments directly

## Comparing Numbers

- You can compare any number of items to find the minimum or maximum
- `Math.min(0, 150, 30, 20, -8, -200)` will return `-200`
- `Math.max(0, 150, 30, 20, -8, -200)` will return `150`

## Exponents

- `Math.pow(base, exponent)` calculates the base to the power of the exponent
- For example, `Math.pow(2, 3)` means 2 multiplied by itself 3 times

## Square Root

- `Math.sqrt(x)` returns the square root of a given number `x`
- For example, `Math.sqrt(9)` will return the value 3

## Cube Root

- `Math.cbrt(x)` returns the cube root of a given number `x`
- For example, `Math.cbrt(27)` will return the value 3

## Absolute Value

- `Math.abs(x)` returns the absolute value of a number `x`
- This operation gives you the positive version of any number
- Useful for measuring distance or magnitude without regard to direction

## Trig Functions

- `Math.sin(x)`, `Math.cos(x)`, `Math.tan(x)` compute sine, cosine, and tangent
- These functions expect their argument `x` to be specified in radians
- Essential for working with angles, waves, and cyclical patterns

## Radians to Degrees

- To convert degrees to radians, multiply degrees by `Math.PI / 180`
- To convert radians to degrees, multiply radians by `180 / Math.PI`
- This conversion is crucial when using JavaScript's trigonometric functions

## Conversion

```javascript
const angleInDegrees = 45;
const angleInRadians = angleInDegrees * Math.PI / 180;
const sineValue = Math.sin(angleInRadians);
console.log(sineValue); // approximately 0.707
```

---

- We first convert 45 degrees into its equivalent radian measure
- Then we calculate the sine of that specific radian value
- The result provides the sine of 45 degrees, approximately 0.707

---

When building a simple animation where an object moves in a circular path, why would `Math.sin()` and `Math.cos()` be particularly useful?

## Other Functions

- `Math.log()` calculates the natural logarithm of a number
- `Math.exp()` computes `e` (Euler's number) to the power of an argument
- Many more specialized functions exist for advanced computations

## Exercise

Calculate the hypotenuse of a right-angled triangle with sides of length 3 and 4, using `Math` methods.
