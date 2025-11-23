'use strict';

const num1 = document.getElementById("num1");
const num2 = document.getElementById("num2");
const operation = document.getElementById("operation");
const btn = document.getElementById("start");
const result = document.getElementById("result");

btn.addEventListener("click", () => {
  const a = Number(num1.value);
  const b = Number(num2.value);
  let r;

  switch (operation.value) {
    case "add":
      r = a + b;
      break;
    case "sub":
      r = a - b;
      break;
    case "multi":
      r = a * b;
      break;
    case "div":
      r = a / b;
      break;
  }

  result.textContent = `Result: ${r}`;
});
