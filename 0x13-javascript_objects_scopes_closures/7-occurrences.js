#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let numOccurences = 0;
  for (const i in list) {
    if (list[i] === searchElement) {
      numOccurences++;
    }
  }
  return numOccurences;
};
