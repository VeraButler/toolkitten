var a = "Sara Gottschalk".length;
var b = "Bituin Callanta".length;

if (a > b) {
    console.log("They are equal in length.");

} else if (a == 20) {
    console.log("Length is twenty.");

} else if (a == 21) {
    console.log("Length is twenty-one.");

} else {
    console.log("a isn't bigger than b", a, b);
}

// var input = ''
// while (input != "bye") {
//     input = prompt()
// }
// alert('Come again soon!')


// var input = ''
// while (true) {
//     input = prompt()
//     if (input == "bye") {
//         break;
//     }
// }
// alert('Come again soon!')



// Codeshare https://codeshare.io/G6lKK0

// var i // while loop that counts number of women in #1millionwomentotech
// var i = 0;
// // while until we reach the mission of 1 million, 1 millionth woman INCLUDED

// // some nice celebration

// // @Rox
// // @Rameela

// while (i < 1000000) {
//     i = i + 1;
// }
// console.log("We have reached One million");

// // @Bituin


// // @Mara

// while (i < 1000000) {
//     input = prompt("Your name:");
//     i++;
//     alert(input, "is our wonderful wonderwoman numer:", i);
// }

// alert("Yeiii, we achieved the mission <3");

// // @Jessi_RS
// while (i <= 1000000) {
//     message = prompt("You are our wonderwoman number: ", i, "");
//     i++;
// }

// alert("")

// // @AnaSustic
// while (i <= 1000000) {
//     i++;
//     console.log("We now have" + i + "ladies in 1mwtt!");

// }
// console.log("We will celebrate now!");


// add your names into the students array
var students = ["Rocio", "Jessica Sanchez", "Rameela Azeez", "Nwamaka Okafor", "Sara Gottschalk","Mara Catalina", "Bituin Callanta", "Krystal", "Anusha Lihala", "Ana Sustic", "Rox Arten", "Angela Balyseviene", "Cristina Tarantino"
]

var student0 = students[0]
var student1 = students[1]

console.log(student0, student1)


// for loops

for (i = 0; i < 1000001; i++) {
    console.log(i)
}



// Q&A

//Please put your questions/code here and I'll go through them ;)

// Mara..hehe sorry
//Than you :)
//Thank you very much :D :D , I am working with realtime Augmented reality applications
// with limited hardware and every nanosecond is supervaluable :) ..
//Which one is more efficient in terms of cpu usage?
//CT var t0 = performance.now(); //Thank you Cristina :)
if (condition){
  //do somehting
} else {}
// CT var t1 = performance.now();
// CT console.log("Call to doSomething took " + (t1 - t0) + " milliseconds.");
//or

//CT var t0 = performance.now();
//var i = (condition ) ? if true :for (i; i < 10; i++) {
//  console.log(i)
//}

for (i = 0; i < 10; i++) {
  console.log(i)
}

//var i = 0;
var j = "a";
var food = ["cake"]
for (; i < 10; i++) {
  console.log(i);
  j += i;
  food.push(j);
}

for (i = 0, j = "a", food = ["cake"]; i < 10; i++) {
  console.log(i)
  j += i;
  food.push(j);
}


// WARNING this is an ADVANCED question, it is NOT for beginners ;)
//
//
//
// Anusha
//Is there a 'for element in array' syntax in JS?

// for-in to iterate objects https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in
// for-of ES6 to iterate arrays https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of
// forEach to iterate arrays https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach
var array1 = ['a', 'b', 'c'];

array1.forEach(function(element) {
  console.log(element);
});

// for-of is extremely efficient

var student = {
  fname: "Anusha",
  lname: "Lihala",
  favFood: "pizza"
}

for (prop in student) {
  console.log(student[prop])
}

//A (Ilona): for, map, reduce
// for forEach, for in, for at
// map and reduce implemented underscore JS library

// map https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map
// reduce https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce

















