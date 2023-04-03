# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0-rc+7.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from typing import List, Dict

from opensilexClientToolsPython.models.season import Season



class ObservationSummary(object):
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
        'collector': 'str',
        'observation_db_id': 'str',
        'observation_time_stamp': 'str',
        'observation_variable_db_id': 'str',
        'observation_variable_name': 'str',
        'season': 'Season'
    }

    attribute_map = {
        'collector': 'collector',
        'observation_db_id': 'observationDbId',
        'observation_time_stamp': 'observationTimeStamp',
        'observation_variable_db_id': 'observationVariableDbId',
        'observation_variable_name': 'observationVariableName',
        'season': 'season'
    }
    def __init__(self,
        collector : 'str' = None,
        observation_db_id : 'str' = None,
        observation_time_stamp : 'str' = None,
        observation_variable_db_id : 'str' = None,
        observation_variable_name : 'str' = None,
        season : 'Season' = None):  # noqa: E501
        """ObservationSummary - a model defined in Swagger"""  # noqa: E501

        self._collector = None
        self._observation_db_id = None
        self._observation_time_stamp = None
        self._observation_variable_db_id = None
        self._observation_variable_name = None
        self._season = None
        self.discriminator = None

        if collector is not None:
            self.collector = collector
        if observation_db_id is not None:
            self.observation_db_id = observation_db_id
        if observation_time_stamp is not None:
            self.observation_time_stamp = observation_time_stamp
        if observation_variable_db_id is not None:
            self.observation_variable_db_id = observation_variable_db_id
        if observation_variable_name is not None:
            self.observation_variable_name = observation_variable_name
        if season is not None:
            self.season = season

    @property
    def collector(self):
        """Gets the collector of this ObservationSummary.  # noqa: E501


        :return: The collector of this ObservationSummary.  # noqa: E501
        :rtype: str
        """
        return self._collector

    @collector.setter
    def collector(self, collector):
        """Sets the collector of this ObservationSummary.


        :param collector: The collector of this ObservationSummary.  # noqa: E501
        :type: str
        """

        self._collector = collector

    @property
    def observation_db_id(self):
        """Gets the observation_db_id of this ObservationSummary.  # noqa: E501


        :return: The observation_db_id of this ObservationSummary.  # noqa: E501
        :rtype: str
        """
        return self._observation_db_id

    @observation_db_id.setter
    def observation_db_id(self, observation_db_id):
        """Sets the observation_db_id of this ObservationSummary.


        :param observation_db_id: The observation_db_id of this ObservationSummary.  # noqa: E501
        :type: str
        """

        self._observation_db_id = observation_db_id

    @property
    def observation_time_stamp(self):
        """Gets the observation_time_stamp of this ObservationSummary.  # noqa: E501


        :return: The observation_time_stamp of this ObservationSummary.  # noqa: E501
        :rtype: str
        """
        return self._observation_time_stamp

    @observation_time_stamp.setter
    def observation_time_stamp(self, observation_time_stamp):
        """Sets the observation_time_stamp of this ObservationSummary.


        :param observation_time_stamp: The observation_time_stamp of this ObservationSummary.  # noqa: E501
        :type: str
        """

        self._observation_time_stamp = observation_time_stamp

    @property
    def observation_variable_db_id(self):
        """Gets the observation_variable_db_id of this ObservationSummary.  # noqa: E501


        :return: The observation_variable_db_id of this ObservationSummary.  # noqa: E501
        :rtype: str
        """
        return self._observation_variable_db_id

    @observation_variable_db_id.setter
    def observation_variable_db_id(self, observation_variable_db_id):
        """Sets the observation_variable_db_id of this ObservationSummary.


        :param observation_variable_db_id: The observation_variable_db_id of this ObservationSummary.  # noqa: E501
        :type: str
        """

        self._observation_variable_db_id = observation_variable_db_id

    @property
    def observation_variable_name(self):
        """Gets the observation_variable_name of this ObservationSummary.  # noqa: E501


        :return: The observation_variable_name of this ObservationSummary.  # noqa: E501
        :rtype: str
        """
        return self._observation_variable_name

    @observation_variable_name.setter
    def observation_variable_name(self, observation_variable_name):
        """Sets the observation_variable_name of this ObservationSummary.


        :param observation_variable_name: The observation_variable_name of this ObservationSummary.  # noqa: E501
        :type: str
        """

        self._observation_variable_name = observation_variable_name

    @property
    def season(self):
        """Gets the season of this ObservationSummary.  # noqa: E501


        :return: The season of this ObservationSummary.  # noqa: E501
        :rtype: Season
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this ObservationSummary.


        :param season: The season of this ObservationSummary.  # noqa: E501
        :type: Season
        """

        self._season = season

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
        if issubclass(ObservationSummary, dict):
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
        if not isinstance(other, ObservationSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

