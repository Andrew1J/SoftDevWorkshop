// Komodo Hedgehogs 
// Softdev pd2
// k32 -- More Moving Parts
// 2022-02-17m

// model for HTML5 canvas-based animation

//access canvas and buttons via DOM
var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var stopButton = document.getElementById("buttonStop");
var movieButton = document.getElementById("buttonMovie");


//prepare to interact with canvas in 2D
var ctx = c.getContext("2d");

//set fill color to team color
ctx.fillStyle = "pink";

var requestID;  //init global var for use with animation frames

//var clear = function(e) {
var clear = (e) => {
    console.log("clear invoked...")
    ctx.clearRect(0, 0, c.clientWidth, c.clientHeight);
};


var radius = 0;
var growing = true;


var drawDot = () => {
    console.log("drawDot invoked...")

    window.cancelAnimationFrame(requestID);
    requestID = window.requestAnimationFrame(drawDot);

    stopped = true;

    clear();
    ctx.beginPath();

    if (radius == c.clientWidth/2 || radius < 0) {
        growing = !growing;
    } 

    if (growing) {
        radius += 2;
    } else {
        radius -= 2;
    }

    ctx.arc(c.clientWidth/2, c.clientHeight/2, radius, 0, 2*Math.PI);
    ctx.fill();
};

var stopped = false;

var stopIt = () => {
    console.log("stopIt invoked...")
    console.log(requestID);
    stopped = true;

    window.cancelAnimationFrame(requestID);
};


var DVD = new Image(80, 40);
DVD.src = 'logo_dvd.jpg';
var x = Math.floor(Math.random() * (500-DVD.width));
var y = Math.floor(Math.random() * (500-DVD.height));
var dx = 5 * Math.cos(Math.PI/4);
var dy = 5 * Math.sin(Math.PI/4);

var startDVD = () =>{
    x = Math.floor(Math.random() * (c.width - DVD.width));
    y = Math.floor(Math.random() * (c.height - DVD.height));

    window.cancelAnimationFrame(requestID);
    requestID = window.requestAnimationFrame(moveDVD);
}

var moveDVD = () => {
    console.log("moveDVD invoked...");

    window.cancelAnimationFrame(requestID);
    requestID = window.requestAnimationFrame(moveDVD);

    clear();

    ctx.drawImage(DVD, x, y, DVD.width,DVD.height);

    if (x<=0 || x>=c.clientWidth-DVD.width) {
        dx *= -1;
    }
    if (y<=0 || y>=c.clientHeight-DVD.height) {
        dy *= -1;
    }
    x += dx;
    y += dy;

}

dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt);
movieButton.addEventListener("click", startDVD);