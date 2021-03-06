'use strict';

let fs = require('fs');
let fileData = fs.readFileSync('data2.txt', 'utf-8');
const data = [];

fileData.split(/\r?\n/).forEach(d => {
  data.push(d);
})

let x = 0;
let y = 0;

for(let d of data) {  
  const directions = d.split(' ')
  const dir = directions[0];
  const val = Number(directions[1]);

  if ( dir === 'forward') {
    x += val;
  } else {
    y = dir === 'up' ? y - val : y + val;
  }
}

const pos = x * y;
console.log(pos);