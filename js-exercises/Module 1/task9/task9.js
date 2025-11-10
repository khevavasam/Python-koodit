'use strict';
const num = Number(prompt('Enter a number:'));
let isPrime = num > 1;

for (let i = 2; i < num; i++) {
  if (num % i === 0) {
    isPrime = false;
    break;
  }
}

document.querySelector('#output').innerHTML =
  `${num} is ${isPrime ? 'a prime' : 'not a prime'} number.`;
