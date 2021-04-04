const app = require("./");

test("Weird", () => {
  expect(app.solve(3)).toBe("Weird");
});

test("Not Weird", () => {
  expect(app.solve(24)).toBe("Not Weird");
});
