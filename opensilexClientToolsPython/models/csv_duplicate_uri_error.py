# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: BUILD-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from typing import List, Dict


class CSVDuplicateURIError(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'row_index': 'int',
        'col_index': 'int',
        'header': 'str',
        'value': 'str',
        'previous_row': 'int',
        'message': 'str'
    }

    attribute_map = {
        'row_index': 'rowIndex',
        'col_index': 'colIndex',
        'header': 'header',
        'value': 'value',
        'previous_row': 'previousRow',
        'message': 'message'
    }
    def __init__(self,
        row_index : 'int' = None,
        col_index : 'int' = None,
        header : 'str' = None,
        value : 'str' = None,
        previous_row : 'int' = None,
        message : 'str' = None):  # noqa: E501
        """CSVDuplicateURIError - a model defined in Swagger"""  # noqa: E501

        self._row_index = None
        self._col_index = None
        self._header = None
        self._value = None
        self._previous_row = None
        self._message = None
        self.discriminator = None

        if row_index is not None:
            self.row_index = row_index
        if col_index is not None:
            self.col_index = col_index
        if header is not None:
            self.header = header
        if value is not None:
            self.value = value
        if previous_row is not None:
            self.previous_row = previous_row
        if message is not None:
            self.message = message

    @property
    def row_index(self):
        """Gets the row_index of this CSVDuplicateURIError.  # noqa: E501


        :return: The row_index of this CSVDuplicateURIError.  # noqa: E501
        :rtype: int
        """
        return self._row_index

    @row_index.setter
    def row_index(self, row_index):
        """Sets the row_index of this CSVDuplicateURIError.


        :param row_index: The row_index of this CSVDuplicateURIError.  # noqa: E501
        :type: int
        """

        self._row_index = row_index

    @property
    def col_index(self):
        """Gets the col_index of this CSVDuplicateURIError.  # noqa: E501


        :return: The col_index of this CSVDuplicateURIError.  # noqa: E501
        :rtype: int
        """
        return self._col_index

    @col_index.setter
    def col_index(self, col_index):
        """Sets the col_index of this CSVDuplicateURIError.


        :param col_index: The col_index of this CSVDuplicateURIError.  # noqa: E501
        :type: int
        """

        self._col_index = col_index

    @property
    def header(self):
        """Gets the header of this CSVDuplicateURIError.  # noqa: E501


        :return: The header of this CSVDuplicateURIError.  # noqa: E501
        :rtype: str
        """
        return self._header

    @header.setter
    def header(self, header):
        """Sets the header of this CSVDuplicateURIError.


        :param header: The header of this CSVDuplicateURIError.  # noqa: E501
        :type: str
        """

        self._header = header

    @property
    def value(self):
        """Gets the value of this CSVDuplicateURIError.  # noqa: E501


        :return: The value of this CSVDuplicateURIError.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CSVDuplicateURIError.


        :param value: The value of this CSVDuplicateURIError.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def previous_row(self):
        """Gets the previous_row of this CSVDuplicateURIError.  # noqa: E501


        :return: The previous_row of this CSVDuplicateURIError.  # noqa: E501
        :rtype: int
        """
        return self._previous_row

    @previous_row.setter
    def previous_row(self, previous_row):
        """Sets the previous_row of this CSVDuplicateURIError.


        :param previous_row: The previous_row of this CSVDuplicateURIError.  # noqa: E501
        :type: int
        """

        self._previous_row = previous_row

    @property
    def message(self):
        """Gets the message of this CSVDuplicateURIError.  # noqa: E501


        :return: The message of this CSVDuplicateURIError.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this CSVDuplicateURIError.


        :param message: The message of this CSVDuplicateURIError.  # noqa: E501
        :type: str
        """

        self._message = message

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(CSVDuplicateURIError, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_api_formated_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[self.attribute_map[attr]] = list(map(
                    lambda x: x.to_api_formated_dict() if hasattr(x, "to_api_formated_dict") else x,
                    value
                ))
            elif hasattr(value, "to_api_formated_dict"):
                result[self.attribute_map[attr]] = value.to_api_formated_dict()
            elif isinstance(value, dict):
                result[self.attribute_map[attr]] = dict(map(
                    lambda item: (item[0], item[1].to_api_formated_dict())
                    if hasattr(item[1], "to_api_formated_dict") else item,
                    value.items()
                ))
            else:
                result[self.attribute_map[attr]] = value
        if issubclass(CSVDuplicateURIError, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CSVDuplicateURIError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other




