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

from opensilexClientToolsPython.models.rdf_object_relation_dto import RDFObjectRelationDTO
from opensilexClientToolsPython.models.geo_json_object import GeoJsonObject



class ScientificObjectUpdateDTO(object):
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
        'experiment': 'str',
        'relations': 'list[RDFObjectRelationDTO]',
        'geometry': 'GeoJsonObject'
    }

    attribute_map = {
        'uri': 'uri',
        'rdf_type': 'rdf_type',
        'name': 'name',
        'experiment': 'experiment',
        'relations': 'relations',
        'geometry': 'geometry'
    }
    def __init__(self, uri : 'str' = None, rdf_type : 'str' = None, name : 'str' = None, experiment : 'str' = None, relations : List['RDFObjectRelationDTO'] = None, geometry : 'GeoJsonObject' = None):  # noqa: E501
        """ScientificObjectUpdateDTO - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self._rdf_type = None
        self._name = None
        self._experiment = None
        self._relations = None
        self._geometry = None
        self.discriminator = None

        self.uri = uri
        self.rdf_type = rdf_type
        self.name = name
        if experiment is not None:
            self.experiment = experiment
        if relations is not None:
            self.relations = relations
        if geometry is not None:
            self.geometry = geometry

    @property
    def uri(self):
        """Gets the uri of this ScientificObjectUpdateDTO.  # noqa: E501

        Scientific object URI  # noqa: E501

        :return: The uri of this ScientificObjectUpdateDTO.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this ScientificObjectUpdateDTO.

        Scientific object URI  # noqa: E501

        :param uri: The uri of this ScientificObjectUpdateDTO.  # noqa: E501
        :type: str
        """
        if uri is None:
            raise ValueError("Invalid value for `uri`, must not be `None`")  # noqa: E501

        self._uri = uri

    @property
    def rdf_type(self):
        """Gets the rdf_type of this ScientificObjectUpdateDTO.  # noqa: E501

        Scientific object type  # noqa: E501

        :return: The rdf_type of this ScientificObjectUpdateDTO.  # noqa: E501
        :rtype: str
        """
        return self._rdf_type

    @rdf_type.setter
    def rdf_type(self, rdf_type):
        """Sets the rdf_type of this ScientificObjectUpdateDTO.

        Scientific object type  # noqa: E501

        :param rdf_type: The rdf_type of this ScientificObjectUpdateDTO.  # noqa: E501
        :type: str
        """
        if rdf_type is None:
            raise ValueError("Invalid value for `rdf_type`, must not be `None`")  # noqa: E501

        self._rdf_type = rdf_type

    @property
    def name(self):
        """Gets the name of this ScientificObjectUpdateDTO.  # noqa: E501

        Scientific object name  # noqa: E501

        :return: The name of this ScientificObjectUpdateDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ScientificObjectUpdateDTO.

        Scientific object name  # noqa: E501

        :param name: The name of this ScientificObjectUpdateDTO.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def experiment(self):
        """Gets the experiment of this ScientificObjectUpdateDTO.  # noqa: E501

        Scientific object experiment URI  # noqa: E501

        :return: The experiment of this ScientificObjectUpdateDTO.  # noqa: E501
        :rtype: str
        """
        return self._experiment

    @experiment.setter
    def experiment(self, experiment):
        """Sets the experiment of this ScientificObjectUpdateDTO.

        Scientific object experiment URI  # noqa: E501

        :param experiment: The experiment of this ScientificObjectUpdateDTO.  # noqa: E501
        :type: str
        """

        self._experiment = experiment

    @property
    def relations(self):
        """Gets the relations of this ScientificObjectUpdateDTO.  # noqa: E501


        :return: The relations of this ScientificObjectUpdateDTO.  # noqa: E501
        :rtype: list[RDFObjectRelationDTO]
        """
        return self._relations

    @relations.setter
    def relations(self, relations):
        """Sets the relations of this ScientificObjectUpdateDTO.


        :param relations: The relations of this ScientificObjectUpdateDTO.  # noqa: E501
        :type: list[RDFObjectRelationDTO]
        """

        self._relations = relations

    @property
    def geometry(self):
        """Gets the geometry of this ScientificObjectUpdateDTO.  # noqa: E501

        The geographical coordinates of the Geospatial  # noqa: E501

        :return: The geometry of this ScientificObjectUpdateDTO.  # noqa: E501
        :rtype: GeoJsonObject
        """
        return self._geometry

    @geometry.setter
    def geometry(self, geometry):
        """Sets the geometry of this ScientificObjectUpdateDTO.

        The geographical coordinates of the Geospatial  # noqa: E501

        :param geometry: The geometry of this ScientificObjectUpdateDTO.  # noqa: E501
        :type: GeoJsonObject
        """

        self._geometry = geometry

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
        if issubclass(ScientificObjectUpdateDTO, dict):
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
        if not isinstance(other, ScientificObjectUpdateDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

