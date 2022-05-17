# Ansible Automation Platform Configuration as a Code

Red Hat Ansible Automation Platform configuration as a Code includes a procedure to configure an Ansible Automation Platform installation creating and configuring some objects through a programmatic procedure. 

The following list includes the Ansible Automation Platform's elements which can be created and configured in this procedure:

-   Organization
-   Users
-   Teams
-   Inventories
-   Projects
-   Credentials
-   Job Templates
-   Workflow Job Templates

## Configurable Resources

In order to create the objects which have been included above, It is required to include their definition in a variables file and configure the inventory file in order to link the Ansible Automation Platform installation.

### vars

-   aap-config.yml -> Configuration as a code file which includes organization, users, teams, projects, credentials and Job Template definitions. On the other hand, includes connection parameters to Ansible Automation Platform Cluster installed.

## Requirements

The below requirements are needed on the host that executes this module.

```$bash
pip install -r requirements.txt
ansible-galaxy collection install -r collections/requirements.yml
```

## Procedure

The programmatic procedure includes both the creation and deletion of the objects.

### Playbooks

-   aap-configuration-deploy.yml -> Using aap-config.yml file, deploy all items in Ansible Automation Platform
-   aap-configuration-undeploy.yml -> Using aap-config.yml file, delete all items in Ansible Automation Platform

### Examples

-   Deploy Red Hat Ansible Automation Platform programmatic configuration
```
$ ansible-playbook aap-configuration-deploy.yml
```

-   Delete Red Hat Ansible Automation Platform programmatic configuration
```
$ ansible-playbook aap-configuration-undeploy.yml
```

## Author

Asier Cidon @RedHat


