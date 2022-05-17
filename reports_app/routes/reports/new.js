const express = require("express");
const router = express.Router();

router.post("/", (req, res) => {
    console.log(req)
    console.log(req.body)
    res.status(200).json({ message: "Report Created", data: req.body });
});

module.exports = router;