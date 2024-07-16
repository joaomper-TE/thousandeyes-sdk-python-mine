# coding: utf-8

"""
    Dashboards API

    Manage ThousandEyes Dashboards.

    The version of the OpenAPI document: 7.0.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from thousandeyes_sdk.dashboards.models.api_duration import ApiDuration
from thousandeyes_sdk.dashboards.models.api_widget_fixed_y_scale_prefix import ApiWidgetFixedYScalePrefix
from thousandeyes_sdk.dashboards.models.api_widget_measure import ApiWidgetMeasure
from thousandeyes_sdk.dashboards.models.dashboard_metric import DashboardMetric
from thousandeyes_sdk.dashboards.models.dashboard_metric_direction import DashboardMetricDirection
from thousandeyes_sdk.dashboards.models.metric_group import MetricGroup
from thousandeyes_sdk.dashboards.models.numbers_card_datasource import NumbersCardDatasource
from typing import Optional, Set
from typing_extensions import Self

class ApiNumbersCard(BaseModel):
    """
    An individual number card within the numbers card widget.
    """ # noqa: E501
    min_scale: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Minimum scale configured in the widget.", alias="minScale")
    max_scale: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Maximum scale configured in the widget.", alias="maxScale")
    unit: Optional[ApiWidgetFixedYScalePrefix] = None
    id: Optional[StrictStr] = Field(default=None, description="Identifier of the widget.")
    description: Optional[StrictStr] = Field(default=None, description="Description of the number card.")
    measure: Optional[ApiWidgetMeasure] = None
    compare_to_previous_value: Optional[StrictBool] = Field(default=None, alias="compareToPreviousValue")
    fixed_timespan: Optional[ApiDuration] = Field(default=None, alias="fixedTimespan")
    should_exclude_alert_suppression_windows: Optional[StrictBool] = Field(default=None, description="Excludes alert suppression windows from the widget when set to `true`.", alias="shouldExcludeAlertSuppressionWindows")
    data_source: Optional[NumbersCardDatasource] = Field(default=None, alias="dataSource")
    metric_group: Optional[MetricGroup] = Field(default=None, alias="metricGroup")
    direction: Optional[DashboardMetricDirection] = None
    metric: Optional[DashboardMetric] = None
    filters: Optional[Dict[str, List[Any]]] = Field(default=None, description="(Optional) Specifies the filters applied to the widget. When present, the `filters` property displays. Each filter object has two properties: `filterProperty` and `filterValue`. The `filterProperty` can be values like `AGENT`, `ENDPOINT_MACHINE_ID`, `TEST`, `MONITOR`, etc.  The `filterValue` represents an identifier array of the selected property.")
    __properties: ClassVar[List[str]] = ["minScale", "maxScale", "unit", "id", "description", "measure", "compareToPreviousValue", "fixedTimespan", "shouldExcludeAlertSuppressionWindows", "dataSource", "metricGroup", "direction", "metric", "filters"]

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
        """Create an instance of ApiNumbersCard from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of measure
        if self.measure:
            _dict['measure'] = self.measure.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fixed_timespan
        if self.fixed_timespan:
            _dict['fixedTimespan'] = self.fixed_timespan.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApiNumbersCard from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "minScale": obj.get("minScale"),
            "maxScale": obj.get("maxScale"),
            "unit": obj.get("unit"),
            "id": obj.get("id"),
            "description": obj.get("description"),
            "measure": ApiWidgetMeasure.from_dict(obj["measure"]) if obj.get("measure") is not None else None,
            "compareToPreviousValue": obj.get("compareToPreviousValue"),
            "fixedTimespan": ApiDuration.from_dict(obj["fixedTimespan"]) if obj.get("fixedTimespan") is not None else None,
            "shouldExcludeAlertSuppressionWindows": obj.get("shouldExcludeAlertSuppressionWindows"),
            "dataSource": obj.get("dataSource"),
            "metricGroup": obj.get("metricGroup"),
            "direction": obj.get("direction"),
            "metric": obj.get("metric"),
            "filters": obj.get("filters")
        })
        return _obj


