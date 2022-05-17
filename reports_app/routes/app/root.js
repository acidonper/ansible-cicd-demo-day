const express = require("express");
const router = express.Router();
const fs = require('fs');

router.get("/", (req, res) => {
    // Log Request
    console.log("GET request received /")

    // read JSON object from file
    fs.readFile('db/reports.json', 'utf-8', (err, data) => {
        if (err) {
            throw err;
        }

        // parse JSON object
        var reports = JSON.parse(data.toString());

        // Define data to render
        let hbs_data = {};
        hbs_data.currentcash = reports.assets.current.cash.toString();
        hbs_data.currentaccount = reports.assets.current.account_receivable.toString();
        hbs_data.curreninventory = reports.assets.current.inventory.toString();
        hbs_data.currenttotal = reports.assets.current.total.toString();
        hbs_data.long_term = reports.assets.long_term.toString();
        hbs_data.total = reports.assets.total.toString();

        // Log data rendered
        console.log("Data Rendered: " + data);
    
        // Render Web Page
        res.render("report", hbs_data);
    });

});

module.exports = router;