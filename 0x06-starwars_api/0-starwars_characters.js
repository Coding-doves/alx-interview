#!/usr/bin/node

const request = require('request'); // request

const movieId = process.argv[2];

if (!movieId) {
  console.log("Please provide a movie ID.");
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error("Error fetching data:", error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error("Failed to fetch data. Status code:", response.statusCode);
    process.exit(1);
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  console.log(`Characters in ${film.title}:`);
  characters.forEach((characterUrl) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error("Error fetching character data:", error);
        return;
      }
      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});
