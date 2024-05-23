# coding: utf-8

"""
    Dashboards API

    Manage ThousandEyes Dashboards.

    The version of the OpenAPI document: 7.0.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thousandeyes_sdk.dashboards.models.validation_error_item import ValidationErrorItem

class TestValidationErrorItem(unittest.TestCase):
    """ValidationErrorItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ValidationErrorItem:
        """Test ValidationErrorItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ValidationErrorItem`
        """
        model = ValidationErrorItem()
        if include_optional:
            return ValidationErrorItem(
                code = '',
                var_field = 56,
                message = ''
            )
        else:
            return ValidationErrorItem(
        )
        """

    def testValidationErrorItem(self):
        """Test ValidationErrorItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
