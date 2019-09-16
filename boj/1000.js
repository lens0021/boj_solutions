// https://www.acmicpc.net/problem/15552
"use strict";

const process = require("process");
let num, addend;
process.stdin.on("data", data => {
  for (const ch of data) {
    switch (ch) {
      case 10: // "\n"
        process.stdout.write(addend + num + "\n");
        num = undefined;
        break;
      case 32: // " "
        addend = num;
        num = undefined;
        break;
      default:
        if (num) {
          num = num * 10 + (ch - 48);
        } else {
          num = ch - 48;
        }
    }
  }
});
