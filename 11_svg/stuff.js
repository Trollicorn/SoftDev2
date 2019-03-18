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
  if (movey){
    for (i = 0; i < savage.children.length; i++){
      c = savage.children[i];
      console.log(c);
      cx = Number(c.getAttribute("cx"));
      cy = parseInt(c.getAttribute("cy"),10);
      vx = parseInt(c.getAttribute("vx"),10);
      vy = parseInt(c.getAttribute("vy"),10);
    //  console.log(""+cx+","+cy+","+vx,+","+vy);
      c.setAttribute("cx",cx+vx);
      c.setAttribute("cy",cy+vy);
    }
    requestID = window.requestAnimationFrame(move);
  }
}

movers = document.getElementById("move");
movers.addEventListener('click',function(){
  if (movey){
    return;
  }else {
    movey = true;
    requestID = window.requestAnimationFrame(move);
  }
});
