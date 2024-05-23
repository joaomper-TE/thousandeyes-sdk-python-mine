# coding: utf-8

"""
    Dashboards API

    Manage ThousandEyes Dashboards.

    The version of the OpenAPI document: 7.0.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thousandeyes_sdk.dashboards.models.pagination_links import PaginationLinks

class TestPaginationLinks(unittest.TestCase):
    """PaginationLinks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginationLinks:
        """Test PaginationLinks
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginationLinks`
        """
        model = PaginationLinks()
        if include_optional:
            return PaginationLinks(
                previous = thousandeyes_sdk.dashboards.models.link.Link(
                    href = 'https://api.thousandeyes.com/v7/link/to/resource/id', 
                    templated = True, 
                    type = '', 
                    deprecation = '', 
                    name = '', 
                    profile = '', 
                    title = '', 
                    hreflang = '', ),
                next = thousandeyes_sdk.dashboards.models.link.Link(
                    href = 'https://api.thousandeyes.com/v7/link/to/resource/id', 
                    templated = True, 
                    type = '', 
                    deprecation = '', 
                    name = '', 
                    profile = '', 
                    title = '', 
                    hreflang = '', ),
                var_self = thousandeyes_sdk.dashboards.models.link.Link(
                    href = 'https://api.thousandeyes.com/v7/link/to/resource/id', 
                    templated = True, 
                    type = '', 
                    deprecation = '', 
                    name = '', 
                    profile = '', 
                    title = '', 
                    hreflang = '', )
            )
        else:
            return PaginationLinks(
        )
        """

    def testPaginationLinks(self):
        """Test PaginationLinks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
