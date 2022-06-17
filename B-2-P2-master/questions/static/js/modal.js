// Get the modal
var modal = document.getElementById("askModal");

// Get the button that opens the modal
var btn = document.getElementById("toggleModal");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

var body = document.body

// When the user clicks on the button, open the modal
btn.onclick = function() {
  modal.style.display = "block";
  body.style.overflow =  "hidden";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
  body.style.overflow =  "auto";
}