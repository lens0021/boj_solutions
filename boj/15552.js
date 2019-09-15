// https://www.acmicpc.net/problem/15552
"use strict";

const process = require("process");
let output = "";
let num, addend;
let sizeIsReaded = false;
process.stdin.on("data", data => {
  let i = 0;
  if (!sizeIsReaded) {
    while (data[i++] !== 10) continue;
    sizeIsReaded = true;
  }

  for (; i < data.length; i++) {
    switch (data[i]) {
      case 10: // "\n"
        output += addend + num + "\n";
        num = undefined;
        break;
      case 32: // " "
        addend = num;
        num = undefined;
        break;
      default:
        num = num ? num * 10 + (data[i] - 48) : data[i] - 48;
    }
  }
});
process.stdin.on("end", () => {
  process.stdout.write(output);
});
