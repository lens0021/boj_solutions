// https://www.acmicpc.net/problem/1431
"use strict";

function sumOfDigit(str) {
  return str
    .replace(/\D/g, "")
    .split("")
    .map(Number)
    .reduce((a, b) => a + b, 0);
}

function compare(a, b) {
  if (a.length != b.length) {
    return a.length - b.length;
  } else {
    const sumOfDigitA = sumOfDigit(a);
    const sumOfDigitB = sumOfDigit(b);
    if (sumOfDigitA != sumOfDigitB) {
      return sumOfDigitA - sumOfDigitB;
    } else {
      return a.localeCompare(b);
    }
  }
}

let names;
let idx = 0;
require("readline")
  .createInterface({ input: process.stdin })
  .on("line", line => {
    if (!names) {
      names = new Array(Number(line));
    } else {
      names[idx++] = line.replace("\n", "");
    }
  })
  .on("close", () => {
    names.sort(compare);
    process.stdout.write(names.join("\n") + "\n");
  });
