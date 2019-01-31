const canvas = document.getElementById("slate");
const ctx = canvas.getContext("2d");
var r = canvas.getBoundingClientRect();
var x = r["x"];
var y = r["y"];
var dot = 0;
var w = 50;
var h = 100;

var clear = function(e){
	ctx.clearRect(0,0,canvas.width,canvas.height);
};

var button = document.getElementById("clear");
button.addEventListener('click',clear);

var toggle = function(e){
	if (dot == 0){
		w = 1;
		h = 1;
		dot = 1;
	}
	else{
		w = 50;
		h = 100;
		dot = 0;
	}
};

var toggler = document.getElementById("switch");
toggler.addEventListener('click',toggle);


var draw = function(e){
	console.log("(" + e.clientX + "," + e.clientY + ")");
	ctx.fillRect(e.clientX - x, e.clientY - y, w,h);
};

canvas.addEventListener('click',draw);
