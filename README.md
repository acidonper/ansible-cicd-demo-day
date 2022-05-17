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

## Environment - Setting Up

First of all, it is required install Ansible Automation Platform in Openshift. Please execute the following command in order to setting up the lab environment:

```$bash
oc login -u <user> -p <pass> <ocp_api_url>
./setup/install.sh
```

## Author

Asier Cidon @RedHat