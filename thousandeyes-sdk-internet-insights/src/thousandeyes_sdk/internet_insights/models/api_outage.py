# coding: utf-8

"""
    Internet Insights API

    We are happy to announce the release of the Internet Insights API set. This limited release includes endpoints that:  * Make our catalog provider and Internet outage data accessible to API users. * Provide access to advanced filtering, which is part of our next-generation API efforts to allow API users to fine-tune queries across all of our APIs in a consistent manner.  Internet Insights provide visibility into core Internet infrastructure, including ISPs, DNS providers, IaaS, CDNs , and SaaS providers. It tracks the macro-level impact of Internet events on individual users and enterprise networks connecting at the edge of the Internet. These events include Outages, Routing hijacks and leaks, DDoS attacks, And political interference, among others.  Future releases of the Internet Insights API set will further unlock access to core Internet Insights functionality, unlocking potential integrations to enrich customer process flows.  For more information about Internet Insights, see the [Internet Insights](https://docs.thousandeyes.com/product-documentation/internet-insights). 

    The version of the OpenAPI document: 7.0.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from thousandeyes_sdk.internet_insights.models.self_links import SelfLinks
from typing import Optional, Set
from typing_extensions import Self

class ApiOutage(BaseModel):
    """
    List of outages.
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="The ID of the outage.")
    type: Optional[StrictStr] = Field(default=None, description="The type of outage e.g. app.")
    provider_name: Optional[StrictStr] = Field(default=None, description="The name of the affected provider.", alias="providerName")
    provider_type: Optional[StrictStr] = Field(default=None, description="The type of the affected provider.", alias="providerType")
    name: Optional[StrictStr] = Field(default=None, description="The name of the affected application.")
    start_date: Optional[StrictStr] = Field(default=None, description="Date and time when the outage started.", alias="startDate")
    start_round_id: Optional[StrictInt] = Field(default=None, description="Epoch time (seconds) when the outage started.", alias="startRoundId")
    end_date: Optional[StrictStr] = Field(default=None, description="Date and time when the outage ended.", alias="endDate")
    end_round_id: Optional[StrictInt] = Field(default=None, description="Epoch time (seconds) when the outage ended.", alias="endRoundId")
    duration: Optional[StrictInt] = Field(default=None, description="Duration of the outage (seconds)")
    affected_tests_count: Optional[StrictInt] = Field(default=None, description="The number of affected tests", alias="affectedTestsCount")
    affected_servers_count: Optional[StrictInt] = Field(default=None, description="The number of affected servers", alias="affectedServersCount")
    affected_locations_count: Optional[StrictInt] = Field(default=None, description="The number of affected locations.", alias="affectedLocationsCount")
    affected_interfaces_count: Optional[StrictInt] = Field(default=None, description="The number of affected interfaces.", alias="affectedInterfacesCount")
    asn: Optional[StrictInt] = Field(default=None, description="ASN number.")
    links: Optional[SelfLinks] = Field(default=None, alias="_links")
    __properties: ClassVar[List[str]] = ["id", "type", "providerName", "providerType", "name", "startDate", "startRoundId", "endDate", "endRoundId", "duration", "affectedTestsCount", "affectedServersCount", "affectedLocationsCount", "affectedInterfacesCount", "asn", "_links"]

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
        """Create an instance of ApiOutage from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApiOutage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "type": obj.get("type"),
            "providerName": obj.get("providerName"),
            "providerType": obj.get("providerType"),
            "name": obj.get("name"),
            "startDate": obj.get("startDate"),
            "startRoundId": obj.get("startRoundId"),
            "endDate": obj.get("endDate"),
            "endRoundId": obj.get("endRoundId"),
            "duration": obj.get("duration"),
            "affectedTestsCount": obj.get("affectedTestsCount"),
            "affectedServersCount": obj.get("affectedServersCount"),
            "affectedLocationsCount": obj.get("affectedLocationsCount"),
            "affectedInterfacesCount": obj.get("affectedInterfacesCount"),
            "asn": obj.get("asn"),
            "_links": SelfLinks.from_dict(obj["_links"]) if obj.get("_links") is not None else None
        })
        return _obj


