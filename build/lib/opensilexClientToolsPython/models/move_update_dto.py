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


class MoveUpdateDTO(object):
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
        'start': 'str',
        'end': 'str',
        'is_instant': 'bool',
        'description': 'str',
        'targets': 'list[str]',
        'relations': 'list[RDFObjectRelationDTO]',
        '_from': 'str',
        'to': 'str',
        'targets_positions': 'list[TargetPositionCreationDTO]'
    }

    attribute_map = {
        'uri': 'uri',
        'rdf_type': 'rdf_type',
        'start': 'start',
        'end': 'end',
        'is_instant': 'is_instant',
        'description': 'description',
        'targets': 'targets',
        'relations': 'relations',
        '_from': 'from',
        'to': 'to',
        'targets_positions': 'targets_positions'
    }

    def __init__(self, uri=None, rdf_type=None, start=None, end=None, is_instant=None, description=None, targets=None, relations=None, _from=None, to=None, targets_positions=None):  # noqa: E501
        """MoveUpdateDTO - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self._rdf_type = None
        self._start = None
        self._end = None
        self._is_instant = None
        self._description = None
        self._targets = None
        self._relations = None
        self.__from = None
        self._to = None
        self._targets_positions = None
        self.discriminator = None

        self.uri = uri
        if rdf_type is not None:
            self.rdf_type = rdf_type
        if start is not None:
            self.start = start
        if end is not None:
            self.end = end
        self.is_instant = is_instant
        if description is not None:
            self.description = description
        self.targets = targets
        if relations is not None:
            self.relations = relations
        if _from is not None:
            self._from = _from
        if to is not None:
            self.to = to
        if targets_positions is not None:
            self.targets_positions = targets_positions

    @property
    def uri(self):
        """Gets the uri of this MoveUpdateDTO.  # noqa: E501


        :return: The uri of this MoveUpdateDTO.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this MoveUpdateDTO.


        :param uri: The uri of this MoveUpdateDTO.  # noqa: E501
        :type: str
        """
        if uri is None:
            raise ValueError("Invalid value for `uri`, must not be `None`")  # noqa: E501

        self._uri = uri

    @property
    def rdf_type(self):
        """Gets the rdf_type of this MoveUpdateDTO.  # noqa: E501

        Event type URI  # noqa: E501

        :return: The rdf_type of this MoveUpdateDTO.  # noqa: E501
        :rtype: str
        """
        return self._rdf_type

    @rdf_type.setter
    def rdf_type(self, rdf_type):
        """Sets the rdf_type of this MoveUpdateDTO.

        Event type URI  # noqa: E501

        :param rdf_type: The rdf_type of this MoveUpdateDTO.  # noqa: E501
        :type: str
        """

        self._rdf_type = rdf_type

    @property
    def start(self):
        """Gets the start of this MoveUpdateDTO.  # noqa: E501


        :return: The start of this MoveUpdateDTO.  # noqa: E501
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this MoveUpdateDTO.


        :param start: The start of this MoveUpdateDTO.  # noqa: E501
        :type: str
        """

        self._start = start

    @property
    def end(self):
        """Gets the end of this MoveUpdateDTO.  # noqa: E501


        :return: The end of this MoveUpdateDTO.  # noqa: E501
        :rtype: str
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this MoveUpdateDTO.


        :param end: The end of this MoveUpdateDTO.  # noqa: E501
        :type: str
        """

        self._end = end

    @property
    def is_instant(self):
        """Gets the is_instant of this MoveUpdateDTO.  # noqa: E501

        Indicate if the event is instant  # noqa: E501

        :return: The is_instant of this MoveUpdateDTO.  # noqa: E501
        :rtype: bool
        """
        return self._is_instant

    @is_instant.setter
    def is_instant(self, is_instant):
        """Sets the is_instant of this MoveUpdateDTO.

        Indicate if the event is instant  # noqa: E501

        :param is_instant: The is_instant of this MoveUpdateDTO.  # noqa: E501
        :type: bool
        """
        if is_instant is None:
            raise ValueError("Invalid value for `is_instant`, must not be `None`")  # noqa: E501

        self._is_instant = is_instant

    @property
    def description(self):
        """Gets the description of this MoveUpdateDTO.  # noqa: E501


        :return: The description of this MoveUpdateDTO.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MoveUpdateDTO.


        :param description: The description of this MoveUpdateDTO.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def targets(self):
        """Gets the targets of this MoveUpdateDTO.  # noqa: E501

        URI(s) of items concerned by this event  # noqa: E501

        :return: The targets of this MoveUpdateDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        """Sets the targets of this MoveUpdateDTO.

        URI(s) of items concerned by this event  # noqa: E501

        :param targets: The targets of this MoveUpdateDTO.  # noqa: E501
        :type: list[str]
        """
        if targets is None:
            raise ValueError("Invalid value for `targets`, must not be `None`")  # noqa: E501

        self._targets = targets

    @property
    def relations(self):
        """Gets the relations of this MoveUpdateDTO.  # noqa: E501


        :return: The relations of this MoveUpdateDTO.  # noqa: E501
        :rtype: list[RDFObjectRelationDTO]
        """
        return self._relations

    @relations.setter
    def relations(self, relations):
        """Sets the relations of this MoveUpdateDTO.


        :param relations: The relations of this MoveUpdateDTO.  # noqa: E501
        :type: list[RDFObjectRelationDTO]
        """

        self._relations = relations

    @property
    def _from(self):
        """Gets the _from of this MoveUpdateDTO.  # noqa: E501


        :return: The _from of this MoveUpdateDTO.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this MoveUpdateDTO.


        :param _from: The _from of this MoveUpdateDTO.  # noqa: E501
        :type: str
        """

        self.__from = _from

    @property
    def to(self):
        """Gets the to of this MoveUpdateDTO.  # noqa: E501


        :return: The to of this MoveUpdateDTO.  # noqa: E501
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this MoveUpdateDTO.


        :param to: The to of this MoveUpdateDTO.  # noqa: E501
        :type: str
        """

        self._to = to

    @property
    def targets_positions(self):
        """Gets the targets_positions of this MoveUpdateDTO.  # noqa: E501


        :return: The targets_positions of this MoveUpdateDTO.  # noqa: E501
        :rtype: list[TargetPositionCreationDTO]
        """
        return self._targets_positions

    @targets_positions.setter
    def targets_positions(self, targets_positions):
        """Sets the targets_positions of this MoveUpdateDTO.


        :param targets_positions: The targets_positions of this MoveUpdateDTO.  # noqa: E501
        :type: list[TargetPositionCreationDTO]
        """

        self._targets_positions = targets_positions

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
        if issubclass(MoveUpdateDTO, dict):
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
        if not isinstance(other, MoveUpdateDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
