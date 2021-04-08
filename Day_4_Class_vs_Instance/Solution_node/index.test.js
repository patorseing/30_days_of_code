const app = require("./");

test("caseI", () => {
  var age = -1;
  var p = new app.Person(age);
  var result = p.amIOldLogic();
  expect(result).toBe("You are young.");
  for (j = 0; j < 3; j++) {
    p.yearPasses();
  }
  result = p.amIOldLogic();
  expect(result).toBe("You are young.");
});

test("caseII", () => {
  var age = 10;
  var p = new app.Person(age);
  var result = p.amIOldLogic();
  expect(result).toBe("You are young.");
  for (j = 0; j < 3; j++) {
    p.yearPasses();
  }
  result = p.amIOldLogic();
  expect(result).toBe("You are a teenager.");
});

test("caseIII", () => {
  var age = 16;
  var p = new app.Person(age);
  var result = p.amIOldLogic();
  expect(result).toBe("You are a teenager.");
  for (j = 0; j < 3; j++) {
    p.yearPasses();
  }
  result = p.amIOldLogic();
  expect(result).toBe("You are old.");
});

test("caseIV", () => {
  var age = 18;
  var p = new app.Person(age);
  var result = p.amIOldLogic();
  expect(result).toBe("You are old.");
  for (j = 0; j < 3; j++) {
    p.yearPasses();
  }
  result = p.amIOldLogic();
  expect(result).toBe("You are old.");
});
