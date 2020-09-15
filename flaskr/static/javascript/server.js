function CompSciClick() {
  alert("CompSciClick");
}
function MathClick() {
  alert("MathClick");
}

// window.setInterval(function(){
//   updateCompScores();
// }, 5000);

function updateCompScores() {
  let x = prompt("Findlay Score: ");
  document.getElementById('findlayCompSci')
  .innerHTML = "Findlay - " + x;
}
