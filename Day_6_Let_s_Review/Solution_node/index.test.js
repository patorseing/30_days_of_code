const app = require("./");


test("caseSplit", () => {
  var result = app.split('2\nHacker\nRank');
  expect(result.length).toBe(3);
});

test("caseContinueFalse", () => {
  var result = app.split('2\nHacker\nRank');
  expect(app.isContinue(result[0])).toBe(false);
});

test("caseContinueTrue", () => {
  var result = app.split('2\nHacker\nRank');
  expect(app.isContinue(result[1])).toBe(true);
});

test("caseSolveI", () => {
  var result = app.split('2\nHacker\nRank');
  expect(app.solve(result[1])).toBe('Hce akr');
});

test("caseSolveII", () => {
  var result = app.split('2\nHacker\nRank');
  expect(app.solve(result[2])).toBe('Rn ak');
});
