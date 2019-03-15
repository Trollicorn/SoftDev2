// Mohammed Uddin
// SoftDev2 pd7
//K #10: Ask Circles [Change || Die]
// 2019-03-14

//getting references to html elements
var savage = document.getElementById("vimage");
var creaty = true;
var movey = false;
var requestID = 0;

savage.addEventListener('click',function(e){
  var cds = {"x":e.offsetX, "y":e.offsetY};
  if (creaty){
    circlify(cds.x,cds.y);
  }else{
    creaty = true;
  }
});

var circlify = function(x,y){
  var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
  c.setAttribute("cx", x);
  c.setAttribute("cy", y);
  c.setAttribute("r", 20);
  c.setAttribute("fill", "purple");
  c.setAttribute("stroke", "black");
  c.setAttribute("first", "yes");
  c.addEventListener('click',function(e){
    creaty = false;
    if (c.getAttribute("first")=="yes"){
      c.setAttribute("first","no");
      c.setAttribute("fill","green");
    }
    else{
      savage.removeChild(c);
      x = Math.floor(Math.random()*500);
      y = Math.floor(Math.random()*500);
      circlify(x,y);
    }
  });
  savage.appendChild(c);
  return c;
};

oofers = document.getElementById("clear");
oofers.addEventListener('click',function(){
  movey = false;
  window.cancelAnimationFrame(requestID);
  while (savage.lastChild){
    savage.removeChild(savage.lastChild);
  }
});

var move = function(){
  for (i in savage.children){
    c = savage.children[i];
    cx = c.getAttribute("cx");
    cx = c.getAttribute("cx");
    vx = c.getAttribute("vx");
    vy = c.getAttribute("vy");
    c.setAttribute("cx",cx+vx);
    c.setAttribute("cy",cy+vy);
  }
}

movers = document.getElementById("move");
movers.addEventListener('click',function(){
  if (movey){
    return;
  }else {
    movey = true;
    requestID = window.requestAnimationFrame(move());
  }
});
