# coding: utf-8

"""
    Test Results API

    Get test result metrics for Cloud and Enterprise Agent tests.

    The version of the OpenAPI document: 7.0.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thousandeyes_sdk.test_results.models.http_test_results import HttpTestResults

class TestHttpTestResults(unittest.TestCase):
    """HttpTestResults unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HttpTestResults:
        """Test HttpTestResults
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HttpTestResults`
        """
        model = HttpTestResults()
        if include_optional:
            return HttpTestResults(
                results = [
                    null
                    ],
                test = { },
                start_date = '2022-07-17T22:00:54Z',
                end_date = '2022-07-18T22:00:54Z',
                links = thousandeyes_sdk.test_results.models.pagination_links.PaginationLinks(
                    previous = thousandeyes_sdk.test_results.models.link.Link(
                        href = 'https://api.thousandeyes.com/v7/link/to/resource/id', 
                        templated = True, 
                        type = '', 
                        deprecation = '', 
                        name = '', 
                        profile = '', 
                        title = '', 
                        hreflang = '', ), 
                    next = thousandeyes_sdk.test_results.models.link.Link(
                        href = 'https://api.thousandeyes.com/v7/link/to/resource/id', 
                        templated = True, 
                        type = '', 
                        deprecation = '', 
                        name = '', 
                        profile = '', 
                        title = '', 
                        hreflang = '', ), 
                    self = , )
            )
        else:
            return HttpTestResults(
        )
        """

    def testHttpTestResults(self):
        """Test HttpTestResults"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
