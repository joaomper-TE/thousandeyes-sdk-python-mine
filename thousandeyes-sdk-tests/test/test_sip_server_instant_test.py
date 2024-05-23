# coding: utf-8

"""
    Tests API

    This API supports listing, creating, editing, and deleting Cloud and Enterprise Agent (CEA) based tests. 

    The version of the OpenAPI document: 7.0.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thousandeyes_sdk.tests.models.sip_server_instant_test import SipServerInstantTest

class TestSipServerInstantTest(unittest.TestCase):
    """SipServerInstantTest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SipServerInstantTest:
        """Test SipServerInstantTest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SipServerInstantTest`
        """
        model = SipServerInstantTest()
        if include_optional:
            return SipServerInstantTest(
                created_by = 'user@user.com',
                created_date = '2022-07-17T22:00:54Z',
                description = 'ThousandEyes Test',
                live_share = False,
                modified_by = 'user@user.com',
                modified_date = '2022-07-17T22:00:54Z',
                saved_event = True,
                test_id = '281474976710706',
                test_name = 'ThousandEyes Test',
                type = 'sip-server',
                links = thousandeyes_sdk.tests.models.test_links.TestLinks(
                    self = null, 
                    test_results = [{"href":"https://api.thousandeyes.com/v7/test-results/281474976710706/network"},{"href":"https://api.thousandeyes.com/v7/test-results/281474976710706/path-vis"}], ),
                labels = [
                    {"labelId":"961","name":"Artem label","isBuiltin":false}
                    ],
                shared_with_accounts = [
                    thousandeyes_sdk.tests.models.shared_with_account.SharedWithAccount(
                        aid = '1234', 
                        name = 'Account name', )
                    ],
                mtu_measurements = False,
                network_measurements = True,
                num_path_traces = 1,
                options_regex = '["a-z"]',
                path_trace_mode = 'classic',
                probe_mode = 'auto',
                register_enabled = True,
                sip_target_time = 100,
                sip_time_limit = 5,
                fixed_packet_rate = 50,
                ipv6_policy = 'use-agent-policy',
                agents = [
                    null
                    ]
            )
        else:
            return SipServerInstantTest(
        )
        """

    def testSipServerInstantTest(self):
        """Test SipServerInstantTest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
