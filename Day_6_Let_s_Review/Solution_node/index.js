const split = (input) => {
  return input.split("\n");
};

const isContinue = (input) => {
  return !Number.isInteger(parseInt(input));
};

const solve = (input) => {
  let odd = [];
  let even = [];
  for (const key in input) {
    if (key % 2 === 0) {
      odd.push(input[key]);
    } else {
      even.push(input[key]);
    }
  }
  return `${odd.join("")} ${even.join("")}`;
};

function processData(input) {
  //Enter your code here
  const inputs = split(input);
  for (const iterator of inputs) {
    if (isContinue(iterator)) {
      console.log(solve(iterator));
    }
  }
}

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
  _input += input;
});

process.stdin.on("end", function () {
  processData(_input);
});

module.exports = {
  solve,
  isContinue,
  split,
};
