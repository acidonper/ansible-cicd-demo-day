Role Name
=========

This role integrates the _My Business Report App API_ functionality in order to be able to create a new data set in the appl

Role Variables
--------------

| Variable     | Type       | Comment                                |
| ------------ | ---------- | -------------------------------------- |
| api_username | String     | My Business Report App username        |
| api_password | String     | My Business Report App user's password |
| api_url      | String     | My Business Report App API Url         |
| report       | Dictionary | Data set                               |

Dependencies
------------

- Custom module - demoday.reports.publish_report

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```
- hosts: localhost
  connection: local
  gather_facts: false
  
  vars: 
    api_username: admin
    api_password: password
    api_url: http://localhost:8080/reports/new
    report: 
      assets:
        current:
            cash: 14.434$
            account_receivable: 234.434$
            inventory: 543.342$
            total: 792.210$
        long_term: 834.875$
        total: 1.627.085$
  
  collections:
    - demoday.reports

  roles:
    - demoday.reports.api_manage
```

License
-------

BSD

Author Information
------------------

- Asier Cidon @RedHat
- Cesar Fernandez @RedHat
- Alejandro de la Hoz @RedHat
