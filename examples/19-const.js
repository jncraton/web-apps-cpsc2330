const pi = { value: 3.14159 }

function f() {
  pi.value = pi.value * pi.value
  console.log(pi.value)
}

f()
console.log(pi.value)
