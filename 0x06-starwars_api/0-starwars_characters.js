#!/usr/bin/node

const request = require('request');

const movieID = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${filmId}`;

request(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const movie = JSON.parse(body);
    const characters = movie.characters;

    if (Array.isArray(characters) && characters.length > 0) {
      characters.forEach((characterURL) => {
        request(characterURL, (charError, charResponse, charBody) => {
          if (!charError && charResponse.statusCode === 200) {
            const character = JSON.parse(charBody);
            console.log(character.name);
          } else {
            console.log('Error fetching character:', charError || charResponse.statusCode);
          }
        });
      });
    } else {
      console.log('No characters found for this movie.');
    }
  } else {
    console.log('Error fetching movie:', error || response.statusCode);
  }
});
