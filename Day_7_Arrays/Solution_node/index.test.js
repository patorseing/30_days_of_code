const app = require("./");

test("2 3 4 1 ", () => {
  var result = app.reverse([1, 4, 3, 2], 4);
  var expected = "2 3 4 1 ";
  expect(result).toBe(expected);
});
