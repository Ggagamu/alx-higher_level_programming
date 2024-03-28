#!/usr/bin/node

const req = require('request');
const movie = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';
req.get(url + movie, function (error, res, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  const dat = data.characters;
  for (const j of dat) {
    req.get(j, function (error, res, body1) {
      if (error) {
        console.log(error);
      }
      const data1 = JSON.parse(body1);
      console.log(data1.name);
    });
  }
});
