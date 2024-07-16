# coding: utf-8

"""
    Test Results API

    Get test result metrics for Cloud and Enterprise Agent tests.

    The version of the OpenAPI document: 7.0.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class Expand(str, Enum):
    """
    Expand
    """

    """
    allowed enum values
    """
    HEADER = 'header'
    CERTIFICATE = 'certificate'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Expand from a JSON string"""
        return cls(json.loads(json_str))


