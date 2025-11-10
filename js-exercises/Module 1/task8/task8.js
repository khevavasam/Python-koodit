'use strict';
const start = Number(prompt('Enter start year:'));
const end = Number(prompt('Enter end year:'));
const output = document.querySelector('#output');

for (let year = start; year <= end; year++) {
  if ((year % 4 === 0 && year % 100 !== 0) || year % 400 === 0) {
    const li = document.createElement('li');
    li.textContent = year;
    output.appendChild(li);
  }
}
