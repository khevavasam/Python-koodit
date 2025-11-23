const dogs = [];

for (let i = 0; i < 6; i++) {
  dogs.push(prompt(`Dog name ${i + 1}:`));
}

dogs.sort().reverse();

const ul = document.getElementById("dogs");
for (let d of dogs) {
  ul.innerHTML += `<li>${d}</li>`;
}
