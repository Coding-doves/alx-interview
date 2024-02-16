#!/usr/bin/node
// starwars api

const request = require('request'); // request
const movieId = process.argv[2];

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request.get(apiUrl, function (error, response, body) {
  if (!error) {
    const urlChar = JSON.parse(body).characters;
    const len = urlChar.length;
    starwarsApi(0, urlChar[0], urlChar, len); 
  }
})

function starwarsApi(k, url, char, len) {
  if (k === len) {
    return
  }

  request.get(url, function (err, res, body) {
    if (!err) {
      console.log(JSON.parse(body).name);
      k++;
      starwarsApi(k, char[k], char, len);
    }
  })
}
