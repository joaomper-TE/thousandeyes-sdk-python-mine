# coding: utf-8

"""
    Tests API

    This API supports listing, creating, editing, and deleting Cloud and Enterprise Agent (CEA) based tests. 

    The version of the OpenAPI document: 7.0.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thousandeyes_sdk.tests.models.dns_trace_instant_test import DnsTraceInstantTest

class TestDnsTraceInstantTest(unittest.TestCase):
    """DnsTraceInstantTest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DnsTraceInstantTest:
        """Test DnsTraceInstantTest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DnsTraceInstantTest`
        """
        model = DnsTraceInstantTest()
        if include_optional:
            return DnsTraceInstantTest(
                created_by = 'user@user.com',
                created_date = '2022-07-17T22:00:54Z',
                description = 'ThousandEyes Test',
                live_share = False,
                modified_by = 'user@user.com',
                modified_date = '2022-07-17T22:00:54Z',
                saved_event = True,
                test_id = '281474976710706',
                test_name = 'ThousandEyes Test',
                type = 'dns-trace',
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
                dns_transport_protocol = 'udp',
                domain = 'www.thousandeyes.com',
                dns_query_class = 'in',
                agents = [
                    null
                    ]
            )
        else:
            return DnsTraceInstantTest(
                domain = 'www.thousandeyes.com',
        )
        """

    def testDnsTraceInstantTest(self):
        """Test DnsTraceInstantTest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
