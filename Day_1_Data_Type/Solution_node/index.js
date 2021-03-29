process.stdin.resume();
process.stdin.setEncoding("ascii");

var input_stdin = "";
var input_stdin_array = "";
var input_currentline = 0;

process.stdin.on("data", function (data) {
  input_stdin += data;
});

process.stdin.on("end", function () {
  input_stdin_array = input_stdin.split("\n");
  main();
});

// Reads complete line from STDIN
function readLine() {
  return input_stdin_array[input_currentline++];
}

const plusInt = (inputInt) => {
  var i = 4;
  return i + parseInt(inputInt);
};

const plusFloat = (inputFloat) => {
  var d = 4.0;
  return (d + parseFloat(inputFloat)).toFixed(1);
};

const concat = (inputString) => {
  var s = "HackerRank ";
  return s + inputString;
};

function main() {
  // Declare second integer, double, and String variables.
  var inputInt;
  var inputFloat;
  var inputString;
  // Read and save an integer, double, and String to your variables.
  inputInt = readLine();
  inputFloat = readLine();
  inputString = readLine();
  // Print the sum of both integer variables on a new line.
  console.log(plusInt(i, inputInt));
  // Print the sum of the double variables on a new line.
  console.log(plusFloat(d, inputFloat));
  // Concatenate and print the String variables on a new line
  // The 's' variable above should be printed first.
  console.log(concat(s, inputString));
}

module.exports = {
  plusInt,
  plusFloat,
  concat
};
