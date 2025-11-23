const amount = Number(prompt("How many participants?"));
const names = [];

for (let i = 0; i < amount; i++) {
  names.push(prompt(`Name of participant ${i + 1}:`));
}

names.sort();

const list = document.getElementById("list");
for (let name of names) {
  list.innerHTML += `<li>${name}</li>`;
}
