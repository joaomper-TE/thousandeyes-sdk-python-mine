# coding: utf-8

"""
    Endpoint Agents API

    Manage ThousandEyes Endpoint Agents using this API.   For more information about Endpoint Agents, see [Endpoint Agents](https://docs.thousandeyes.com/product-documentation/global-vantage-points/endpoint-agents).

    The version of the OpenAPI document: 7.0.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class AgentLicenseType(str, Enum):
    """
    AgentLicenseType
    """

    """
    allowed enum values
    """
    ESSENTIALS = 'essentials'
    ADVANTAGE = 'advantage'
    EMBEDDED = 'embedded'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AgentLicenseType from a JSON string"""
        return cls(json.loads(json_str))


