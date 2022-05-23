
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


def common_args():
    set_module_args({
        'username': 'AAAA',
        'password': 'BBBB',
        'url': 'localhost',
        'report': {
            'current': {
                'cash': '14.434$',
                'account_receivable': '234.434$',
                'inventory': '543.342$',
                'total': '792.210$'
            },
            'long_term': '834.875$',
            'total': '1.627.085$'
        }
    })


def publish_report_mock(cls, **kwargs):
    return {
        "status_code": 200
    }


def publish_report_raise_validation_exception(cls, **kwargs):
    raise HTTPError('test Error')


def test_publish_report(module_mock):
    set_module_args({
        'username': 'AAAA',
        'password': 'BBBB',
        'url': 'localhost',
        'report': {
            'assets': {
                'current': {
                    'cash': '14.434$',
                    'account_receivable': '234.434$',
                    'inventory': '543.342$',
                    'total': '792.210$'
                },
                'long_term': '834.875$',
                'total': '1.627.085$'
            }
        }
    })

    def __init__(self, argument_spec,
            supports_check_mode=False):
        self.argument_spec = argument_spec
        self.supports_check_mode = supports_check_mode
        self.check_mode = True
    with mock.patch.object(AnsibleModule, '__init__', __init__):
        with pytest.raises(AnsibleExitJson) as result:
            my_module.main()

    assert result.value.args[0]['changed'] is True
    assert result.value.args[0]['imported'] == {'assets': {
                'current': { 
                    'cash': '14.434$',
                    'account_receivable': '234.434$',
                    'inventory': '543.342$',
                    'total': '792.210$'
                }, 
                'long_term': '834.875$',
                'total': '1.627.085$'
            }}
