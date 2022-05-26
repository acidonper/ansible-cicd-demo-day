# Company Assets Report Application

This repository contains an application based on Javascript to display critical information about the companies assets. This application is able to obtain a set of assets report data via API Rest and generate an HTML report ready to use in business dashboards and other tools.

## Requisites

- npm +8.3.1 

## Deploy App in Openshift

It is possible to deploy the application in Openshift easily through applying some k8s objects descriptors. Please follow the next step to deploy this application in multiple environments:

- Development

```$bash
oc new-project dev
oc apply -f ./openshift/deploy.yaml
```

- Production

```$bash
oc new-project pro
oc apply -f ./openshift/deploy.yaml
```

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


## Authors

Asier Cidon @redhat
