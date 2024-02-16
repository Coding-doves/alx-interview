#!/usr/bin/node
// starwars api

const request = require('request'); // request

const movieId = process.argv[2];

if (!movieId) {
  console.log("Please provide a movie ID.");
  process.exit(1);
}

// movieId
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

function starwarsApi(url){
  return new Promise( (res, rej) => {
    request(url, (error, response, body) => {
      if (!error && response.statusCode === 200) {
        res(JSON.parse(body));
      } else {
        rej(error);
      }
    });
  });
}

// entry point

async function main (apiUrl) {
  const result = await starwarsApi(apiUrl);

  for (const i of result.characters) {
    const n = await starwarsApi(i);
    console.log(n.name);
  }
}

main(apiUrl);
