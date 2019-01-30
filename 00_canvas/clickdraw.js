const canvas = document.getElementById("slate");
const ctx = canvas.getContext("2d");

var clear = function(e){
	ctx.clearRect(0,0,canvas.width,canvas.height);
};

var button = document.getElementById("clear");
button.addEventListener('click',clear);

var draw = function(e){
	console.log("(" + e.clientX + "," + e.clientY + ")");
}
canvas.addEventListener('click',draw);
