# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: INSTANCE-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


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
        'rdf_type_name': 'str',
        'name': 'str',
        'organisation': 'str',
        'relations': 'list[RDFObjectRelationDTO]'
    }

    attribute_map = {
        'uri': 'uri',
        'rdf_type': 'rdf_type',
        'rdf_type_name': 'rdf_type_name',
        'name': 'name',
        'organisation': 'organisation',
        'relations': 'relations'
    }

    def __init__(self, uri=None, rdf_type=None, rdf_type_name=None, name=None, organisation=None, relations=None):  # noqa: E501
        """InfrastructureFacilityUpdateDTO - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self._rdf_type = None
        self._rdf_type_name = None
        self._name = None
        self._organisation = None
        self._relations = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if rdf_type is not None:
            self.rdf_type = rdf_type
        if rdf_type_name is not None:
            self.rdf_type_name = rdf_type_name
        if name is not None:
            self.name = name
        self.organisation = organisation
        if relations is not None:
            self.relations = relations

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
    def organisation(self):
        """Gets the organisation of this InfrastructureFacilityUpdateDTO.  # noqa: E501


        :return: The organisation of this InfrastructureFacilityUpdateDTO.  # noqa: E501
        :rtype: str
        """
        return self._organisation

    @organisation.setter
    def organisation(self, organisation):
        """Sets the organisation of this InfrastructureFacilityUpdateDTO.


        :param organisation: The organisation of this InfrastructureFacilityUpdateDTO.  # noqa: E501
        :type: str
        """
        if organisation is None:
            raise ValueError("Invalid value for `organisation`, must not be `None`")  # noqa: E501

        self._organisation = organisation

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
