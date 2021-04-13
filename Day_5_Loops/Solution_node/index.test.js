const app = require("./");

test("caseI", () => {
  var result = app.solve(2,1);
  expect(result).toBe("2 x 1 = 2");
});

test("caseII", () => {
  var result = app.solve(2,2);
  expect(result).toBe("2 x 2 = 4");
});
