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




class GermplasmDTO(object):
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
        'accession_number': 'str',
        'acquisition_date': 'str',
        'additional_info': 'str',
        'biological_status_of_accession_code': 'str',
        'biological_status_of_accession_description': 'str',
        'breeding_method_db_id': 'str',
        'collection': 'str',
        'common_crop_name': 'str',
        'country_of_origin_code': 'str',
        'default_display_name': 'str',
        'documentation_url': 'str',
        'donors': 'list[object]',
        'external_references': 'list[object]',
        'genus': 'str',
        'germplasm_db_id': 'str',
        'germplasm_name': 'str',
        'germplasm_origin': 'list[object]',
        'germplasm_preprocessing': 'str',
        'institute_code': 'str',
        'institute_name': 'str',
        'pedigree': 'str',
        'seed_source': 'str',
        'seed_source_description': 'str',
        'species': 'str',
        'species_authority': 'str',
        'storage_types': 'list[object]',
        'subtaxa': 'str',
        'subtaxa_authority': 'str',
        'synonyms': 'list[object]',
        'taxon_ids': 'list[object]'
    }

    attribute_map = {
        'accession_number': 'accessionNumber',
        'acquisition_date': 'acquisitionDate',
        'additional_info': 'additionalInfo',
        'biological_status_of_accession_code': 'biologicalStatusOfAccessionCode',
        'biological_status_of_accession_description': 'biologicalStatusOfAccessionDescription',
        'breeding_method_db_id': 'breedingMethodDbId',
        'collection': 'collection',
        'common_crop_name': 'commonCropName',
        'country_of_origin_code': 'countryOfOriginCode',
        'default_display_name': 'defaultDisplayName',
        'documentation_url': 'documentationURL',
        'donors': 'donors',
        'external_references': 'externalReferences',
        'genus': 'genus',
        'germplasm_db_id': 'germplasmDbId',
        'germplasm_name': 'germplasmName',
        'germplasm_origin': 'germplasmOrigin',
        'germplasm_preprocessing': 'germplasmPreprocessing',
        'institute_code': 'instituteCode',
        'institute_name': 'instituteName',
        'pedigree': 'pedigree',
        'seed_source': 'seedSource',
        'seed_source_description': 'seedSourceDescription',
        'species': 'species',
        'species_authority': 'speciesAuthority',
        'storage_types': 'storageTypes',
        'subtaxa': 'subtaxa',
        'subtaxa_authority': 'subtaxaAuthority',
        'synonyms': 'synonyms',
        'taxon_ids': 'taxonIds'
    }
    def __init__(self,
        accession_number : 'str' = None,
        acquisition_date : 'str' = None,
        additional_info : 'str' = None,
        biological_status_of_accession_code : 'str' = None,
        biological_status_of_accession_description : 'str' = None,
        breeding_method_db_id : 'str' = None,
        collection : 'str' = None,
        common_crop_name : 'str' = None,
        country_of_origin_code : 'str' = None,
        default_display_name : 'str' = None,
        documentation_url : 'str' = None,
        donors : 'List[object]' = None,
        external_references : 'List[object]' = None,
        genus : 'str' = None,
        germplasm_db_id : 'str' = None,
        germplasm_name : 'str' = None,
        germplasm_origin : 'List[object]' = None,
        germplasm_preprocessing : 'str' = None,
        institute_code : 'str' = None,
        institute_name : 'str' = None,
        pedigree : 'str' = None,
        seed_source : 'str' = None,
        seed_source_description : 'str' = None,
        species : 'str' = None,
        species_authority : 'str' = None,
        storage_types : 'List[object]' = None,
        subtaxa : 'str' = None,
        subtaxa_authority : 'str' = None,
        synonyms : 'List[object]' = None,
        taxon_ids : 'List[object]' = None):  # noqa: E501
        """GermplasmDTO - a model defined in Swagger"""  # noqa: E501

        self._accession_number = None
        self._acquisition_date = None
        self._additional_info = None
        self._biological_status_of_accession_code = None
        self._biological_status_of_accession_description = None
        self._breeding_method_db_id = None
        self._collection = None
        self._common_crop_name = None
        self._country_of_origin_code = None
        self._default_display_name = None
        self._documentation_url = None
        self._donors = None
        self._external_references = None
        self._genus = None
        self._germplasm_db_id = None
        self._germplasm_name = None
        self._germplasm_origin = None
        self._germplasm_preprocessing = None
        self._institute_code = None
        self._institute_name = None
        self._pedigree = None
        self._seed_source = None
        self._seed_source_description = None
        self._species = None
        self._species_authority = None
        self._storage_types = None
        self._subtaxa = None
        self._subtaxa_authority = None
        self._synonyms = None
        self._taxon_ids = None
        self.discriminator = None

        if accession_number is not None:
            self.accession_number = accession_number
        if acquisition_date is not None:
            self.acquisition_date = acquisition_date
        if additional_info is not None:
            self.additional_info = additional_info
        if biological_status_of_accession_code is not None:
            self.biological_status_of_accession_code = biological_status_of_accession_code
        if biological_status_of_accession_description is not None:
            self.biological_status_of_accession_description = biological_status_of_accession_description
        if breeding_method_db_id is not None:
            self.breeding_method_db_id = breeding_method_db_id
        if collection is not None:
            self.collection = collection
        if common_crop_name is not None:
            self.common_crop_name = common_crop_name
        if country_of_origin_code is not None:
            self.country_of_origin_code = country_of_origin_code
        if default_display_name is not None:
            self.default_display_name = default_display_name
        if documentation_url is not None:
            self.documentation_url = documentation_url
        if donors is not None:
            self.donors = donors
        if external_references is not None:
            self.external_references = external_references
        if genus is not None:
            self.genus = genus
        if germplasm_db_id is not None:
            self.germplasm_db_id = germplasm_db_id
        if germplasm_name is not None:
            self.germplasm_name = germplasm_name
        if germplasm_origin is not None:
            self.germplasm_origin = germplasm_origin
        if germplasm_preprocessing is not None:
            self.germplasm_preprocessing = germplasm_preprocessing
        if institute_code is not None:
            self.institute_code = institute_code
        if institute_name is not None:
            self.institute_name = institute_name
        if pedigree is not None:
            self.pedigree = pedigree
        if seed_source is not None:
            self.seed_source = seed_source
        if seed_source_description is not None:
            self.seed_source_description = seed_source_description
        if species is not None:
            self.species = species
        if species_authority is not None:
            self.species_authority = species_authority
        if storage_types is not None:
            self.storage_types = storage_types
        if subtaxa is not None:
            self.subtaxa = subtaxa
        if subtaxa_authority is not None:
            self.subtaxa_authority = subtaxa_authority
        if synonyms is not None:
            self.synonyms = synonyms
        if taxon_ids is not None:
            self.taxon_ids = taxon_ids

    @property
    def accession_number(self):
        """Gets the accession_number of this GermplasmDTO.  # noqa: E501


        :return: The accession_number of this GermplasmDTO.  # noqa: E501
        :rtype: str
        """
        return self._accession_number

    @accession_number.setter
    def accession_number(self, accession_number):
        """Sets the accession_number of this GermplasmDTO.


        :param accession_number: The accession_number of this GermplasmDTO.  # noqa: E501
        :type: str
        """

        self._accession_number = accession_number

    @property
    def acquisition_date(self):
        """Gets the acquisition_date of this GermplasmDTO.  # noqa: E501


        :return: The acquisition_date of this GermplasmDTO.  # noqa: E501
        :rtype: str
        """
        return self._acquisition_date

    @acquisition_date.setter
    def acquisition_date(self, acquisition_date):
        """Sets the acquisition_date of this GermplasmDTO.


        :param acquisition_date: The acquisition_date of this GermplasmDTO.  # noqa: E501
        :type: str
        """

        self._acquisition_date = acquisition_date

    @property
    def additional_info(self):
        """Gets the additional_info of this GermplasmDTO.  # noqa: E501


        :return: The additional_info of this GermplasmDTO.  # noqa: E501
        :rtype: str
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this GermplasmDTO.


        :param additional_info: The additional_info of this GermplasmDTO.  # noqa: E501
        :type: str
        """

        self._additional_info = additional_info

    @property
    def biological_status_of_accession_code(self):
        """Gets the biological_status_of_accession_code of this GermplasmDTO.  # noqa: E501


        :return: The biological_status_of_accession_code of this GermplasmDTO.  # noqa: E501
        :rtype: str
        """
        return self._biological_status_of_accession_code

    @biological_status_of_accession_code.setter
    def biological_status_of_accession_code(self, biological_status_of_accession_code):
        """Sets the biological_status_of_accession_code of this GermplasmDTO.


        :param biological_status_of_accession_code: The biological_status_of_accession_code of this GermplasmDTO.  # noqa: E501
        :type: str
        """

        self._biological_status_of_accession_code = biological_status_of_accession_code

    @property
    def biological_status_of_accession_description(self):
        """Gets the biological_status_of_accession_description of this GermplasmDTO.  # noqa: E501


        :return: The biological_status_of_accession_description of this GermplasmDTO.  # noqa: E501
        :rtype: str
        """
        return self._biological_status_of_accession_description

    @biological_status_of_accession_description.setter
    def biological_status_of_accession_description(self, biological_status_of_accession_description):
        """Sets the biological_status_of_accession_description of this GermplasmDTO.


        :param biological_status_of_accession_description: The biological_status_of_accession_description of this GermplasmDTO.  # noqa: E501
        :type: str
        """

        self._biological_status_of_accession_description = biological_status_of_accession_description

    @property
    def breeding_method_db_id(self):
        """Gets the breeding_method_db_id of this GermplasmDTO.  # noqa: E501


        :return: The breeding_method_db_id of this GermplasmDTO.  # noqa: E501
        :rtype: str
        """
        return self._breeding_method_db_id

    @breeding_method_db_id.setter
    def breeding_method_db_id(self, breeding_method_db_id):
        """Sets the breeding_method_db_id of this GermplasmDTO.


        :param breeding_method_db_id: The breeding_method_db_id of this GermplasmDTO.  # noqa: E501
        :type: str
        """

        self._breeding_method_db_id = breeding_method_db_id

    @property
    def collection(self):
        """Gets the collection of this GermplasmDTO.  # noqa: E501


        :return: The collection of this GermplasmDTO.  # noqa: E501
        :rtype: str
        """
        return self._collection

    @collection.setter
    def collection(self, collection):
        """Sets the collection of this GermplasmDTO.


        :param collection: The collection of this GermplasmDTO.  # noqa: E501
        :type: str
        """

        self._collection = collection

    @property
    def common_crop_name(self):
        """Gets the common_crop_name of this GermplasmDTO.  # noqa: E501


        :return: The common_crop_name of this GermplasmDTO.  # noqa: E501
        :rtype: str
        """
        return self._common_crop_name

    @common_crop_name.setter
    def common_crop_name(self, common_crop_name):
        """Sets the common_crop_name of this GermplasmDTO.


        :param common_crop_name: The common_crop_name of this GermplasmDTO.  # noqa: E501
        :type: str
        """

        self._common_crop_name = common_crop_name

    @property
    def country_of_origin_code(self):
        """Gets the country_of_origin_code of this GermplasmDTO.  # noqa: E501


        :return: The country_of_origin_code of this GermplasmDTO.  # noqa: E501
        :rtype: str
        """
        return self._country_of_origin_code

    @country_of_origin_code.setter
    def country_of_origin_code(self, country_of_origin_code):
        """Sets the country_of_origin_code of this GermplasmDTO.


        :param country_of_origin_code: The country_of_origin_code of this GermplasmDTO.  # noqa: E501
        :type: str
        """

        self._country_of_origin_code = country_of_origin_code

    @property
    def default_display_name(self):
        """Gets the default_display_name of this GermplasmDTO.  # noqa: E501


        :return: The default_display_name of this GermplasmDTO.  # noqa: E501
        :rtype: str
        """
        return self._default_display_name

    @default_display_name.setter
    def default_display_name(self, default_display_name):
        """Sets the default_display_name of this GermplasmDTO.


        :param default_display_name: The default_display_name of this GermplasmDTO.  # noqa: E501
        :type: str
        """

        self._default_display_name = default_display_name

    @property
    def documentation_url(self):
        """Gets the documentation_url of this GermplasmDTO.  # noqa: E501


        :return: The documentation_url of this GermplasmDTO.  # noqa: E501
        :rtype: str
        """
        return self._documentation_url

    @documentation_url.setter
    def documentation_url(self, documentation_url):
        """Sets the documentation_url of this GermplasmDTO.


        :param documentation_url: The documentation_url of this GermplasmDTO.  # noqa: E501
        :type: str
        """

        self._documentation_url = documentation_url

    @property
    def donors(self):
        """Gets the donors of this GermplasmDTO.  # noqa: E501


        :return: The donors of this GermplasmDTO.  # noqa: E501
        :rtype: list[object]
        """
        return self._donors

    @donors.setter
    def donors(self, donors):
        """Sets the donors of this GermplasmDTO.


        :param donors: The donors of this GermplasmDTO.  # noqa: E501
        :type: list[object]
        """

        self._donors = donors

    @property
    def external_references(self):
        """Gets the external_references of this GermplasmDTO.  # noqa: E501


        :return: The external_references of this GermplasmDTO.  # noqa: E501
        :rtype: list[object]
        """
        return self._external_references

    @external_references.setter
    def external_references(self, external_references):
        """Sets the external_references of this GermplasmDTO.


        :param external_references: The external_references of this GermplasmDTO.  # noqa: E501
        :type: list[object]
        """

        self._external_references = external_references

    @property
    def genus(self):
        """Gets the genus of this GermplasmDTO.  # noqa: E501


        :return: The genus of this GermplasmDTO.  # noqa: E501
        :rtype: str
        """
        return self._genus

    @genus.setter
    def genus(self, genus):
        """Sets the genus of this GermplasmDTO.


        :param genus: The genus of this GermplasmDTO.  # noqa: E501
        :type: str
        """

        self._genus = genus

    @property
    def germplasm_db_id(self):
        """Gets the germplasm_db_id of this GermplasmDTO.  # noqa: E501


        :return: The germplasm_db_id of this GermplasmDTO.  # noqa: E501
        :rtype: str
        """
        return self._germplasm_db_id

    @germplasm_db_id.setter
    def germplasm_db_id(self, germplasm_db_id):
        """Sets the germplasm_db_id of this GermplasmDTO.


        :param germplasm_db_id: The germplasm_db_id of this GermplasmDTO.  # noqa: E501
        :type: str
        """

        self._germplasm_db_id = germplasm_db_id

    @property
    def germplasm_name(self):
        """Gets the germplasm_name of this GermplasmDTO.  # noqa: E501


        :return: The germplasm_name of this GermplasmDTO.  # noqa: E501
        :rtype: str
        """
        return self._germplasm_name

    @germplasm_name.setter
    def germplasm_name(self, germplasm_name):
        """Sets the germplasm_name of this GermplasmDTO.


        :param germplasm_name: The germplasm_name of this GermplasmDTO.  # noqa: E501
        :type: str
        """

        self._germplasm_name = germplasm_name

    @property
    def germplasm_origin(self):
        """Gets the germplasm_origin of this GermplasmDTO.  # noqa: E501


        :return: The germplasm_origin of this GermplasmDTO.  # noqa: E501
        :rtype: list[object]
        """
        return self._germplasm_origin

    @germplasm_origin.setter
    def germplasm_origin(self, germplasm_origin):
        """Sets the germplasm_origin of this GermplasmDTO.


        :param germplasm_origin: The germplasm_origin of this GermplasmDTO.  # noqa: E501
        :type: list[object]
        """

        self._germplasm_origin = germplasm_origin

    @property
    def germplasm_preprocessing(self):
        """Gets the germplasm_preprocessing of this GermplasmDTO.  # noqa: E501


        :return: The germplasm_preprocessing of this GermplasmDTO.  # noqa: E501
        :rtype: str
        """
        return self._germplasm_preprocessing

    @germplasm_preprocessing.setter
    def germplasm_preprocessing(self, germplasm_preprocessing):
        """Sets the germplasm_preprocessing of this GermplasmDTO.


        :param germplasm_preprocessing: The germplasm_preprocessing of this GermplasmDTO.  # noqa: E501
        :type: str
        """

        self._germplasm_preprocessing = germplasm_preprocessing

    @property
    def institute_code(self):
        """Gets the institute_code of this GermplasmDTO.  # noqa: E501


        :return: The institute_code of this GermplasmDTO.  # noqa: E501
        :rtype: str
        """
        return self._institute_code

    @institute_code.setter
    def institute_code(self, institute_code):
        """Sets the institute_code of this GermplasmDTO.


        :param institute_code: The institute_code of this GermplasmDTO.  # noqa: E501
        :type: str
        """

        self._institute_code = institute_code

    @property
    def institute_name(self):
        """Gets the institute_name of this GermplasmDTO.  # noqa: E501


        :return: The institute_name of this GermplasmDTO.  # noqa: E501
        :rtype: str
        """
        return self._institute_name

    @institute_name.setter
    def institute_name(self, institute_name):
        """Sets the institute_name of this GermplasmDTO.


        :param institute_name: The institute_name of this GermplasmDTO.  # noqa: E501
        :type: str
        """

        self._institute_name = institute_name

    @property
    def pedigree(self):
        """Gets the pedigree of this GermplasmDTO.  # noqa: E501


        :return: The pedigree of this GermplasmDTO.  # noqa: E501
        :rtype: str
        """
        return self._pedigree

    @pedigree.setter
    def pedigree(self, pedigree):
        """Sets the pedigree of this GermplasmDTO.


        :param pedigree: The pedigree of this GermplasmDTO.  # noqa: E501
        :type: str
        """

        self._pedigree = pedigree

    @property
    def seed_source(self):
        """Gets the seed_source of this GermplasmDTO.  # noqa: E501


        :return: The seed_source of this GermplasmDTO.  # noqa: E501
        :rtype: str
        """
        return self._seed_source

    @seed_source.setter
    def seed_source(self, seed_source):
        """Sets the seed_source of this GermplasmDTO.


        :param seed_source: The seed_source of this GermplasmDTO.  # noqa: E501
        :type: str
        """

        self._seed_source = seed_source

    @property
    def seed_source_description(self):
        """Gets the seed_source_description of this GermplasmDTO.  # noqa: E501


        :return: The seed_source_description of this GermplasmDTO.  # noqa: E501
        :rtype: str
        """
        return self._seed_source_description

    @seed_source_description.setter
    def seed_source_description(self, seed_source_description):
        """Sets the seed_source_description of this GermplasmDTO.


        :param seed_source_description: The seed_source_description of this GermplasmDTO.  # noqa: E501
        :type: str
        """

        self._seed_source_description = seed_source_description

    @property
    def species(self):
        """Gets the species of this GermplasmDTO.  # noqa: E501


        :return: The species of this GermplasmDTO.  # noqa: E501
        :rtype: str
        """
        return self._species

    @species.setter
    def species(self, species):
        """Sets the species of this GermplasmDTO.


        :param species: The species of this GermplasmDTO.  # noqa: E501
        :type: str
        """

        self._species = species

    @property
    def species_authority(self):
        """Gets the species_authority of this GermplasmDTO.  # noqa: E501


        :return: The species_authority of this GermplasmDTO.  # noqa: E501
        :rtype: str
        """
        return self._species_authority

    @species_authority.setter
    def species_authority(self, species_authority):
        """Sets the species_authority of this GermplasmDTO.


        :param species_authority: The species_authority of this GermplasmDTO.  # noqa: E501
        :type: str
        """

        self._species_authority = species_authority

    @property
    def storage_types(self):
        """Gets the storage_types of this GermplasmDTO.  # noqa: E501


        :return: The storage_types of this GermplasmDTO.  # noqa: E501
        :rtype: list[object]
        """
        return self._storage_types

    @storage_types.setter
    def storage_types(self, storage_types):
        """Sets the storage_types of this GermplasmDTO.


        :param storage_types: The storage_types of this GermplasmDTO.  # noqa: E501
        :type: list[object]
        """

        self._storage_types = storage_types

    @property
    def subtaxa(self):
        """Gets the subtaxa of this GermplasmDTO.  # noqa: E501


        :return: The subtaxa of this GermplasmDTO.  # noqa: E501
        :rtype: str
        """
        return self._subtaxa

    @subtaxa.setter
    def subtaxa(self, subtaxa):
        """Sets the subtaxa of this GermplasmDTO.


        :param subtaxa: The subtaxa of this GermplasmDTO.  # noqa: E501
        :type: str
        """

        self._subtaxa = subtaxa

    @property
    def subtaxa_authority(self):
        """Gets the subtaxa_authority of this GermplasmDTO.  # noqa: E501


        :return: The subtaxa_authority of this GermplasmDTO.  # noqa: E501
        :rtype: str
        """
        return self._subtaxa_authority

    @subtaxa_authority.setter
    def subtaxa_authority(self, subtaxa_authority):
        """Sets the subtaxa_authority of this GermplasmDTO.


        :param subtaxa_authority: The subtaxa_authority of this GermplasmDTO.  # noqa: E501
        :type: str
        """

        self._subtaxa_authority = subtaxa_authority

    @property
    def synonyms(self):
        """Gets the synonyms of this GermplasmDTO.  # noqa: E501


        :return: The synonyms of this GermplasmDTO.  # noqa: E501
        :rtype: list[object]
        """
        return self._synonyms

    @synonyms.setter
    def synonyms(self, synonyms):
        """Sets the synonyms of this GermplasmDTO.


        :param synonyms: The synonyms of this GermplasmDTO.  # noqa: E501
        :type: list[object]
        """

        self._synonyms = synonyms

    @property
    def taxon_ids(self):
        """Gets the taxon_ids of this GermplasmDTO.  # noqa: E501


        :return: The taxon_ids of this GermplasmDTO.  # noqa: E501
        :rtype: list[object]
        """
        return self._taxon_ids

    @taxon_ids.setter
    def taxon_ids(self, taxon_ids):
        """Sets the taxon_ids of this GermplasmDTO.


        :param taxon_ids: The taxon_ids of this GermplasmDTO.  # noqa: E501
        :type: list[object]
        """

        self._taxon_ids = taxon_ids

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
        if issubclass(GermplasmDTO, dict):
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
        if not isinstance(other, GermplasmDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

