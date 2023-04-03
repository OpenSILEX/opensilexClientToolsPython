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




class OWLClassPropertyRestrictionDTO(object):
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
        'required': 'bool',
        'list': 'bool',
        'rdf_type': 'str',
        'domain': 'str',
        '_property': 'str'
    }

    attribute_map = {
        'required': 'required',
        'list': 'list',
        'rdf_type': 'rdf_type',
        'domain': 'domain',
        '_property': 'property'
    }
    def __init__(self,
        rdf_type : 'str',
        domain : 'str',
        _property : 'str',
        required : 'bool' = None,
        list : 'bool' = None):  # noqa: E501
        """OWLClassPropertyRestrictionDTO - a model defined in Swagger"""  # noqa: E501

        self._required = None
        self._list = None
        self._rdf_type = None
        self._domain = None
        self.__property = None
        self.discriminator = None

        if required is not None:
            self.required = required
        if list is not None:
            self.list = list
        self.rdf_type = rdf_type
        self.domain = domain
        self._property = _property

    @property
    def required(self):
        """Gets the required of this OWLClassPropertyRestrictionDTO.  # noqa: E501


        :return: The required of this OWLClassPropertyRestrictionDTO.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this OWLClassPropertyRestrictionDTO.


        :param required: The required of this OWLClassPropertyRestrictionDTO.  # noqa: E501
        :type: bool
        """

        self._required = required

    @property
    def list(self):
        """Gets the list of this OWLClassPropertyRestrictionDTO.  # noqa: E501


        :return: The list of this OWLClassPropertyRestrictionDTO.  # noqa: E501
        :rtype: bool
        """
        return self._list

    @list.setter
    def list(self, list):
        """Sets the list of this OWLClassPropertyRestrictionDTO.


        :param list: The list of this OWLClassPropertyRestrictionDTO.  # noqa: E501
        :type: bool
        """

        self._list = list

    @property
    def rdf_type(self):
        """Gets the rdf_type of this OWLClassPropertyRestrictionDTO.  # noqa: E501

        RDF type  # noqa: E501

        :return: The rdf_type of this OWLClassPropertyRestrictionDTO.  # noqa: E501
        :rtype: str
        """
        return self._rdf_type

    @rdf_type.setter
    def rdf_type(self, rdf_type):
        """Sets the rdf_type of this OWLClassPropertyRestrictionDTO.

        RDF type  # noqa: E501

        :param rdf_type: The rdf_type of this OWLClassPropertyRestrictionDTO.  # noqa: E501
        :type: str
        """
        if rdf_type is None:
            raise ValueError("Invalid value for `rdf_type`, must not be `None`")  # noqa: E501

        self._rdf_type = rdf_type

    @property
    def domain(self):
        """Gets the domain of this OWLClassPropertyRestrictionDTO.  # noqa: E501

        Domain URI  # noqa: E501

        :return: The domain of this OWLClassPropertyRestrictionDTO.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this OWLClassPropertyRestrictionDTO.

        Domain URI  # noqa: E501

        :param domain: The domain of this OWLClassPropertyRestrictionDTO.  # noqa: E501
        :type: str
        """
        if domain is None:
            raise ValueError("Invalid value for `domain`, must not be `None`")  # noqa: E501

        self._domain = domain

    @property
    def _property(self):
        """Gets the _property of this OWLClassPropertyRestrictionDTO.  # noqa: E501

        Property URI  # noqa: E501

        :return: The _property of this OWLClassPropertyRestrictionDTO.  # noqa: E501
        :rtype: str
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """Sets the _property of this OWLClassPropertyRestrictionDTO.

        Property URI  # noqa: E501

        :param _property: The _property of this OWLClassPropertyRestrictionDTO.  # noqa: E501
        :type: str
        """
        if _property is None:
            raise ValueError("Invalid value for `_property`, must not be `None`")  # noqa: E501

        self.__property = _property

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
        if issubclass(OWLClassPropertyRestrictionDTO, dict):
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
        if not isinstance(other, OWLClassPropertyRestrictionDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

