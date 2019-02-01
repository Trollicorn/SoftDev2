// Mohammed Uddin
// SoftDev2 pd7
// K0  I see a Red Door
// 2019-01-30

const canvas = document.getElementById("slate");
const ctx = canvas.getContext("2d");

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
		w = 5;
		h = 5;
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
	if (Boolean(dot)){
		ctx.beginPath();
		ctx.ellipse(e.offsetX, e.offsetY,5,5,0,0,Math.PI*2);
		ctx.fill();
		ctx.closePath();
	}
	else {
		ctx.fillRect(e.offsetX, e.offsetY, w,h);
	}
};

canvas.addEventListener('click',draw);
