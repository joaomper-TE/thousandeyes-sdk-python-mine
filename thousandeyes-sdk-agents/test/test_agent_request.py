# coding: utf-8

"""
    Agents API

     ## Overview Manage all agents available to your account in ThousandEyes, including both Cloud and Enterprise Agents.

    The version of the OpenAPI document: 7.0.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thousandeyes_sdk.agents.models.agent_request import AgentRequest

class TestAgentRequest(unittest.TestCase):
    """AgentRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AgentRequest:
        """Test AgentRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AgentRequest`
        """
        model = AgentRequest()
        if include_optional:
            return AgentRequest(
                agent_name = 'thousandeyes-stg-va-254',
                enabled = True,
                account_groups = ["1234","1"],
                ipv6_policy = 'force-ipv4',
                keep_browser_cache = True,
                target_for_tests = '1.1.1.1',
                local_resolution_prefixes = ["10.2.3.3/24","10.2.3.3/25"],
                tests = ["12313145","12345"]
            )
        else:
            return AgentRequest(
        )
        """

    def testAgentRequest(self):
        """Test AgentRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
