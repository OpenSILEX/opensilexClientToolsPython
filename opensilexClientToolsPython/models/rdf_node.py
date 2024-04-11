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


class RDFNode(object):
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
        'resource': 'bool',
        'model': 'Model',
        'literal': 'bool',
        'anon': 'bool',
        'uriresource': 'bool',
        'stmt_resource': 'bool'
    }

    attribute_map = {
        'resource': 'resource',
        'model': 'model',
        'literal': 'literal',
        'anon': 'anon',
        'uriresource': 'uriresource',
        'stmt_resource': 'stmtResource'
    }
    def __init__(self,
        resource : 'bool' = None,
        model : 'Model' = None,
        literal : 'bool' = None,
        anon : 'bool' = None,
        uriresource : 'bool' = None,
        stmt_resource : 'bool' = None):  # noqa: E501
        """RDFNode - a model defined in Swagger"""  # noqa: E501

        self._resource = None
        self._model = None
        self._literal = None
        self._anon = None
        self._uriresource = None
        self._stmt_resource = None
        self.discriminator = None

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
    def resource(self):
        """Gets the resource of this RDFNode.  # noqa: E501


        :return: The resource of this RDFNode.  # noqa: E501
        :rtype: bool
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this RDFNode.


        :param resource: The resource of this RDFNode.  # noqa: E501
        :type: bool
        """

        self._resource = resource

    @property
    def model(self):
        """Gets the model of this RDFNode.  # noqa: E501


        :return: The model of this RDFNode.  # noqa: E501
        :rtype: Model
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this RDFNode.


        :param model: The model of this RDFNode.  # noqa: E501
        :type: Model
        """

        self._model = model

    @property
    def literal(self):
        """Gets the literal of this RDFNode.  # noqa: E501


        :return: The literal of this RDFNode.  # noqa: E501
        :rtype: bool
        """
        return self._literal

    @literal.setter
    def literal(self, literal):
        """Sets the literal of this RDFNode.


        :param literal: The literal of this RDFNode.  # noqa: E501
        :type: bool
        """

        self._literal = literal

    @property
    def anon(self):
        """Gets the anon of this RDFNode.  # noqa: E501


        :return: The anon of this RDFNode.  # noqa: E501
        :rtype: bool
        """
        return self._anon

    @anon.setter
    def anon(self, anon):
        """Sets the anon of this RDFNode.


        :param anon: The anon of this RDFNode.  # noqa: E501
        :type: bool
        """

        self._anon = anon

    @property
    def uriresource(self):
        """Gets the uriresource of this RDFNode.  # noqa: E501


        :return: The uriresource of this RDFNode.  # noqa: E501
        :rtype: bool
        """
        return self._uriresource

    @uriresource.setter
    def uriresource(self, uriresource):
        """Sets the uriresource of this RDFNode.


        :param uriresource: The uriresource of this RDFNode.  # noqa: E501
        :type: bool
        """

        self._uriresource = uriresource

    @property
    def stmt_resource(self):
        """Gets the stmt_resource of this RDFNode.  # noqa: E501


        :return: The stmt_resource of this RDFNode.  # noqa: E501
        :rtype: bool
        """
        return self._stmt_resource

    @stmt_resource.setter
    def stmt_resource(self, stmt_resource):
        """Sets the stmt_resource of this RDFNode.


        :param stmt_resource: The stmt_resource of this RDFNode.  # noqa: E501
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
        if issubclass(RDFNode, dict):
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
        if issubclass(RDFNode, dict):
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
        if not isinstance(other, RDFNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other


from opensilexClientToolsPython.models.model import Model


