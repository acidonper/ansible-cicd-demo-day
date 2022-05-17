const express = require("express");
const router = express.Router();

router.get("/", (req, res) => {
    console.log(req)
    console.log(req.body)
    data = { id: "invento", data: "datos" }
    res.render("report", data);
});

module.exports = router;