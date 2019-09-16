// https://www.acmicpc.net/problem/1427
"use strict";

const str = require("fs")
  .readFileSync("/dev/stdin")
  .toString();
if (str[str.length - 1] == "\n") {
  process.stdout.write(
    `${str
      .slice(0, -1)
      .split("")
      .sort()
      .reverse()
      .join("")}\n`
  );
} else {
  process.stdout.write(
    `${str
      .split("")
      .sort()
      .reverse()
      .join("")}\n`
  );
}
