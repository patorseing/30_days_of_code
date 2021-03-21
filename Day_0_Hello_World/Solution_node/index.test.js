const app = require('./');

test('cancat Hello world \n name', () => {
  expect(app.concat('name')).toBe("Hello, World.\nname");
});
