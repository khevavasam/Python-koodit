'use strict';

document.getElementById("btn").addEventListener("click", async () => {
  const jokeEl = document.getElementById("joke");

  try {
    const resp = await fetch("https://api.chucknorris.io/jokes/random");
    const data = await resp.json();

    jokeEl.textContent = data.value;
  } catch (err) {
    jokeEl.textContent = "Error loading joke";
    console.error(err);
  }
});
