#!/usr/bin/node

let num = 0;
exports.logMe = function (item) {
  num++;
  console.log(num + ': ' + item);
};
