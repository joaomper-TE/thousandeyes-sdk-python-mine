# coding: utf-8

"""
    Test Results API

    Get test result metrics for Cloud and Enterprise Agent tests.

    The version of the OpenAPI document: 7.0.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thousandeyes_sdk.test_results.models.api_request_detail import ApiRequestDetail

class TestApiRequestDetail(unittest.TestCase):
    """ApiRequestDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiRequestDetail:
        """Test ApiRequestDetail
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiRequestDetail`
        """
        model = ApiRequestDetail()
        if include_optional:
            return ApiRequestDetail(
                api_call_time = 900.9,
                assert_error_count = 0,
                blocked_time = 49.9,
                connect_time = 12.1,
                completion = 100,
                dns_time = 11.1,
                name = 'First Step to Acquire Token',
                processing_time = 59.9,
                receive_time = 224.1,
                response_time = 440.8,
                send_time = 8.1,
                step_number = 1,
                step_time = 990.1,
                url = 'https://api.thousandeyes.com/v7/status',
                wait_time = 18.1,
                assertions = [
                    thousandeyes_sdk.test_results.models.api_request_detail_assertion.ApiRequestDetailAssertion(
                        step = 1, 
                        has_failed = False, )
                    ]
            )
        else:
            return ApiRequestDetail(
        )
        """

    def testApiRequestDetail(self):
        """Test ApiRequestDetail"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
