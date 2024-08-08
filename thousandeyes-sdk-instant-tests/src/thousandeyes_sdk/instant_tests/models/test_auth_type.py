# coding: utf-8

"""
    Instant Tests API

    The Instant Tests API endpoint lets you create and run new instant tests. You will need to be a regular user or have the following permissions:   * `API Access`   * `View tests`  The response does not include the immediate test results. Use the Test Results endpoints to get test results after creating and executing an instant test. You can find the URLs for these endpoints in the _links section of the test definition that is returned when you create the instant test. 

    The version of the OpenAPI document: 7.0.14
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class TestAuthType(str, Enum):
    """
    HTTP authentication type.
    """

    """
    allowed enum values
    """
    NONE = 'none'
    BASIC = 'basic'
    NTLM = 'ntlm'
    KERBEROS = 'kerberos'
    OAUTH = 'oauth'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TestAuthType from a JSON string"""
        return cls(json.loads(json_str))


