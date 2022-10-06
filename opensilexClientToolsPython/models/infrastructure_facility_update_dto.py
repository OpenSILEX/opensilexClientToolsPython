# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.00-rc+5.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from typing import List, Dict

from opensilexClientToolsPython.models.facility_address_dto import FacilityAddressDTO
from opensilexClientToolsPython.models.rdf_object_relation_dto import RDFObjectRelationDTO



class InfrastructureFacilityUpdateDTO(object):
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
        'rdf_type': 'str',
        'name': 'str',
        'organizations': 'list[str]',
        'address': 'FacilityAddressDTO',
        'relations': 'list[RDFObjectRelationDTO]',
        'rdf_type_name': 'str'
    }

    attribute_map = {
        'uri': 'uri',
        'rdf_type': 'rdf_type',
        'name': 'name',
        'organizations': 'organizations',
        'address': 'address',
        'relations': 'relations',
        'rdf_type_name': 'rdf_type_name'
    }
    def __init__(self, uri : 'str' = None, rdf_type : 'str' = None, name : 'str' = None, organizations : List['str'] = None, address : 'FacilityAddressDTO' = None, relations : List['RDFObjectRelationDTO'] = None, rdf_type_name : 'str' = None):  # noqa: E501
        """InfrastructureFacilityUpdateDTO - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self._rdf_type = None
        self._name = None
        self._organizations = None
        self._address = None
        self._relations = None
        self._rdf_type_name = None
        self.discriminator = None

        self.uri = uri
        if rdf_type is not None:
            self.rdf_type = rdf_type
        if name is not None:
            self.name = name
        if organizations is not None:
            self.organizations = organizations
        if address is not None:
            self.address = address
        if relations is not None:
            self.relations = relations
        if rdf_type_name is not None:
            self.rdf_type_name = rdf_type_name

    @property
    def uri(self):
        """Gets the uri of this InfrastructureFacilityUpdateDTO.  # noqa: E501


        :return: The uri of this InfrastructureFacilityUpdateDTO.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this InfrastructureFacilityUpdateDTO.


        :param uri: The uri of this InfrastructureFacilityUpdateDTO.  # noqa: E501
        :type: str
        """
        if uri is None:
            raise ValueError("Invalid value for `uri`, must not be `None`")  # noqa: E501

        self._uri = uri

    @property
    def rdf_type(self):
        """Gets the rdf_type of this InfrastructureFacilityUpdateDTO.  # noqa: E501


        :return: The rdf_type of this InfrastructureFacilityUpdateDTO.  # noqa: E501
        :rtype: str
        """
        return self._rdf_type

    @rdf_type.setter
    def rdf_type(self, rdf_type):
        """Sets the rdf_type of this InfrastructureFacilityUpdateDTO.


        :param rdf_type: The rdf_type of this InfrastructureFacilityUpdateDTO.  # noqa: E501
        :type: str
        """

        self._rdf_type = rdf_type

    @property
    def name(self):
        """Gets the name of this InfrastructureFacilityUpdateDTO.  # noqa: E501


        :return: The name of this InfrastructureFacilityUpdateDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InfrastructureFacilityUpdateDTO.


        :param name: The name of this InfrastructureFacilityUpdateDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def organizations(self):
        """Gets the organizations of this InfrastructureFacilityUpdateDTO.  # noqa: E501


        :return: The organizations of this InfrastructureFacilityUpdateDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._organizations

    @organizations.setter
    def organizations(self, organizations):
        """Sets the organizations of this InfrastructureFacilityUpdateDTO.


        :param organizations: The organizations of this InfrastructureFacilityUpdateDTO.  # noqa: E501
        :type: list[str]
        """

        self._organizations = organizations

    @property
    def address(self):
        """Gets the address of this InfrastructureFacilityUpdateDTO.  # noqa: E501


        :return: The address of this InfrastructureFacilityUpdateDTO.  # noqa: E501
        :rtype: FacilityAddressDTO
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this InfrastructureFacilityUpdateDTO.


        :param address: The address of this InfrastructureFacilityUpdateDTO.  # noqa: E501
        :type: FacilityAddressDTO
        """

        self._address = address

    @property
    def relations(self):
        """Gets the relations of this InfrastructureFacilityUpdateDTO.  # noqa: E501


        :return: The relations of this InfrastructureFacilityUpdateDTO.  # noqa: E501
        :rtype: list[RDFObjectRelationDTO]
        """
        return self._relations

    @relations.setter
    def relations(self, relations):
        """Sets the relations of this InfrastructureFacilityUpdateDTO.


        :param relations: The relations of this InfrastructureFacilityUpdateDTO.  # noqa: E501
        :type: list[RDFObjectRelationDTO]
        """

        self._relations = relations

    @property
    def rdf_type_name(self):
        """Gets the rdf_type_name of this InfrastructureFacilityUpdateDTO.  # noqa: E501


        :return: The rdf_type_name of this InfrastructureFacilityUpdateDTO.  # noqa: E501
        :rtype: str
        """
        return self._rdf_type_name

    @rdf_type_name.setter
    def rdf_type_name(self, rdf_type_name):
        """Sets the rdf_type_name of this InfrastructureFacilityUpdateDTO.


        :param rdf_type_name: The rdf_type_name of this InfrastructureFacilityUpdateDTO.  # noqa: E501
        :type: str
        """

        self._rdf_type_name = rdf_type_name

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
        if issubclass(InfrastructureFacilityUpdateDTO, dict):
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
        if not isinstance(other, InfrastructureFacilityUpdateDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

