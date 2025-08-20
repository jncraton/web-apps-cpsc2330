# Structuring Web Content

## What is a list?

  - A way to group related items
  - Like a grocery list
  - Or a list of directions

## Kinds of lists

  - Unordered lists
  - Ordered lists
  - Description lists

## Unordered Lists

  - For items without a specific order
  - Use the `<ul>` tag
  - Each item uses the `<li>` tag

## Unordered Example

```html
<ul>
  <li>Milk</li>
  <li>Eggs</li>
  <li>Bread</li>
</ul>
```

## Ordered Lists

  - For items with a specific order
  - Like a recipe or instructions
  - Use the `<ol>` tag

## Ordered Example

```html
<ol>
  <li>Beat the eggs</li>
  <li>Stir in the flour</li>
  <li>Bake at 350</li>
</ol>
```

-----

How would you choose between an ordered and an unordered list for a set of links on a website's navigation bar?

## Description Lists

  - A way to define terms and descriptions
  - Use the `<dl>` tag
  - Not a typical bulleted list

## Anatomy of a DL

  - Term is inside `<dt>`
  - Description is inside `<dd>`
  - Both are inside `<dl>`

## Description List Example

```html
<dl>
  <dt>Hummus</dt>
  <dd>A delicious dip made from chickpeas</dd>
</dl>
```

## Exercise

Using the provided tags, mark up the following content as a list: apples, bananas, oranges.

## Nesting Lists

  - You can put lists inside lists
  - Add a new list inside an `<li>`
  - This creates sub-items

## Nesting Example

```html
<ul>
  <li>Fruits
    <ul>
      <li>Apples</li>
      <li>Bananas</li>
    </ul>
  </li>
  <li>Vegetables</li>
</ul>
```

-----

What are some potential challenges or accessibility issues that could arise from using deeply nested lists?

## Adding a DL

  - A description list can be nested
  - For a more complex structure
  - Or to provide more detail

-----

How might you use an ordered list to structure a syllabus for a class? What about an unordered list?

## Exercise

Mark up the following recipe with a mix of ordered and unordered lists, including nested lists: Hummus ingredients: chickpeas, tahini, lemon juice. Instructions: blend, serve with pita.

## List Best Practices

  - Use the right list for the job
  - Use lists to improve readability
  - Lists are semantic tags

## Lists and Semantics

  - Lists provide meaning
  - Not just visual formatting
  - Browsers and screen readers use them

## Exercise

Find a list on a website you use daily. Can you describe its structure using the list types we've discussed?

-----

What is a semantic tag, and why are they important for web development?
