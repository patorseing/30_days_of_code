const app = require('./');

test('cancat Hello world \n Welcome to 30 Days of Code!', () => {
  expect(app.concat('Welcome to 30 Days of Code!')).toBe("Hello, World.\nWelcome to 30 Days of Code!");
});
