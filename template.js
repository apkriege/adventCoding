'use strict';

let fs = require('fs');
let fileData = fs.readFileSync('data1.txt', 'utf-8');
const data = [];

fileData.split(/\r?\n/).forEach(d => {
  data.push(d);
})

console.log(data)
