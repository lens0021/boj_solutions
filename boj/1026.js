// https://www.acmicpc.net/problem/1026
"use strict";

const lines = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .split("\n");
const nums1 = lines[1]
  .split(" ")
  .map(Number)
  .sort((a, b) => a - b);
const nums2 = lines[2]
  .split(" ")
  .map(Number)
  .sort((a, b) => b - a);

let sum = 0;
for (const [i, num] of nums1.entries()) {
  sum += num * nums2[i];
}
process.stdout.write(sum + "\n");
