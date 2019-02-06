// william lu but better --- Tina Wong and Mohammed Uddin
// SoftDev2 pd7
// K03 -- They lock us in the tower whenever we get caught ...which is often
// 2019-02-04

var c = document.getElementById("playground");
var width = c.getAttribute("width");
var height = c.getAttribute("height");
var ctx = c.getContext("2d");
var requestID;
var radius = 1;
var growing = 1;
var status = "off";
var w = c.width/2;
var h = c.width/2;

var stop = document.getElementById('stop');
stop.addEventListener('click', function(e) {
  status = "off";
  window.cancelAnimationFrame(requestID);
});

ctx.fillStyle = "#00ffff"; // cyan

var clear = function() {
  ctx.clearRect(0, 0, c.width, c.height);
}

var draw = function(){
  if (status != "on"){
    status = "on";
    drawDot();
  }
}

var drawDot = function() {
  // change the way the radius is growing
  if ((w - radius) * (h-radius) * radius == 0){ //if radius is = to width or height or 0, the entire thing will be 0
    growing *= -1;
  }
  radius += growing;

  // clear to prevent canvas color to be changed when circle covers the canvas
  clear();

  // draw circle
  ctx.beginPath();
  ctx.arc( w, h, radius, 0, 2 * Math.PI);
  ctx.stroke();
  ctx.fill();
  requestID = window.requestAnimationFrame(drawDot);
};
circle.addEventListener('click', draw);
