'use strict';
const a = Number(prompt('Enter first number:'));
const b = Number(prompt('Enter second number:'));
const c = Number(prompt('Enter third number:'));
const sum = a + b + c;
const product = a * b * c;
const average = sum / 3;

document.querySelector('#output').innerHTML = `
  <p>Sum: ${sum}</p>
  <p>Product: ${product}</p>
  <p>Average: ${average}</p>`;
