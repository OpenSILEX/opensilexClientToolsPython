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




class ActivityCreationDTO(object):
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
        'rdf_type': 'str',
        'uri': 'str',
        'start_date': 'str',
        'end_date': 'str',
        'timezone': 'str',
        'settings': 'dict(str, object)'
    }

    attribute_map = {
        'rdf_type': 'rdf_type',
        'uri': 'uri',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'timezone': 'timezone',
        'settings': 'settings'
    }
    def __init__(self,
        rdf_type : 'str' = None,
        uri : 'str' = None,
        start_date : 'str' = None,
        end_date : 'str' = None,
        timezone : 'str' = None,
        settings : 'Dict[str, object]' = None):  # noqa: E501
        """ActivityCreationDTO - a model defined in Swagger"""  # noqa: E501

        self._rdf_type = None
        self._uri = None
        self._start_date = None
        self._end_date = None
        self._timezone = None
        self._settings = None
        self.discriminator = None

        if rdf_type is not None:
            self.rdf_type = rdf_type
        if uri is not None:
            self.uri = uri
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if timezone is not None:
            self.timezone = timezone
        if settings is not None:
            self.settings = settings

    @property
    def rdf_type(self):
        """Gets the rdf_type of this ActivityCreationDTO.  # noqa: E501

        activity type defined in the ontology  # noqa: E501

        :return: The rdf_type of this ActivityCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._rdf_type

    @rdf_type.setter
    def rdf_type(self, rdf_type):
        """Sets the rdf_type of this ActivityCreationDTO.

        activity type defined in the ontology  # noqa: E501

        :param rdf_type: The rdf_type of this ActivityCreationDTO.  # noqa: E501
        :type: str
        """

        self._rdf_type = rdf_type

    @property
    def uri(self):
        """Gets the uri of this ActivityCreationDTO.  # noqa: E501

        external uri of the activity or process  # noqa: E501

        :return: The uri of this ActivityCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this ActivityCreationDTO.

        external uri of the activity or process  # noqa: E501

        :param uri: The uri of this ActivityCreationDTO.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def start_date(self):
        """Gets the start_date of this ActivityCreationDTO.  # noqa: E501

        start date or datetime  # noqa: E501

        :return: The start_date of this ActivityCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ActivityCreationDTO.

        start date or datetime  # noqa: E501

        :param start_date: The start_date of this ActivityCreationDTO.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this ActivityCreationDTO.  # noqa: E501

        end date or datetime  # noqa: E501

        :return: The end_date of this ActivityCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ActivityCreationDTO.

        end date or datetime  # noqa: E501

        :param end_date: The end_date of this ActivityCreationDTO.  # noqa: E501
        :type: str
        """

        self._end_date = end_date

    @property
    def timezone(self):
        """Gets the timezone of this ActivityCreationDTO.  # noqa: E501

        to specify if the offset is not in the dates and if the timezone is different from the default one  # noqa: E501

        :return: The timezone of this ActivityCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this ActivityCreationDTO.

        to specify if the offset is not in the dates and if the timezone is different from the default one  # noqa: E501

        :param timezone: The timezone of this ActivityCreationDTO.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def settings(self):
        """Gets the settings of this ActivityCreationDTO.  # noqa: E501

        a key-value system to store process parameters  # noqa: E501

        :return: The settings of this ActivityCreationDTO.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this ActivityCreationDTO.

        a key-value system to store process parameters  # noqa: E501

        :param settings: The settings of this ActivityCreationDTO.  # noqa: E501
        :type: dict(str, object)
        """

        self._settings = settings

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
        if issubclass(ActivityCreationDTO, dict):
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
        if not isinstance(other, ActivityCreationDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

