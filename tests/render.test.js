const _ = require("lodash");
const { renderEmail } = require("../src/render");

test("renders a name", () => {
  expect(renderEmail("Hi <%= n %>", _.merge({}, { n: "a" }))).toBe("Hi a");
});
