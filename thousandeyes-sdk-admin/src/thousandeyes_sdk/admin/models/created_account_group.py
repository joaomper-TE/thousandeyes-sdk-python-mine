# coding: utf-8

"""
    Administrative API

    ## Overview Manage users, accounts, and account groups in the ThousandEyes platform using the Administrative API. This API provides the following endpoints that define the operations to manage your organization:     * `/account-groups`: Account groups are used to divide an organization into different sections. These endpoints can be used to create, retrieve, update and delete account groups.   * `/users`: Create, retrieve, update and delete users within an organization.    * `/roles`: Create, retrieve and update roles for the current user.    * `/permissions`: Retrieve all assignable permissions. Used in the context of modifying roles.    * `/audit-user-events`: Retrieve all activity log events.    For more information about the administrative models, see [Account Management](https://docs.thousandeyes.com/product-documentation/user-management).

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
from thousandeyes_sdk.admin.models.self_links import SelfLinks
from thousandeyes_sdk.admin.models.user_account_group import UserAccountGroup
from typing import Optional, Set
from typing_extensions import Self

class CreatedAccountGroup(BaseModel):
    """
    CreatedAccountGroup
    """ # noqa: E501
    aid: Optional[StrictStr] = Field(default=None, description="A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint.")
    account_group_name: Optional[StrictStr] = Field(default=None, description="Account group name", alias="accountGroupName")
    is_current_account_group: Optional[StrictBool] = Field(default=None, description="Indicates whether the requested aid is the context of the current account.", alias="isCurrentAccountGroup")
    is_default_account_group: Optional[StrictBool] = Field(default=None, description="Indicates whether the aid is the default one for the requesting user.", alias="isDefaultAccountGroup")
    organization_name: Optional[StrictStr] = Field(default=None, description="(Optional) Indicates whether the aid is the default one for the requesting user.", alias="organizationName")
    users: Optional[List[UserAccountGroup]] = None
    links: Optional[SelfLinks] = Field(default=None, alias="_links")
    __properties: ClassVar[List[str]] = ["aid", "accountGroupName", "isCurrentAccountGroup", "isDefaultAccountGroup", "organizationName", "users", "_links"]

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
        """Create an instance of CreatedAccountGroup from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in users (list)
        _items = []
        if self.users:
            for _item in self.users:
                if _item:
                    _items.append(_item.to_dict())
            _dict['users'] = _items
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreatedAccountGroup from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "aid": obj.get("aid"),
            "accountGroupName": obj.get("accountGroupName"),
            "isCurrentAccountGroup": obj.get("isCurrentAccountGroup"),
            "isDefaultAccountGroup": obj.get("isDefaultAccountGroup"),
            "organizationName": obj.get("organizationName"),
            "users": [UserAccountGroup.from_dict(_item) for _item in obj["users"]] if obj.get("users") is not None else None,
            "_links": SelfLinks.from_dict(obj["_links"]) if obj.get("_links") is not None else None
        })
        return _obj


