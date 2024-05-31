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


class ModelProperty(object):
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
        'local_name': 'str',
        'name_space': 'str',
        '_property': 'bool',
        'ordinal': 'int',
        'id': 'AnonId',
        'uri': 'str',
        'stmt_term': 'Statement',
        'resource': 'bool',
        'model': 'Model',
        'literal': 'bool',
        'anon': 'bool',
        'uriresource': 'bool',
        'stmt_resource': 'bool'
    }

    attribute_map = {
        'local_name': 'localName',
        'name_space': 'nameSpace',
        '_property': 'property',
        'ordinal': 'ordinal',
        'id': 'id',
        'uri': 'uri',
        'stmt_term': 'stmtTerm',
        'resource': 'resource',
        'model': 'model',
        'literal': 'literal',
        'anon': 'anon',
        'uriresource': 'uriresource',
        'stmt_resource': 'stmtResource'
    }
    def __init__(self,
        local_name : 'str' = None,
        name_space : 'str' = None,
        _property : 'bool' = None,
        ordinal : 'int' = None,
        id : 'AnonId' = None,
        uri : 'str' = None,
        stmt_term : 'Statement' = None,
        resource : 'bool' = None,
        model : 'Model' = None,
        literal : 'bool' = None,
        anon : 'bool' = None,
        uriresource : 'bool' = None,
        stmt_resource : 'bool' = None):  # noqa: E501
        """ModelProperty - a model defined in Swagger"""  # noqa: E501

        self._local_name = None
        self._name_space = None
        self.__property = None
        self._ordinal = None
        self._id = None
        self._uri = None
        self._stmt_term = None
        self._resource = None
        self._model = None
        self._literal = None
        self._anon = None
        self._uriresource = None
        self._stmt_resource = None
        self.discriminator = None

        if local_name is not None:
            self.local_name = local_name
        if name_space is not None:
            self.name_space = name_space
        if _property is not None:
            self._property = _property
        if ordinal is not None:
            self.ordinal = ordinal
        if id is not None:
            self.id = id
        if uri is not None:
            self.uri = uri
        if stmt_term is not None:
            self.stmt_term = stmt_term
        if resource is not None:
            self.resource = resource
        if model is not None:
            self.model = model
        if literal is not None:
            self.literal = literal
        if anon is not None:
            self.anon = anon
        if uriresource is not None:
            self.uriresource = uriresource
        if stmt_resource is not None:
            self.stmt_resource = stmt_resource

    @property
    def local_name(self):
        """Gets the local_name of this ModelProperty.  # noqa: E501


        :return: The local_name of this ModelProperty.  # noqa: E501
        :rtype: str
        """
        return self._local_name

    @local_name.setter
    def local_name(self, local_name):
        """Sets the local_name of this ModelProperty.


        :param local_name: The local_name of this ModelProperty.  # noqa: E501
        :type: str
        """

        self._local_name = local_name

    @property
    def name_space(self):
        """Gets the name_space of this ModelProperty.  # noqa: E501


        :return: The name_space of this ModelProperty.  # noqa: E501
        :rtype: str
        """
        return self._name_space

    @name_space.setter
    def name_space(self, name_space):
        """Sets the name_space of this ModelProperty.


        :param name_space: The name_space of this ModelProperty.  # noqa: E501
        :type: str
        """

        self._name_space = name_space

    @property
    def _property(self):
        """Gets the _property of this ModelProperty.  # noqa: E501


        :return: The _property of this ModelProperty.  # noqa: E501
        :rtype: bool
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """Sets the _property of this ModelProperty.


        :param _property: The _property of this ModelProperty.  # noqa: E501
        :type: bool
        """

        self.__property = _property

    @property
    def ordinal(self):
        """Gets the ordinal of this ModelProperty.  # noqa: E501


        :return: The ordinal of this ModelProperty.  # noqa: E501
        :rtype: int
        """
        return self._ordinal

    @ordinal.setter
    def ordinal(self, ordinal):
        """Sets the ordinal of this ModelProperty.


        :param ordinal: The ordinal of this ModelProperty.  # noqa: E501
        :type: int
        """

        self._ordinal = ordinal

    @property
    def id(self):
        """Gets the id of this ModelProperty.  # noqa: E501


        :return: The id of this ModelProperty.  # noqa: E501
        :rtype: AnonId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ModelProperty.


        :param id: The id of this ModelProperty.  # noqa: E501
        :type: AnonId
        """

        self._id = id

    @property
    def uri(self):
        """Gets the uri of this ModelProperty.  # noqa: E501


        :return: The uri of this ModelProperty.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this ModelProperty.


        :param uri: The uri of this ModelProperty.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def stmt_term(self):
        """Gets the stmt_term of this ModelProperty.  # noqa: E501


        :return: The stmt_term of this ModelProperty.  # noqa: E501
        :rtype: Statement
        """
        return self._stmt_term

    @stmt_term.setter
    def stmt_term(self, stmt_term):
        """Sets the stmt_term of this ModelProperty.


        :param stmt_term: The stmt_term of this ModelProperty.  # noqa: E501
        :type: Statement
        """

        self._stmt_term = stmt_term

    @property
    def resource(self):
        """Gets the resource of this ModelProperty.  # noqa: E501


        :return: The resource of this ModelProperty.  # noqa: E501
        :rtype: bool
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this ModelProperty.


        :param resource: The resource of this ModelProperty.  # noqa: E501
        :type: bool
        """

        self._resource = resource

    @property
    def model(self):
        """Gets the model of this ModelProperty.  # noqa: E501


        :return: The model of this ModelProperty.  # noqa: E501
        :rtype: Model
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this ModelProperty.


        :param model: The model of this ModelProperty.  # noqa: E501
        :type: Model
        """

        self._model = model

    @property
    def literal(self):
        """Gets the literal of this ModelProperty.  # noqa: E501


        :return: The literal of this ModelProperty.  # noqa: E501
        :rtype: bool
        """
        return self._literal

    @literal.setter
    def literal(self, literal):
        """Sets the literal of this ModelProperty.


        :param literal: The literal of this ModelProperty.  # noqa: E501
        :type: bool
        """

        self._literal = literal

    @property
    def anon(self):
        """Gets the anon of this ModelProperty.  # noqa: E501


        :return: The anon of this ModelProperty.  # noqa: E501
        :rtype: bool
        """
        return self._anon

    @anon.setter
    def anon(self, anon):
        """Sets the anon of this ModelProperty.


        :param anon: The anon of this ModelProperty.  # noqa: E501
        :type: bool
        """

        self._anon = anon

    @property
    def uriresource(self):
        """Gets the uriresource of this ModelProperty.  # noqa: E501


        :return: The uriresource of this ModelProperty.  # noqa: E501
        :rtype: bool
        """
        return self._uriresource

    @uriresource.setter
    def uriresource(self, uriresource):
        """Sets the uriresource of this ModelProperty.


        :param uriresource: The uriresource of this ModelProperty.  # noqa: E501
        :type: bool
        """

        self._uriresource = uriresource

    @property
    def stmt_resource(self):
        """Gets the stmt_resource of this ModelProperty.  # noqa: E501


        :return: The stmt_resource of this ModelProperty.  # noqa: E501
        :rtype: bool
        """
        return self._stmt_resource

    @stmt_resource.setter
    def stmt_resource(self, stmt_resource):
        """Sets the stmt_resource of this ModelProperty.


        :param stmt_resource: The stmt_resource of this ModelProperty.  # noqa: E501
        :type: bool
        """

        self._stmt_resource = stmt_resource

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
        if issubclass(ModelProperty, dict):
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
        if issubclass(ModelProperty, dict):
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
        if not isinstance(other, ModelProperty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other


from opensilexClientToolsPython.models.anon_id import AnonId
from opensilexClientToolsPython.models.statement import Statement
from opensilexClientToolsPython.models.model import Model


