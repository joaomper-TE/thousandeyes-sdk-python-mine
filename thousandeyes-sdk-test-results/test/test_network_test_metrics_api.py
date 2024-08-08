# coding: utf-8

"""
    Test Results API

    Get test result metrics for Cloud and Enterprise Agent tests.

    The version of the OpenAPI document: 7.0.14
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import unittest
import thousandeyes_sdk.test_results.models

from .test_utils import assert_constructed_model_matches_example_json
from thousandeyes_sdk.test_results.api.network_test_metrics_api import NetworkTestMetricsApi


class TestNetworkTestMetricsApi(unittest.TestCase):
    """NetworkTestMetricsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = NetworkTestMetricsApi()

    def tearDown(self) -> None:
        pass

    def test_get_test_network_results_models_validation(self) -> None:
        """Test case for get_test_network_results request and response models"""

        response_body_json = """
                {
                  "test" : {
                    "_links" : {
                      "testResults" : [ {
                        "href" : "https://api.thousandeyes.com/v7/test-results/281474976710706/network"
                      }, {
                        "href" : "https://api.thousandeyes.com/v7/test-results/281474976710706/path-vis"
                      } ],
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
                    "liveShare" : false,
                    "savedEvent" : true,
                    "description" : "ThousandEyes Test",
                    "type" : "agent-to-server",
                    "enabled" : true,
                    "createdDate" : "2022-07-17T22:00:54Z",
                    "createdBy" : "user@user.com",
                    "modifiedDate" : "2022-07-17T22:00:54Z",
                    "interval" : 120,
                    "modifiedBy" : "user@user.com",
                    "testId" : "281474976710706",
                    "alertsEnabled" : true,
                    "testName" : "ThousandEyes Test"
                  },
                  "endDate" : "2022-07-18T22:00:54Z",
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
                  "results" : [ {
                    "date" : "2022-07-17T22:00:54Z",
                    "server" : "www.thousandeyes.com:80",
                    "availableBandwidth" : 9.100464,
                    "agent" : {
                      "agentId" : "281474976710706",
                      "agentName" : "thousandeyes-stg-va-254",
                      "location" : "San Francisco Bay Area",
                      "countryId" : "US"
                    },
                    "packetsBySecond" : [ [ ], [ 0 ], [ 2 ], [ 2, 1 ], [ 1, 1 ] ],
                    "avgLatency" : 167.04,
                    "bandwidth" : 4.3313155,
                    "minLatency" : 167.0,
                    "_links" : {
                      "appLink" : {
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
                    "maxLatency" : 168.0,
                    "healthScore" : 0.98,
                    "capacity" : 210.10854,
                    "loss" : 0.0,
                    "jitter" : 0.076808,
                    "serverIp" : "50.18.127.223",
                    "startTime" : 1384309800,
                    "endTime" : 1384309800,
                    "roundId" : 1384309800,
                    "direction" : "to-target"
                  }, {
                    "date" : "2022-07-17T22:00:54Z",
                    "server" : "www.thousandeyes.com:80",
                    "availableBandwidth" : 9.100464,
                    "agent" : {
                      "agentId" : "281474976710706",
                      "agentName" : "thousandeyes-stg-va-254",
                      "location" : "San Francisco Bay Area",
                      "countryId" : "US"
                    },
                    "packetsBySecond" : [ [ ], [ 0 ], [ 2 ], [ 2, 1 ], [ 1, 1 ] ],
                    "avgLatency" : 167.04,
                    "bandwidth" : 4.3313155,
                    "minLatency" : 167.0,
                    "_links" : {
                      "appLink" : {
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
                    "maxLatency" : 168.0,
                    "healthScore" : 0.98,
                    "capacity" : 210.10854,
                    "loss" : 0.0,
                    "jitter" : 0.076808,
                    "serverIp" : "50.18.127.223",
                    "startTime" : 1384309800,
                    "endTime" : 1384309800,
                    "roundId" : 1384309800,
                    "direction" : "to-target"
                  } ],
                  "startDate" : "2022-07-17T22:00:54Z"
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.test_results.models.NetworkTestResults.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_get_test_path_vis_agent_round_results_models_validation(self) -> None:
        """Test case for get_test_path_vis_agent_round_results request and response models"""

        response_body_json = """
                {
                  "test" : {
                    "_links" : {
                      "testResults" : [ {
                        "href" : "https://api.thousandeyes.com/v7/test-results/281474976710706/network"
                      }, {
                        "href" : "https://api.thousandeyes.com/v7/test-results/281474976710706/path-vis"
                      } ],
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
                    "liveShare" : false,
                    "savedEvent" : true,
                    "description" : "ThousandEyes Test",
                    "type" : "agent-to-server",
                    "enabled" : true,
                    "createdDate" : "2022-07-17T22:00:54Z",
                    "createdBy" : "user@user.com",
                    "modifiedDate" : "2022-07-17T22:00:54Z",
                    "interval" : 120,
                    "modifiedBy" : "user@user.com",
                    "testId" : "281474976710706",
                    "alertsEnabled" : true,
                    "testName" : "ThousandEyes Test"
                  },
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
                  "results" : [ {
                    "date" : "2022-07-17T22:00:54Z",
                    "server" : "www.google.com:443",
                    "agent" : {
                      "agentId" : "281474976710706",
                      "agentName" : "thousandeyes-stg-va-254",
                      "location" : "San Francisco Bay Area",
                      "countryId" : "US"
                    },
                    "_links" : {
                      "appLink" : {
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
                    "targetIsProxy" : true,
                    "sourcePrefix" : "196.40.96.0/20",
                    "sourceIp" : "196.40.106.237",
                    "pathTraces" : [ {
                      "hops" : [ {
                        "rdns" : "core-router1.cpt2.host-h.net",
                        "prefix" : "196.40.96.0/20",
                        "responseTime" : 1,
                        "hop" : 1,
                        "ipAddress" : "196.40.106.237",
                        "mpls" : "mpls",
                        "location" : "Cape Town, South Africa",
                        "network" : "HETZNER (Pty) Ltd (AS 37153)"
                      }, {
                        "rdns" : "core-router1.cpt2.host-h.net",
                        "prefix" : "196.40.96.0/20",
                        "responseTime" : 1,
                        "hop" : 1,
                        "ipAddress" : "196.40.106.237",
                        "mpls" : "mpls",
                        "location" : "Cape Town, South Africa",
                        "network" : "HETZNER (Pty) Ltd (AS 37153)"
                      } ],
                      "pathId" : "4711301366345855606023718047703941305741293841502186803"
                    }, {
                      "hops" : [ {
                        "rdns" : "core-router1.cpt2.host-h.net",
                        "prefix" : "196.40.96.0/20",
                        "responseTime" : 1,
                        "hop" : 1,
                        "ipAddress" : "196.40.106.237",
                        "mpls" : "mpls",
                        "location" : "Cape Town, South Africa",
                        "network" : "HETZNER (Pty) Ltd (AS 37153)"
                      }, {
                        "rdns" : "core-router1.cpt2.host-h.net",
                        "prefix" : "196.40.96.0/20",
                        "responseTime" : 1,
                        "hop" : 1,
                        "ipAddress" : "196.40.106.237",
                        "mpls" : "mpls",
                        "location" : "Cape Town, South Africa",
                        "network" : "HETZNER (Pty) Ltd (AS 37153)"
                      } ],
                      "pathId" : "4711301366345855606023718047703941305741293841502186803"
                    } ],
                    "serverIp" : "172.217.170.68",
                    "startTime" : 1384309800,
                    "endTime" : 1384309800,
                    "roundId" : 1384309800,
                    "direction" : "to-target"
                  }, {
                    "date" : "2022-07-17T22:00:54Z",
                    "server" : "www.google.com:443",
                    "agent" : {
                      "agentId" : "281474976710706",
                      "agentName" : "thousandeyes-stg-va-254",
                      "location" : "San Francisco Bay Area",
                      "countryId" : "US"
                    },
                    "_links" : {
                      "appLink" : {
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
                    "targetIsProxy" : true,
                    "sourcePrefix" : "196.40.96.0/20",
                    "sourceIp" : "196.40.106.237",
                    "pathTraces" : [ {
                      "hops" : [ {
                        "rdns" : "core-router1.cpt2.host-h.net",
                        "prefix" : "196.40.96.0/20",
                        "responseTime" : 1,
                        "hop" : 1,
                        "ipAddress" : "196.40.106.237",
                        "mpls" : "mpls",
                        "location" : "Cape Town, South Africa",
                        "network" : "HETZNER (Pty) Ltd (AS 37153)"
                      }, {
                        "rdns" : "core-router1.cpt2.host-h.net",
                        "prefix" : "196.40.96.0/20",
                        "responseTime" : 1,
                        "hop" : 1,
                        "ipAddress" : "196.40.106.237",
                        "mpls" : "mpls",
                        "location" : "Cape Town, South Africa",
                        "network" : "HETZNER (Pty) Ltd (AS 37153)"
                      } ],
                      "pathId" : "4711301366345855606023718047703941305741293841502186803"
                    }, {
                      "hops" : [ {
                        "rdns" : "core-router1.cpt2.host-h.net",
                        "prefix" : "196.40.96.0/20",
                        "responseTime" : 1,
                        "hop" : 1,
                        "ipAddress" : "196.40.106.237",
                        "mpls" : "mpls",
                        "location" : "Cape Town, South Africa",
                        "network" : "HETZNER (Pty) Ltd (AS 37153)"
                      }, {
                        "rdns" : "core-router1.cpt2.host-h.net",
                        "prefix" : "196.40.96.0/20",
                        "responseTime" : 1,
                        "hop" : 1,
                        "ipAddress" : "196.40.106.237",
                        "mpls" : "mpls",
                        "location" : "Cape Town, South Africa",
                        "network" : "HETZNER (Pty) Ltd (AS 37153)"
                      } ],
                      "pathId" : "4711301366345855606023718047703941305741293841502186803"
                    } ],
                    "serverIp" : "172.217.170.68",
                    "startTime" : 1384309800,
                    "endTime" : 1384309800,
                    "roundId" : 1384309800,
                    "direction" : "to-target"
                  } ]
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.test_results.models.PathVisDetailTestResults.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_get_test_path_vis_results_models_validation(self) -> None:
        """Test case for get_test_path_vis_results request and response models"""

        response_body_json = """
                {
                  "test" : {
                    "_links" : {
                      "testResults" : [ {
                        "href" : "https://api.thousandeyes.com/v7/test-results/281474976710706/network"
                      }, {
                        "href" : "https://api.thousandeyes.com/v7/test-results/281474976710706/path-vis"
                      } ],
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
                    "liveShare" : false,
                    "savedEvent" : true,
                    "description" : "ThousandEyes Test",
                    "type" : "agent-to-server",
                    "enabled" : true,
                    "createdDate" : "2022-07-17T22:00:54Z",
                    "createdBy" : "user@user.com",
                    "modifiedDate" : "2022-07-17T22:00:54Z",
                    "interval" : 120,
                    "modifiedBy" : "user@user.com",
                    "testId" : "281474976710706",
                    "alertsEnabled" : true,
                    "testName" : "ThousandEyes Test"
                  },
                  "endDate" : "2022-07-18T22:00:54Z",
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
                  "results" : [ {
                    "date" : "2022-07-17T22:00:54Z",
                    "server" : "www.google.com:443",
                    "agent" : {
                      "agentId" : "281474976710706",
                      "agentName" : "thousandeyes-stg-va-254",
                      "location" : "San Francisco Bay Area",
                      "countryId" : "US"
                    },
                    "_links" : {
                      "appLink" : {
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
                    "targetIsProxy" : true,
                    "sourcePrefix" : "196.40.96.0/20",
                    "sourceIp" : "196.40.106.237",
                    "pathTraces" : [ {
                      "numberOfHops" : 15,
                      "responseTime" : 1500,
                      "ipAddress" : "196.40.106.237",
                      "pathMtu" : 1500,
                      "pathId" : "1230899668701775614109128428722974545787322404682781961521",
                      "mss" : 1460
                    }, {
                      "numberOfHops" : 15,
                      "responseTime" : 1500,
                      "ipAddress" : "196.40.106.237",
                      "pathMtu" : 1500,
                      "pathId" : "1230899668701775614109128428722974545787322404682781961521",
                      "mss" : 1460
                    } ],
                    "serverIp" : "172.217.170.68",
                    "startTime" : 1384309800,
                    "endTime" : 1384309800,
                    "roundId" : 1384309800,
                    "direction" : "to-target"
                  }, {
                    "date" : "2022-07-17T22:00:54Z",
                    "server" : "www.google.com:443",
                    "agent" : {
                      "agentId" : "281474976710706",
                      "agentName" : "thousandeyes-stg-va-254",
                      "location" : "San Francisco Bay Area",
                      "countryId" : "US"
                    },
                    "_links" : {
                      "appLink" : {
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
                    "targetIsProxy" : true,
                    "sourcePrefix" : "196.40.96.0/20",
                    "sourceIp" : "196.40.106.237",
                    "pathTraces" : [ {
                      "numberOfHops" : 15,
                      "responseTime" : 1500,
                      "ipAddress" : "196.40.106.237",
                      "pathMtu" : 1500,
                      "pathId" : "1230899668701775614109128428722974545787322404682781961521",
                      "mss" : 1460
                    }, {
                      "numberOfHops" : 15,
                      "responseTime" : 1500,
                      "ipAddress" : "196.40.106.237",
                      "pathMtu" : 1500,
                      "pathId" : "1230899668701775614109128428722974545787322404682781961521",
                      "mss" : 1460
                    } ],
                    "serverIp" : "172.217.170.68",
                    "startTime" : 1384309800,
                    "endTime" : 1384309800,
                    "roundId" : 1384309800,
                    "direction" : "to-target"
                  } ],
                  "startDate" : "2022-07-17T22:00:54Z"
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.test_results.models.PathVisTestResults.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)


if __name__ == '__main__':
    unittest.main()
