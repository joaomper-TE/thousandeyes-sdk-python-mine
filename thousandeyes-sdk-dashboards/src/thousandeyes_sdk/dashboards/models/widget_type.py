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
from enum import Enum
from typing_extensions import Self


class WidgetType(str, Enum):
    """
    Type of the Widget
    """

    """
    allowed enum values
    """
    BAR_CHART_COLON__STACKED = 'Bar Chart: Stacked'
    BAR_CHART_COLON__GROUPED = 'Bar Chart: Grouped'
    TIME_SERIES_COLON__LINE = 'Time Series: Line'
    TIME_SERIES_COLON__STACKED_AREA = 'Time Series: Stacked Area'
    PIE_CHART = 'Pie Chart'
    TABLE = 'Table'
    MULTI_METRIC_TABLE = 'Multi Metric Table'
    NUMBER = 'Number'
    AGENT_STATUS = 'Agent Status'
    COLOR_GRID = 'Color Grid'
    ALERT_LIST = 'Alert List'
    TEST_TABLE = 'Test Table'
    MAP = 'Map'
    BOX_AND_WHISKERS = 'Box and Whiskers'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of WidgetType from a JSON string"""
        return cls(json.loads(json_str))


