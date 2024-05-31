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


class Graph(object):
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
        'closed': 'bool',
        'prefix_mapping': 'PrefixMapping',
        'transaction_handler': 'TransactionHandler',
        'event_manager': 'GraphEventManager',
        'capabilities': 'Capabilities'
    }

    attribute_map = {
        'empty': 'empty',
        'closed': 'closed',
        'prefix_mapping': 'prefixMapping',
        'transaction_handler': 'transactionHandler',
        'event_manager': 'eventManager',
        'capabilities': 'capabilities'
    }
    def __init__(self,
        empty : 'bool' = None,
        closed : 'bool' = None,
        prefix_mapping : 'PrefixMapping' = None,
        transaction_handler : 'TransactionHandler' = None,
        event_manager : 'GraphEventManager' = None,
        capabilities : 'Capabilities' = None):  # noqa: E501
        """Graph - a model defined in Swagger"""  # noqa: E501

        self._empty = None
        self._closed = None
        self._prefix_mapping = None
        self._transaction_handler = None
        self._event_manager = None
        self._capabilities = None
        self.discriminator = None

        if empty is not None:
            self.empty = empty
        if closed is not None:
            self.closed = closed
        if prefix_mapping is not None:
            self.prefix_mapping = prefix_mapping
        if transaction_handler is not None:
            self.transaction_handler = transaction_handler
        if event_manager is not None:
            self.event_manager = event_manager
        if capabilities is not None:
            self.capabilities = capabilities

    @property
    def empty(self):
        """Gets the empty of this Graph.  # noqa: E501


        :return: The empty of this Graph.  # noqa: E501
        :rtype: bool
        """
        return self._empty

    @empty.setter
    def empty(self, empty):
        """Sets the empty of this Graph.


        :param empty: The empty of this Graph.  # noqa: E501
        :type: bool
        """

        self._empty = empty

    @property
    def closed(self):
        """Gets the closed of this Graph.  # noqa: E501


        :return: The closed of this Graph.  # noqa: E501
        :rtype: bool
        """
        return self._closed

    @closed.setter
    def closed(self, closed):
        """Sets the closed of this Graph.


        :param closed: The closed of this Graph.  # noqa: E501
        :type: bool
        """

        self._closed = closed

    @property
    def prefix_mapping(self):
        """Gets the prefix_mapping of this Graph.  # noqa: E501


        :return: The prefix_mapping of this Graph.  # noqa: E501
        :rtype: PrefixMapping
        """
        return self._prefix_mapping

    @prefix_mapping.setter
    def prefix_mapping(self, prefix_mapping):
        """Sets the prefix_mapping of this Graph.


        :param prefix_mapping: The prefix_mapping of this Graph.  # noqa: E501
        :type: PrefixMapping
        """

        self._prefix_mapping = prefix_mapping

    @property
    def transaction_handler(self):
        """Gets the transaction_handler of this Graph.  # noqa: E501


        :return: The transaction_handler of this Graph.  # noqa: E501
        :rtype: TransactionHandler
        """
        return self._transaction_handler

    @transaction_handler.setter
    def transaction_handler(self, transaction_handler):
        """Sets the transaction_handler of this Graph.


        :param transaction_handler: The transaction_handler of this Graph.  # noqa: E501
        :type: TransactionHandler
        """

        self._transaction_handler = transaction_handler

    @property
    def event_manager(self):
        """Gets the event_manager of this Graph.  # noqa: E501


        :return: The event_manager of this Graph.  # noqa: E501
        :rtype: GraphEventManager
        """
        return self._event_manager

    @event_manager.setter
    def event_manager(self, event_manager):
        """Sets the event_manager of this Graph.


        :param event_manager: The event_manager of this Graph.  # noqa: E501
        :type: GraphEventManager
        """

        self._event_manager = event_manager

    @property
    def capabilities(self):
        """Gets the capabilities of this Graph.  # noqa: E501


        :return: The capabilities of this Graph.  # noqa: E501
        :rtype: Capabilities
        """
        return self._capabilities

    @capabilities.setter
    def capabilities(self, capabilities):
        """Sets the capabilities of this Graph.


        :param capabilities: The capabilities of this Graph.  # noqa: E501
        :type: Capabilities
        """

        self._capabilities = capabilities

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
        if issubclass(Graph, dict):
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
        if issubclass(Graph, dict):
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
        if not isinstance(other, Graph):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other


from opensilexClientToolsPython.models.prefix_mapping import PrefixMapping
from opensilexClientToolsPython.models.transaction_handler import TransactionHandler
from opensilexClientToolsPython.models.graph_event_manager import GraphEventManager
from opensilexClientToolsPython.models.capabilities import Capabilities


