const concat = (inputString) => {
  return "Hello, World.\n"+inputString;
}

function processData(inputString) {
  // This line of code prints the first line of output
  // console.log("Hello, World.");

  // Write the second line of output that prints the contents of 'inputString' here.
  // console.log(inputString);
  console.log(concat(inputString))
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
  concat,
  processData
};
