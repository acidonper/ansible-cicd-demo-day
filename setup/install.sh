#!/bin/bash
##
# Script to install AAP in Openshift
##

# Variables
AAP_PASS=ansible

# Functions
waitpodup(){
  x=1
  test=""
  while [ -z "${test}" ]
  do 
    echo "Waiting ${x} times for pod ${1} in ns ${2}" $(( x++ ))
    sleep 1 
    test=$(oc get po -n ${2} | grep ${1})
  done
}

waitpod() {
  NS=ansible-automation-platform
  waitpodup $1 ${NS}
  oc get pods -n ${NS} | grep ${1} | awk '{print "oc wait --for condition=Ready -n '${NS}' pod/" $1 " --timeout 300s"}' | sh
}

# Install AAP operator
echo "## INFO - Creating AAP Namespace..."
oc new-project ansible-automation-platform

echo "## INFO - Installing AAP Operators..."
oc apply -f ./setup/files/aap_operator.yaml
waitpod automation-controller-operator
waitpod automation-hub-operator
waitpod resource-operator

## Install AAP and Hub
echo "## INFO - Installing AAP..."
oc create secret generic aap-admin-credential --from-literal=password=${AAP_PASS}
oc apply -f setup/files/aap.yaml
waitpod aap-postgres
waitpod aap

echo "## INFO - Installing AAP Hub..."
oc apply -f setup/files/hub.yaml
waitpod hub-postgres
waitpod hub-redis
waitpod hub-content
waitpod hub-worker
waitpod hub-web
waitpod hub-api

AAP_ROUTE=$(oc get route aap -o jsonpath='{.status.ingress[0].host}')
HUB_ROUTE=$(oc get route hub -o jsonpath='{.status.ingress[0].host}')
echo "## AAP INFO ##"
echo " - AAP: ${AAP_ROUTE} (User: admin/${AAP_PASS})"
echo " - AAP Hub: ${HUB_ROUTE} (User: admin/${AAP_PASS})"
