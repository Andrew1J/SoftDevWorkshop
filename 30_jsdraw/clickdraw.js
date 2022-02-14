// retrieve node in DOM via ID
var c = document.getElementById("slate");

// instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");

// init global state var
var mode = "rect";

// var toggleMode = function(e) {}
var toggleMode = (e) => {
    console.log("toggling...");
    if (mode=="rect") {
        mode = "circ";
    } else {
        mode = "rect";
    }
}

var drawRect = function(e) {
    var mouseX = e.offsetX;
    var mouseY = e.offsetY;
    console.log("mouseclick registered at ", mouseX, mouseY);
}

var drawCircle = function(e) {
    console.log("mouseclick registered at ", mouseX, mouseY);
}

var draw = (e) => {
    togglemode(e);
}

var wipecanvas = (e) => {

}

c.addEventListener("click", draw);
var bToggler = document.getElementById("buttonToggle");
bToggler.addEventListener("click", toggleMode); 
var clearB = document.getElementById("buttonClear");
clearB.addEventListener("click", wipeCanvas);