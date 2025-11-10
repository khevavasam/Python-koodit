'use strict';
const year = Number(prompt('Enter a year:'));
if ((year % 4 === 0 && year % 100 !== 0) || year % 400 === 0)
  document.querySelector('#output').innerHTML = `${year} is a leap year.`;
else
  document.querySelector('#output').innerHTML = `${year} is not a leap year.`;
