"""
Main module for package
"""
from __future__ import absolute_import

from traits.api import HasTraits, Instance, List, Dict

from azure.servicemanagement import ServiceManagementService


class Choices(HasTraits):
    """ Provides choice for various items in the Azure subscription"""

    # Service Management Service object for relevant subscription
    sms = Instance(ServiceManagementService)

    # choices of locations
    locations = Dict

    # choices of images
    images = Dict

    # choices of services
    services = Dict

    def _locations_default(self):
        return self.get_locations()

    def _images_default(self):
        return self.get_images()

    def _services_default(self):
        return self.get_services()

    def get_locations(self):
        d = dict([(loc.display_name, loc) for loc in locs])
        return d

    def get_images(self):
        images = self.sms.list_images()
        d = dict([(im.label, im) for im in images.images])
        return d

    def get_services(self):
        svcs = self.sms.list_services()
        d = dict([(svc.name, svc) for svc in svcs])
        return d


class AzureVM(HasTraits):
    """
    represents a single virtual machine
    """
    sms = Instance(ServiceManagementService)
