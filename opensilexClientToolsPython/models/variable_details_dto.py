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


class VariableDetailsDTO(object):
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
        'alternative_name': 'str',
        'description': 'str',
        'entity': 'EntityGetDTO',
        'entity_of_interest': 'InterestEntityGetDTO',
        'characteristic': 'CharacteristicGetDTO',
        'trait': 'str',
        'trait_name': 'str',
        'method': 'MethodGetDTO',
        'unit': 'UnitDetailsDTO',
        'species': 'list[SpeciesDTO]',
        'time_interval': 'str',
        'sampling_interval': 'str',
        'datatype': 'str',
        'exact_match': 'list[str]',
        'close_match': 'list[str]',
        'broad_match': 'list[str]',
        'narrow_match': 'list[str]',
        'publisher': 'UserGetDTO',
        'publication_date': 'datetime',
        'last_updated_date': 'datetime',
        'from_shared_resource_instance': 'SharedResourceInstanceDTO'
    }

    attribute_map = {
        'uri': 'uri',
        'name': 'name',
        'alternative_name': 'alternative_name',
        'description': 'description',
        'entity': 'entity',
        'entity_of_interest': 'entity_of_interest',
        'characteristic': 'characteristic',
        'trait': 'trait',
        'trait_name': 'trait_name',
        'method': 'method',
        'unit': 'unit',
        'species': 'species',
        'time_interval': 'time_interval',
        'sampling_interval': 'sampling_interval',
        'datatype': 'datatype',
        'exact_match': 'exact_match',
        'close_match': 'close_match',
        'broad_match': 'broad_match',
        'narrow_match': 'narrow_match',
        'publisher': 'publisher',
        'publication_date': 'publication_date',
        'last_updated_date': 'last_updated_date',
        'from_shared_resource_instance': 'from_shared_resource_instance'
    }
    def __init__(self,
        uri : 'str' = None,
        name : 'str' = None,
        alternative_name : 'str' = None,
        description : 'str' = None,
        entity : 'EntityGetDTO' = None,
        entity_of_interest : 'InterestEntityGetDTO' = None,
        characteristic : 'CharacteristicGetDTO' = None,
        trait : 'str' = None,
        trait_name : 'str' = None,
        method : 'MethodGetDTO' = None,
        unit : 'UnitDetailsDTO' = None,
        species : 'List[SpeciesDTO]' = None,
        time_interval : 'str' = None,
        sampling_interval : 'str' = None,
        datatype : 'str' = None,
        exact_match : 'List[str]' = None,
        close_match : 'List[str]' = None,
        broad_match : 'List[str]' = None,
        narrow_match : 'List[str]' = None,
        publisher : 'UserGetDTO' = None,
        publication_date : 'datetime' = None,
        last_updated_date : 'datetime' = None,
        from_shared_resource_instance : 'SharedResourceInstanceDTO' = None):  # noqa: E501
        """VariableDetailsDTO - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self._name = None
        self._alternative_name = None
        self._description = None
        self._entity = None
        self._entity_of_interest = None
        self._characteristic = None
        self._trait = None
        self._trait_name = None
        self._method = None
        self._unit = None
        self._species = None
        self._time_interval = None
        self._sampling_interval = None
        self._datatype = None
        self._exact_match = None
        self._close_match = None
        self._broad_match = None
        self._narrow_match = None
        self._publisher = None
        self._publication_date = None
        self._last_updated_date = None
        self._from_shared_resource_instance = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if name is not None:
            self.name = name
        if alternative_name is not None:
            self.alternative_name = alternative_name
        if description is not None:
            self.description = description
        if entity is not None:
            self.entity = entity
        if entity_of_interest is not None:
            self.entity_of_interest = entity_of_interest
        if characteristic is not None:
            self.characteristic = characteristic
        if trait is not None:
            self.trait = trait
        if trait_name is not None:
            self.trait_name = trait_name
        if method is not None:
            self.method = method
        if unit is not None:
            self.unit = unit
        if species is not None:
            self.species = species
        if time_interval is not None:
            self.time_interval = time_interval
        if sampling_interval is not None:
            self.sampling_interval = sampling_interval
        if datatype is not None:
            self.datatype = datatype
        if exact_match is not None:
            self.exact_match = exact_match
        if close_match is not None:
            self.close_match = close_match
        if broad_match is not None:
            self.broad_match = broad_match
        if narrow_match is not None:
            self.narrow_match = narrow_match
        if publisher is not None:
            self.publisher = publisher
        if publication_date is not None:
            self.publication_date = publication_date
        if last_updated_date is not None:
            self.last_updated_date = last_updated_date
        if from_shared_resource_instance is not None:
            self.from_shared_resource_instance = from_shared_resource_instance

    @property
    def uri(self):
        """Gets the uri of this VariableDetailsDTO.  # noqa: E501


        :return: The uri of this VariableDetailsDTO.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this VariableDetailsDTO.


        :param uri: The uri of this VariableDetailsDTO.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def name(self):
        """Gets the name of this VariableDetailsDTO.  # noqa: E501


        :return: The name of this VariableDetailsDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VariableDetailsDTO.


        :param name: The name of this VariableDetailsDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def alternative_name(self):
        """Gets the alternative_name of this VariableDetailsDTO.  # noqa: E501


        :return: The alternative_name of this VariableDetailsDTO.  # noqa: E501
        :rtype: str
        """
        return self._alternative_name

    @alternative_name.setter
    def alternative_name(self, alternative_name):
        """Sets the alternative_name of this VariableDetailsDTO.


        :param alternative_name: The alternative_name of this VariableDetailsDTO.  # noqa: E501
        :type: str
        """

        self._alternative_name = alternative_name

    @property
    def description(self):
        """Gets the description of this VariableDetailsDTO.  # noqa: E501


        :return: The description of this VariableDetailsDTO.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VariableDetailsDTO.


        :param description: The description of this VariableDetailsDTO.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def entity(self):
        """Gets the entity of this VariableDetailsDTO.  # noqa: E501


        :return: The entity of this VariableDetailsDTO.  # noqa: E501
        :rtype: EntityGetDTO
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """Sets the entity of this VariableDetailsDTO.


        :param entity: The entity of this VariableDetailsDTO.  # noqa: E501
        :type: EntityGetDTO
        """

        self._entity = entity

    @property
    def entity_of_interest(self):
        """Gets the entity_of_interest of this VariableDetailsDTO.  # noqa: E501


        :return: The entity_of_interest of this VariableDetailsDTO.  # noqa: E501
        :rtype: InterestEntityGetDTO
        """
        return self._entity_of_interest

    @entity_of_interest.setter
    def entity_of_interest(self, entity_of_interest):
        """Sets the entity_of_interest of this VariableDetailsDTO.


        :param entity_of_interest: The entity_of_interest of this VariableDetailsDTO.  # noqa: E501
        :type: InterestEntityGetDTO
        """

        self._entity_of_interest = entity_of_interest

    @property
    def characteristic(self):
        """Gets the characteristic of this VariableDetailsDTO.  # noqa: E501


        :return: The characteristic of this VariableDetailsDTO.  # noqa: E501
        :rtype: CharacteristicGetDTO
        """
        return self._characteristic

    @characteristic.setter
    def characteristic(self, characteristic):
        """Sets the characteristic of this VariableDetailsDTO.


        :param characteristic: The characteristic of this VariableDetailsDTO.  # noqa: E501
        :type: CharacteristicGetDTO
        """

        self._characteristic = characteristic

    @property
    def trait(self):
        """Gets the trait of this VariableDetailsDTO.  # noqa: E501


        :return: The trait of this VariableDetailsDTO.  # noqa: E501
        :rtype: str
        """
        return self._trait

    @trait.setter
    def trait(self, trait):
        """Sets the trait of this VariableDetailsDTO.


        :param trait: The trait of this VariableDetailsDTO.  # noqa: E501
        :type: str
        """

        self._trait = trait

    @property
    def trait_name(self):
        """Gets the trait_name of this VariableDetailsDTO.  # noqa: E501


        :return: The trait_name of this VariableDetailsDTO.  # noqa: E501
        :rtype: str
        """
        return self._trait_name

    @trait_name.setter
    def trait_name(self, trait_name):
        """Sets the trait_name of this VariableDetailsDTO.


        :param trait_name: The trait_name of this VariableDetailsDTO.  # noqa: E501
        :type: str
        """

        self._trait_name = trait_name

    @property
    def method(self):
        """Gets the method of this VariableDetailsDTO.  # noqa: E501


        :return: The method of this VariableDetailsDTO.  # noqa: E501
        :rtype: MethodGetDTO
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this VariableDetailsDTO.


        :param method: The method of this VariableDetailsDTO.  # noqa: E501
        :type: MethodGetDTO
        """

        self._method = method

    @property
    def unit(self):
        """Gets the unit of this VariableDetailsDTO.  # noqa: E501


        :return: The unit of this VariableDetailsDTO.  # noqa: E501
        :rtype: UnitDetailsDTO
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this VariableDetailsDTO.


        :param unit: The unit of this VariableDetailsDTO.  # noqa: E501
        :type: UnitDetailsDTO
        """

        self._unit = unit

    @property
    def species(self):
        """Gets the species of this VariableDetailsDTO.  # noqa: E501


        :return: The species of this VariableDetailsDTO.  # noqa: E501
        :rtype: list[SpeciesDTO]
        """
        return self._species

    @species.setter
    def species(self, species):
        """Sets the species of this VariableDetailsDTO.


        :param species: The species of this VariableDetailsDTO.  # noqa: E501
        :type: list[SpeciesDTO]
        """

        self._species = species

    @property
    def time_interval(self):
        """Gets the time_interval of this VariableDetailsDTO.  # noqa: E501


        :return: The time_interval of this VariableDetailsDTO.  # noqa: E501
        :rtype: str
        """
        return self._time_interval

    @time_interval.setter
    def time_interval(self, time_interval):
        """Sets the time_interval of this VariableDetailsDTO.


        :param time_interval: The time_interval of this VariableDetailsDTO.  # noqa: E501
        :type: str
        """

        self._time_interval = time_interval

    @property
    def sampling_interval(self):
        """Gets the sampling_interval of this VariableDetailsDTO.  # noqa: E501


        :return: The sampling_interval of this VariableDetailsDTO.  # noqa: E501
        :rtype: str
        """
        return self._sampling_interval

    @sampling_interval.setter
    def sampling_interval(self, sampling_interval):
        """Sets the sampling_interval of this VariableDetailsDTO.


        :param sampling_interval: The sampling_interval of this VariableDetailsDTO.  # noqa: E501
        :type: str
        """

        self._sampling_interval = sampling_interval

    @property
    def datatype(self):
        """Gets the datatype of this VariableDetailsDTO.  # noqa: E501


        :return: The datatype of this VariableDetailsDTO.  # noqa: E501
        :rtype: str
        """
        return self._datatype

    @datatype.setter
    def datatype(self, datatype):
        """Sets the datatype of this VariableDetailsDTO.


        :param datatype: The datatype of this VariableDetailsDTO.  # noqa: E501
        :type: str
        """

        self._datatype = datatype

    @property
    def exact_match(self):
        """Gets the exact_match of this VariableDetailsDTO.  # noqa: E501


        :return: The exact_match of this VariableDetailsDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._exact_match

    @exact_match.setter
    def exact_match(self, exact_match):
        """Sets the exact_match of this VariableDetailsDTO.


        :param exact_match: The exact_match of this VariableDetailsDTO.  # noqa: E501
        :type: list[str]
        """

        self._exact_match = exact_match

    @property
    def close_match(self):
        """Gets the close_match of this VariableDetailsDTO.  # noqa: E501


        :return: The close_match of this VariableDetailsDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._close_match

    @close_match.setter
    def close_match(self, close_match):
        """Sets the close_match of this VariableDetailsDTO.


        :param close_match: The close_match of this VariableDetailsDTO.  # noqa: E501
        :type: list[str]
        """

        self._close_match = close_match

    @property
    def broad_match(self):
        """Gets the broad_match of this VariableDetailsDTO.  # noqa: E501


        :return: The broad_match of this VariableDetailsDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._broad_match

    @broad_match.setter
    def broad_match(self, broad_match):
        """Sets the broad_match of this VariableDetailsDTO.


        :param broad_match: The broad_match of this VariableDetailsDTO.  # noqa: E501
        :type: list[str]
        """

        self._broad_match = broad_match

    @property
    def narrow_match(self):
        """Gets the narrow_match of this VariableDetailsDTO.  # noqa: E501


        :return: The narrow_match of this VariableDetailsDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._narrow_match

    @narrow_match.setter
    def narrow_match(self, narrow_match):
        """Sets the narrow_match of this VariableDetailsDTO.


        :param narrow_match: The narrow_match of this VariableDetailsDTO.  # noqa: E501
        :type: list[str]
        """

        self._narrow_match = narrow_match

    @property
    def publisher(self):
        """Gets the publisher of this VariableDetailsDTO.  # noqa: E501


        :return: The publisher of this VariableDetailsDTO.  # noqa: E501
        :rtype: UserGetDTO
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        """Sets the publisher of this VariableDetailsDTO.


        :param publisher: The publisher of this VariableDetailsDTO.  # noqa: E501
        :type: UserGetDTO
        """

        self._publisher = publisher

    @property
    def publication_date(self):
        """Gets the publication_date of this VariableDetailsDTO.  # noqa: E501


        :return: The publication_date of this VariableDetailsDTO.  # noqa: E501
        :rtype: datetime
        """
        return self._publication_date

    @publication_date.setter
    def publication_date(self, publication_date):
        """Sets the publication_date of this VariableDetailsDTO.


        :param publication_date: The publication_date of this VariableDetailsDTO.  # noqa: E501
        :type: datetime
        """

        self._publication_date = publication_date

    @property
    def last_updated_date(self):
        """Gets the last_updated_date of this VariableDetailsDTO.  # noqa: E501


        :return: The last_updated_date of this VariableDetailsDTO.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated_date

    @last_updated_date.setter
    def last_updated_date(self, last_updated_date):
        """Sets the last_updated_date of this VariableDetailsDTO.


        :param last_updated_date: The last_updated_date of this VariableDetailsDTO.  # noqa: E501
        :type: datetime
        """

        self._last_updated_date = last_updated_date

    @property
    def from_shared_resource_instance(self):
        """Gets the from_shared_resource_instance of this VariableDetailsDTO.  # noqa: E501


        :return: The from_shared_resource_instance of this VariableDetailsDTO.  # noqa: E501
        :rtype: SharedResourceInstanceDTO
        """
        return self._from_shared_resource_instance

    @from_shared_resource_instance.setter
    def from_shared_resource_instance(self, from_shared_resource_instance):
        """Sets the from_shared_resource_instance of this VariableDetailsDTO.


        :param from_shared_resource_instance: The from_shared_resource_instance of this VariableDetailsDTO.  # noqa: E501
        :type: SharedResourceInstanceDTO
        """

        self._from_shared_resource_instance = from_shared_resource_instance

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
        if issubclass(VariableDetailsDTO, dict):
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
        if not isinstance(other, VariableDetailsDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other


from opensilexClientToolsPython.models.entity_get_dto import EntityGetDTO
from opensilexClientToolsPython.models.interest_entity_get_dto import InterestEntityGetDTO
from opensilexClientToolsPython.models.characteristic_get_dto import CharacteristicGetDTO
from opensilexClientToolsPython.models.method_get_dto import MethodGetDTO
from opensilexClientToolsPython.models.unit_details_dto import UnitDetailsDTO
from opensilexClientToolsPython.models.species_dto import SpeciesDTO
from opensilexClientToolsPython.models.user_get_dto import UserGetDTO
from opensilexClientToolsPython.models.shared_resource_instance_dto import SharedResourceInstanceDTO


