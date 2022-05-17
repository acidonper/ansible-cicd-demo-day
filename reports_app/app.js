const express = require("express");
const bp = require("body-parser");
const basicAuth = require('express-basic-auth');
const hbs = require("hbs");

const PORT = 8080;
const app = express();

app.use(express.static(__dirname + "/public"));
app.set("views", __dirname + "/views");
app.set("view engine", "hbs");
hbs.registerPartials(__dirname + "/views/partials");

app.use(bp.urlencoded({ extended: true }));
app.use(bp.json());

app.use("/reports", basicAuth({users: { 'admin': 'password' }}), require("./routes/reports"));
app.use("/", require("./routes/app"));

app.use((req, res) => {
    res.status(404).json({ message: "page not found" });
});

app.listen(PORT, () => console.log(`NodeJS listen to port ${PORT}`));