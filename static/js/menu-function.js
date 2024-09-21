let menuButton = document.getElementById("menuButton");
menuButton.addEventListener("click", openMenu);

let closeButton = document.getElementById("closeButton");
closeButton.addEventListener("click", closeMenu);


function openMenu() {
  if (window.innerWidth > 700) {
  document.getElementById("mainMenu").style.width = "30%";
  } else {
  document.getElementById("mainMenu").style.width = "75%";
  }
}

function closeMenu() {
  document.getElementById("mainMenu").style.width = "0%";
}