// https://www.acmicpc.net/problem/1212
"use strict";

const input = require('fs').readFileSync('/dev/stdin').toString();
const num = parseInt(input, 8);

console.log(num.toString(2));
