# coding: utf-8

"""
    Test Results API

    Get test result metrics for Cloud and Enterprise Agent tests.

    The version of the OpenAPI document: 7.0.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thousandeyes_sdk.test_results.models.path_vis_route import PathVisRoute

class TestPathVisRoute(unittest.TestCase):
    """PathVisRoute unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PathVisRoute:
        """Test PathVisRoute
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PathVisRoute`
        """
        model = PathVisRoute()
        if include_optional:
            return PathVisRoute(
                path_id = '4711301366345855606023718047703941305741293841502186803',
                hops = [
                    thousandeyes_sdk.test_results.models.path_vis_hop.PathVisHop(
                        hop = 1, 
                        ip_address = '196.40.106.237', 
                        prefix = '196.40.96.0/20', 
                        rdns = 'core-router1.cpt2.host-h.net', 
                        network = 'HETZNER (Pty) Ltd (AS 37153)', 
                        response_time = 1, 
                        location = 'Cape Town, South Africa', 
                        mpls = '', )
                    ]
            )
        else:
            return PathVisRoute(
        )
        """

    def testPathVisRoute(self):
        """Test PathVisRoute"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
