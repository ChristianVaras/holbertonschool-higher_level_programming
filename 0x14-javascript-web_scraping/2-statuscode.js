#!/usr/bin/node
/**
* Request status code
*/

const axios = require('axios').default;
const url = process.argv[2];

axios.get(url)
  .then(res => {
    // handle success
    console.log('code:', res.status);
  })
  .catch(function (error) {
    // handle error
    console.log('code:', error.response.status);
  })
  .then(function () {
    // always executed
  });
