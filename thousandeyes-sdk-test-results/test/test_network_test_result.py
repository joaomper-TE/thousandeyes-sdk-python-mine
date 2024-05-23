# coding: utf-8

"""
    Test Results API

    Get test result metrics for Cloud and Enterprise Agent tests.

    The version of the OpenAPI document: 7.0.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thousandeyes_sdk.test_results.models.network_test_result import NetworkTestResult

class TestNetworkTestResult(unittest.TestCase):
    """NetworkTestResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NetworkTestResult:
        """Test NetworkTestResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NetworkTestResult`
        """
        model = NetworkTestResult()
        if include_optional:
            return NetworkTestResult(
                var_date = '2022-07-17T22:00:54Z',
                round_id = 1384309800,
                links = None,
                start_time = 1384309800,
                end_time = 1384309800,
                available_bandwidth = 9.100464,
                avg_latency = 167.04,
                bandwidth = 4.3313155,
                capacity = 210.10854,
                jitter = 0.076808,
                loss = 0.0,
                max_latency = 168.0,
                min_latency = 167.0,
                packets_by_second = [[],[0],[2],[2,1],[1,1]],
                agent = thousandeyes_sdk.test_results.models.agent.Agent(
                    agent_id = '281474976710706', 
                    agent_name = 'thousandeyes-stg-va-254', 
                    country_id = 'US', 
                    location = 'San Francisco Bay Area', ),
                server_ip = '50.18.127.223',
                server = 'www.thousandeyes.com:80',
                direction = 'to-target'
            )
        else:
            return NetworkTestResult(
        )
        """

    def testNetworkTestResult(self):
        """Test NetworkTestResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
