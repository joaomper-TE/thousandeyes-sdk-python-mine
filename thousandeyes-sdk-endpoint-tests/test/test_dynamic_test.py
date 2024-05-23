# coding: utf-8

"""
    Endpoint Tests API

     Manage endpoint agent dynamic and scheduled tests using the Endpoint Tests API. 

    The version of the OpenAPI document: 7.0.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thousandeyes_sdk.endpoint_tests.models.dynamic_test import DynamicTest

class TestDynamicTest(unittest.TestCase):
    """DynamicTest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DynamicTest:
        """Test DynamicTest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DynamicTest`
        """
        model = DynamicTest()
        if include_optional:
            return DynamicTest(
                aid = '1234',
                links = thousandeyes_sdk.endpoint_tests.models.dynamic_test_links.DynamicTestLinks(
                    self = null, 
                    test_results = [{"href":"https://api.thousandeyes.com/v7/endpoint/test-results/dynamic-tests/281474976710706/network/filter"},{"href":"https://api.thousandeyes.com/v7/endpoint/test-results/dynamic-tests/281474976710706/pathvis"}], ),
                agent_selector_config = thousandeyes_sdk.endpoint_tests.models.endpoint_agent_selector_config.EndpointAgentSelectorConfig(),
                application = 'webex',
                created_date = '2022-07-17T22:00:54Z',
                interval = 120,
                is_enabled = True,
                has_path_trace_in_session = True,
                has_ping = True,
                has_traceroute = True,
                modified_date = '2022-07-17T22:00:54Z',
                network_measurements = True,
                protocol = 'icmp',
                tcp_probe_mode = 'auto',
                test_id = '281474976710706',
                test_name = 'Test name',
                labels = [
                    {"labelId":"961","name":"Artem label","isBuiltin":false}
                    ]
            )
        else:
            return DynamicTest(
        )
        """

    def testDynamicTest(self):
        """Test DynamicTest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
