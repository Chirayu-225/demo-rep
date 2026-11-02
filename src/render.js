// Renders notification e-mails from templates stored by administrators.
const _ = require("lodash");

function renderEmail(templateSource, data) {
  // lodash.template compiles the template into a function: the trigger for CVE-2021-23337
  const compiled = _.template(templateSource);
  return compiled(data);
}

module.exports = { renderEmail };
