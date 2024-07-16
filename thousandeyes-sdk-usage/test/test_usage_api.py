# coding: utf-8

"""
    Usage API

     These usage endpoints define the following operations:  * **Usage**: Retrieve usage data for the specified time period (default is one month).          * Users must have the `View Billing` permission to access this endpoint.     * This endpoint offers visibility across all account groups within the organization.     * Users with `View Billing` permission in multiple organizations should query the endpoint with the `aid` query string parameter (see optional parameters) for each organization.  * **Quotas**: Obtain organization and account usage quotas. Additionally, users with the appropriate permissions can create, update, or delete these quotas.          * Users must have the necessary permissions to perform quota-related actions.  Refer to the Usage API endpoints for detailed usage instructions and optional parameters. 

    The version of the OpenAPI document: 7.0.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import unittest
import thousandeyes_sdk.usage.models

from .test_utils import assert_constructed_model_matches_example_json
from thousandeyes_sdk.usage.api.usage_api import UsageApi


class TestUsageApi(unittest.TestCase):
    """UsageApi unit test stubs"""

    def setUp(self) -> None:
        self.api = UsageApi()

    def tearDown(self) -> None:
        pass

    def test_get_enterprise_agents_units_usage_models_validation(self) -> None:
        """Test case for get_enterprise_agents_units_usage request and response models"""

        response_body_json = """
                {
                  "_links" : {
                    "next" : {
                      "hreflang" : "hreflang",
                      "templated" : true,
                      "profile" : "profile",
                      "name" : "name",
                      "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                      "type" : "type",
                      "deprecation" : "deprecation",
                      "title" : "title"
                    },
                    "previous" : {
                      "hreflang" : "hreflang",
                      "templated" : true,
                      "profile" : "profile",
                      "name" : "name",
                      "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                      "type" : "type",
                      "deprecation" : "deprecation",
                      "title" : "title"
                    },
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
                  "breakdowns" : [ {
                    "aid" : "1234",
                    "agentId" : "121404",
                    "accountGroupName" : "Support",
                    "agentName" : "TEVA-test-agent",
                    "enterpriseUnitsUsed" : 599878,
                    "enterpriseUnitsProjected" : 597808,
                    "vagentId" : "123456"
                  }, {
                    "aid" : "315",
                    "agentId" : "121404",
                    "accountGroupName" : "Documentation",
                    "agentName" : "lab-physical-appliance-1",
                    "enterpriseUnitsUsed" : 597123,
                    "enterpriseUnitsProjected" : 597808,
                    "vagentId" : "789"
                  } ]
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.usage.models.EnterpriseAgentsUsage.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_get_tests_units_usage_models_validation(self) -> None:
        """Test case for get_tests_units_usage request and response models"""

        response_body_json = """
                {
                  "_links" : {
                    "next" : {
                      "hreflang" : "hreflang",
                      "templated" : true,
                      "profile" : "profile",
                      "name" : "name",
                      "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                      "type" : "type",
                      "deprecation" : "deprecation",
                      "title" : "title"
                    },
                    "previous" : {
                      "hreflang" : "hreflang",
                      "templated" : true,
                      "profile" : "profile",
                      "name" : "name",
                      "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                      "type" : "type",
                      "deprecation" : "deprecation",
                      "title" : "title"
                    },
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
                  "breakdowns" : [ {
                    "testId" : "1158",
                    "testName" : "https://app.thousandeyes.com",
                    "testType" : "Web-Page Load",
                    "enterpriseUnitsUsed" : 14050,
                    "enterpriseUnitsProjected" : 340674,
                    "cloudUnitsUsed" : 10000,
                    "cloudUnitsProjected" : 12000,
                    "aid" : "1234",
                    "accountGroupName" : "Support"
                  }, {
                    "testId" : "1221",
                    "testName" : "https://app.thousandeyes.com",
                    "testType" : "Web - HTTP Server",
                    "enterpriseUnitsUsed" : 194051,
                    "enterpriseUnitsProjected" : 30622,
                    "cloudUnitsUsed" : 12000,
                    "cloudUnitsProjected" : 13000,
                    "aid" : "1234",
                    "accountGroupName" : "Support"
                  } ]
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.usage.models.TestsUsage.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_get_usage_models_validation(self) -> None:
        """Test case for get_usage request and response models"""

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
                  "usage" : {
                    "cloudUnitsProjected" : 20993812,
                    "enterpriseAgentsUsed" : 58,
                    "endpointAgents" : [ {
                      "aid" : "1234",
                      "accountGroupName" : "Support",
                      "endpointAgentsUsed" : 22
                    }, {
                      "aid" : "12345",
                      "accountGroupName" : "Documentation",
                      "endpointAgentsUsed" : 14
                    } ],
                    "cloudUnitsNextBillingPeriod" : 25123456,
                    "enterpriseUnitsNextBillingPeriod" : 0,
                    "endpointAgentsUsed" : 42,
                    "enterpriseUnitsUsed" : 79640902,
                    "cloudUnitsUsed" : 8500489,
                    "tests" : [ {
                      "aid" : "1234",
                      "testId" : "1158",
                      "accountGroupName" : "Documentation",
                      "testName" : "https://app.thousandeyes.com",
                      "testType" : "Web-Page Load",
                      "cloudUnitsUsed" : 14050,
                      "cloudUnitsProjected" : 340674
                    }, {
                      "aid" : "12345",
                      "testId" : "1159",
                      "accountGroupName" : "Documentation",
                      "testName" : "https://support.thousandeyes.com",
                      "testType" : "Web - HTTP Server",
                      "cloudUnitsUsed" : 64390,
                      "cloudUnitsProjected" : 164457
                    } ],
                    "endpointAgentsEmbedded" : [ {
                      "aid" : "1234",
                      "accountGroupName" : "Support",
                      "endpointAgentsEmbeddedUsed" : 2
                    }, {
                      "aid" : "12345",
                      "accountGroupName" : "Documentation",
                      "endpointAgentsEmbeddedUsed" : 3
                    } ],
                    "endpointAgentsEssentialsUsed" : 5,
                    "quota" : {
                      "monthEnd" : "2020-02-05T08:00:00Z",
                      "endpointAgentsEmbeddedIncluded" : 10,
                      "enterpriseAgentsIncluded" : 25,
                      "monthStart" : "2020-01-05T08:00:00Z",
                      "cloudUnitsIncluded" : 4320000000,
                      "endpointAgentsIncluded" : 200,
                      "endpointAgentsEssentialsIncluded" : 10
                    },
                    "enterpriseUnitsProjected" : 108016317,
                    "endpointAgentsEmbeddedUsed" : 5,
                    "enterpriseAgents" : [ {
                      "aid" : "1234",
                      "accountGroupName" : "Support",
                      "enterpriseAgentsUsed" : 7
                    }, {
                      "aid" : "12345",
                      "accountGroupName" : "Documentation",
                      "enterpriseAgentsUsed" : 1
                    } ],
                    "enterpriseAgentUnits" : [ {
                      "aid" : "1234",
                      "agentId" : "121404",
                      "accountGroupName" : "Support",
                      "agentName" : "TEVA-test-agent",
                      "enterpriseUnitsUsed" : 599878,
                      "enterpriseUnitsProjected" : 597808,
                      "vagentId" : "123456"
                    }, {
                      "aid" : "315",
                      "agentId" : "121404",
                      "accountGroupName" : "Documentation",
                      "agentName" : "lab-physical-appliance-1",
                      "enterpriseUnitsUsed" : 597123,
                      "enterpriseUnitsProjected" : 597808,
                      "vagentId" : "789"
                    } ],
                    "endpointAgentsEssentials" : [ {
                      "aid" : "1234",
                      "accountGroupName" : "Support",
                      "endpointAgentsEssentialsUsed" : 2
                    }, {
                      "aid" : "12345",
                      "accountGroupName" : "Documentation",
                      "endpointAgentsEssentialsUsed" : 3
                    } ]
                  }
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.usage.models.Usage.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)


if __name__ == '__main__':
    unittest.main()
