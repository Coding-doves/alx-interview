#!/usr/bin/node
// get movies

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request.get(apiUrl, function (error, response, body) {
  if (!error) {
    const urlChar = JSON.parse(body).characters;
    const len = urlChar.length;
    starwarsApi(0, urlChar[0], urlChar, len); 
  }
});

function Names (i, url, chars, len) {
  if (i === len) {
    return;
  }
  request.get(url, function (err, response, body) {
    if (!err) {
      console.log(JSON.parse(body).name);
      i++;
      Names(i, chars[i], chars, len);
    }
  });
}
