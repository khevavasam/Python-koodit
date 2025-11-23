function roll() {
  return Math.floor(Math.random() * 6) + 1;
}

const ul = document.getElementById("rolls");

let result;
do {
  result = roll();
  ul.innerHTML += `<li>${result}</li>`;
} while (result !== 6);
