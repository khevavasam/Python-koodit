'use strict';

const form = document.getElementById("source");
const target = document.getElementById("target");

form.addEventListener("submit", (event) => {
  event.preventDefault();

  const firstname = form.querySelector("input[name='firstname']").value;
  const lastname = form.querySelector("input[name='lastname']").value;

  target.textContent = `Your name is ${firstname} ${lastname}`;
});
