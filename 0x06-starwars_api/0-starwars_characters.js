#!/usr/bin/node

const request = require('request-promise-native');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

(async () => {
  try {
    const filmData = await request(apiUrl);
    const characters = JSON.parse(filmData).characters;


    for (const characterUrl of characters) {
      const characterData = await request(characterUrl);
      console.log(JSON.parse(characterData).name);
    }
  } catch (error) {
    console.error(error);
  }
})();
