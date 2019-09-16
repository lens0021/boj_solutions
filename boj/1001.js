// https://www.acmicpc.net/problem/1001

const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .split(" ");
console.log(Number(input[0]) - Number(input[1]));
