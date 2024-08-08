# coding: utf-8

"""
    Test Snapshots API

    Creates a new test snapshot in ThousandEyes.

    The version of the OpenAPI document: 7.0.14
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from thousandeyes_sdk.snapshots.models.snapshot_links import SnapshotLinks
from thousandeyes_sdk.snapshots.models.snapshot_test import SnapshotTest
from typing import Optional, Set
from typing_extensions import Self

class SnapshotResponse(BaseModel):
    """
    SnapshotResponse
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Snapshot ID.")
    start_round_id: Optional[StrictInt] = Field(default=None, description="The start time of the test snapshot, represented in epoch time format (in seconds).", alias="startRoundId")
    end_round_id: Optional[StrictInt] = Field(default=None, description="The end time of the test snapshot, represented in epoch time format (in seconds).", alias="endRoundId")
    round_id: Optional[StrictInt] = Field(default=None, description="The selected time of the test snapshot, represented in epoch time format (in seconds).", alias="roundId")
    share_date: Optional[datetime] = Field(default=None, description="The date when the test snapshot was created in UTC time, formatted in ISO date-time.", alias="shareDate")
    source_test_id: Optional[StrictStr] = Field(default=None, description="Snapshot test ID.", alias="sourceTestId")
    test_id: Optional[StrictStr] = Field(default=None, description="Snapshot test ID.", alias="testId")
    uid: Optional[StrictStr] = Field(default=None, description="User ID.")
    display_name: Optional[StrictStr] = Field(default=None, description="Snapshot title.", alias="displayName")
    extra_params: Optional[StrictStr] = Field(default=None, description="Extra parameters.", alias="extraParams")
    test: Optional[SnapshotTest] = None
    links: Optional[SnapshotLinks] = Field(default=None, alias="_links")
    __properties: ClassVar[List[str]] = ["id", "startRoundId", "endRoundId", "roundId", "shareDate", "sourceTestId", "testId", "uid", "displayName", "extraParams", "test", "_links"]

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
        """Create an instance of SnapshotResponse from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "start_round_id",
            "end_round_id",
            "round_id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of test
        if self.test:
            _dict['test'] = self.test.to_dict()
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SnapshotResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "startRoundId": obj.get("startRoundId"),
            "endRoundId": obj.get("endRoundId"),
            "roundId": obj.get("roundId"),
            "shareDate": obj.get("shareDate"),
            "sourceTestId": obj.get("sourceTestId"),
            "testId": obj.get("testId"),
            "uid": obj.get("uid"),
            "displayName": obj.get("displayName"),
            "extraParams": obj.get("extraParams"),
            "test": SnapshotTest.from_dict(obj["test"]) if obj.get("test") is not None else None,
            "_links": SnapshotLinks.from_dict(obj["_links"]) if obj.get("_links") is not None else None
        })
        return _obj


