// azrael --- Jason Tung and Mohammed Uddin
// SoftDev2 pd7
//K #02: Connecting the Dots
// 2019-01-31

//getting references to html elements
var c = document.getElementById("playground");
var ctx = c.getContext("2d");

var first = "yes"

var cbtn = document.getElementById("clear");

//set the fill colors now
ctx.fillStyle = "red";
ctx.strokeStyle = "black";

//add listened to clear button to wipe the page
cbtn.addEventListener('click', function () {
  ctx.clearRect(0, 0, w, h);
  first = "yes";
});



//adds event listener to canvas to draw on it when theres a click
c.addEventListener('click', function (e) {
    //OFFSETX/OFFSETY --- gets mousex and mousey relative to the event e rather than the webpage
  var cds = {"x":e.offsetX, "y":e.offsetY};
  if (first != "yes"){ //if not first click, draw line to click
    ctx.lineTo(cds.x,cds.y);
    ctx.stroke();
    ctx.closePath();
  }else{  //if first click, skip above
    first = "no";
  }
  ctx.beginPath();
  ctx.ellipse(cds.x, cds.y, 10, 10, 0, 0, 2 * Math.PI);
  ctx.fill();  //fills circle but this erases the line this is so sad
  ctx.closePath();
  ctx.moveTo(cds.x,cds.y);
});
