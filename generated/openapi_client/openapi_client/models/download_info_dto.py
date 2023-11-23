# coding: utf-8

"""
    Immich

    Immich API

    The version of the OpenAPI document: 1.88.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist

class DownloadInfoDto(BaseModel):
    """
    DownloadInfoDto
    """
    album_id: Optional[StrictStr] = Field(None, alias="albumId")
    archive_size: Optional[StrictInt] = Field(None, alias="archiveSize")
    asset_ids: Optional[conlist(StrictStr)] = Field(None, alias="assetIds")
    user_id: Optional[StrictStr] = Field(None, alias="userId")
    __properties = ["albumId", "archiveSize", "assetIds", "userId"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> DownloadInfoDto:
        """Create an instance of DownloadInfoDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DownloadInfoDto:
        """Create an instance of DownloadInfoDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DownloadInfoDto.parse_obj(obj)

        _obj = DownloadInfoDto.parse_obj({
            "album_id": obj.get("albumId"),
            "archive_size": obj.get("archiveSize"),
            "asset_ids": obj.get("assetIds"),
            "user_id": obj.get("userId")
        })
        return _obj

