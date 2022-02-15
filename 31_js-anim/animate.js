// Team Phantom Tollbooth :: Clyde Sinclair, Fierce Dragon
// SoftDev pd0
// K31 -- canvas based JS animation
// 2022-02-15t

// model for HTML5 canvas-based animation

//access canvas and buttons via DOM
var c = document.getElementsByID("playground");
var dotButton = document.getElementByID("buttonCircle");
var stopButton = document.getElementByID("buttonStop");

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


//var drawDot = function() {
var drawDot = () => {
    console.log("drawDot invoked...")

    window.requestAnimationFrame();
    
    while (requestID == True) {
        clear();
        ctx.beginPath();
        ctx.arc(mouseX, mouseY, radius, 0, 360);
    }

    // YOUR CODE HERE

    /*
      ...to
      Wipe the canvas,
      Repaint the circle,
      ...and somewhere (where/when is the right time?)
      Update requestID to propagate the animation.
      You will need
      window.cancelAnimationFrame()
      window.requestAnimationFrame()
     */
};


//var stopIt = function() {
var stopIt = () => {
    console.log("stopIt invoked...")
    console.log(requestID);

    // YOUR CODE HERE
    /*
      ...to
      Stop the animation
      You will need
      window.cancelAnimationFrame()
    */
};


dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt);