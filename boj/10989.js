// https://www.acmicpc.net/problem/10989
"use strict";

const counter = {};
let size;
let num = null;
new require("fs")
  .ReadStream(null, { fd: 0, autoClose: false })
  .on("readable", () => {
    let char;
    while ((char = process.stdin.read(1)) !== null) {
      switch (char[0]) {
        case 10:
          if (!size) size = num;
          // size is Unused
          else if (counter[num] == undefined) counter[num] = 1;
          else counter[num] += 1;
          num = null;
          break;
        default:
          num = num ? num * 10 + char[0] - 48 : char[0] - 48;
      }
    }
  })
  .on("end", () => {
    for (let num = 1; num < 10000 + 1; num++) {
      if (counter[num] !== undefined) {
        for (let ct = 0; ct < counter[num]; ct++) {
          process.stdout.write(`${num}\n`);
        }
      }
    }
  });
