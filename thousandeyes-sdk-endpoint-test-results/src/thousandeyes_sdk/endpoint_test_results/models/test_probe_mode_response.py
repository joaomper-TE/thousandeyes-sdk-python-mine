# coding: utf-8

"""
    Endpoint Test Results API

    Retrieve results for scheduled and dynamic tests on endpoint agents.

    The version of the OpenAPI document: 7.0.14
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class TestProbeModeResponse(str, Enum):
    """
    Probe mode used by network test, only valid when the protocol is set to TCP.
    """

    """
    allowed enum values
    """
    AUTO = 'auto'
    SACK = 'sack'
    SYN = 'syn'
    UNKNOWN = 'unknown'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TestProbeModeResponse from a JSON string"""
        return cls(json.loads(json_str))


