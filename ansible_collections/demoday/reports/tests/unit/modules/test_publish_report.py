
from __future__ import absolute_import, division, print_function
__metaclass__ = type

import pytest
import mock

from ....plugins.modules import publish_report as my_module
from .commun_test import AnsibleExitJson, \
    set_module_args, AnsibleFailJson, module_mock
from ansible.module_utils.basic import AnsibleModule
import requests
import json
from requests.exceptions import HTTPError


def publish_report_mock(cls, **kwargs):
    return {
        "status_code": 200
    }


def publish_report_raise_validation_exception(cls, **kwargs):
    raise HTTPError('test Error')


def test_publish_report(module_mock):
    set_module_args({
        'username': 'admin',
        'password': 'password',
        'url': 'http://appreports-app-report-dev.apps.ocp4cluster.ocp4.cfernand.com/reports/new',
        'report': {
            'assets': {
                'current': {
                    'cash': '104.434$',
                    'account_receivable': '23.434$',
                    'inventory': '54.342$',
                    'total': '72.210$'
                },
                'long_term': '83.875$',
                'total': '627.085$'
            }
        }
    })

    with pytest.raises(AnsibleExitJson) as result:
        my_module.main()

    assert result.value.args[0]['changed'] is True
    assert result.value.args[0]['response']['data'] == {'assets': {
        'current': {
            'cash': '104.434$',
            'account_receivable': '23.434$',
            'inventory': '54.342$',
            'total': '72.210$'
        },
        'long_term': '83.875$',
        'total': '627.085$'
    }}
