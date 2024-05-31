# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.2.7-rdg
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from typing import List, Dict


class VueObjectTypeDTO(object):
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
        'name': 'str',
        'short_uri': 'str',
        'input_component': 'str',
        'input_components_by_property': 'dict(str, str)',
        'view_component': 'str',
        'rdf_type': 'RDFTypeTranslatedDTO'
    }

    attribute_map = {
        'uri': 'uri',
        'name': 'name',
        'short_uri': 'short_uri',
        'input_component': 'input_component',
        'input_components_by_property': 'input_components_by_property',
        'view_component': 'view_component',
        'rdf_type': 'rdf_type'
    }
    def __init__(self,
        uri : 'str' = None,
        name : 'str' = None,
        short_uri : 'str' = None,
        input_component : 'str' = None,
        input_components_by_property : 'Dict[str, str]' = None,
        view_component : 'str' = None,
        rdf_type : 'RDFTypeTranslatedDTO' = None):  # noqa: E501
        """VueObjectTypeDTO - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self._name = None
        self._short_uri = None
        self._input_component = None
        self._input_components_by_property = None
        self._view_component = None
        self._rdf_type = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if name is not None:
            self.name = name
        if short_uri is not None:
            self.short_uri = short_uri
        if input_component is not None:
            self.input_component = input_component
        if input_components_by_property is not None:
            self.input_components_by_property = input_components_by_property
        if view_component is not None:
            self.view_component = view_component
        if rdf_type is not None:
            self.rdf_type = rdf_type

    @property
    def uri(self):
        """Gets the uri of this VueObjectTypeDTO.  # noqa: E501


        :return: The uri of this VueObjectTypeDTO.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this VueObjectTypeDTO.


        :param uri: The uri of this VueObjectTypeDTO.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def name(self):
        """Gets the name of this VueObjectTypeDTO.  # noqa: E501


        :return: The name of this VueObjectTypeDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VueObjectTypeDTO.


        :param name: The name of this VueObjectTypeDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def short_uri(self):
        """Gets the short_uri of this VueObjectTypeDTO.  # noqa: E501


        :return: The short_uri of this VueObjectTypeDTO.  # noqa: E501
        :rtype: str
        """
        return self._short_uri

    @short_uri.setter
    def short_uri(self, short_uri):
        """Sets the short_uri of this VueObjectTypeDTO.


        :param short_uri: The short_uri of this VueObjectTypeDTO.  # noqa: E501
        :type: str
        """

        self._short_uri = short_uri

    @property
    def input_component(self):
        """Gets the input_component of this VueObjectTypeDTO.  # noqa: E501


        :return: The input_component of this VueObjectTypeDTO.  # noqa: E501
        :rtype: str
        """
        return self._input_component

    @input_component.setter
    def input_component(self, input_component):
        """Sets the input_component of this VueObjectTypeDTO.


        :param input_component: The input_component of this VueObjectTypeDTO.  # noqa: E501
        :type: str
        """

        self._input_component = input_component

    @property
    def input_components_by_property(self):
        """Gets the input_components_by_property of this VueObjectTypeDTO.  # noqa: E501


        :return: The input_components_by_property of this VueObjectTypeDTO.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._input_components_by_property

    @input_components_by_property.setter
    def input_components_by_property(self, input_components_by_property):
        """Sets the input_components_by_property of this VueObjectTypeDTO.


        :param input_components_by_property: The input_components_by_property of this VueObjectTypeDTO.  # noqa: E501
        :type: dict(str, str)
        """

        self._input_components_by_property = input_components_by_property

    @property
    def view_component(self):
        """Gets the view_component of this VueObjectTypeDTO.  # noqa: E501


        :return: The view_component of this VueObjectTypeDTO.  # noqa: E501
        :rtype: str
        """
        return self._view_component

    @view_component.setter
    def view_component(self, view_component):
        """Sets the view_component of this VueObjectTypeDTO.


        :param view_component: The view_component of this VueObjectTypeDTO.  # noqa: E501
        :type: str
        """

        self._view_component = view_component

    @property
    def rdf_type(self):
        """Gets the rdf_type of this VueObjectTypeDTO.  # noqa: E501


        :return: The rdf_type of this VueObjectTypeDTO.  # noqa: E501
        :rtype: RDFTypeTranslatedDTO
        """
        return self._rdf_type

    @rdf_type.setter
    def rdf_type(self, rdf_type):
        """Sets the rdf_type of this VueObjectTypeDTO.


        :param rdf_type: The rdf_type of this VueObjectTypeDTO.  # noqa: E501
        :type: RDFTypeTranslatedDTO
        """

        self._rdf_type = rdf_type

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
        if issubclass(VueObjectTypeDTO, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_api_formated_dict(self):
        """Returns a dict of properties as named in the API rather than in the model itself"""
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
        if issubclass(VueObjectTypeDTO, dict):
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
        if not isinstance(other, VueObjectTypeDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other


from opensilexClientToolsPython.models.rdf_type_translated_dto import RDFTypeTranslatedDTO


