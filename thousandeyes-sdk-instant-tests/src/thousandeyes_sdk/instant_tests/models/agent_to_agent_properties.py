# coding: utf-8

"""
    Instant Tests API

    The Instant Tests API endpoint lets you create and run new instant tests. You will need to be a regular user or have the following permissions:   * `API Access`   * `View tests`  The response does not include the immediate test results. Use the Test Results endpoints to get test results after creating and executing an instant test. You can find the URLs for these endpoints in the _links section of the test definition that is returned when you create the instant test. 

    The version of the OpenAPI document: 7.0.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from thousandeyes_sdk.instant_tests.models.agent_to_agent_test_protocol import AgentToAgentTestProtocol
from thousandeyes_sdk.instant_tests.models.test_direction import TestDirection
from thousandeyes_sdk.instant_tests.models.test_dscp_id import TestDscpId
from thousandeyes_sdk.instant_tests.models.test_path_trace_mode import TestPathTraceMode
from typing import Optional, Set
from typing_extensions import Self

class AgentToAgentProperties(BaseModel):
    """
    AgentToAgentProperties
    """ # noqa: E501
    direction: Optional[TestDirection] = None
    dscp: Optional[StrictStr] = Field(default=None, description="DSCP label.")
    dscp_id: Optional[TestDscpId] = Field(default=None, alias="dscpId")
    mss: Optional[Annotated[int, Field(le=1400, strict=True, ge=20)]] = Field(default=None, description="Maximum segment size, in bytes.")
    num_path_traces: Optional[Annotated[int, Field(le=10, strict=True, ge=1)]] = Field(default=3, description="Number of path traces executed by the agent.", alias="numPathTraces")
    path_trace_mode: Optional[TestPathTraceMode] = Field(default=None, alias="pathTraceMode")
    port: Optional[Annotated[int, Field(le=65535, strict=True, ge=1)]] = Field(default=49153, description="Target port.")
    protocol: Optional[AgentToAgentTestProtocol] = None
    target_agent_id: StrictStr = Field(description="`agentId` of the target agent for the test.", alias="targetAgentId")
    throughput_measurements: Optional[StrictBool] = Field(default=False, description="Enable or disable throughput measurements. Throughput measurements cannot be enabled when the source or target of the test is a cloud agent.", alias="throughputMeasurements")
    throughput_duration: Optional[Annotated[int, Field(le=30000, strict=True, ge=5000)]] = Field(default=10000, description="The throughput duration.", alias="throughputDuration")
    throughput_rate: Optional[Annotated[int, Field(le=1000, strict=True, ge=8)]] = Field(default=None, description="The throughput rate, only applicable for UDP protocol.", alias="throughputRate")
    fixed_packet_rate: Optional[Annotated[int, Field(le=100, strict=True, ge=0)]] = Field(default=None, description="Sets packets rate sent to measure the network in packets per second.", alias="fixedPacketRate")
    type: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["direction", "dscp", "dscpId", "mss", "numPathTraces", "pathTraceMode", "port", "protocol", "targetAgentId", "throughputMeasurements", "throughputDuration", "throughputRate", "fixedPacketRate", "type"]

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
        """Create an instance of AgentToAgentProperties from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "dscp",
            "type",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AgentToAgentProperties from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "direction": obj.get("direction"),
            "dscp": obj.get("dscp"),
            "dscpId": obj.get("dscpId"),
            "mss": obj.get("mss"),
            "numPathTraces": obj.get("numPathTraces") if obj.get("numPathTraces") is not None else 3,
            "pathTraceMode": obj.get("pathTraceMode"),
            "port": obj.get("port") if obj.get("port") is not None else 49153,
            "protocol": obj.get("protocol"),
            "targetAgentId": obj.get("targetAgentId"),
            "throughputMeasurements": obj.get("throughputMeasurements") if obj.get("throughputMeasurements") is not None else False,
            "throughputDuration": obj.get("throughputDuration") if obj.get("throughputDuration") is not None else 10000,
            "throughputRate": obj.get("throughputRate"),
            "fixedPacketRate": obj.get("fixedPacketRate"),
            "type": obj.get("type")
        })
        return _obj


