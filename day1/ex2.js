'use strict';

let fs = require('fs');

let increased = 0;
let decreased = 0;
let numbers = [];
let _3nums = []

let fileData = fs.readFileSync('data1.txt', 'utf-8');

fileData.split(/\r?\n/).forEach(data => {
  numbers.push(Number(data));
})


for(let x = 0; x < numbers.length-2; x++) {
  let num = numbers[x] + numbers[x+1] + numbers[x+2];
  _3nums.push(num);
}

for(let x = 0; x < _3nums.length; x++) {
 if(_3nums[x] < _3nums[x+1]) {
    increased++;
  } else {
    decreased++;
  }
}

console.log(_3nums, increased, decreased)