# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class InlineObject1(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, file=None):  # noqa: E501
        """InlineObject1 - a model defined in OpenAPI

        :param file: The file of this InlineObject1.  # noqa: E501
        :type file: file
        """
        self.openapi_types = {
            'file': file
        }

        self.attribute_map = {
            'file': 'file'
        }

        self._file = file

    @classmethod
    def from_dict(cls, dikt) -> 'InlineObject1':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_object_1 of this InlineObject1.  # noqa: E501
        :rtype: InlineObject1
        """
        return util.deserialize_model(dikt, cls)

    @property
    def file(self):
        """Gets the file of this InlineObject1.


        :return: The file of this InlineObject1.
        :rtype: file
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this InlineObject1.


        :param file: The file of this InlineObject1.
        :type file: file
        """

        self._file = file
