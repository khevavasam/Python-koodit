'use strict';

const input = document.getElementById("calculation");
const btn = document.getElementById("start");
const result = document.getElementById("result");

btn.addEventListener("click", () => {
  const expr = input.value.trim();
  let a, b, r;

  if (expr.includes("+")) {
    [a, b] = expr.split("+");
    r = Number(a) + Number(b);
  } else if (expr.includes("-")) {
    [a, b] = expr.split("-");
    r = Number(a) - Number(b);
  } else if (expr.includes("*")) {
    [a, b] = expr.split("*");
    r = Number(a) * Number(b);
  } else if (expr.includes("/")) {
    [a, b] = expr.split("/");
    r = Number(a) / Number(b);
  } else {
    r = "Invalid input";
  }

  result.textContent = `Result: ${r}`;
});
