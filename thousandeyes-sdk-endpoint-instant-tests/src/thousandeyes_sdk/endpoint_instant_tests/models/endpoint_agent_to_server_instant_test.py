# coding: utf-8

"""
    Endpoint Instant Scheduled Tests API

     You can create and execute a new endpoint instant scheduled test within ThousandEyes using this API. The test parameters are specified in the `POST` data.  The following applies to the Endpoint Instant Scheduled Tests API:  * To initiate the creation and execution of an instant scheduled test, the user must possess the `Edit endpoint tests` permission.  * Upon successful creation of an instant scheduled test, the API responds with an HTTP/201 CREATED status code and return the test definition. * It's important to note that the response does not include the results of the instant scheduled test. To retrieve test results, users can utilize the Endpoint Test Data endpoints. The URLs for these API test data endpoints are provided within the test definition output when an instant scheduled test is created. 

    The version of the OpenAPI document: 7.0.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from thousandeyes_sdk.endpoint_instant_tests.models.endpoint_test_agent_selector_type import EndpointTestAgentSelectorType
from typing import Optional, Set
from typing_extensions import Self

class EndpointAgentToServerInstantTest(BaseModel):
    """
    EndpointAgentToServerInstantTest
    """ # noqa: E501
    agent_selector_type: EndpointTestAgentSelectorType = Field(alias="agentSelectorType")
    agents: Optional[List[StrictStr]] = Field(default=None, description="List of endpoint agent IDs (obtained from `/endpoint/agents` endpoint). Required when `agentSelectorType` is set to `specific-agent`.")
    has_ping: Optional[StrictBool] = Field(default=True, description="Optional flag indicating if the test should run ping.", alias="hasPing")
    has_traceroute: Optional[StrictBool] = Field(default=True, description="Optional flag indicating if the test should run traceroute.", alias="hasTraceroute")
    endpoint_agent_labels: Optional[List[StrictStr]] = Field(default=None, description="List of endpoint agent label IDs (obtained from `/endpoint/labels` endpoint), required when `agentSelectorType` is set to `agent-labels`.", alias="endpointAgentLabels")
    max_machines: Annotated[int, Field(le=50000, strict=True, ge=1)] = Field(description="Maximum number of agents which can execute the test.", alias="maxMachines")
    port: Optional[StrictInt] = Field(default=None, description="Port number, if not specified, the port is selected based on a protocol (HTTP 80, HTTPS 443).")
    test_name: StrictStr = Field(description="Name of the test.", alias="testName")
    server_name: StrictStr = Field(description="A server address without a protocol or IP address.", alias="serverName")
    __properties: ClassVar[List[str]] = ["agentSelectorType", "agents", "hasPing", "hasTraceroute", "endpointAgentLabels", "maxMachines", "port", "testName", "serverName"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of EndpointAgentToServerInstantTest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EndpointAgentToServerInstantTest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "agentSelectorType": obj.get("agentSelectorType"),
            "agents": obj.get("agents"),
            "hasPing": obj.get("hasPing") if obj.get("hasPing") is not None else True,
            "hasTraceroute": obj.get("hasTraceroute") if obj.get("hasTraceroute") is not None else True,
            "endpointAgentLabels": obj.get("endpointAgentLabels"),
            "maxMachines": obj.get("maxMachines"),
            "port": obj.get("port"),
            "testName": obj.get("testName"),
            "serverName": obj.get("serverName")
        })
        return _obj


