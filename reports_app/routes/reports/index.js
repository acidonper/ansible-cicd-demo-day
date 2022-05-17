const Express = require("express");
const router = Express.Router();

router.use("/new", require("./new"));

module.exports = router;