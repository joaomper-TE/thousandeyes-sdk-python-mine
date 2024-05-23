# coding: utf-8

"""
    Endpoint Tests API

     Manage endpoint agent dynamic and scheduled tests using the Endpoint Tests API. 

    The version of the OpenAPI document: 7.0.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thousandeyes_sdk.endpoint_tests.models.endpoint_specific_agents_selector_config import EndpointSpecificAgentsSelectorConfig

class TestEndpointSpecificAgentsSelectorConfig(unittest.TestCase):
    """EndpointSpecificAgentsSelectorConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EndpointSpecificAgentsSelectorConfig:
        """Test EndpointSpecificAgentsSelectorConfig
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EndpointSpecificAgentsSelectorConfig`
        """
        model = EndpointSpecificAgentsSelectorConfig()
        if include_optional:
            return EndpointSpecificAgentsSelectorConfig(
                agent_selector_type = 'specific-agents',
                max_machines = 10,
                agents = ["0a3b9998-dc3a-4ff2-b50d-ac4a7cd986e1","66eec0f1-72b4-4755-aa83-3aed61d17f3c"]
            )
        else:
            return EndpointSpecificAgentsSelectorConfig(
                agent_selector_type = 'specific-agents',
        )
        """

    def testEndpointSpecificAgentsSelectorConfig(self):
        """Test EndpointSpecificAgentsSelectorConfig"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
