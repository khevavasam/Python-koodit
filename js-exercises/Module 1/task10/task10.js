'use strict';
const dice = Number(prompt('How many dice?'));
const target = Number(prompt('Target sum?'));
let count = 0;
const trials = 10000;

for (let i = 0; i < trials; i++) {
  let sum = 0;
  for (let j = 0; j < dice; j++) {
    sum += Math.floor(Math.random() * 6) + 1;
  }
  if (sum === target) count++;
}

const probability = (count / trials) * 100;
document.querySelector('#output').innerHTML =
  `Probability to get sum ${target} with ${dice} dice is ${probability.toFixed(2)}%.`;
