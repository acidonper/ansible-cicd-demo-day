# Ansible Automation Platform Configuration as a Code

_Red Hat Ansible Automation Platform__ configuration as a Code includes a procedure to configure an _Ansible Automation Platform_ installation creating and configuring some objects through a programmatic procedure. 

The following list includes the _Ansible Automation Platform_'s elements which can be created and configured in this procedure:

-   Organization
-   Users
-   Teams
-   Inventories
-   Projects
-   Credentials
-   Job Templates
-   Workflow Job Templates

## Configurable Resources

In order to create the objects which have been included above, It is required to include their definition in a variables file and configure the inventory file in order to link the _Ansible Automation Platform_ installation.

### Variables

- vars/aap-config.yml -> Configuration as a code file which includes organization, users, teams, projects, credentials and Job Template definitions. On the other hand, includes connection parameters to _Ansible Automation Platform_ Cluster installed.

#### Privates

- vault/vault.yml -> This file included encrypted variables that contains sensitive information.

| Variable                  | Type             | Example                                |
| ------------------------- | ---------------- | -------------------------------------- |
| vault_gitlab_access_token | String           | aasd2123sad234123s                     |
| vault_sendgrid_api_key    | String           | AsreDqeEEr12341232                     |
| vault_aap_host            | String           | aap.mycluster.com                      |
| vault_aap_user            | String           | admin                                  |
| vault_aap_pass            | String           | password                               |
| vault_hub_host            | String           | hub.mycluster.com                      |
| vault_hub_token           | String           | a1231234asdasd12334sddsf1              |
| vault_gitlab_private_key  | Multiline String | -----BEGIN OPENSSH PRIVATE KEY-----... |

## Requirements

The below requirements are needed on the host that executes this module.

```$bash
pip install -r requirements.txt
ansible-galaxy collection install -r collections/requirements.yml
```

NOTE: it is important to configure the ansible.cfg file in order to be able to download collections from Red Hat Automation Hub server. Please go to https://cloud.redhat.com/ansible/automation-hub/token/ and click Get API token from the version dropdown to copy your API token.

```$bash
vi /etc/ansible/ansible.cfg
[galaxy]
server_list = automation_hub

[galaxy_server.automation_hub]
url=https://console.redhat.com/api/automation-hub/
auth_url=https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token
token=<my_ah_token>
```

## Procedure

The programmatic procedure includes both the creation and deletion of the objects.

### Playbooks

-   aap-configuration-deploy.yml -> Using aap-config.yml file, deploy all items in _Ansible Automation Platform_
-   aap-configuration-undeploy.yml -> Using aap-config.yml file, delete all items in _Ansible Automation Platform_

### Examples

-   Deploy Red Hat _Ansible Automation Platform_ programmatic configuration
```
$ ansible-navigator run aap-configuration-deploy.yml --ask-vault-password -m stdout
```

-   Delete Red Hat _Ansible Automation Platform_ programmatic configuration
```
$ ansible-navigator run aap-configuration-undeploy.yml --ask-vault-password -m stdout
```

## Authors

- Asier Cidon @RedHat
- Cesar Fernandez @RedHat
- Alejandro de la Hoz @RedHat
