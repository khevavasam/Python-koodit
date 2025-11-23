const nums = [];

for (let i = 0; i < 5; i++) {
  const n = Number(prompt(`Give number ${i + 1}:`));
  nums.push(n);
}

console.log("Reversed order:");
for (let i = nums.length - 1; i >= 0; i--) {
  console.log(nums[i]);
}
