'use strict';

let fs = require('fs');
let fileData = fs.readFileSync('data2.txt', 'utf-8');
const data = [];

fileData.split(/\r?\n/).forEach(d => {
  data.push(d);
})

let hor = 0;
let aim = 0;
let depth = 0;

for(let d of data) {  
  const directions = d.split(' ')
  const dir = directions[0];
  const val = Number(directions[1]);

  if(dir === 'forward') {
    hor += val;
    depth += (aim * val);
  } else {
    aim = dir === 'up' ? aim - val : aim + val;
  }
}

const pos = hor * depth;
console.log(pos);