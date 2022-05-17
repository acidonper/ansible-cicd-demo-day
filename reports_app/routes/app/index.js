const Express = require("express");
const router = Express.Router();

router.use("/", require("./root"));

module.exports = router;