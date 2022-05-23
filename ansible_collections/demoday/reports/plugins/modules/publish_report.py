#!/usr/bin/python
# -*- coding: utf-8 -*-

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.0',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: publish_report
short_description: Module to publish a report in a Publish Report API
version_added: "1.0.0"
description:
    - "Module to publish a report in a Publish Report API"
options:
    username:
        description:
            - The user to connect to the API
        required: True
        type: str
    password:
        description:
            - The password to connect to the API
        required: True
        type: str
    url:
        description:
            - The url base of the API
        required: True
        type: str
    report:
        description:
            - Report to be published
        required: True
        type: dict
author:
  - Asier Cidon (@RedHat)
'''

EXAMPLES = '''
# Pass in a message
- name: Publish Report
  demoday.reports.publish_report:
    username: admin
    password: password
    url: http://api.domain.com/
    report:
      assets:
        current:
            cash: 14.434$
            account_receivable: 234.434$
            inventory: 543.342$
            total: 792.210$
        long_term: 834.875$
        total: 1.627.085$
'''

RETURN = '''
imported:
    description: Dictionary with the report included
    returned: always
    type: dict
    sample:
        response:
            data:
                assets:
                    current:
                        cash: 14.434$
                        account_receivable: 234.434$
                        inventory: 543.342$
                        total: 792.210$
                    long_term: 834.875$
                    total: 1.627.085$
            message: Report Created
'''

from ansible.module_utils.basic import AnsibleModule
import requests
from requests.exceptions import HTTPError
import json

try:
    from requests import RequestException

    def run_module():
        """
        Method include all execution functions when run from ansible module
        """
        module_args = dict(
            username=dict(type='str', required=True),
            password=dict(type='str', required=True, no_log=True),
            url=dict(type='str', required=True),
            report=dict(type='dict', required=True, default=None),
        )

        module = AnsibleModule(
            argument_spec=module_args,
            supports_check_mode=True
        )

        result = dict(
            changed=False,
            response={
                "data": {
                    "assets": {
                        "current": "123.123$",
                        "long_term": "123.123$",
                        "total": "246.246$"
                    }
                }
            }
        )

        if module.check_mode:
            module.exit_json(**result)

        figures = module.params['report']
        api_user = module.params['username']
        api_pass = module.params['password']
        api_url = module.params['url']

        json_data = json.dumps(figures, indent=4)
        json.loads(json_data)
        headers_req = {'Content-Type': 'application/json'}

        try:
            r = requests.post(api_url, headers=headers_req, auth=(api_user, api_pass), data=json_data)
            r.raise_for_status()
            response_print = json.loads(r.text)
            result['response'].update(response_print)
            result['changed'] = True
        except HTTPError as http_err:
            module.log(f'HTTP error occurred: {http_err}')
            module.fail_json(msg=str(http_err), changed=False)
        except Exception as err:
            module.log(f'Other error occurred: {err}')
            module.fail_json(msg=str(err), changed=False)

        # in the event of a successful module execution, you will want to
        # simple AnsibleModule.exit_json(), passing the key/value results
        module.exit_json(**result)

except ImportError:
    def run_module():
        pass


def main():
    """
    Method main of class execution
    """
    run_module()


if __name__ == '__main__':
    main()  # pragma: no cover
