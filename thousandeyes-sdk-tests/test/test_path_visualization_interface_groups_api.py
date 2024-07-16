# coding: utf-8

"""
    Tests API

    This API supports listing, creating, editing, and deleting Cloud and Enterprise Agent (CEA) based tests. 

    The version of the OpenAPI document: 7.0.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import unittest
import thousandeyes_sdk.tests.models

from .test_utils import assert_constructed_model_matches_example_json
from thousandeyes_sdk.tests.api.path_visualization_interface_groups_api import PathVisualizationInterfaceGroupsApi


class TestPathVisualizationInterfaceGroupsApi(unittest.TestCase):
    """PathVisualizationInterfaceGroupsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PathVisualizationInterfaceGroupsApi()

    def tearDown(self) -> None:
        pass

    def test_create_path_vis_interface_groups_models_validation(self) -> None:
        """Test case for create_path_vis_interface_groups request and response models"""
        request_body_json = """
                {
                  "groupName" : "PathVis Interface Group",
                  "rdnsRegexes" : [ "aggr403b-1.iad3.rackspace.net", "aggr403c-1.iad3.rackspace.net" ],
                  "groupId" : "281474976710706",
                  "ipAddresses" : [ "1.1.1.1", "8.8.8.8" ],
                  "aid" : "1234"
                }"""

        request_loaded_json = json.loads(request_body_json)
        request_from_json = thousandeyes_sdk.tests.models.InterfaceGroup.from_json(request_body_json)
        assert_constructed_model_matches_example_json(request_from_json, request_loaded_json)

        response_body_json = """
                {
                  "groupName" : "PathVis Interface Group",
                  "rdnsRegexes" : [ "aggr403b-1.iad3.rackspace.net", "aggr403c-1.iad3.rackspace.net" ],
                  "groupId" : "281474976710706",
                  "ipAddresses" : [ "1.1.1.1", "8.8.8.8" ],
                  "aid" : "1234"
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.tests.models.InterfaceGroup.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_delete_path_vis_interface_group_models_validation(self) -> None:
        """Test case for delete_path_vis_interface_group request and response models"""


    def test_get_path_vis_interface_groups_models_validation(self) -> None:
        """Test case for get_path_vis_interface_groups request and response models"""

        response_body_json = """
                {
                  "pathVisInterfaceGroups" : [ {
                    "groupName" : "PathVis Interface Group",
                    "rdnsRegexes" : [ "aggr403b-1.iad3.rackspace.net", "aggr403c-1.iad3.rackspace.net" ],
                    "groupId" : "281474976710706",
                    "ipAddresses" : [ "1.1.1.1", "8.8.8.8" ],
                    "aid" : "1234"
                  }, {
                    "groupName" : "PathVis Interface Group",
                    "rdnsRegexes" : [ "aggr403b-1.iad3.rackspace.net", "aggr403c-1.iad3.rackspace.net" ],
                    "groupId" : "281474976710706",
                    "ipAddresses" : [ "1.1.1.1", "8.8.8.8" ],
                    "aid" : "1234"
                  } ],
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
                  }
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.tests.models.InterfaceGroups.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_update_path_vis_interface_group_models_validation(self) -> None:
        """Test case for update_path_vis_interface_group request and response models"""
        request_body_json = """
                {
                  "groupName" : "PathVis Interface Group",
                  "rdnsRegexes" : [ "aggr403b-1.iad3.rackspace.net", "aggr403c-1.iad3.rackspace.net" ],
                  "groupId" : "281474976710706",
                  "ipAddresses" : [ "1.1.1.1", "8.8.8.8" ],
                  "aid" : "1234"
                }"""

        request_loaded_json = json.loads(request_body_json)
        request_from_json = thousandeyes_sdk.tests.models.InterfaceGroup.from_json(request_body_json)
        assert_constructed_model_matches_example_json(request_from_json, request_loaded_json)

        response_body_json = """
                {
                  "groupName" : "PathVis Interface Group",
                  "rdnsRegexes" : [ "aggr403b-1.iad3.rackspace.net", "aggr403c-1.iad3.rackspace.net" ],
                  "groupId" : "281474976710706",
                  "ipAddresses" : [ "1.1.1.1", "8.8.8.8" ],
                  "aid" : "1234"
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.tests.models.InterfaceGroup.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)


if __name__ == '__main__':
    unittest.main()
