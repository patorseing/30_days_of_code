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

function readLine() {
  return input_stdin_array[input_currentline++];
}

function Person(initialAge) {
  this._age = initialAge;
  if (this._age < 0) {
    console.log("Age is not valid, setting age to 0.");
    this._age = 0;
  }
  // Add some more code to run some checks on initialAge
  this.amIOldLogic = function () {
    // Do some computations in here and print out the correct statement to the console
    var str = "";
    if (this._age < 0) {
      str = "Age is not valid, setting age to 0.";
    } else if (this._age < 13) {
      str = "You are young.";
    } else if (this._age >= 13 && this._age <18) {
      str = "You are a teenager.";
    } else {
      str = "You are old.";
    }
    return str;
  };
  this.amIOld = function () {
    // Do some computations in here and print out the correct statement to the console
    console.log(this.amIOldLogic());
  };
  this.yearPasses = function () {
    // Increment the age of the person in here
    this._age++;
  };
}

function main() {
  var T = parseInt(readLine());
  for (i = 0; i < T; i++) {
    var age = parseInt(readLine());
    var p = new Person(age);
    p.amIOld();
    for (j = 0; j < 3; j++) {
      p.yearPasses();
    }
    p.amIOld();
    console.log("");
  }
}

module.exports = {
  Person,
};
