#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const data = JSON.parse(body);
  const characters = data.characters;
  for (const character of characters) {
    request(character, (err, response, body) => {
      if (err) {
        console.log(err);
        return;
      }
      const display = JSON.parse(body);
      console.log(display.name);
    });
  }
});
