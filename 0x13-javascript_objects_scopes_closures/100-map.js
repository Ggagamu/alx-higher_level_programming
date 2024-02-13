#!/usr/bin/node
const array = require('./100-data').array;
console.log(array);
const arrayed = array.map((value, elemnt) => value * elemnt);
console.log(arrayed);
