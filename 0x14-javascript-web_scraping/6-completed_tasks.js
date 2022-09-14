#!/usr/bin/node
/**
* Script that computes the number of tasks completed by user id
*/

const axios = require('axios').default;
const url = process.argv[2];

axios.get(url)
  .then(({ data }) => {
    const task = {};
    data.forEach((element) => {
      if (element.completed === true) {
        const userId = element.userId;
        if (task[userId] === undefined) {
          task[userId] = 1;
        } else {
          task[userId] += 1;
        }
      }
    });
    console.log(task);
  })
  .catch((error) => console.log(error.response.statusText));
