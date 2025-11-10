'use strict';
const rolls = Number(prompt('How many dice rolls?'));
let sum = 0;
for (let i = 0; i < rolls; i++) {
  sum += Math.floor(Math.random() * 6) + 1;
}
document.querySelector('#output').innerHTML = `Sum of dice rolls: ${sum}`;
