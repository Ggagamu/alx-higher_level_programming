#!/usr/bin/node
let quote = 0;
exports.logMe = function (item) { console.log(`${quote++}: ${item}`); };
