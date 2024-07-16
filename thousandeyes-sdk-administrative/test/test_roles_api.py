# coding: utf-8

"""
    Administrative API

    Manage users, accounts, and account groups in the ThousandEyes platform using the Administrative API. This API provides the following endpoints that define the operations to manage your organization:     * `/account-groups`: Account groups are used to divide an organization into different sections. These endpoints can be used to create, retrieve, update and delete account groups.   * `/users`: Create, retrieve, update and delete users within an organization.    * `/roles`: Create, retrieve and update roles for the current user.    * `/permissions`: Retrieve all assignable permissions. Used in the context of modifying roles.    * `/audit-user-events`: Retrieve all activity log events.    For more information about the administrative models, see [Account Management](https://docs.thousandeyes.com/product-documentation/user-management).

    The version of the OpenAPI document: 7.0.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import unittest
import thousandeyes_sdk.administrative.models

from .test_utils import assert_constructed_model_matches_example_json
from thousandeyes_sdk.administrative.api.roles_api import RolesApi


class TestRolesApi(unittest.TestCase):
    """RolesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = RolesApi()

    def tearDown(self) -> None:
        pass

    def test_create_role_models_validation(self) -> None:
        """Test case for create_role request and response models"""
        request_body_json = """
                {
                  "permissions" : [ "56", "315" ],
                  "name" : "Organization Admin"
                }"""

        request_loaded_json = json.loads(request_body_json)
        request_from_json = thousandeyes_sdk.administrative.models.RoleRequestBody.from_json(request_body_json)
        assert_constructed_model_matches_example_json(request_from_json, request_loaded_json)

        response_body_json = """
                {
                  "_links" : {
                    "self" : {
                      "hreflang" : "hreflang",
                      "templated" : true,
                      "profile" : "profile",
                      "name" : "name",
                      "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                      "type" : "type",
                      "deprecation" : "deprecation",
                      "title" : "title"
                    }
                  },
                  "roleId" : "35",
                  "permissions" : [ {
                    "label" : "View reports",
                    "permissionId" : "1",
                    "isManagementPermission" : true,
                    "permission" : "REPORT_READ"
                  }, {
                    "label" : "View snapshots",
                    "permissionId" : "51",
                    "isManagementPermission" : false,
                    "permission" : "REPORT_SNAPSHOTS_READ"
                  } ],
                  "name" : "Organization Admin",
                  "isBuiltin" : true
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.administrative.models.RoleDetail.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_delete_role_models_validation(self) -> None:
        """Test case for delete_role request and response models"""


    def test_get_role_models_validation(self) -> None:
        """Test case for get_role request and response models"""

        response_body_json = """
                {
                  "_links" : {
                    "self" : {
                      "hreflang" : "hreflang",
                      "templated" : true,
                      "profile" : "profile",
                      "name" : "name",
                      "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                      "type" : "type",
                      "deprecation" : "deprecation",
                      "title" : "title"
                    }
                  },
                  "roleId" : "35",
                  "permissions" : [ {
                    "label" : "View reports",
                    "permissionId" : "1",
                    "isManagementPermission" : true,
                    "permission" : "REPORT_READ"
                  }, {
                    "label" : "View snapshots",
                    "permissionId" : "51",
                    "isManagementPermission" : false,
                    "permission" : "REPORT_SNAPSHOTS_READ"
                  } ],
                  "name" : "Organization Admin",
                  "isBuiltin" : true
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.administrative.models.RoleDetail.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_get_roles_models_validation(self) -> None:
        """Test case for get_roles request and response models"""

        response_body_json = """
                {
                  "_links" : {
                    "self" : {
                      "hreflang" : "hreflang",
                      "templated" : true,
                      "profile" : "profile",
                      "name" : "name",
                      "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                      "type" : "type",
                      "deprecation" : "deprecation",
                      "title" : "title"
                    }
                  },
                  "roles" : [ {
                    "roleId" : "35",
                    "name" : "Organization Admin",
                    "isBuiltin" : true,
                    "hasManagementPermissions" : true
                  }, {
                    "roleId" : "35",
                    "name" : "Organization Admin",
                    "isBuiltin" : true,
                    "hasManagementPermissions" : true
                  } ]
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.administrative.models.Roles.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_update_role_models_validation(self) -> None:
        """Test case for update_role request and response models"""
        request_body_json = """
                {
                  "permissions" : [ "56", "315" ],
                  "name" : "Organization Admin"
                }"""

        request_loaded_json = json.loads(request_body_json)
        request_from_json = thousandeyes_sdk.administrative.models.RoleRequestBody.from_json(request_body_json)
        assert_constructed_model_matches_example_json(request_from_json, request_loaded_json)

        response_body_json = """
                {
                  "_links" : {
                    "self" : {
                      "hreflang" : "hreflang",
                      "templated" : true,
                      "profile" : "profile",
                      "name" : "name",
                      "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                      "type" : "type",
                      "deprecation" : "deprecation",
                      "title" : "title"
                    }
                  },
                  "roleId" : "35",
                  "permissions" : [ {
                    "label" : "View reports",
                    "permissionId" : "1",
                    "isManagementPermission" : true,
                    "permission" : "REPORT_READ"
                  }, {
                    "label" : "View snapshots",
                    "permissionId" : "51",
                    "isManagementPermission" : false,
                    "permission" : "REPORT_SNAPSHOTS_READ"
                  } ],
                  "name" : "Organization Admin",
                  "isBuiltin" : true
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.administrative.models.RoleDetail.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)


if __name__ == '__main__':
    unittest.main()
