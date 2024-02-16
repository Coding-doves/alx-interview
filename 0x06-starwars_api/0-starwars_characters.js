#!/usr/bin/node
// get movies

const request = require('request');
const apiUrl = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request.get(apiUrl, function (err, response, body) {
  if (!err) {
    const urlchars = JSON.parse(body).characters;
    const len = urlchars.length;
    starwarsApi(0, urlchars[0], urlchars, len);
  }
});

function starwarsApi (i, apiUrl, chars, len) {
  if (i === len) {
    return;
  }
  request.get(apiUrl, function (err, response, body) {
    if (!err) {
      console.log(JSON.parse(body).name);
      i++;
      starwarsApi(i, chars[i], chars, len);
    }
  });
}
