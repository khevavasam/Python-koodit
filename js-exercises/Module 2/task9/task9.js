function even(arr) {
  const result = [];
  for (let n of arr) {
    if (n % 2 === 0) result.push(n);
  }
  return result;
}

const nums = [2, 7, 4, 11, 18, 21, 42];

console.log("original:", nums);
console.log("evens:", even(nums));
