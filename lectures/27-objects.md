---
reading: '[MDN: Objects](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Object_basics)'
...

# JavaScript Objects

## What are Objects?

- Objects are collections of related data and functionality
- They consist of named values, which are referred to as properties
- An object provides a structured representation of a single entity

## Creating Objects

- The most common creation method uses the object literal syntax
- We define properties and values inside curly braces `{}`

```javascript
let dog = {
  name: 'Fido',
  color: 'brown'
}
```

## Accessing Properties

- You can access properties using the direct dot notation
- This syntax is generally considered cleaner and more readable

```javascript
dog.name
// returns 'Fido'
```

---

- Bracket notation is an alternative that allows variable property names

```javascript
dog['color']
// returns 'brown'
```

## Adding Functionality

- Functionality attached to an object is called a method
- A method is simply a property where the value is a function definition

```javascript
let cat = {
  greet: function() {
    return 'Meow'
  }
}
```

## The 'this' Keyword

- Inside any object method, `this` refers to the method's owner object
- It allows a method to access the object's specific properties

```javascript
let fido = {
  name: 'Fido',
  bark: function() {
    console.log(this.name + ' barks')
  }
}
```

## Repeated Objects

- Creating many structurally similar objects via literals is tedious and error-prone
- We need a reliable and scalable blueprint for generating object instances
- This issue of repetition is critical for large-scale application development

## Introducing Constructors

- A constructor function serves as a standardized object factory
- It is a regular function invoked specifically with the `new` operator

## Defining a Constructor

- Constructor functions should begin with a capital letter as a convention
- Instance properties are defined and assigned using the `this` keyword

```javascript
function Student(name, id) {
  this.name = name
  this.id = id
}
```

## The New Operator

- The `new` keyword instructs JavaScript to create a fresh, empty object
- It binds the `this` keyword inside the constructor to this new object
- It ensures the constructor returns the newly created object instance

## Creating an Instance

- We use `new` to generate unique objects from the constructor blueprint

```javascript
let sophia = new Student('Sophia', 456)
let liam = new Student('Liam', 123)

sophia.name
// returns 'Sophia'
```

## Instance Properties

- Every object instance possesses its own unique copy of the data properties
- Sophia and Liam each have distinct memory for their `name` and `id` values
- This approach is inefficient if all objects share the same method implementation

## The Prototype Problem

- If we define a method inside the constructor, it is recreated for every single instance
- This leads to significant memory waste when method logic is identical across objects

## The Object Prototype

- Every JavaScript object includes an internal link, `prototype`, to another object
- This linked object acts as a fallback source for inherited properties and methods

## Constructor Prototypes

- All constructor functions expose a shared `prototype` property
- This `prototype` object is automatically linked to all instances created by the constructor
- We use this shared space to store common methods efficiently

## Adding to Prototype

- Methods that all instances share must be added directly to the constructor's `prototype`
- This ensures the function is created only once and referenced by all instances

```javascript
Student.prototype.getInfo = function() {
  return 'Name: ' + this.name
}
```

---

Why is placing a method on a constructor's prototype object better for overall memory consumption than defining it inside the constructor body?

## Prototype Chain

- When an instance accesses a property, JavaScript first checks the instance itself
- If the property is missing, the search continues up the `prototype` link
- This series of linked objects forms the conceptual prototype chain

## The Base Object

- The ultimate link in nearly every prototype chain is `Object.prototype`
- Essential, universal methods like `toString()` are inherited from here
- The chain enables foundational inheritance in JavaScript

---

How does the concept of the prototype chain inherently support the programming principle of "Don't Repeat Yourself" (DRY)?

## Exercise

Assuming the `Student` constructor is defined. Write the two lines of code necessary to create a new instance named `Chris`, and then add a new method called `sayMajor` to the `Student.prototype` that returns the string 'Computer Science'.
