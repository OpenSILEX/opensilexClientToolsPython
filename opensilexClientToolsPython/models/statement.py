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


class Statement(object):
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
        'object': 'RDFNode',
        'boolean': 'bool',
        'byte': 'str',
        'short': 'int',
        'char': 'str',
        '_int': 'int',
        'long': 'int',
        '_float': 'float',
        'double': 'float',
        'resource': 'Resource',
        'language': 'str',
        'string': 'str',
        'list': 'RDFList',
        'model': 'Model',
        'subject': 'Resource',
        'literal': 'Literal',
        'predicate': 'ModelProperty',
        'bag': 'Bag',
        'alt': 'Alt',
        'seq': 'Seq',
        'reified': 'bool'
    }

    attribute_map = {
        'object': 'object',
        'boolean': 'boolean',
        'byte': 'byte',
        'short': 'short',
        'char': 'char',
        '_int': 'int',
        'long': 'long',
        '_float': 'float',
        'double': 'double',
        'resource': 'resource',
        'language': 'language',
        'string': 'string',
        'list': 'list',
        'model': 'model',
        'subject': 'subject',
        'literal': 'literal',
        'predicate': 'predicate',
        'bag': 'bag',
        'alt': 'alt',
        'seq': 'seq',
        'reified': 'reified'
    }
    def __init__(self,
        object : 'RDFNode' = None,
        boolean : 'bool' = None,
        byte : 'str' = None,
        short : 'int' = None,
        char : 'str' = None,
        _int : 'int' = None,
        long : 'int' = None,
        _float : 'float' = None,
        double : 'float' = None,
        resource : 'Resource' = None,
        language : 'str' = None,
        string : 'str' = None,
        list : 'RDFList' = None,
        model : 'Model' = None,
        subject : 'Resource' = None,
        literal : 'Literal' = None,
        predicate : 'ModelProperty' = None,
        bag : 'Bag' = None,
        alt : 'Alt' = None,
        seq : 'Seq' = None,
        reified : 'bool' = None):  # noqa: E501
        """Statement - a model defined in Swagger"""  # noqa: E501

        self._object = None
        self._boolean = None
        self._byte = None
        self._short = None
        self._char = None
        self.__int = None
        self._long = None
        self.__float = None
        self._double = None
        self._resource = None
        self._language = None
        self._string = None
        self._list = None
        self._model = None
        self._subject = None
        self._literal = None
        self._predicate = None
        self._bag = None
        self._alt = None
        self._seq = None
        self._reified = None
        self.discriminator = None

        if object is not None:
            self.object = object
        if boolean is not None:
            self.boolean = boolean
        if byte is not None:
            self.byte = byte
        if short is not None:
            self.short = short
        if char is not None:
            self.char = char
        if _int is not None:
            self._int = _int
        if long is not None:
            self.long = long
        if _float is not None:
            self._float = _float
        if double is not None:
            self.double = double
        if resource is not None:
            self.resource = resource
        if language is not None:
            self.language = language
        if string is not None:
            self.string = string
        if list is not None:
            self.list = list
        if model is not None:
            self.model = model
        if subject is not None:
            self.subject = subject
        if literal is not None:
            self.literal = literal
        if predicate is not None:
            self.predicate = predicate
        if bag is not None:
            self.bag = bag
        if alt is not None:
            self.alt = alt
        if seq is not None:
            self.seq = seq
        if reified is not None:
            self.reified = reified

    @property
    def object(self):
        """Gets the object of this Statement.  # noqa: E501


        :return: The object of this Statement.  # noqa: E501
        :rtype: RDFNode
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this Statement.


        :param object: The object of this Statement.  # noqa: E501
        :type: RDFNode
        """

        self._object = object

    @property
    def boolean(self):
        """Gets the boolean of this Statement.  # noqa: E501


        :return: The boolean of this Statement.  # noqa: E501
        :rtype: bool
        """
        return self._boolean

    @boolean.setter
    def boolean(self, boolean):
        """Sets the boolean of this Statement.


        :param boolean: The boolean of this Statement.  # noqa: E501
        :type: bool
        """

        self._boolean = boolean

    @property
    def byte(self):
        """Gets the byte of this Statement.  # noqa: E501


        :return: The byte of this Statement.  # noqa: E501
        :rtype: str
        """
        return self._byte

    @byte.setter
    def byte(self, byte):
        """Sets the byte of this Statement.


        :param byte: The byte of this Statement.  # noqa: E501
        :type: str
        """
        if byte is not None and not re.search(r'^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', byte):  # noqa: E501
            raise ValueError(r"Invalid value for `byte`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._byte = byte

    @property
    def short(self):
        """Gets the short of this Statement.  # noqa: E501


        :return: The short of this Statement.  # noqa: E501
        :rtype: int
        """
        return self._short

    @short.setter
    def short(self, short):
        """Sets the short of this Statement.


        :param short: The short of this Statement.  # noqa: E501
        :type: int
        """

        self._short = short

    @property
    def char(self):
        """Gets the char of this Statement.  # noqa: E501


        :return: The char of this Statement.  # noqa: E501
        :rtype: str
        """
        return self._char

    @char.setter
    def char(self, char):
        """Sets the char of this Statement.


        :param char: The char of this Statement.  # noqa: E501
        :type: str
        """

        self._char = char

    @property
    def _int(self):
        """Gets the _int of this Statement.  # noqa: E501


        :return: The _int of this Statement.  # noqa: E501
        :rtype: int
        """
        return self.__int

    @_int.setter
    def _int(self, _int):
        """Sets the _int of this Statement.


        :param _int: The _int of this Statement.  # noqa: E501
        :type: int
        """

        self.__int = _int

    @property
    def long(self):
        """Gets the long of this Statement.  # noqa: E501


        :return: The long of this Statement.  # noqa: E501
        :rtype: int
        """
        return self._long

    @long.setter
    def long(self, long):
        """Sets the long of this Statement.


        :param long: The long of this Statement.  # noqa: E501
        :type: int
        """

        self._long = long

    @property
    def _float(self):
        """Gets the _float of this Statement.  # noqa: E501


        :return: The _float of this Statement.  # noqa: E501
        :rtype: float
        """
        return self.__float

    @_float.setter
    def _float(self, _float):
        """Sets the _float of this Statement.


        :param _float: The _float of this Statement.  # noqa: E501
        :type: float
        """

        self.__float = _float

    @property
    def double(self):
        """Gets the double of this Statement.  # noqa: E501


        :return: The double of this Statement.  # noqa: E501
        :rtype: float
        """
        return self._double

    @double.setter
    def double(self, double):
        """Sets the double of this Statement.


        :param double: The double of this Statement.  # noqa: E501
        :type: float
        """

        self._double = double

    @property
    def resource(self):
        """Gets the resource of this Statement.  # noqa: E501


        :return: The resource of this Statement.  # noqa: E501
        :rtype: Resource
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this Statement.


        :param resource: The resource of this Statement.  # noqa: E501
        :type: Resource
        """

        self._resource = resource

    @property
    def language(self):
        """Gets the language of this Statement.  # noqa: E501


        :return: The language of this Statement.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this Statement.


        :param language: The language of this Statement.  # noqa: E501
        :type: str
        """

        self._language = language

    @property
    def string(self):
        """Gets the string of this Statement.  # noqa: E501


        :return: The string of this Statement.  # noqa: E501
        :rtype: str
        """
        return self._string

    @string.setter
    def string(self, string):
        """Sets the string of this Statement.


        :param string: The string of this Statement.  # noqa: E501
        :type: str
        """

        self._string = string

    @property
    def list(self):
        """Gets the list of this Statement.  # noqa: E501


        :return: The list of this Statement.  # noqa: E501
        :rtype: RDFList
        """
        return self._list

    @list.setter
    def list(self, list):
        """Sets the list of this Statement.


        :param list: The list of this Statement.  # noqa: E501
        :type: RDFList
        """

        self._list = list

    @property
    def model(self):
        """Gets the model of this Statement.  # noqa: E501


        :return: The model of this Statement.  # noqa: E501
        :rtype: Model
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this Statement.


        :param model: The model of this Statement.  # noqa: E501
        :type: Model
        """

        self._model = model

    @property
    def subject(self):
        """Gets the subject of this Statement.  # noqa: E501


        :return: The subject of this Statement.  # noqa: E501
        :rtype: Resource
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this Statement.


        :param subject: The subject of this Statement.  # noqa: E501
        :type: Resource
        """

        self._subject = subject

    @property
    def literal(self):
        """Gets the literal of this Statement.  # noqa: E501


        :return: The literal of this Statement.  # noqa: E501
        :rtype: Literal
        """
        return self._literal

    @literal.setter
    def literal(self, literal):
        """Sets the literal of this Statement.


        :param literal: The literal of this Statement.  # noqa: E501
        :type: Literal
        """

        self._literal = literal

    @property
    def predicate(self):
        """Gets the predicate of this Statement.  # noqa: E501


        :return: The predicate of this Statement.  # noqa: E501
        :rtype: ModelProperty
        """
        return self._predicate

    @predicate.setter
    def predicate(self, predicate):
        """Sets the predicate of this Statement.


        :param predicate: The predicate of this Statement.  # noqa: E501
        :type: ModelProperty
        """

        self._predicate = predicate

    @property
    def bag(self):
        """Gets the bag of this Statement.  # noqa: E501


        :return: The bag of this Statement.  # noqa: E501
        :rtype: Bag
        """
        return self._bag

    @bag.setter
    def bag(self, bag):
        """Sets the bag of this Statement.


        :param bag: The bag of this Statement.  # noqa: E501
        :type: Bag
        """

        self._bag = bag

    @property
    def alt(self):
        """Gets the alt of this Statement.  # noqa: E501


        :return: The alt of this Statement.  # noqa: E501
        :rtype: Alt
        """
        return self._alt

    @alt.setter
    def alt(self, alt):
        """Sets the alt of this Statement.


        :param alt: The alt of this Statement.  # noqa: E501
        :type: Alt
        """

        self._alt = alt

    @property
    def seq(self):
        """Gets the seq of this Statement.  # noqa: E501


        :return: The seq of this Statement.  # noqa: E501
        :rtype: Seq
        """
        return self._seq

    @seq.setter
    def seq(self, seq):
        """Sets the seq of this Statement.


        :param seq: The seq of this Statement.  # noqa: E501
        :type: Seq
        """

        self._seq = seq

    @property
    def reified(self):
        """Gets the reified of this Statement.  # noqa: E501


        :return: The reified of this Statement.  # noqa: E501
        :rtype: bool
        """
        return self._reified

    @reified.setter
    def reified(self, reified):
        """Sets the reified of this Statement.


        :param reified: The reified of this Statement.  # noqa: E501
        :type: bool
        """

        self._reified = reified

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
        if issubclass(Statement, dict):
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
        if not isinstance(other, Statement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other


from opensilexClientToolsPython.models.rdf_node import RDFNode
from opensilexClientToolsPython.models.resource import Resource
from opensilexClientToolsPython.models.rdf_list import RDFList
from opensilexClientToolsPython.models.model import Model
from opensilexClientToolsPython.models.resource import Resource
from opensilexClientToolsPython.models.literal import Literal
from opensilexClientToolsPython.models.model_property import ModelProperty
from opensilexClientToolsPython.models.bag import Bag
from opensilexClientToolsPython.models.alt import Alt
from opensilexClientToolsPython.models.seq import Seq


