# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Setting(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, key=None, value=None):  # noqa: E501
        """Setting - a model defined in OpenAPI

        :param key: The key of this Setting.  # noqa: E501
        :type key: str
        :param value: The value of this Setting.  # noqa: E501
        :type value: str
        """
        self.openapi_types = {
            'key': str,
            'value': str
        }

        self.attribute_map = {
            'key': 'key',
            'value': 'value'
        }

        self._key = key
        self._value = value

    @classmethod
    def from_dict(cls, dikt) -> 'Setting':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Setting of this Setting.  # noqa: E501
        :rtype: Setting
        """
        return util.deserialize_model(dikt, cls)

    @property
    def key(self):
        """Gets the key of this Setting.


        :return: The key of this Setting.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this Setting.


        :param key: The key of this Setting.
        :type key: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def value(self):
        """Gets the value of this Setting.


        :return: The value of this Setting.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Setting.


        :param value: The value of this Setting.
        :type value: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value
