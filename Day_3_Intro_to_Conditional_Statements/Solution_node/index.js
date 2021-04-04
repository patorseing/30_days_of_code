"use strict";

process.stdin.resume();
process.stdin.setEncoding("utf-8");

let inputString = "";
let currentLine = 0;

process.stdin.on("data", (inputStdin) => {
  inputString += inputStdin;
});

process.stdin.on("end", (_) => {
  inputString = inputString
    .replace(/\s*$/, "")
    .split("\n")
    .map((str) => str.replace(/\s*$/, ""));

  main();
});

function readLine() {
  return inputString[currentLine++];
}

const solve = (N) => {
  let str = "";

  if (N % 2 == 1) {
    str = "Weird";
  } else {
    if (N > 1 && N < 6) {
      str = "Not Weird";
    } else if (N > 5 && N < 21) {
      str = "Weird";
    } else {
      str = "Not Weird";
    }
  }
  return str;
};

function main() {
  const N = parseInt(readLine(), 10);
  console.log(solve(N));
}

module.exports = {
  solve,
};
