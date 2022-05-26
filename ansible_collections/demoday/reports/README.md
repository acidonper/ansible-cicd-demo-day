# Ansible Collection - demoday.publish_report

This collection allows user to interact with _My Business Report App_ in order to be able to define new data sets and import them in the web application.

Content
-------

There are some resources included in this collection to support the functionality mentioned before:

- [Publish Report](./plugins/modules/publish_report.py) Custom Module: Allow users to define a data set and publish it in the _My Business Report_ web application
- [API Manage](./plugins/modules/publish_report.py) Role: Allow users to define a data set and publish it through the _Publish Report_ custom module.
- [Publish Report](./playbooks/publish_report.yml) Playbook: An example of the API Manage role execution.

Dependencies
------------

Please review _requirements.txt_ in order to identify the collection's dependencies.

Prerequisites
-------

- Ansible 2.9

Installing
-------

This collection is hosted in a private Hub and it is required to modify the galaxy server configuration file to refer this private Ansible collections server:

```$bash
ansible-galaxy collection install demoday.publish_report
```

Testing
-------

TBD

License
-------

BSD

Author Information
------------------

- Asier Cidon @RedHat
- Cesar Fernandez @RedHat
- Alejandro de la Hoz @RedHat