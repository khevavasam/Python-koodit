const candidateCount = Number(prompt("How many candidates?"));
const candidates = [];

for (let i = 0; i < candidateCount; i++) {
  const name = prompt(`Name of candidate ${i + 1}:`);
  candidates.push({ name, votes: 0 });
}

const voters = Number(prompt("How many voters?"));

for (let i = 0; i < voters; i++) {
  const vote = prompt(`Voter ${i + 1}, your vote:`);

  if (vote === "") continue;

  const cand = candidates.find(c => c.name === vote);
  if (cand) cand.votes++;
}

candidates.sort((a, b) => b.votes - a.votes);

console.log(`The winner is ${candidates[0].name} with ${candidates[0].votes} votes.`);
console.log("Results:");
for (let c of candidates) console.log(`${c.name}: ${c.votes} votes`);
