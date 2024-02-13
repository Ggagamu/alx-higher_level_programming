#!/usr/bin/node
const dic = require('./101-data.js').dict;
const dicNew = {};
for (const key in dic) {
  if (dicNew[dic[key]]) dicNew[dic[key]].push(key);
  else dicNew[dic[key]] = [key];
}
console.log(dicNew);
