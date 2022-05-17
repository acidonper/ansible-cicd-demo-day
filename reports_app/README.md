# Company Assets Report Application

This repository contains an application based on Javascript to display critical information about the companies assets. This application is able to obtain a set of assets report data via API Rest and generate an HTML report ready to use in business dashboards and other tools.

## Requisites

- npm +8.3.1 

## Test Locally

## Setting Up

- Install NPM dependencies

```$bash
$ npm install
```

- Up the server

```$bash
$ npm run start

> reports_app@1.0.0 start
> node app.js

NodeJS listen to port 8080
```

## Requests

- Load assets dataset

```$bash
curl http://localhost:8080/reports/new -H "Content-Type: application/json" -H "authorization: Basic YWRtaW46cGFzc3dvcmQ=" -d '{"assets":{"current":{"cash":"434$","account_receivable":"646$","inventory":"234$","total":"1.314$"},"long_term":"875$","total":"2.189$"}}' -v
```

- Visit the report from a web browser (http://localhost:8080/)

## Author

Asier Cidon @redhat
