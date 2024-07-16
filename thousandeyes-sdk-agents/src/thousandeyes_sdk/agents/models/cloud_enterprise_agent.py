# coding: utf-8

"""
    Agents API

     ## Overview Manage all agents available to your account in ThousandEyes, including both Cloud and Enterprise Agents.

    The version of the OpenAPI document: 7.0.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Optional
from thousandeyes_sdk.agents.models.agent import Agent
from thousandeyes_sdk.agents.models.enterprise_agent import EnterpriseAgent
from typing import Union, Any, List, Set, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal, Self
from pydantic import Field, model_serializer

CLOUDENTERPRISEAGENT_ANY_OF_SCHEMAS = ["Agent", "EnterpriseAgent"]

class CloudEnterpriseAgent(BaseModel):
    """
    CloudEnterpriseAgent
    """

    # data type: Agent
    anyof_schema_1_validator: Optional[Agent] = None
    # data type: EnterpriseAgent
    anyof_schema_2_validator: Optional[EnterpriseAgent] = None
    if TYPE_CHECKING:
        actual_instance: Optional[Union[Agent, EnterpriseAgent]] = None
    else:
        actual_instance: Any = None
    any_of_schemas: Set[str] = { "Agent", "EnterpriseAgent" }

    model_config = {
        "validate_assignment": True,
        "protected_namespaces": (),
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
    def actual_instance_must_validate_anyof(cls, v):
        instance = CloudEnterpriseAgent.model_construct()
        error_messages = []
        # validate data type: Agent
        if not isinstance(v, Agent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Agent`")
        else:
            return v

        # validate data type: EnterpriseAgent
        if not isinstance(v, EnterpriseAgent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `EnterpriseAgent`")
        else:
            return v

        if error_messages:
            # no match
            raise ValueError("No match found when setting the actual_instance in CloudEnterpriseAgent with anyOf schemas: Agent, EnterpriseAgent. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        # anyof_schema_1_validator: Optional[Agent] = None
        try:
            instance.actual_instance = Agent.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[EnterpriseAgent] = None
        try:
            instance.actual_instance = EnterpriseAgent.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into CloudEnterpriseAgent with anyOf schemas: Agent, EnterpriseAgent. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], Agent, EnterpriseAgent]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


