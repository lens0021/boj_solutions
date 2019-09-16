// https://www.acmicpc.net/problem/1110
"use strict";

const num = Number(require("fs").readFileSync("/dev/stdin"));
let num2 = num;
let cnt = 0;
do {
  // return num % 10 * 10 + (num // 10 + num % 10) % 10
  num2 = (num2 % 10) * 10 + ((Math.floor(num2 / 10) + (num2 % 10)) % 10);
  cnt++;
} while (num2 != num);

console.log(cnt);
