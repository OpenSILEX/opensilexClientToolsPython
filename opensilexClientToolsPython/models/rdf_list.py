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


class RDFList(object):
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
        'empty': 'bool',
        'head': 'RDFNode',
        'strict': 'bool',
        'tail': 'RDFList',
        'valid': 'bool',
        'validity_error_message': 'str',
        'id': 'AnonId',
        'name_space': 'str',
        'stmt_term': 'Statement',
        'uri': 'str',
        'local_name': 'str',
        'resource': 'bool',
        'model': 'Model',
        'literal': 'bool',
        'anon': 'bool',
        'uriresource': 'bool',
        'stmt_resource': 'bool'
    }

    attribute_map = {
        'empty': 'empty',
        'head': 'head',
        'strict': 'strict',
        'tail': 'tail',
        'valid': 'valid',
        'validity_error_message': 'validityErrorMessage',
        'id': 'id',
        'name_space': 'nameSpace',
        'stmt_term': 'stmtTerm',
        'uri': 'uri',
        'local_name': 'localName',
        'resource': 'resource',
        'model': 'model',
        'literal': 'literal',
        'anon': 'anon',
        'uriresource': 'uriresource',
        'stmt_resource': 'stmtResource'
    }
    def __init__(self,
        empty : 'bool' = None,
        head : 'RDFNode' = None,
        strict : 'bool' = None,
        tail : 'RDFList' = None,
        valid : 'bool' = None,
        validity_error_message : 'str' = None,
        id : 'AnonId' = None,
        name_space : 'str' = None,
        stmt_term : 'Statement' = None,
        uri : 'str' = None,
        local_name : 'str' = None,
        resource : 'bool' = None,
        model : 'Model' = None,
        literal : 'bool' = None,
        anon : 'bool' = None,
        uriresource : 'bool' = None,
        stmt_resource : 'bool' = None):  # noqa: E501
        """RDFList - a model defined in Swagger"""  # noqa: E501

        self._empty = None
        self._head = None
        self._strict = None
        self._tail = None
        self._valid = None
        self._validity_error_message = None
        self._id = None
        self._name_space = None
        self._stmt_term = None
        self._uri = None
        self._local_name = None
        self._resource = None
        self._model = None
        self._literal = None
        self._anon = None
        self._uriresource = None
        self._stmt_resource = None
        self.discriminator = None

        if empty is not None:
            self.empty = empty
        if head is not None:
            self.head = head
        if strict is not None:
            self.strict = strict
        if tail is not None:
            self.tail = tail
        if valid is not None:
            self.valid = valid
        if validity_error_message is not None:
            self.validity_error_message = validity_error_message
        if id is not None:
            self.id = id
        if name_space is not None:
            self.name_space = name_space
        if stmt_term is not None:
            self.stmt_term = stmt_term
        if uri is not None:
            self.uri = uri
        if local_name is not None:
            self.local_name = local_name
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
    def empty(self):
        """Gets the empty of this RDFList.  # noqa: E501


        :return: The empty of this RDFList.  # noqa: E501
        :rtype: bool
        """
        return self._empty

    @empty.setter
    def empty(self, empty):
        """Sets the empty of this RDFList.


        :param empty: The empty of this RDFList.  # noqa: E501
        :type: bool
        """

        self._empty = empty

    @property
    def head(self):
        """Gets the head of this RDFList.  # noqa: E501


        :return: The head of this RDFList.  # noqa: E501
        :rtype: RDFNode
        """
        return self._head

    @head.setter
    def head(self, head):
        """Sets the head of this RDFList.


        :param head: The head of this RDFList.  # noqa: E501
        :type: RDFNode
        """

        self._head = head

    @property
    def strict(self):
        """Gets the strict of this RDFList.  # noqa: E501


        :return: The strict of this RDFList.  # noqa: E501
        :rtype: bool
        """
        return self._strict

    @strict.setter
    def strict(self, strict):
        """Sets the strict of this RDFList.


        :param strict: The strict of this RDFList.  # noqa: E501
        :type: bool
        """

        self._strict = strict

    @property
    def tail(self):
        """Gets the tail of this RDFList.  # noqa: E501


        :return: The tail of this RDFList.  # noqa: E501
        :rtype: RDFList
        """
        return self._tail

    @tail.setter
    def tail(self, tail):
        """Sets the tail of this RDFList.


        :param tail: The tail of this RDFList.  # noqa: E501
        :type: RDFList
        """

        self._tail = tail

    @property
    def valid(self):
        """Gets the valid of this RDFList.  # noqa: E501


        :return: The valid of this RDFList.  # noqa: E501
        :rtype: bool
        """
        return self._valid

    @valid.setter
    def valid(self, valid):
        """Sets the valid of this RDFList.


        :param valid: The valid of this RDFList.  # noqa: E501
        :type: bool
        """

        self._valid = valid

    @property
    def validity_error_message(self):
        """Gets the validity_error_message of this RDFList.  # noqa: E501


        :return: The validity_error_message of this RDFList.  # noqa: E501
        :rtype: str
        """
        return self._validity_error_message

    @validity_error_message.setter
    def validity_error_message(self, validity_error_message):
        """Sets the validity_error_message of this RDFList.


        :param validity_error_message: The validity_error_message of this RDFList.  # noqa: E501
        :type: str
        """

        self._validity_error_message = validity_error_message

    @property
    def id(self):
        """Gets the id of this RDFList.  # noqa: E501


        :return: The id of this RDFList.  # noqa: E501
        :rtype: AnonId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RDFList.


        :param id: The id of this RDFList.  # noqa: E501
        :type: AnonId
        """

        self._id = id

    @property
    def name_space(self):
        """Gets the name_space of this RDFList.  # noqa: E501


        :return: The name_space of this RDFList.  # noqa: E501
        :rtype: str
        """
        return self._name_space

    @name_space.setter
    def name_space(self, name_space):
        """Sets the name_space of this RDFList.


        :param name_space: The name_space of this RDFList.  # noqa: E501
        :type: str
        """

        self._name_space = name_space

    @property
    def stmt_term(self):
        """Gets the stmt_term of this RDFList.  # noqa: E501


        :return: The stmt_term of this RDFList.  # noqa: E501
        :rtype: Statement
        """
        return self._stmt_term

    @stmt_term.setter
    def stmt_term(self, stmt_term):
        """Sets the stmt_term of this RDFList.


        :param stmt_term: The stmt_term of this RDFList.  # noqa: E501
        :type: Statement
        """

        self._stmt_term = stmt_term

    @property
    def uri(self):
        """Gets the uri of this RDFList.  # noqa: E501


        :return: The uri of this RDFList.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this RDFList.


        :param uri: The uri of this RDFList.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def local_name(self):
        """Gets the local_name of this RDFList.  # noqa: E501


        :return: The local_name of this RDFList.  # noqa: E501
        :rtype: str
        """
        return self._local_name

    @local_name.setter
    def local_name(self, local_name):
        """Sets the local_name of this RDFList.


        :param local_name: The local_name of this RDFList.  # noqa: E501
        :type: str
        """

        self._local_name = local_name

    @property
    def resource(self):
        """Gets the resource of this RDFList.  # noqa: E501


        :return: The resource of this RDFList.  # noqa: E501
        :rtype: bool
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this RDFList.


        :param resource: The resource of this RDFList.  # noqa: E501
        :type: bool
        """

        self._resource = resource

    @property
    def model(self):
        """Gets the model of this RDFList.  # noqa: E501


        :return: The model of this RDFList.  # noqa: E501
        :rtype: Model
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this RDFList.


        :param model: The model of this RDFList.  # noqa: E501
        :type: Model
        """

        self._model = model

    @property
    def literal(self):
        """Gets the literal of this RDFList.  # noqa: E501


        :return: The literal of this RDFList.  # noqa: E501
        :rtype: bool
        """
        return self._literal

    @literal.setter
    def literal(self, literal):
        """Sets the literal of this RDFList.


        :param literal: The literal of this RDFList.  # noqa: E501
        :type: bool
        """

        self._literal = literal

    @property
    def anon(self):
        """Gets the anon of this RDFList.  # noqa: E501


        :return: The anon of this RDFList.  # noqa: E501
        :rtype: bool
        """
        return self._anon

    @anon.setter
    def anon(self, anon):
        """Sets the anon of this RDFList.


        :param anon: The anon of this RDFList.  # noqa: E501
        :type: bool
        """

        self._anon = anon

    @property
    def uriresource(self):
        """Gets the uriresource of this RDFList.  # noqa: E501


        :return: The uriresource of this RDFList.  # noqa: E501
        :rtype: bool
        """
        return self._uriresource

    @uriresource.setter
    def uriresource(self, uriresource):
        """Sets the uriresource of this RDFList.


        :param uriresource: The uriresource of this RDFList.  # noqa: E501
        :type: bool
        """

        self._uriresource = uriresource

    @property
    def stmt_resource(self):
        """Gets the stmt_resource of this RDFList.  # noqa: E501


        :return: The stmt_resource of this RDFList.  # noqa: E501
        :rtype: bool
        """
        return self._stmt_resource

    @stmt_resource.setter
    def stmt_resource(self, stmt_resource):
        """Sets the stmt_resource of this RDFList.


        :param stmt_resource: The stmt_resource of this RDFList.  # noqa: E501
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
        if issubclass(RDFList, dict):
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
        if not isinstance(other, RDFList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other


from opensilexClientToolsPython.models.rdf_node import RDFNode
from opensilexClientToolsPython.models.anon_id import AnonId
from opensilexClientToolsPython.models.statement import Statement
from opensilexClientToolsPython.models.model import Model


