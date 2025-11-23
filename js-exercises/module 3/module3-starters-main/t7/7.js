'use strict';

const img = document.getElementById("target");
const trigger = document.getElementById("trigger");

trigger.addEventListener("mouseover", () => {
  img.src = "img/picA.jpg".replace("A", "B");
});

trigger.addEventListener("mouseout", () => {
  img.src = "img/picA.jpg";
});
