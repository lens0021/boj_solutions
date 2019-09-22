// https://www.acmicpc.net/problem/1003
"use strict";

const callOfZero = Array(41).fill(0);
const callOfOne = Array(41).fill(0);
callOfZero[0] = 1;
callOfOne[1] = 1;
for (let n = 2; n <= 40; n++) {
  callOfZero[n] = callOfZero[n - 1] + callOfZero[n - 2];
  callOfOne[n] = callOfOne[n - 1] + callOfOne[n - 2];
}
process.stdout.write(
  require("fs")
    .readFileSync(0)
    .toString()
    .trim()
    .split("\n")
    .slice(1)
    .map(Number)
    .map(n => {
      return `${callOfZero[n]} ${callOfOne[n]}`;
    })
    .join("\n") + "\n"
);
