# coding: utf-8

"""
    Endpoint Test Results API

    Retrieve results for scheduled and dynamic tests on endpoint agents.

    The version of the OpenAPI document: 7.0.14
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from thousandeyes_sdk.endpoint_test_results.models.tests_data_search_filter import TestsDataSearchFilter
from thousandeyes_sdk.endpoint_test_results.models.tests_data_search_sort import TestsDataSearchSort
from thousandeyes_sdk.endpoint_test_results.models.tests_data_threshold_filters import TestsDataThresholdFilters
from typing import Optional, Set
from typing_extensions import Self

class TestsDataRoundsSearch(BaseModel):
    """
    TestsDataRoundsSearch
    """ # noqa: E501
    search_sort: Optional[List[TestsDataSearchSort]] = Field(default=None, alias="searchSort")
    threshold_filter: Optional[TestsDataThresholdFilters] = Field(default=None, alias="thresholdFilter")
    search_filters: Optional[TestsDataSearchFilter] = Field(default=None, alias="searchFilters")
    __properties: ClassVar[List[str]] = ["searchSort", "thresholdFilter", "searchFilters"]

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
        """Create an instance of TestsDataRoundsSearch from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in search_sort (list)
        _items = []
        if self.search_sort:
            for _item in self.search_sort:
                if _item:
                    _items.append(_item.to_dict())
            _dict['searchSort'] = _items
        # override the default output from pydantic by calling `to_dict()` of threshold_filter
        if self.threshold_filter:
            _dict['thresholdFilter'] = self.threshold_filter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of search_filters
        if self.search_filters:
            _dict['searchFilters'] = self.search_filters.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TestsDataRoundsSearch from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "searchSort": [TestsDataSearchSort.from_dict(_item) for _item in obj["searchSort"]] if obj.get("searchSort") is not None else None,
            "thresholdFilter": TestsDataThresholdFilters.from_dict(obj["thresholdFilter"]) if obj.get("thresholdFilter") is not None else None,
            "searchFilters": TestsDataSearchFilter.from_dict(obj["searchFilters"]) if obj.get("searchFilters") is not None else None
        })
        return _obj


