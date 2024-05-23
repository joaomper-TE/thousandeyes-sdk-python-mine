# coding: utf-8

"""
    Endpoint Agents API

    Manage ThousandEyes Endpoint Agents using this API.   For more information about Endpoint Agents, see [Endpoint Agents](https://docs.thousandeyes.com/product-documentation/global-vantage-points/endpoint-agents).

    The version of the OpenAPI document: 7.0.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thousandeyes_sdk.endpoint_agents.models.ethernet_profile import EthernetProfile

class TestEthernetProfile(unittest.TestCase):
    """EthernetProfile unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EthernetProfile:
        """Test EthernetProfile
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EthernetProfile`
        """
        model = EthernetProfile()
        if include_optional:
            return EthernetProfile(
                link_speed = 56
            )
        else:
            return EthernetProfile(
        )
        """

    def testEthernetProfile(self):
        """Test EthernetProfile"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
