# coding: utf-8

"""
    Dashboards API

    Manage ThousandEyes Dashboards.

    The version of the OpenAPI document: 7.0.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from thousandeyes_sdk.dashboards.models.api_agent_status_widget import ApiAgentStatusWidget
from thousandeyes_sdk.dashboards.models.api_alert_list_widget import ApiAlertListWidget
from thousandeyes_sdk.dashboards.models.api_box_and_whiskers_widget import ApiBoxAndWhiskersWidget
from thousandeyes_sdk.dashboards.models.api_color_grid_widget import ApiColorGridWidget
from thousandeyes_sdk.dashboards.models.api_geo_map_widget import ApiGeoMapWidget
from thousandeyes_sdk.dashboards.models.api_grouped_barchart_widget import ApiGroupedBarchartWidget
from thousandeyes_sdk.dashboards.models.api_multi_metric_table_widget import ApiMultiMetricTableWidget
from thousandeyes_sdk.dashboards.models.api_numbers_card_widget import ApiNumbersCardWidget
from thousandeyes_sdk.dashboards.models.api_pie_chart_widget import ApiPieChartWidget
from thousandeyes_sdk.dashboards.models.api_stacked_area_chart_widget import ApiStackedAreaChartWidget
from thousandeyes_sdk.dashboards.models.api_stacked_barchart_widget import ApiStackedBarchartWidget
from thousandeyes_sdk.dashboards.models.api_table_widget import ApiTableWidget
from thousandeyes_sdk.dashboards.models.api_test_table_widget import ApiTestTableWidget
from thousandeyes_sdk.dashboards.models.api_timeseries_widget import ApiTimeseriesWidget
from pydantic import StrictStr, Field, model_serializer
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

APIWIDGET_ONE_OF_SCHEMAS = ["ApiAgentStatusWidget", "ApiAlertListWidget", "ApiBoxAndWhiskersWidget", "ApiColorGridWidget", "ApiGeoMapWidget", "ApiGroupedBarchartWidget", "ApiMultiMetricTableWidget", "ApiNumbersCardWidget", "ApiPieChartWidget", "ApiStackedAreaChartWidget", "ApiStackedBarchartWidget", "ApiTableWidget", "ApiTestTableWidget", "ApiTimeseriesWidget"]

class ApiWidget(BaseModel):
    """
    ApiWidget
    """
    # data type: ApiAgentStatusWidget
    oneof_schema_1_validator: Optional[ApiAgentStatusWidget] = None
    # data type: ApiAlertListWidget
    oneof_schema_2_validator: Optional[ApiAlertListWidget] = None
    # data type: ApiBoxAndWhiskersWidget
    oneof_schema_3_validator: Optional[ApiBoxAndWhiskersWidget] = None
    # data type: ApiColorGridWidget
    oneof_schema_4_validator: Optional[ApiColorGridWidget] = None
    # data type: ApiGeoMapWidget
    oneof_schema_5_validator: Optional[ApiGeoMapWidget] = None
    # data type: ApiGroupedBarchartWidget
    oneof_schema_6_validator: Optional[ApiGroupedBarchartWidget] = None
    # data type: ApiMultiMetricTableWidget
    oneof_schema_7_validator: Optional[ApiMultiMetricTableWidget] = None
    # data type: ApiNumbersCardWidget
    oneof_schema_8_validator: Optional[ApiNumbersCardWidget] = None
    # data type: ApiPieChartWidget
    oneof_schema_9_validator: Optional[ApiPieChartWidget] = None
    # data type: ApiStackedAreaChartWidget
    oneof_schema_10_validator: Optional[ApiStackedAreaChartWidget] = None
    # data type: ApiStackedBarchartWidget
    oneof_schema_11_validator: Optional[ApiStackedBarchartWidget] = None
    # data type: ApiTableWidget
    oneof_schema_12_validator: Optional[ApiTableWidget] = None
    # data type: ApiTestTableWidget
    oneof_schema_13_validator: Optional[ApiTestTableWidget] = None
    # data type: ApiTimeseriesWidget
    oneof_schema_14_validator: Optional[ApiTimeseriesWidget] = None
    actual_instance: Optional[Union[ApiAgentStatusWidget, ApiAlertListWidget, ApiBoxAndWhiskersWidget, ApiColorGridWidget, ApiGeoMapWidget, ApiGroupedBarchartWidget, ApiMultiMetricTableWidget, ApiNumbersCardWidget, ApiPieChartWidget, ApiStackedAreaChartWidget, ApiStackedBarchartWidget, ApiTableWidget, ApiTestTableWidget, ApiTimeseriesWidget]] = None
    one_of_schemas: Set[str] = { "ApiAgentStatusWidget", "ApiAlertListWidget", "ApiBoxAndWhiskersWidget", "ApiColorGridWidget", "ApiGeoMapWidget", "ApiGroupedBarchartWidget", "ApiMultiMetricTableWidget", "ApiNumbersCardWidget", "ApiPieChartWidget", "ApiStackedAreaChartWidget", "ApiStackedBarchartWidget", "ApiTableWidget", "ApiTestTableWidget", "ApiTimeseriesWidget" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    discriminator_value_class_map: Dict[str, str] = {
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = ApiWidget.model_construct()
        error_messages = []
        match = 0
        # validate data type: ApiAgentStatusWidget
        if not isinstance(v, ApiAgentStatusWidget):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ApiAgentStatusWidget`")
        else:
            match += 1
        # validate data type: ApiAlertListWidget
        if not isinstance(v, ApiAlertListWidget):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ApiAlertListWidget`")
        else:
            match += 1
        # validate data type: ApiBoxAndWhiskersWidget
        if not isinstance(v, ApiBoxAndWhiskersWidget):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ApiBoxAndWhiskersWidget`")
        else:
            match += 1
        # validate data type: ApiColorGridWidget
        if not isinstance(v, ApiColorGridWidget):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ApiColorGridWidget`")
        else:
            match += 1
        # validate data type: ApiGeoMapWidget
        if not isinstance(v, ApiGeoMapWidget):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ApiGeoMapWidget`")
        else:
            match += 1
        # validate data type: ApiGroupedBarchartWidget
        if not isinstance(v, ApiGroupedBarchartWidget):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ApiGroupedBarchartWidget`")
        else:
            match += 1
        # validate data type: ApiMultiMetricTableWidget
        if not isinstance(v, ApiMultiMetricTableWidget):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ApiMultiMetricTableWidget`")
        else:
            match += 1
        # validate data type: ApiNumbersCardWidget
        if not isinstance(v, ApiNumbersCardWidget):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ApiNumbersCardWidget`")
        else:
            match += 1
        # validate data type: ApiPieChartWidget
        if not isinstance(v, ApiPieChartWidget):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ApiPieChartWidget`")
        else:
            match += 1
        # validate data type: ApiStackedAreaChartWidget
        if not isinstance(v, ApiStackedAreaChartWidget):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ApiStackedAreaChartWidget`")
        else:
            match += 1
        # validate data type: ApiStackedBarchartWidget
        if not isinstance(v, ApiStackedBarchartWidget):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ApiStackedBarchartWidget`")
        else:
            match += 1
        # validate data type: ApiTableWidget
        if not isinstance(v, ApiTableWidget):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ApiTableWidget`")
        else:
            match += 1
        # validate data type: ApiTestTableWidget
        if not isinstance(v, ApiTestTableWidget):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ApiTestTableWidget`")
        else:
            match += 1
        # validate data type: ApiTimeseriesWidget
        if not isinstance(v, ApiTimeseriesWidget):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ApiTimeseriesWidget`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in ApiWidget with oneOf schemas: ApiAgentStatusWidget, ApiAlertListWidget, ApiBoxAndWhiskersWidget, ApiColorGridWidget, ApiGeoMapWidget, ApiGroupedBarchartWidget, ApiMultiMetricTableWidget, ApiNumbersCardWidget, ApiPieChartWidget, ApiStackedAreaChartWidget, ApiStackedBarchartWidget, ApiTableWidget, ApiTestTableWidget, ApiTimeseriesWidget. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in ApiWidget with oneOf schemas: ApiAgentStatusWidget, ApiAlertListWidget, ApiBoxAndWhiskersWidget, ApiColorGridWidget, ApiGeoMapWidget, ApiGroupedBarchartWidget, ApiMultiMetricTableWidget, ApiNumbersCardWidget, ApiPieChartWidget, ApiStackedAreaChartWidget, ApiStackedBarchartWidget, ApiTableWidget, ApiTestTableWidget, ApiTimeseriesWidget. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into ApiAgentStatusWidget
        try:
            instance.actual_instance = ApiAgentStatusWidget.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ApiAlertListWidget
        try:
            instance.actual_instance = ApiAlertListWidget.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ApiBoxAndWhiskersWidget
        try:
            instance.actual_instance = ApiBoxAndWhiskersWidget.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ApiColorGridWidget
        try:
            instance.actual_instance = ApiColorGridWidget.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ApiGeoMapWidget
        try:
            instance.actual_instance = ApiGeoMapWidget.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ApiGroupedBarchartWidget
        try:
            instance.actual_instance = ApiGroupedBarchartWidget.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ApiMultiMetricTableWidget
        try:
            instance.actual_instance = ApiMultiMetricTableWidget.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ApiNumbersCardWidget
        try:
            instance.actual_instance = ApiNumbersCardWidget.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ApiPieChartWidget
        try:
            instance.actual_instance = ApiPieChartWidget.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ApiStackedAreaChartWidget
        try:
            instance.actual_instance = ApiStackedAreaChartWidget.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ApiStackedBarchartWidget
        try:
            instance.actual_instance = ApiStackedBarchartWidget.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ApiTableWidget
        try:
            instance.actual_instance = ApiTableWidget.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ApiTestTableWidget
        try:
            instance.actual_instance = ApiTestTableWidget.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ApiTimeseriesWidget
        try:
            instance.actual_instance = ApiTimeseriesWidget.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ApiWidget with oneOf schemas: ApiAgentStatusWidget, ApiAlertListWidget, ApiBoxAndWhiskersWidget, ApiColorGridWidget, ApiGeoMapWidget, ApiGroupedBarchartWidget, ApiMultiMetricTableWidget, ApiNumbersCardWidget, ApiPieChartWidget, ApiStackedAreaChartWidget, ApiStackedBarchartWidget, ApiTableWidget, ApiTestTableWidget, ApiTimeseriesWidget. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ApiWidget with oneOf schemas: ApiAgentStatusWidget, ApiAlertListWidget, ApiBoxAndWhiskersWidget, ApiColorGridWidget, ApiGeoMapWidget, ApiGroupedBarchartWidget, ApiMultiMetricTableWidget, ApiNumbersCardWidget, ApiPieChartWidget, ApiStackedAreaChartWidget, ApiStackedBarchartWidget, ApiTableWidget, ApiTestTableWidget, ApiTimeseriesWidget. Details: " + ", ".join(error_messages))
        else:
            return instance

    @model_serializer(when_used="json")
    def serialize_model(self):
        return json.loads(self.to_json())

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], ApiAgentStatusWidget, ApiAlertListWidget, ApiBoxAndWhiskersWidget, ApiColorGridWidget, ApiGeoMapWidget, ApiGroupedBarchartWidget, ApiMultiMetricTableWidget, ApiNumbersCardWidget, ApiPieChartWidget, ApiStackedAreaChartWidget, ApiStackedBarchartWidget, ApiTableWidget, ApiTestTableWidget, ApiTimeseriesWidget]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


