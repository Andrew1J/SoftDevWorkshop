/*
   your PPTASK:
   
   Test drive each bit of code in this file,
    and insert comments galore, indicating anything
     you discover,
    	have questions about,
    		or otherwise deem notable.
    		
    		Write with your future self or teammates in mind.
    		
    		If you find yourself falling out of flow mode, consult 
    		other teams
    		MDN

   A few comments have been pre-filled for you...
   
   (delete this block comment once you are done)
*/

// Team HAM :: Andrew Juang, Hebe Huang, Michelle Lo 
// SoftDev pd0
// K28 -- Getting more comfortable with the dev console and the DOM
// 2022-02-08t
// --------------------------------------------------


//send diagnostic output to console
console.log("AYO"); // Prints AYO to the console

// Sets i,j to hello and 20 respectively
let i = "hello"; 
let j = 20;
// console.log(i);
// console.log(j);


//assign an anonymous fxn to a let
// declares a function f that adds 30 to the value passed in
let f = function(x) {
  let j=30;
  return j+x;
};
console.log(f(j)); // 50
console.log(f(i)); // 30hello


//instantiate an object
// similar to a dictionary or a struct in C
let o = { 'name' : 'Thluffy',
          age : 15,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
            return x+30;
          }
        };
console.log(o.morestuff); // you can nest an object in an object
console.log(o.age); // you can print the stuff with a period
console.log(o.func(j)); // can call a function similarly 


let addItem = function(text) {
  let list = document.getElementById("thelist");
  let newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};
let bob = "bob";
addItem(bob); // adds bob to the html list 

let removeItem = function(n) {
  let listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};
// removeItem(2); // removes item 0 from the list


let red = function() {
  let items = document.getElementsByTagName("li");
  for(let i = 0; i < items.length; i++) {
    items[i].classList.add('red');
    console.log(items[i].classList) // prints the classes of li tags
  }
};
red();

let stripe = function() {
  let items = document.getElementsByTagName("li");
  for(let i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};

//insert your implementations here for...
// FIB
// FAC
// GCD
