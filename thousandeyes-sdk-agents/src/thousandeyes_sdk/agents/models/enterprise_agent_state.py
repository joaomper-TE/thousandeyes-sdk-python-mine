# coding: utf-8

"""
    Agents API

     ## Overview Manage all agents available to your account in ThousandEyes, including both Cloud and Enterprise Agents.

    The version of the OpenAPI document: 7.0.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class EnterpriseAgentState(str, Enum):
    """
    State of the agent.
    """

    """
    allowed enum values
    """
    ONLINE = 'online'
    OFFLINE = 'offline'
    DISABLED = 'disabled'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of EnterpriseAgentState from a JSON string"""
        return cls(json.loads(json_str))


