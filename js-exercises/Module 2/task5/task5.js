const nums = [];

while (true) {
  const n = Number(prompt("Give a number:"));

  if (nums.includes(n)) {
    console.log("Number already given!");
    break;
  }

  nums.push(n);
}

nums.sort((a, b) => a - b);
console.log(nums);
