# coding: utf-8

"""
    Test Results API

    Get test result metrics for Cloud and Enterprise Agent tests.

    The version of the OpenAPI document: 7.0.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thousandeyes_sdk.test_results.models.path_vis_endpoint import PathVisEndpoint

class TestPathVisEndpoint(unittest.TestCase):
    """PathVisEndpoint unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PathVisEndpoint:
        """Test PathVisEndpoint
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PathVisEndpoint`
        """
        model = PathVisEndpoint()
        if include_optional:
            return PathVisEndpoint(
                ip_address = '196.40.106.237',
                mss = 1460,
                number_of_hops = 15,
                path_id = '1230899668701775614109128428722974545787322404682781961521',
                path_mtu = 1500,
                response_time = 1500
            )
        else:
            return PathVisEndpoint(
        )
        """

    def testPathVisEndpoint(self):
        """Test PathVisEndpoint"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
