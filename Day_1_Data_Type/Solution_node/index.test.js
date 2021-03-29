const app = require("./");

test("plusInt", () => {
  expect(app.plusInt(12)).toBe(16);
});

test("plusFloat", () => {
  expect(app.plusFloat(4.0)).toBe((8.0).toFixed(1));
});

test("concat", () => {
  expect(app.concat("is the best place to learn and practice coding!")).toBe(
    "HackerRank is the best place to learn and practice coding!"
  );
});
