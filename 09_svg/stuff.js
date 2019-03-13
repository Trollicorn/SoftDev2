// Mohammed Uddin
// SoftDev2 pd7
//K #09: Connect the Dots
// 2019-03-19

//getting references to html elements
var savage = document.getElementById("vimage");

var first = "yes"
var prev = {"x":0, "y":0}

savage.addEventListener('click',function(e){
  var cds = {"x":e.offsetX, "y":e.offsetY}
  var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
  c.setAttribute("cx", cds.x);
  c.setAttribute("cy", cds.y);
  c.setAttribute("r", 10);
  c.setAttribute("fill", "red");
  c.setAttribute("stroke", "black");
  savage.appendChild(c);

  if (first != "yes"){ //if not first click, draw line to click
    var line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
    line.setAttribute('x1', prev.x);
    line.setAttribute('x2', cds.x);
    line.setAttribute('y1', prev.y);
    line.setAttribute('y2', cds.y);
    line.setAttribute('stroke', 'black');
    savage.appendChild(line);
  }else{  //if first click, skip above
    first = "no";
  }
  prev.x = cds.x;
  prev.y = cds.y;
});

oofers = document.getElementById("clear");
oofers.addEventListener('click',function(){
  while (savage.lastChild){
    savage.removeChild(savage.lastChild);
  }
  prev.x = 0;
  prev.y = 0;
  first = "yes";
});
