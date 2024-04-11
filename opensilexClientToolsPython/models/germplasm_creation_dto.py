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


class GermplasmCreationDTO(object):
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
        'synonyms': 'list[str]',
        'code': 'str',
        'production_year': 'int',
        'description': 'str',
        'species': 'str',
        'variety': 'str',
        'accession': 'str',
        'institute': 'str',
        'website': 'str',
        'relations': 'list[RDFObjectRelationDTO]',
        'metadata': 'dict(str, str)',
        'publisher': 'UserGetDTO',
        'publication_date': 'datetime',
        'last_updated_date': 'datetime'
    }

    attribute_map = {
        'uri': 'uri',
        'rdf_type': 'rdf_type',
        'name': 'name',
        'synonyms': 'synonyms',
        'code': 'code',
        'production_year': 'production_year',
        'description': 'description',
        'species': 'species',
        'variety': 'variety',
        'accession': 'accession',
        'institute': 'institute',
        'website': 'website',
        'relations': 'relations',
        'metadata': 'metadata',
        'publisher': 'publisher',
        'publication_date': 'publication_date',
        'last_updated_date': 'last_updated_date'
    }
    def __init__(self,
        rdf_type : 'str',
        name : 'str',
        uri : 'str' = None,
        synonyms : 'List[str]' = None,
        code : 'str' = None,
        production_year : 'int' = None,
        description : 'str' = None,
        species : 'str' = None,
        variety : 'str' = None,
        accession : 'str' = None,
        institute : 'str' = None,
        website : 'str' = None,
        relations : 'List[RDFObjectRelationDTO]' = None,
        metadata : 'Dict[str, str]' = None,
        publisher : 'UserGetDTO' = None,
        publication_date : 'datetime' = None,
        last_updated_date : 'datetime' = None):  # noqa: E501
        """GermplasmCreationDTO - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self._rdf_type = None
        self._name = None
        self._synonyms = None
        self._code = None
        self._production_year = None
        self._description = None
        self._species = None
        self._variety = None
        self._accession = None
        self._institute = None
        self._website = None
        self._relations = None
        self._metadata = None
        self._publisher = None
        self._publication_date = None
        self._last_updated_date = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        self.rdf_type = rdf_type
        self.name = name
        if synonyms is not None:
            self.synonyms = synonyms
        if code is not None:
            self.code = code
        if production_year is not None:
            self.production_year = production_year
        if description is not None:
            self.description = description
        if species is not None:
            self.species = species
        if variety is not None:
            self.variety = variety
        if accession is not None:
            self.accession = accession
        if institute is not None:
            self.institute = institute
        if website is not None:
            self.website = website
        if relations is not None:
            self.relations = relations
        if metadata is not None:
            self.metadata = metadata
        if publisher is not None:
            self.publisher = publisher
        if publication_date is not None:
            self.publication_date = publication_date
        if last_updated_date is not None:
            self.last_updated_date = last_updated_date

    @property
    def uri(self):
        """Gets the uri of this GermplasmCreationDTO.  # noqa: E501

        Germplasm URI  # noqa: E501

        :return: The uri of this GermplasmCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this GermplasmCreationDTO.

        Germplasm URI  # noqa: E501

        :param uri: The uri of this GermplasmCreationDTO.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def rdf_type(self):
        """Gets the rdf_type of this GermplasmCreationDTO.  # noqa: E501

        Germplasm type  # noqa: E501

        :return: The rdf_type of this GermplasmCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._rdf_type

    @rdf_type.setter
    def rdf_type(self, rdf_type):
        """Sets the rdf_type of this GermplasmCreationDTO.

        Germplasm type  # noqa: E501

        :param rdf_type: The rdf_type of this GermplasmCreationDTO.  # noqa: E501
        :type: str
        """
        if rdf_type is None:
            raise ValueError("Invalid value for `rdf_type`, must not be `None`")  # noqa: E501

        self._rdf_type = rdf_type

    @property
    def name(self):
        """Gets the name of this GermplasmCreationDTO.  # noqa: E501

        Germplasm name  # noqa: E501

        :return: The name of this GermplasmCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GermplasmCreationDTO.

        Germplasm name  # noqa: E501

        :param name: The name of this GermplasmCreationDTO.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def synonyms(self):
        """Gets the synonyms of this GermplasmCreationDTO.  # noqa: E501


        :return: The synonyms of this GermplasmCreationDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._synonyms

    @synonyms.setter
    def synonyms(self, synonyms):
        """Sets the synonyms of this GermplasmCreationDTO.


        :param synonyms: The synonyms of this GermplasmCreationDTO.  # noqa: E501
        :type: list[str]
        """

        self._synonyms = synonyms

    @property
    def code(self):
        """Gets the code of this GermplasmCreationDTO.  # noqa: E501

        Germplasm code (accessionNumber, varietyCode...)  # noqa: E501

        :return: The code of this GermplasmCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this GermplasmCreationDTO.

        Germplasm code (accessionNumber, varietyCode...)  # noqa: E501

        :param code: The code of this GermplasmCreationDTO.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def production_year(self):
        """Gets the production_year of this GermplasmCreationDTO.  # noqa: E501

        production year  # noqa: E501

        :return: The production_year of this GermplasmCreationDTO.  # noqa: E501
        :rtype: int
        """
        return self._production_year

    @production_year.setter
    def production_year(self, production_year):
        """Sets the production_year of this GermplasmCreationDTO.

        production year  # noqa: E501

        :param production_year: The production_year of this GermplasmCreationDTO.  # noqa: E501
        :type: int
        """

        self._production_year = production_year

    @property
    def description(self):
        """Gets the description of this GermplasmCreationDTO.  # noqa: E501

        comment  # noqa: E501

        :return: The description of this GermplasmCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GermplasmCreationDTO.

        comment  # noqa: E501

        :param description: The description of this GermplasmCreationDTO.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def species(self):
        """Gets the species of this GermplasmCreationDTO.  # noqa: E501

        species URI  # noqa: E501

        :return: The species of this GermplasmCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._species

    @species.setter
    def species(self, species):
        """Sets the species of this GermplasmCreationDTO.

        species URI  # noqa: E501

        :param species: The species of this GermplasmCreationDTO.  # noqa: E501
        :type: str
        """

        self._species = species

    @property
    def variety(self):
        """Gets the variety of this GermplasmCreationDTO.  # noqa: E501

        variety URI  # noqa: E501

        :return: The variety of this GermplasmCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._variety

    @variety.setter
    def variety(self, variety):
        """Sets the variety of this GermplasmCreationDTO.

        variety URI  # noqa: E501

        :param variety: The variety of this GermplasmCreationDTO.  # noqa: E501
        :type: str
        """

        self._variety = variety

    @property
    def accession(self):
        """Gets the accession of this GermplasmCreationDTO.  # noqa: E501

        accession URI  # noqa: E501

        :return: The accession of this GermplasmCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._accession

    @accession.setter
    def accession(self, accession):
        """Sets the accession of this GermplasmCreationDTO.

        accession URI  # noqa: E501

        :param accession: The accession of this GermplasmCreationDTO.  # noqa: E501
        :type: str
        """

        self._accession = accession

    @property
    def institute(self):
        """Gets the institute of this GermplasmCreationDTO.  # noqa: E501

        institute  # noqa: E501

        :return: The institute of this GermplasmCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._institute

    @institute.setter
    def institute(self, institute):
        """Sets the institute of this GermplasmCreationDTO.

        institute  # noqa: E501

        :param institute: The institute of this GermplasmCreationDTO.  # noqa: E501
        :type: str
        """

        self._institute = institute

    @property
    def website(self):
        """Gets the website of this GermplasmCreationDTO.  # noqa: E501

        website  # noqa: E501

        :return: The website of this GermplasmCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this GermplasmCreationDTO.

        website  # noqa: E501

        :param website: The website of this GermplasmCreationDTO.  # noqa: E501
        :type: str
        """

        self._website = website

    @property
    def relations(self):
        """Gets the relations of this GermplasmCreationDTO.  # noqa: E501


        :return: The relations of this GermplasmCreationDTO.  # noqa: E501
        :rtype: list[RDFObjectRelationDTO]
        """
        return self._relations

    @relations.setter
    def relations(self, relations):
        """Sets the relations of this GermplasmCreationDTO.


        :param relations: The relations of this GermplasmCreationDTO.  # noqa: E501
        :type: list[RDFObjectRelationDTO]
        """

        self._relations = relations

    @property
    def metadata(self):
        """Gets the metadata of this GermplasmCreationDTO.  # noqa: E501


        :return: The metadata of this GermplasmCreationDTO.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this GermplasmCreationDTO.


        :param metadata: The metadata of this GermplasmCreationDTO.  # noqa: E501
        :type: dict(str, str)
        """

        self._metadata = metadata

    @property
    def publisher(self):
        """Gets the publisher of this GermplasmCreationDTO.  # noqa: E501


        :return: The publisher of this GermplasmCreationDTO.  # noqa: E501
        :rtype: UserGetDTO
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        """Sets the publisher of this GermplasmCreationDTO.


        :param publisher: The publisher of this GermplasmCreationDTO.  # noqa: E501
        :type: UserGetDTO
        """

        self._publisher = publisher

    @property
    def publication_date(self):
        """Gets the publication_date of this GermplasmCreationDTO.  # noqa: E501


        :return: The publication_date of this GermplasmCreationDTO.  # noqa: E501
        :rtype: datetime
        """
        return self._publication_date

    @publication_date.setter
    def publication_date(self, publication_date):
        """Sets the publication_date of this GermplasmCreationDTO.


        :param publication_date: The publication_date of this GermplasmCreationDTO.  # noqa: E501
        :type: datetime
        """

        self._publication_date = publication_date

    @property
    def last_updated_date(self):
        """Gets the last_updated_date of this GermplasmCreationDTO.  # noqa: E501


        :return: The last_updated_date of this GermplasmCreationDTO.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated_date

    @last_updated_date.setter
    def last_updated_date(self, last_updated_date):
        """Sets the last_updated_date of this GermplasmCreationDTO.


        :param last_updated_date: The last_updated_date of this GermplasmCreationDTO.  # noqa: E501
        :type: datetime
        """

        self._last_updated_date = last_updated_date

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
        if issubclass(GermplasmCreationDTO, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_api_formated_dict(self):
        """Returns the model properties as a dict"""
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
        if issubclass(GermplasmCreationDTO, dict):
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
        if not isinstance(other, GermplasmCreationDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other


from opensilexClientToolsPython.models.rdf_object_relation_dto import RDFObjectRelationDTO
from opensilexClientToolsPython.models.user_get_dto import UserGetDTO


