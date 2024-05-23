# coding: utf-8

"""
    Endpoint Tests API

     Manage endpoint agent dynamic and scheduled tests using the Endpoint Tests API. 

    The version of the OpenAPI document: 7.0.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thousandeyes_sdk.endpoint_tests.models.endpoint_agent_to_server_tests import EndpointAgentToServerTests

class TestEndpointAgentToServerTests(unittest.TestCase):
    """EndpointAgentToServerTests unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EndpointAgentToServerTests:
        """Test EndpointAgentToServerTests
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EndpointAgentToServerTests`
        """
        model = EndpointAgentToServerTests()
        if include_optional:
            return EndpointAgentToServerTests(
                tests = [
                    null
                    ],
                links = thousandeyes_sdk.endpoint_tests.models.self_links.SelfLinks(
                    self = thousandeyes_sdk.endpoint_tests.models.link.Link(
                        href = 'https://api.thousandeyes.com/v7/link/to/resource/id', 
                        templated = True, 
                        type = '', 
                        deprecation = '', 
                        name = '', 
                        profile = '', 
                        title = '', 
                        hreflang = '', ), )
            )
        else:
            return EndpointAgentToServerTests(
        )
        """

    def testEndpointAgentToServerTests(self):
        """Test EndpointAgentToServerTests"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
