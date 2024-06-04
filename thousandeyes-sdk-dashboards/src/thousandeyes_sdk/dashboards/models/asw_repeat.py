# coding: utf-8

"""
    Dashboards API

    Manage ThousandEyes Dashboards.

    The version of the OpenAPI document: 7.0.6
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class AswRepeat(str, Enum):
    """
    AswRepeat
    """

    """
    allowed enum values
    """
    NONE = 'none'
    EVERY_MINUS_DAY = 'every-day'
    ALT_MINUS_EVERY_MINUS_DAY = 'alt-every-day'
    EVERY_MINUS_WEEK = 'every-week'
    EVERY_MINUS_TWO_MINUS_WEEK = 'every-two-week'
    EVERY_MINUS_MONTH = 'every-month'
    EVERY_MINUS_THREE_MINUS_MONTH = 'every-three-month'
    CUSTOM = 'custom'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AswRepeat from a JSON string"""
        return cls(json.loads(json_str))


