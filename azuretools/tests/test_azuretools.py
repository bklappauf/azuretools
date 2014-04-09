"""
Main module for package
"""
from __future__ import absolute_import
import os

import unittest
from pprint import pprint


class TestChoices(unittest.TestCase):
    """ Test Util module"""

    def setUp(self):
        from azuretools.util.util import get_azure_login
        id, cert_path = get_azure_login()
        from azure.servicemanagement import ServiceManagementService
        sms = ServiceManagementService(id, cert_path)
        from azuretools.ui.azuretools import Choices
        self.choices = Choices(sms=sms)

    def test_locations(self):
        self.assertIsInstance(self.choices.locations, dict)
        print self.choices.locations

    def test_locations(self):
        self.assertIsInstance(self.choices.images, dict)
        print self.choices.images

    def test_services(self):
        self.assertIsInstance(self.choices.services, dict)
        pprint(self.choices.services)


if __name__ == "__main__":
    # from package use "python -m unittest discover -v -s ./tests/"
    unittest.main()
