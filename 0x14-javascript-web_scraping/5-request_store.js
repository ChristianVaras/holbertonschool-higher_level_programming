#!/usr/bin/node
/**
* Script that gets the contents of a webpage and stores it in a file
*/

const axios = require('axios').default;
const fs = require('fs');
const url = process.argv[2];
const filename = process.argv[3];

axios.get(url)
  .then(response => {
    // handle sucess
    fs.writeFile(filename, response.data, 'utf-8', err => {
      if (err) {
        console.error(err);
      }
    });
  })
  .catch((error) => console.log(error.response.statusText));
