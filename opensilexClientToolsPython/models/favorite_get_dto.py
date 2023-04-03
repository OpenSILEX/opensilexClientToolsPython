# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0-rc+7.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from typing import List, Dict

from opensilexClientToolsPython.models.favorite_get_graph_name_dto import FavoriteGetGraphNameDTO



class FavoriteGetDTO(object):
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
        'uri': 'str',
        'type': 'str',
        'default_name': 'str',
        'graph_names': 'list[FavoriteGetGraphNameDTO]'
    }

    attribute_map = {
        'uri': 'uri',
        'type': 'type',
        'default_name': 'defaultName',
        'graph_names': 'graphNames'
    }
    def __init__(self,
        uri : 'str' = None,
        type : 'str' = None,
        default_name : 'str' = None,
        graph_names : 'List[FavoriteGetGraphNameDTO]' = None):  # noqa: E501
        """FavoriteGetDTO - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self._type = None
        self._default_name = None
        self._graph_names = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if type is not None:
            self.type = type
        if default_name is not None:
            self.default_name = default_name
        if graph_names is not None:
            self.graph_names = graph_names

    @property
    def uri(self):
        """Gets the uri of this FavoriteGetDTO.  # noqa: E501


        :return: The uri of this FavoriteGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this FavoriteGetDTO.


        :param uri: The uri of this FavoriteGetDTO.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def type(self):
        """Gets the type of this FavoriteGetDTO.  # noqa: E501


        :return: The type of this FavoriteGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FavoriteGetDTO.


        :param type: The type of this FavoriteGetDTO.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def default_name(self):
        """Gets the default_name of this FavoriteGetDTO.  # noqa: E501


        :return: The default_name of this FavoriteGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._default_name

    @default_name.setter
    def default_name(self, default_name):
        """Sets the default_name of this FavoriteGetDTO.


        :param default_name: The default_name of this FavoriteGetDTO.  # noqa: E501
        :type: str
        """

        self._default_name = default_name

    @property
    def graph_names(self):
        """Gets the graph_names of this FavoriteGetDTO.  # noqa: E501


        :return: The graph_names of this FavoriteGetDTO.  # noqa: E501
        :rtype: list[FavoriteGetGraphNameDTO]
        """
        return self._graph_names

    @graph_names.setter
    def graph_names(self, graph_names):
        """Sets the graph_names of this FavoriteGetDTO.


        :param graph_names: The graph_names of this FavoriteGetDTO.  # noqa: E501
        :type: list[FavoriteGetGraphNameDTO]
        """

        self._graph_names = graph_names

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
        if issubclass(FavoriteGetDTO, dict):
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
        if not isinstance(other, FavoriteGetDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

