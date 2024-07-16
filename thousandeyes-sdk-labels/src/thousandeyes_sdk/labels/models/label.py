# coding: utf-8

"""
    Labels API

    ### Overview This is API for the Labels API (formerly called groups).

    The version of the OpenAPI document: 7.0.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from thousandeyes_sdk.labels.models.label_type import LabelType
from typing import Optional, Set
from typing_extensions import Self

class Label(BaseModel):
    """
    Label
    """ # noqa: E501
    label_id: Optional[StrictStr] = Field(default=None, description="Unique ID of the label; this number is negative for built-in labels. Query `/v7/labels/{type}/{id}` endpoint to see the list of agent/test/dashboard ids with this label. ", alias="labelId")
    is_built_in: Optional[StrictBool] = Field(default=None, description="`true` for built-in labels, and `false` for user-created labels. Note that built-in labels are read-only. ", alias="isBuiltIn")
    name: Optional[StrictStr] = Field(default=None, description="The name of the new label - this must be unique.")
    type: Optional[LabelType] = None
    __properties: ClassVar[List[str]] = ["labelId", "isBuiltIn", "name", "type"]

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
        """Create an instance of Label from a JSON string"""
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
        """Create an instance of Label from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "labelId": obj.get("labelId"),
            "isBuiltIn": obj.get("isBuiltIn"),
            "name": obj.get("name"),
            "type": obj.get("type")
        })
        return _obj


