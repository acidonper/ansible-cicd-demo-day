# Company Assets Report Application

This repository contains an application based on Javascript to display critical information about the companies assets. This application is able to obtain a set of assets report data via API Rest and generate an HTML report ready to use in business dashboards and other tools.

## Requisites

- npm +8.3.1 

## Deploy App in Openshift

### Build

First of all, it is required to build the application container image in order to be able to deploy it in Openshift. 

In order to build this container image using out-of-the-box Openshift tools, it is possible to follow the next procedure:

- Create de CICD namespace and the respective resources

```$bash
oc new-project app-report-cicd

oc apply -f ./openshift/build.yaml -n app-report-cicd
```

- Execute the container image build process

```$bash
oc start-build appreports -n app-report-cicd

oc get build -n app-report-cicd
NAME           TYPE     FROM          STATUS     STARTED              DURATION
appreports-1   Source   Git@052b631   Complete   About a minute ago   1m5s
```

### Deployment

It is possible to deploy the application in Openshift easily through applying some k8s objects descriptors once the container image has been built. 

Please follow the next step to deploy this application in multiple environments:

- Development

```$bash
oc new-project app-report-dev

oc apply -f ./openshift/deploy-internal.yaml -n app-report-dev

oc get pod -n app-report-dev
NAME                          READY   STATUS    RESTARTS   AGE
appreports-79f7c74c64-2gx2p   1/1     Running   0          12m

oc get route -n app-report-dev
NAME         HOST/PORT                                                    PATH   SERVICES     PORT   TERMINATION   WILDCARD
appreports   appreports-app-report-dev.apps.aap.sandbox1672.opentlc.com          appreports   8080                 None
```

- Production

```$bash
oc new-project app-report-pro

oc apply -f ./openshift/deploy-internal.yaml -n app-report-pro

oc get pod -n app-report-pro
NAME                          READY   STATUS    RESTARTS   AGE
appreports-79f7c74c64-bmpwq   1/1     Running   0          1m

oc get route -n app-report-pro
NAME         HOST/PORT                                                    PATH   SERVICES     PORT   TERMINATION   WILDCARD
appreports   appreports-app-report-pro.apps.aap.sandbox1672.opentlc.com          appreports   8080                 None
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
