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


class VueRDFTypeDTO(object):
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
        'comment': 'str',
        'parent': 'str',
        'icon': 'str',
        'name_translations': 'dict(str, str)',
        'comment_translations': 'dict(str, str)',
        'is_abstract': 'bool',
        'data_properties': 'list[VueRDFTypePropertyDTO]',
        'object_properties': 'list[VueRDFTypePropertyDTO]',
        'properties_order': 'list[str]'
    }

    attribute_map = {
        'uri': 'uri',
        'name': 'name',
        'comment': 'comment',
        'parent': 'parent',
        'icon': 'icon',
        'name_translations': 'name_translations',
        'comment_translations': 'comment_translations',
        'is_abstract': 'is_abstract',
        'data_properties': 'data_properties',
        'object_properties': 'object_properties',
        'properties_order': 'properties_order'
    }

    def __init__(self, uri=None, name=None, comment=None, parent=None, icon=None, name_translations=None, comment_translations=None, is_abstract=None, data_properties=None, object_properties=None, properties_order=None):  # noqa: E501
        """VueRDFTypeDTO - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self._name = None
        self._comment = None
        self._parent = None
        self._icon = None
        self._name_translations = None
        self._comment_translations = None
        self._is_abstract = None
        self._data_properties = None
        self._object_properties = None
        self._properties_order = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if name is not None:
            self.name = name
        if comment is not None:
            self.comment = comment
        if parent is not None:
            self.parent = parent
        if icon is not None:
            self.icon = icon
        if name_translations is not None:
            self.name_translations = name_translations
        if comment_translations is not None:
            self.comment_translations = comment_translations
        if is_abstract is not None:
            self.is_abstract = is_abstract
        if data_properties is not None:
            self.data_properties = data_properties
        if object_properties is not None:
            self.object_properties = object_properties
        if properties_order is not None:
            self.properties_order = properties_order

    @property
    def uri(self):
        """Gets the uri of this VueRDFTypeDTO.  # noqa: E501


        :return: The uri of this VueRDFTypeDTO.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this VueRDFTypeDTO.


        :param uri: The uri of this VueRDFTypeDTO.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def name(self):
        """Gets the name of this VueRDFTypeDTO.  # noqa: E501


        :return: The name of this VueRDFTypeDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VueRDFTypeDTO.


        :param name: The name of this VueRDFTypeDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def comment(self):
        """Gets the comment of this VueRDFTypeDTO.  # noqa: E501


        :return: The comment of this VueRDFTypeDTO.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this VueRDFTypeDTO.


        :param comment: The comment of this VueRDFTypeDTO.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def parent(self):
        """Gets the parent of this VueRDFTypeDTO.  # noqa: E501


        :return: The parent of this VueRDFTypeDTO.  # noqa: E501
        :rtype: str
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this VueRDFTypeDTO.


        :param parent: The parent of this VueRDFTypeDTO.  # noqa: E501
        :type: str
        """

        self._parent = parent

    @property
    def icon(self):
        """Gets the icon of this VueRDFTypeDTO.  # noqa: E501


        :return: The icon of this VueRDFTypeDTO.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this VueRDFTypeDTO.


        :param icon: The icon of this VueRDFTypeDTO.  # noqa: E501
        :type: str
        """

        self._icon = icon

    @property
    def name_translations(self):
        """Gets the name_translations of this VueRDFTypeDTO.  # noqa: E501


        :return: The name_translations of this VueRDFTypeDTO.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._name_translations

    @name_translations.setter
    def name_translations(self, name_translations):
        """Sets the name_translations of this VueRDFTypeDTO.


        :param name_translations: The name_translations of this VueRDFTypeDTO.  # noqa: E501
        :type: dict(str, str)
        """

        self._name_translations = name_translations

    @property
    def comment_translations(self):
        """Gets the comment_translations of this VueRDFTypeDTO.  # noqa: E501


        :return: The comment_translations of this VueRDFTypeDTO.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._comment_translations

    @comment_translations.setter
    def comment_translations(self, comment_translations):
        """Sets the comment_translations of this VueRDFTypeDTO.


        :param comment_translations: The comment_translations of this VueRDFTypeDTO.  # noqa: E501
        :type: dict(str, str)
        """

        self._comment_translations = comment_translations

    @property
    def is_abstract(self):
        """Gets the is_abstract of this VueRDFTypeDTO.  # noqa: E501


        :return: The is_abstract of this VueRDFTypeDTO.  # noqa: E501
        :rtype: bool
        """
        return self._is_abstract

    @is_abstract.setter
    def is_abstract(self, is_abstract):
        """Sets the is_abstract of this VueRDFTypeDTO.


        :param is_abstract: The is_abstract of this VueRDFTypeDTO.  # noqa: E501
        :type: bool
        """

        self._is_abstract = is_abstract

    @property
    def data_properties(self):
        """Gets the data_properties of this VueRDFTypeDTO.  # noqa: E501


        :return: The data_properties of this VueRDFTypeDTO.  # noqa: E501
        :rtype: list[VueRDFTypePropertyDTO]
        """
        return self._data_properties

    @data_properties.setter
    def data_properties(self, data_properties):
        """Sets the data_properties of this VueRDFTypeDTO.


        :param data_properties: The data_properties of this VueRDFTypeDTO.  # noqa: E501
        :type: list[VueRDFTypePropertyDTO]
        """

        self._data_properties = data_properties

    @property
    def object_properties(self):
        """Gets the object_properties of this VueRDFTypeDTO.  # noqa: E501


        :return: The object_properties of this VueRDFTypeDTO.  # noqa: E501
        :rtype: list[VueRDFTypePropertyDTO]
        """
        return self._object_properties

    @object_properties.setter
    def object_properties(self, object_properties):
        """Sets the object_properties of this VueRDFTypeDTO.


        :param object_properties: The object_properties of this VueRDFTypeDTO.  # noqa: E501
        :type: list[VueRDFTypePropertyDTO]
        """

        self._object_properties = object_properties

    @property
    def properties_order(self):
        """Gets the properties_order of this VueRDFTypeDTO.  # noqa: E501


        :return: The properties_order of this VueRDFTypeDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._properties_order

    @properties_order.setter
    def properties_order(self, properties_order):
        """Sets the properties_order of this VueRDFTypeDTO.


        :param properties_order: The properties_order of this VueRDFTypeDTO.  # noqa: E501
        :type: list[str]
        """

        self._properties_order = properties_order

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
        if issubclass(VueRDFTypeDTO, dict):
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
        if not isinstance(other, VueRDFTypeDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
