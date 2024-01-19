# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.2.0-rdg
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from typing import List, Dict


class Model(object):
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
        'lock': 'Lock',
        'reader': 'RDFReaderI',
        'writer': 'RDFWriterI',
        'graph': 'Graph',
        'ns_prefix_map': 'dict(str, str)'
    }

    attribute_map = {
        'empty': 'empty',
        'closed': 'closed',
        'lock': 'lock',
        'reader': 'reader',
        'writer': 'writer',
        'graph': 'graph',
        'ns_prefix_map': 'nsPrefixMap'
    }
    def __init__(self,
        empty : 'bool' = None,
        closed : 'bool' = None,
        lock : 'Lock' = None,
        reader : 'RDFReaderI' = None,
        writer : 'RDFWriterI' = None,
        graph : 'Graph' = None,
        ns_prefix_map : 'Dict[str, str]' = None):  # noqa: E501
        """Model - a model defined in Swagger"""  # noqa: E501

        self._empty = None
        self._closed = None
        self._lock = None
        self._reader = None
        self._writer = None
        self._graph = None
        self._ns_prefix_map = None
        self.discriminator = None

        if empty is not None:
            self.empty = empty
        if closed is not None:
            self.closed = closed
        if lock is not None:
            self.lock = lock
        if reader is not None:
            self.reader = reader
        if writer is not None:
            self.writer = writer
        if graph is not None:
            self.graph = graph
        if ns_prefix_map is not None:
            self.ns_prefix_map = ns_prefix_map

    @property
    def empty(self):
        """Gets the empty of this Model.  # noqa: E501


        :return: The empty of this Model.  # noqa: E501
        :rtype: bool
        """
        return self._empty

    @empty.setter
    def empty(self, empty):
        """Sets the empty of this Model.


        :param empty: The empty of this Model.  # noqa: E501
        :type: bool
        """

        self._empty = empty

    @property
    def closed(self):
        """Gets the closed of this Model.  # noqa: E501


        :return: The closed of this Model.  # noqa: E501
        :rtype: bool
        """
        return self._closed

    @closed.setter
    def closed(self, closed):
        """Sets the closed of this Model.


        :param closed: The closed of this Model.  # noqa: E501
        :type: bool
        """

        self._closed = closed

    @property
    def lock(self):
        """Gets the lock of this Model.  # noqa: E501


        :return: The lock of this Model.  # noqa: E501
        :rtype: Lock
        """
        return self._lock

    @lock.setter
    def lock(self, lock):
        """Sets the lock of this Model.


        :param lock: The lock of this Model.  # noqa: E501
        :type: Lock
        """

        self._lock = lock

    @property
    def reader(self):
        """Gets the reader of this Model.  # noqa: E501


        :return: The reader of this Model.  # noqa: E501
        :rtype: RDFReaderI
        """
        return self._reader

    @reader.setter
    def reader(self, reader):
        """Sets the reader of this Model.


        :param reader: The reader of this Model.  # noqa: E501
        :type: RDFReaderI
        """

        self._reader = reader

    @property
    def writer(self):
        """Gets the writer of this Model.  # noqa: E501


        :return: The writer of this Model.  # noqa: E501
        :rtype: RDFWriterI
        """
        return self._writer

    @writer.setter
    def writer(self, writer):
        """Sets the writer of this Model.


        :param writer: The writer of this Model.  # noqa: E501
        :type: RDFWriterI
        """

        self._writer = writer

    @property
    def graph(self):
        """Gets the graph of this Model.  # noqa: E501


        :return: The graph of this Model.  # noqa: E501
        :rtype: Graph
        """
        return self._graph

    @graph.setter
    def graph(self, graph):
        """Sets the graph of this Model.


        :param graph: The graph of this Model.  # noqa: E501
        :type: Graph
        """

        self._graph = graph

    @property
    def ns_prefix_map(self):
        """Gets the ns_prefix_map of this Model.  # noqa: E501


        :return: The ns_prefix_map of this Model.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._ns_prefix_map

    @ns_prefix_map.setter
    def ns_prefix_map(self, ns_prefix_map):
        """Sets the ns_prefix_map of this Model.


        :param ns_prefix_map: The ns_prefix_map of this Model.  # noqa: E501
        :type: dict(str, str)
        """

        self._ns_prefix_map = ns_prefix_map

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
        if issubclass(Model, dict):
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
        if not isinstance(other, Model):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other


from opensilexClientToolsPython.models.lock import Lock
from opensilexClientToolsPython.models.rdf_reader_i import RDFReaderI
from opensilexClientToolsPython.models.rdf_writer_i import RDFWriterI
from opensilexClientToolsPython.models.graph import Graph


