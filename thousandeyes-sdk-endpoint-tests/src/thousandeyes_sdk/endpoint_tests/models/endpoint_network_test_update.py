# coding: utf-8

"""
    Endpoint Tests API

     Manage endpoint agent dynamic and scheduled tests using the Endpoint Tests API. 

    The version of the OpenAPI document: 7.0.6
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
from thousandeyes_sdk.endpoint_tests.models.endpoint_test_protocol import EndpointTestProtocol
from thousandeyes_sdk.endpoint_tests.models.test_interval import TestInterval
from thousandeyes_sdk.endpoint_tests.models.test_probe_mode import TestProbeMode
from typing import Optional, Set
from typing_extensions import Self

class EndpointNetworkTestUpdate(BaseModel):
    """
    EndpointNetworkTestUpdate
    """ # noqa: E501
    interval: Optional[TestInterval] = None
    test_name: Optional[StrictStr] = Field(default=None, description="Name of the test.", alias="testName")
    protocol: Optional[EndpointTestProtocol] = None
    is_enabled: Optional[StrictBool] = Field(default=True, description="Indicates if test is enabled.", alias="isEnabled")
    tcp_probe_mode: Optional[TestProbeMode] = Field(default=None, alias="tcpProbeMode")
    port: Optional[Annotated[int, Field(le=65535, strict=True, ge=1)]] = Field(default=49153, description="Target port.")
    server: Optional[StrictStr] = Field(default=None, description="Target domain name or IP address.")
    __properties: ClassVar[List[str]] = ["interval", "testName", "protocol", "isEnabled", "tcpProbeMode", "port", "server"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
        extra="allow",
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return self.model_dump_json(by_alias=True, exclude_unset=True, exclude_none=True)

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of EndpointNetworkTestUpdate from a JSON string"""
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
        """Create an instance of EndpointNetworkTestUpdate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "interval": obj.get("interval"),
            "testName": obj.get("testName"),
            "protocol": obj.get("protocol"),
            "isEnabled": obj.get("isEnabled") if obj.get("isEnabled") is not None else True,
            "tcpProbeMode": obj.get("tcpProbeMode"),
            "port": obj.get("port") if obj.get("port") is not None else 49153,
            "server": obj.get("server")
        })
        return _obj


