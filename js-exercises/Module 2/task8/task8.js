function concat(arr) {
  let s = "";
  for (let item of arr) s += item;
  return s;
}

const arr = ["Johnny", "DeeDee", "Joey", "Marky"];
document.getElementById("output").textContent = concat(arr);
