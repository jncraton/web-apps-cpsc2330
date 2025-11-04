console.log(Math.PI)

console.log(Math.round(Math.PI))
console.log(Math.round(0.5))
console.log(Math.round(1.9))
console.log(Math.round(-0.9))

function randInt(start, end) {
  return Math.floor(Math.random() * (end - start + 1)) + start
}

Math.randInt = randInt

console.log(Math.randInt(1, 10))
