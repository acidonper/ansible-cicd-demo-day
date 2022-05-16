# Ansible Tower Configuration as a Code

Red Hat Ansible Tower configuration as a Code includes a procedure to configure an Ansible Tower installation creating and configuring some objects through a programmatic procedure. 

The following list includes the Ansible Tower's elements which can be created and configured in this procedure:

-   Organization
-   Users
-   Teams
-   Inventories
-   Projects
-   Credentials
-   Job Templates
-   Workflow Job Templates

## Configurable Resources

In order to create the objects which have been included above, It is required to include their definition in a variables file and configure the inventory file in order to link the Ansible Tower installation.

### vars

-   tower-config.yml -> Configuration as a code file which includes organization, users, teams, projects, credentials and Job Template definitions. On the other hand, includes connection parameters to Ansible Tower Cluster installed.

## Requirements

The below requirements are needed on the host that executes this module.

```$bash
pip install -r requirements.txt
ansible-galaxy collection install -r collections/requirements.yml
```

## Procedure

The programmatic procedure includes both the creation and deletion of the objects.

### Playbooks

-   tower-configuration-deploy.yml -> Using tower-config.yml file, deploy all items in Ansible Tower
-   tower-configuration-undeploy.yml -> Using tower-config.yml file, delete all items in Ansible Tower

### Examples

-   Deploy Red Hat Ansible Tower programmatic configuration
```
$ ansible-playbook tower-configuration-deploy.yml
```

-   Delete Red Hat Ansible Tower programmatic configuration
```
$ ansible-playbook tower-configuration-undeploy.yml
```

## Author

Asier Cidon @RedHat


