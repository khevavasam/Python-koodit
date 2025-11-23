const nums = [];

while (true) {
  const n = Number(prompt("Give number (0 stops):"));
  if (n === 0) break;
  nums.push(n);
}

nums.sort((a, b) => b - a);

console.log(nums);
