function roll(sides) {
  return Math.floor(Math.random() * sides) + 1;
}

const max = Number(prompt("Dice sides:"));
const ul = document.getElementById("rolls");

let r;
do {
  r = roll(max);
  ul.innerHTML += `<li>${r}</li>`;
} while (r !== max);
