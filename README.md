# Ansible CI/CD Workflow - Demo Day 

This repository includes some resources and documentation for deploying an Ansible CI/CD Pipeline

## Prerequisites

- Openshift +4.10

## Folders

| Folder              | Comment                                                               |
| ------------------- | --------------------------------------------------------------------- |
| setup               | Ansible Automation Platform installation procedure (Controller & Hub) |
| aap_iac             | Ansible Automation Platform configuration automatism                  |
| ansible_tools       | CI/CD and Onboarding Playbooks                                        |
| ansible_collections | Collections ready to use in production                                |
| reports_app         | Application Based on Javascript to expose reports                     |

## Steps

This section includes a set of subsection for deploying the _Ansible Automation Platform_ solution and the laboratory. 

### Setting Ansible Automation Platform Up

First of all, it is required install Ansible Automation Platform in Openshift. Please execute the following command in order to setting up the lab environment:

```$bash
oc login -u <user> -p <pass> <ocp_api_url>
./setup/install.sh
```

### Configure Ansible Automation Plaform

Once _Ansible Automation Platform_ has been installed, it is time to configure the solution. Please visit [Ansible Automation Platform Infrastructure As Code](./aap_iac/README.md) for more information about configuring _Ansible Automation Platform_.


### Deploy _App Reports_

In this step, it is required to deploy an application in Openshift in order to be able to test the integration scenario. Once the application has been delpoyed and is running properly, it will be possible to start working with the Ansible resources generated.

Please visit [App Reports](./reports_app/README.md) for more information about deploying _App Report_ in Openshift.

## Authors

- Asier Cidon @RedHat
- Cesar Fernandez @RedHat
- Alejandro de la Hoz @RedHat