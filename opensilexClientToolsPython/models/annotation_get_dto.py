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

from opensilexClientToolsPython.models.motivation_get_dto import MotivationGetDTO



class AnnotationGetDTO(object):
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
        'description': 'str',
        'targets': 'list[str]',
        'motivation': 'MotivationGetDTO',
        'created': 'str',
        'author': 'str'
    }

    attribute_map = {
        'uri': 'uri',
        'description': 'description',
        'targets': 'targets',
        'motivation': 'motivation',
        'created': 'created',
        'author': 'author'
    }
    def __init__(self, uri : 'str' = None, description : 'str' = None, targets : List['str'] = None, motivation : 'MotivationGetDTO' = None, created : 'str' = None, author : 'str' = None):  # noqa: E501
        """AnnotationGetDTO - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self._description = None
        self._targets = None
        self._motivation = None
        self._created = None
        self._author = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if description is not None:
            self.description = description
        if targets is not None:
            self.targets = targets
        if motivation is not None:
            self.motivation = motivation
        if created is not None:
            self.created = created
        if author is not None:
            self.author = author

    @property
    def uri(self):
        """Gets the uri of this AnnotationGetDTO.  # noqa: E501

        Annotation URI  # noqa: E501

        :return: The uri of this AnnotationGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this AnnotationGetDTO.

        Annotation URI  # noqa: E501

        :param uri: The uri of this AnnotationGetDTO.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def description(self):
        """Gets the description of this AnnotationGetDTO.  # noqa: E501

        Content of the annotation  # noqa: E501

        :return: The description of this AnnotationGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AnnotationGetDTO.

        Content of the annotation  # noqa: E501

        :param description: The description of this AnnotationGetDTO.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def targets(self):
        """Gets the targets of this AnnotationGetDTO.  # noqa: E501


        :return: The targets of this AnnotationGetDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        """Sets the targets of this AnnotationGetDTO.


        :param targets: The targets of this AnnotationGetDTO.  # noqa: E501
        :type: list[str]
        """

        self._targets = targets

    @property
    def motivation(self):
        """Gets the motivation of this AnnotationGetDTO.  # noqa: E501


        :return: The motivation of this AnnotationGetDTO.  # noqa: E501
        :rtype: MotivationGetDTO
        """
        return self._motivation

    @motivation.setter
    def motivation(self, motivation):
        """Sets the motivation of this AnnotationGetDTO.


        :param motivation: The motivation of this AnnotationGetDTO.  # noqa: E501
        :type: MotivationGetDTO
        """

        self._motivation = motivation

    @property
    def created(self):
        """Gets the created of this AnnotationGetDTO.  # noqa: E501

        Creation date  # noqa: E501

        :return: The created of this AnnotationGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this AnnotationGetDTO.

        Creation date  # noqa: E501

        :param created: The created of this AnnotationGetDTO.  # noqa: E501
        :type: str
        """

        self._created = created

    @property
    def author(self):
        """Gets the author of this AnnotationGetDTO.  # noqa: E501

        Annotation author URI  # noqa: E501

        :return: The author of this AnnotationGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this AnnotationGetDTO.

        Annotation author URI  # noqa: E501

        :param author: The author of this AnnotationGetDTO.  # noqa: E501
        :type: str
        """

        self._author = author

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
        if issubclass(AnnotationGetDTO, dict):
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
        if not isinstance(other, AnnotationGetDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

