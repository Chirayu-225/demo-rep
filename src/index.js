const mkdirp = require("mkdirp");
const { renderEmail } = require("./render");

mkdirp.sync("out");
console.log(renderEmail("Hello <%= name %>", { name: "world" }));
