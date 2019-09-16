// https://www.acmicpc.net/problem/1002
"use strict";
const rl = require("readline").createInterface({ input: process.stdin });

let numOfCases;
let output = "";
rl.on("line", line => {
  if (!numOfCases) {
    numOfCases = line; // Unused
    return;
  }

  const [x1, y1, r1, x2, y2, r2] = line.split(" ").map(Number);
  const distance = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2);
  const rDiff = r1 > r2 ? r1 - r2 : r2 - r1;
  const rSum = r1 + r2;

  if (x1 == x2 && y1 == y2 && r1 == r2) {
    output += "-1\n";
  } else if (
    distance == 0 ||
    rDiff * rDiff > distance ||
    rSum * rSum < distance
  ) {
    output += "0\n";
  } else if (rDiff * rDiff == distance || rSum * rSum == distance) {
    output += "1\n";
  } else {
    output += "2\n";
  }
});

rl.on("close", () => {
  process.stdout.write(output);
});
