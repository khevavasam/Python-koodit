'use strict';

const form = document.getElementById("searchForm");
const results = document.getElementById("results");

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const q = document.getElementById("query").value.trim();
  if (!q) return;

  const url = `https://api.chucknorris.io/jokes/search?query=${q}`;
  const resp = await fetch(url);
  const data = await resp.json();

  results.innerHTML = "";

  data.result.forEach(joke => {
    const article = document.createElement("article");
    article.innerHTML = `<p>${joke.value}</p>`;
    results.appendChild(article);
  });
});
