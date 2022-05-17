const express = require("express");
const router = express.Router();
const fs = require('fs');

router.post("/", (req, res) => {
    // Log request body information
    console.log("POST request received /reports/new")
    console.log(req.body)

    // convert JSON object to string
    const data = JSON.stringify(req.body);

    // write JSON string to a file
    fs.writeFile('db/reports.json', data, (err) => {
        if (err) {
            throw err;
        }
        console.log("JSON data is saved.");
    });

    // return OK
    res.status(200).json({ message: "Report Created", data: req.body });
});

module.exports = router;