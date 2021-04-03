const app = require("./");

test("solve", () => {
  expect(app.solve(12.00,20,8)).toBe(15);
});

test("solve2", () => {
  expect(app.solve(10.25,17,5)).toBe(13);
});
