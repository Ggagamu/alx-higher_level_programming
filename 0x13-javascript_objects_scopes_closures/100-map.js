#!/usr/bin/node
const arr = require('./100-data').arr;
console.log(arr);
const arrayed = arr.map((value, elemnt) => value * elemnt);
console.log(arrayed);
