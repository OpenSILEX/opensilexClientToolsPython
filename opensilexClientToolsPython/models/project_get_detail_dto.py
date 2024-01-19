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


class ProjectGetDetailDTO(object):
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
        'publisher': 'UserGetDTO',
        'publication_date': 'datetime',
        'last_updated_date': 'datetime',
        'name': 'str',
        'shortname': 'str',
        'start_date': 'str',
        'end_date': 'str',
        'description': 'str',
        'objective': 'str',
        'financial_funding': 'str',
        'website': 'str',
        'related_projects': 'list[str]',
        'coordinators': 'list[str]',
        'scientific_contacts': 'list[str]',
        'administrative_contacts': 'list[str]',
        'experiments': 'list[str]'
    }

    attribute_map = {
        'uri': 'uri',
        'publisher': 'publisher',
        'publication_date': 'publication_date',
        'last_updated_date': 'last_updated_date',
        'name': 'name',
        'shortname': 'shortname',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'description': 'description',
        'objective': 'objective',
        'financial_funding': 'financial_funding',
        'website': 'website',
        'related_projects': 'related_projects',
        'coordinators': 'coordinators',
        'scientific_contacts': 'scientific_contacts',
        'administrative_contacts': 'administrative_contacts',
        'experiments': 'experiments'
    }
    def __init__(self,
        name : 'str',
        start_date : 'str',
        uri : 'str' = None,
        publisher : 'UserGetDTO' = None,
        publication_date : 'datetime' = None,
        last_updated_date : 'datetime' = None,
        shortname : 'str' = None,
        end_date : 'str' = None,
        description : 'str' = None,
        objective : 'str' = None,
        financial_funding : 'str' = None,
        website : 'str' = None,
        related_projects : 'List[str]' = None,
        coordinators : 'List[str]' = None,
        scientific_contacts : 'List[str]' = None,
        administrative_contacts : 'List[str]' = None,
        experiments : 'List[str]' = None):  # noqa: E501
        """ProjectGetDetailDTO - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self._publisher = None
        self._publication_date = None
        self._last_updated_date = None
        self._name = None
        self._shortname = None
        self._start_date = None
        self._end_date = None
        self._description = None
        self._objective = None
        self._financial_funding = None
        self._website = None
        self._related_projects = None
        self._coordinators = None
        self._scientific_contacts = None
        self._administrative_contacts = None
        self._experiments = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if publisher is not None:
            self.publisher = publisher
        if publication_date is not None:
            self.publication_date = publication_date
        if last_updated_date is not None:
            self.last_updated_date = last_updated_date
        self.name = name
        if shortname is not None:
            self.shortname = shortname
        self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if description is not None:
            self.description = description
        if objective is not None:
            self.objective = objective
        if financial_funding is not None:
            self.financial_funding = financial_funding
        if website is not None:
            self.website = website
        if related_projects is not None:
            self.related_projects = related_projects
        if coordinators is not None:
            self.coordinators = coordinators
        if scientific_contacts is not None:
            self.scientific_contacts = scientific_contacts
        if administrative_contacts is not None:
            self.administrative_contacts = administrative_contacts
        if experiments is not None:
            self.experiments = experiments

    @property
    def uri(self):
        """Gets the uri of this ProjectGetDetailDTO.  # noqa: E501


        :return: The uri of this ProjectGetDetailDTO.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this ProjectGetDetailDTO.


        :param uri: The uri of this ProjectGetDetailDTO.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def publisher(self):
        """Gets the publisher of this ProjectGetDetailDTO.  # noqa: E501


        :return: The publisher of this ProjectGetDetailDTO.  # noqa: E501
        :rtype: UserGetDTO
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        """Sets the publisher of this ProjectGetDetailDTO.


        :param publisher: The publisher of this ProjectGetDetailDTO.  # noqa: E501
        :type: UserGetDTO
        """

        self._publisher = publisher

    @property
    def publication_date(self):
        """Gets the publication_date of this ProjectGetDetailDTO.  # noqa: E501


        :return: The publication_date of this ProjectGetDetailDTO.  # noqa: E501
        :rtype: datetime
        """
        return self._publication_date

    @publication_date.setter
    def publication_date(self, publication_date):
        """Sets the publication_date of this ProjectGetDetailDTO.


        :param publication_date: The publication_date of this ProjectGetDetailDTO.  # noqa: E501
        :type: datetime
        """

        self._publication_date = publication_date

    @property
    def last_updated_date(self):
        """Gets the last_updated_date of this ProjectGetDetailDTO.  # noqa: E501


        :return: The last_updated_date of this ProjectGetDetailDTO.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated_date

    @last_updated_date.setter
    def last_updated_date(self, last_updated_date):
        """Sets the last_updated_date of this ProjectGetDetailDTO.


        :param last_updated_date: The last_updated_date of this ProjectGetDetailDTO.  # noqa: E501
        :type: datetime
        """

        self._last_updated_date = last_updated_date

    @property
    def name(self):
        """Gets the name of this ProjectGetDetailDTO.  # noqa: E501


        :return: The name of this ProjectGetDetailDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProjectGetDetailDTO.


        :param name: The name of this ProjectGetDetailDTO.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def shortname(self):
        """Gets the shortname of this ProjectGetDetailDTO.  # noqa: E501


        :return: The shortname of this ProjectGetDetailDTO.  # noqa: E501
        :rtype: str
        """
        return self._shortname

    @shortname.setter
    def shortname(self, shortname):
        """Sets the shortname of this ProjectGetDetailDTO.


        :param shortname: The shortname of this ProjectGetDetailDTO.  # noqa: E501
        :type: str
        """

        self._shortname = shortname

    @property
    def start_date(self):
        """Gets the start_date of this ProjectGetDetailDTO.  # noqa: E501


        :return: The start_date of this ProjectGetDetailDTO.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ProjectGetDetailDTO.


        :param start_date: The start_date of this ProjectGetDetailDTO.  # noqa: E501
        :type: str
        """
        if start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this ProjectGetDetailDTO.  # noqa: E501


        :return: The end_date of this ProjectGetDetailDTO.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ProjectGetDetailDTO.


        :param end_date: The end_date of this ProjectGetDetailDTO.  # noqa: E501
        :type: str
        """

        self._end_date = end_date

    @property
    def description(self):
        """Gets the description of this ProjectGetDetailDTO.  # noqa: E501


        :return: The description of this ProjectGetDetailDTO.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProjectGetDetailDTO.


        :param description: The description of this ProjectGetDetailDTO.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def objective(self):
        """Gets the objective of this ProjectGetDetailDTO.  # noqa: E501


        :return: The objective of this ProjectGetDetailDTO.  # noqa: E501
        :rtype: str
        """
        return self._objective

    @objective.setter
    def objective(self, objective):
        """Sets the objective of this ProjectGetDetailDTO.


        :param objective: The objective of this ProjectGetDetailDTO.  # noqa: E501
        :type: str
        """

        self._objective = objective

    @property
    def financial_funding(self):
        """Gets the financial_funding of this ProjectGetDetailDTO.  # noqa: E501


        :return: The financial_funding of this ProjectGetDetailDTO.  # noqa: E501
        :rtype: str
        """
        return self._financial_funding

    @financial_funding.setter
    def financial_funding(self, financial_funding):
        """Sets the financial_funding of this ProjectGetDetailDTO.


        :param financial_funding: The financial_funding of this ProjectGetDetailDTO.  # noqa: E501
        :type: str
        """

        self._financial_funding = financial_funding

    @property
    def website(self):
        """Gets the website of this ProjectGetDetailDTO.  # noqa: E501


        :return: The website of this ProjectGetDetailDTO.  # noqa: E501
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this ProjectGetDetailDTO.


        :param website: The website of this ProjectGetDetailDTO.  # noqa: E501
        :type: str
        """

        self._website = website

    @property
    def related_projects(self):
        """Gets the related_projects of this ProjectGetDetailDTO.  # noqa: E501


        :return: The related_projects of this ProjectGetDetailDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._related_projects

    @related_projects.setter
    def related_projects(self, related_projects):
        """Sets the related_projects of this ProjectGetDetailDTO.


        :param related_projects: The related_projects of this ProjectGetDetailDTO.  # noqa: E501
        :type: list[str]
        """

        self._related_projects = related_projects

    @property
    def coordinators(self):
        """Gets the coordinators of this ProjectGetDetailDTO.  # noqa: E501


        :return: The coordinators of this ProjectGetDetailDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._coordinators

    @coordinators.setter
    def coordinators(self, coordinators):
        """Sets the coordinators of this ProjectGetDetailDTO.


        :param coordinators: The coordinators of this ProjectGetDetailDTO.  # noqa: E501
        :type: list[str]
        """

        self._coordinators = coordinators

    @property
    def scientific_contacts(self):
        """Gets the scientific_contacts of this ProjectGetDetailDTO.  # noqa: E501


        :return: The scientific_contacts of this ProjectGetDetailDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._scientific_contacts

    @scientific_contacts.setter
    def scientific_contacts(self, scientific_contacts):
        """Sets the scientific_contacts of this ProjectGetDetailDTO.


        :param scientific_contacts: The scientific_contacts of this ProjectGetDetailDTO.  # noqa: E501
        :type: list[str]
        """

        self._scientific_contacts = scientific_contacts

    @property
    def administrative_contacts(self):
        """Gets the administrative_contacts of this ProjectGetDetailDTO.  # noqa: E501


        :return: The administrative_contacts of this ProjectGetDetailDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._administrative_contacts

    @administrative_contacts.setter
    def administrative_contacts(self, administrative_contacts):
        """Sets the administrative_contacts of this ProjectGetDetailDTO.


        :param administrative_contacts: The administrative_contacts of this ProjectGetDetailDTO.  # noqa: E501
        :type: list[str]
        """

        self._administrative_contacts = administrative_contacts

    @property
    def experiments(self):
        """Gets the experiments of this ProjectGetDetailDTO.  # noqa: E501


        :return: The experiments of this ProjectGetDetailDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._experiments

    @experiments.setter
    def experiments(self, experiments):
        """Sets the experiments of this ProjectGetDetailDTO.


        :param experiments: The experiments of this ProjectGetDetailDTO.  # noqa: E501
        :type: list[str]
        """

        self._experiments = experiments

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
        if issubclass(ProjectGetDetailDTO, dict):
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
        if not isinstance(other, ProjectGetDetailDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other


from opensilexClientToolsPython.models.user_get_dto import UserGetDTO


