#!/usr/bin/node
/**
* Request status code
*/

const axios = require('axios').default;
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;

axios.get(url)
  .then(response => {
    // handle success
    console.log(response.data.title);
  })
  .catch(function (error) {
    // handle error
    console.log(error.response.data.detail);
  })
  .then(function () {
    // always executed
  });
