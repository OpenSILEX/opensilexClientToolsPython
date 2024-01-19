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


class SiteGetDTO(object):
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
        'rdf_type_name': 'str',
        'publisher': 'UserGetDTO',
        'publication_date': 'datetime',
        'last_updated_date': 'datetime',
        'name': 'str',
        'address': 'SiteAddressDTO',
        'organizations': 'list[NamedResourceDTOOrganizationModel]',
        'facilities': 'list[NamedResourceDTOFacilityModel]',
        'groups': 'list[NamedResourceDTOGroupModel]',
        'geometry': 'GeoJsonObject'
    }

    attribute_map = {
        'uri': 'uri',
        'rdf_type': 'rdf_type',
        'rdf_type_name': 'rdf_type_name',
        'publisher': 'publisher',
        'publication_date': 'publication_date',
        'last_updated_date': 'last_updated_date',
        'name': 'name',
        'address': 'address',
        'organizations': 'organizations',
        'facilities': 'facilities',
        'groups': 'groups',
        'geometry': 'geometry'
    }
    def __init__(self,
        uri : 'str' = None,
        rdf_type : 'str' = None,
        rdf_type_name : 'str' = None,
        publisher : 'UserGetDTO' = None,
        publication_date : 'datetime' = None,
        last_updated_date : 'datetime' = None,
        name : 'str' = None,
        address : 'SiteAddressDTO' = None,
        organizations : 'List[NamedResourceDTOOrganizationModel]' = None,
        facilities : 'List[NamedResourceDTOFacilityModel]' = None,
        groups : 'List[NamedResourceDTOGroupModel]' = None,
        geometry : 'GeoJsonObject' = None):  # noqa: E501
        """SiteGetDTO - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self._rdf_type = None
        self._rdf_type_name = None
        self._publisher = None
        self._publication_date = None
        self._last_updated_date = None
        self._name = None
        self._address = None
        self._organizations = None
        self._facilities = None
        self._groups = None
        self._geometry = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if rdf_type is not None:
            self.rdf_type = rdf_type
        if rdf_type_name is not None:
            self.rdf_type_name = rdf_type_name
        if publisher is not None:
            self.publisher = publisher
        if publication_date is not None:
            self.publication_date = publication_date
        if last_updated_date is not None:
            self.last_updated_date = last_updated_date
        if name is not None:
            self.name = name
        if address is not None:
            self.address = address
        if organizations is not None:
            self.organizations = organizations
        if facilities is not None:
            self.facilities = facilities
        if groups is not None:
            self.groups = groups
        if geometry is not None:
            self.geometry = geometry

    @property
    def uri(self):
        """Gets the uri of this SiteGetDTO.  # noqa: E501


        :return: The uri of this SiteGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this SiteGetDTO.


        :param uri: The uri of this SiteGetDTO.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def rdf_type(self):
        """Gets the rdf_type of this SiteGetDTO.  # noqa: E501


        :return: The rdf_type of this SiteGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._rdf_type

    @rdf_type.setter
    def rdf_type(self, rdf_type):
        """Sets the rdf_type of this SiteGetDTO.


        :param rdf_type: The rdf_type of this SiteGetDTO.  # noqa: E501
        :type: str
        """

        self._rdf_type = rdf_type

    @property
    def rdf_type_name(self):
        """Gets the rdf_type_name of this SiteGetDTO.  # noqa: E501


        :return: The rdf_type_name of this SiteGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._rdf_type_name

    @rdf_type_name.setter
    def rdf_type_name(self, rdf_type_name):
        """Sets the rdf_type_name of this SiteGetDTO.


        :param rdf_type_name: The rdf_type_name of this SiteGetDTO.  # noqa: E501
        :type: str
        """

        self._rdf_type_name = rdf_type_name

    @property
    def publisher(self):
        """Gets the publisher of this SiteGetDTO.  # noqa: E501


        :return: The publisher of this SiteGetDTO.  # noqa: E501
        :rtype: UserGetDTO
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        """Sets the publisher of this SiteGetDTO.


        :param publisher: The publisher of this SiteGetDTO.  # noqa: E501
        :type: UserGetDTO
        """

        self._publisher = publisher

    @property
    def publication_date(self):
        """Gets the publication_date of this SiteGetDTO.  # noqa: E501


        :return: The publication_date of this SiteGetDTO.  # noqa: E501
        :rtype: datetime
        """
        return self._publication_date

    @publication_date.setter
    def publication_date(self, publication_date):
        """Sets the publication_date of this SiteGetDTO.


        :param publication_date: The publication_date of this SiteGetDTO.  # noqa: E501
        :type: datetime
        """

        self._publication_date = publication_date

    @property
    def last_updated_date(self):
        """Gets the last_updated_date of this SiteGetDTO.  # noqa: E501


        :return: The last_updated_date of this SiteGetDTO.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated_date

    @last_updated_date.setter
    def last_updated_date(self, last_updated_date):
        """Sets the last_updated_date of this SiteGetDTO.


        :param last_updated_date: The last_updated_date of this SiteGetDTO.  # noqa: E501
        :type: datetime
        """

        self._last_updated_date = last_updated_date

    @property
    def name(self):
        """Gets the name of this SiteGetDTO.  # noqa: E501


        :return: The name of this SiteGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SiteGetDTO.


        :param name: The name of this SiteGetDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def address(self):
        """Gets the address of this SiteGetDTO.  # noqa: E501


        :return: The address of this SiteGetDTO.  # noqa: E501
        :rtype: SiteAddressDTO
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this SiteGetDTO.


        :param address: The address of this SiteGetDTO.  # noqa: E501
        :type: SiteAddressDTO
        """

        self._address = address

    @property
    def organizations(self):
        """Gets the organizations of this SiteGetDTO.  # noqa: E501


        :return: The organizations of this SiteGetDTO.  # noqa: E501
        :rtype: list[NamedResourceDTOOrganizationModel]
        """
        return self._organizations

    @organizations.setter
    def organizations(self, organizations):
        """Sets the organizations of this SiteGetDTO.


        :param organizations: The organizations of this SiteGetDTO.  # noqa: E501
        :type: list[NamedResourceDTOOrganizationModel]
        """

        self._organizations = organizations

    @property
    def facilities(self):
        """Gets the facilities of this SiteGetDTO.  # noqa: E501


        :return: The facilities of this SiteGetDTO.  # noqa: E501
        :rtype: list[NamedResourceDTOFacilityModel]
        """
        return self._facilities

    @facilities.setter
    def facilities(self, facilities):
        """Sets the facilities of this SiteGetDTO.


        :param facilities: The facilities of this SiteGetDTO.  # noqa: E501
        :type: list[NamedResourceDTOFacilityModel]
        """

        self._facilities = facilities

    @property
    def groups(self):
        """Gets the groups of this SiteGetDTO.  # noqa: E501


        :return: The groups of this SiteGetDTO.  # noqa: E501
        :rtype: list[NamedResourceDTOGroupModel]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this SiteGetDTO.


        :param groups: The groups of this SiteGetDTO.  # noqa: E501
        :type: list[NamedResourceDTOGroupModel]
        """

        self._groups = groups

    @property
    def geometry(self):
        """Gets the geometry of this SiteGetDTO.  # noqa: E501


        :return: The geometry of this SiteGetDTO.  # noqa: E501
        :rtype: GeoJsonObject
        """
        return self._geometry

    @geometry.setter
    def geometry(self, geometry):
        """Sets the geometry of this SiteGetDTO.


        :param geometry: The geometry of this SiteGetDTO.  # noqa: E501
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
        if issubclass(SiteGetDTO, dict):
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
        if not isinstance(other, SiteGetDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other


from opensilexClientToolsPython.models.user_get_dto import UserGetDTO
from opensilexClientToolsPython.models.site_address_dto import SiteAddressDTO
from opensilexClientToolsPython.models.named_resource_dto_organization_model import NamedResourceDTOOrganizationModel
from opensilexClientToolsPython.models.named_resource_dto_facility_model import NamedResourceDTOFacilityModel
from opensilexClientToolsPython.models.named_resource_dto_group_model import NamedResourceDTOGroupModel
from opensilexClientToolsPython.models.geo_json_object import GeoJsonObject


