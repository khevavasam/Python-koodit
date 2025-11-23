'use strict';

const form = document.getElementById("searchForm");
const resultsDiv = document.getElementById("results");

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const query = document.getElementById("query").value.trim();
  if (!query) return;

  const url = `https://api.tvmaze.com/search/shows?q=${query}`;

  const response = await fetch(url);
  const data = await response.json();

  console.log("Raw API Result:", data);

  resultsDiv.innerHTML = "";

  data.forEach(item => {
    const show = item.show;

    const imgSrc = show.image && show.image.medium
      ? show.image.medium
      : "https://placehold.co/210x295?text=Not%20Found";

    const article = document.createElement("article");

    article.innerHTML = `
      <h2>${show.name}</h2>
      <img src="${imgSrc}" alt="${show.name}">
      <p><a href="${show.url}" target="_blank">More info</a></p>
    `;

    resultsDiv.appendChild(article);
  });
});
