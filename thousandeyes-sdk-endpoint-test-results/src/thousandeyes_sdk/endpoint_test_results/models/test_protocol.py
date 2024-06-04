# coding: utf-8

"""
    Endpoint Test Results API

    Retrieve results for scheduled and dynamic tests on endpoint agents.

    The version of the OpenAPI document: 7.0.6
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class TestProtocol(str, Enum):
    """
    Protocol used by dependent network tests (end-to-end, path trace, PMTUD).
    """

    """
    allowed enum values
    """
    TCP = 'tcp'
    ICMP = 'icmp'
    UDP = 'udp'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TestProtocol from a JSON string"""
        return cls(json.loads(json_str))


