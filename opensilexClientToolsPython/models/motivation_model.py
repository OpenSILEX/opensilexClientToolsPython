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


class MotivationModel(object):
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
        'publisher': 'str',
        'publication_date': 'datetime',
        'last_update_date': 'datetime',
        'creator': 'str',
        'relations': 'list[SPARQLModelRelation]',
        'name': 'str',
        'type': 'str',
        'type_label': 'SPARQLLabel'
    }

    attribute_map = {
        'uri': 'uri',
        'publisher': 'publisher',
        'publication_date': 'publicationDate',
        'last_update_date': 'lastUpdateDate',
        'creator': 'creator',
        'relations': 'relations',
        'name': 'name',
        'type': 'type',
        'type_label': 'typeLabel'
    }
    def __init__(self,
        uri : 'str' = None,
        publisher : 'str' = None,
        publication_date : 'datetime' = None,
        last_update_date : 'datetime' = None,
        creator : 'str' = None,
        relations : 'List[SPARQLModelRelation]' = None,
        name : 'str' = None,
        type : 'str' = None,
        type_label : 'SPARQLLabel' = None):  # noqa: E501
        """MotivationModel - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self._publisher = None
        self._publication_date = None
        self._last_update_date = None
        self._creator = None
        self._relations = None
        self._name = None
        self._type = None
        self._type_label = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if publisher is not None:
            self.publisher = publisher
        if publication_date is not None:
            self.publication_date = publication_date
        if last_update_date is not None:
            self.last_update_date = last_update_date
        if creator is not None:
            self.creator = creator
        if relations is not None:
            self.relations = relations
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if type_label is not None:
            self.type_label = type_label

    @property
    def uri(self):
        """Gets the uri of this MotivationModel.  # noqa: E501


        :return: The uri of this MotivationModel.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this MotivationModel.


        :param uri: The uri of this MotivationModel.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def publisher(self):
        """Gets the publisher of this MotivationModel.  # noqa: E501


        :return: The publisher of this MotivationModel.  # noqa: E501
        :rtype: str
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        """Sets the publisher of this MotivationModel.


        :param publisher: The publisher of this MotivationModel.  # noqa: E501
        :type: str
        """

        self._publisher = publisher

    @property
    def publication_date(self):
        """Gets the publication_date of this MotivationModel.  # noqa: E501


        :return: The publication_date of this MotivationModel.  # noqa: E501
        :rtype: datetime
        """
        return self._publication_date

    @publication_date.setter
    def publication_date(self, publication_date):
        """Sets the publication_date of this MotivationModel.


        :param publication_date: The publication_date of this MotivationModel.  # noqa: E501
        :type: datetime
        """

        self._publication_date = publication_date

    @property
    def last_update_date(self):
        """Gets the last_update_date of this MotivationModel.  # noqa: E501


        :return: The last_update_date of this MotivationModel.  # noqa: E501
        :rtype: datetime
        """
        return self._last_update_date

    @last_update_date.setter
    def last_update_date(self, last_update_date):
        """Sets the last_update_date of this MotivationModel.


        :param last_update_date: The last_update_date of this MotivationModel.  # noqa: E501
        :type: datetime
        """

        self._last_update_date = last_update_date

    @property
    def creator(self):
        """Gets the creator of this MotivationModel.  # noqa: E501


        :return: The creator of this MotivationModel.  # noqa: E501
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this MotivationModel.


        :param creator: The creator of this MotivationModel.  # noqa: E501
        :type: str
        """

        self._creator = creator

    @property
    def relations(self):
        """Gets the relations of this MotivationModel.  # noqa: E501


        :return: The relations of this MotivationModel.  # noqa: E501
        :rtype: list[SPARQLModelRelation]
        """
        return self._relations

    @relations.setter
    def relations(self, relations):
        """Sets the relations of this MotivationModel.


        :param relations: The relations of this MotivationModel.  # noqa: E501
        :type: list[SPARQLModelRelation]
        """

        self._relations = relations

    @property
    def name(self):
        """Gets the name of this MotivationModel.  # noqa: E501


        :return: The name of this MotivationModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MotivationModel.


        :param name: The name of this MotivationModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this MotivationModel.  # noqa: E501


        :return: The type of this MotivationModel.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MotivationModel.


        :param type: The type of this MotivationModel.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def type_label(self):
        """Gets the type_label of this MotivationModel.  # noqa: E501


        :return: The type_label of this MotivationModel.  # noqa: E501
        :rtype: SPARQLLabel
        """
        return self._type_label

    @type_label.setter
    def type_label(self, type_label):
        """Sets the type_label of this MotivationModel.


        :param type_label: The type_label of this MotivationModel.  # noqa: E501
        :type: SPARQLLabel
        """

        self._type_label = type_label

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
        if issubclass(MotivationModel, dict):
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
        if not isinstance(other, MotivationModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other


from opensilexClientToolsPython.models.sparql_model_relation import SPARQLModelRelation
from opensilexClientToolsPython.models.sparql_label import SPARQLLabel


