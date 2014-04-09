"""
azure tools
===

Tools for working with Azure python API
"""

from __future__ import absolute_import
import os
import json


AZURE_DATA_PATH = '/Users/bklappauf/.azure'


def get_azure_login():
    cert_path = os.path.join(*[AZURE_DATA_PATH, "managementCertificate.pem"])
    config_path = os.path.join(*[AZURE_DATA_PATH, "config.json"])
    with open(config_path, 'r') as f:
        data = json.load(f)
        subscription_id = data['subscription']

    return subscription_id, cert_path
