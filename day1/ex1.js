'use strict';

let fs = require('fs');

let increased = 0;
let decreased = 0;
let numbers = [];

let fileData = fs.readFileSync('data1.txt', 'utf-8');

fileData.split(/\r?\n/).forEach(data => {
  numbers.push(Number(data));
})


for(let x = 0; x < numbers.length; x++) { 
  if(numbers[x] < numbers[x+1]) {
    increased++;
  } else {
    decreased++;
  }
}

console.log(increased, decreased)