#!/usr/bin/node
const No = process.argv[2];

function factorial (No) {
  if (No <= 1 || isNaN(No)) {
    return 1;
  } else {
    return No * factorial(No - 1);
  }
}

console.log(factorial(No));
