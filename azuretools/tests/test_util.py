"""
Main module for package
"""
from __future__ import absolute_import
import os

import unittest


class TestUtil(unittest.TestCase):
    """ Test Util module"""

    def test_get_azure_login(self):
        from azuretools.util.util import get_azure_login
        id, cert_path = get_azure_login()
        self.assertTrue(os.path.isfile(cert_path))
        from azure.servicemanagement import ServiceManagementService
        sms = ServiceManagementService(id, cert_path)
        self.assertIsInstance(sms, ServiceManagementService)


if __name__ == "__main__":
    # from package use "python -m unittest discover -v -s ./tests/"
    unittest.main()
