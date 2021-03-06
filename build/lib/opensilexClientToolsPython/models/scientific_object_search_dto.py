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


class ScientificObjectSearchDTO(object):
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
        'uris': 'list[str]',
        'excluded_uris': 'list[str]',
        'experiment': 'str',
        'rdf_types': 'list[str]',
        'name': 'str',
        'parent': 'str',
        'germplasm': 'str',
        'factor_levels': 'list[str]',
        'facility': 'str',
        'existence_date': 'date',
        'creation_date': 'date',
        'order_by': 'list[OrderBy]',
        'page': 'int',
        'page_sze': 'int'
    }

    attribute_map = {
        'uris': 'uris',
        'excluded_uris': 'excluded_uris',
        'experiment': 'experiment',
        'rdf_types': 'rdf_types',
        'name': 'name',
        'parent': 'parent',
        'germplasm': 'germplasm',
        'factor_levels': 'factor_levels',
        'facility': 'facility',
        'existence_date': 'existence_date',
        'creation_date': 'creation_date',
        'order_by': 'order_by',
        'page': 'page',
        'page_sze': 'page_sze'
    }

    def __init__(self, uris=None, excluded_uris=None, experiment=None, rdf_types=None, name=None, parent=None, germplasm=None, factor_levels=None, facility=None, existence_date=None, creation_date=None, order_by=None, page=None, page_sze=None):  # noqa: E501
        """ScientificObjectSearchDTO - a model defined in Swagger"""  # noqa: E501

        self._uris = None
        self._excluded_uris = None
        self._experiment = None
        self._rdf_types = None
        self._name = None
        self._parent = None
        self._germplasm = None
        self._factor_levels = None
        self._facility = None
        self._existence_date = None
        self._creation_date = None
        self._order_by = None
        self._page = None
        self._page_sze = None
        self.discriminator = None

        if uris is not None:
            self.uris = uris
        if excluded_uris is not None:
            self.excluded_uris = excluded_uris
        if experiment is not None:
            self.experiment = experiment
        if rdf_types is not None:
            self.rdf_types = rdf_types
        if name is not None:
            self.name = name
        if parent is not None:
            self.parent = parent
        if germplasm is not None:
            self.germplasm = germplasm
        if factor_levels is not None:
            self.factor_levels = factor_levels
        if facility is not None:
            self.facility = facility
        if existence_date is not None:
            self.existence_date = existence_date
        if creation_date is not None:
            self.creation_date = creation_date
        if order_by is not None:
            self.order_by = order_by
        if page is not None:
            self.page = page
        if page_sze is not None:
            self.page_sze = page_sze

    @property
    def uris(self):
        """Gets the uris of this ScientificObjectSearchDTO.  # noqa: E501


        :return: The uris of this ScientificObjectSearchDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._uris

    @uris.setter
    def uris(self, uris):
        """Sets the uris of this ScientificObjectSearchDTO.


        :param uris: The uris of this ScientificObjectSearchDTO.  # noqa: E501
        :type: list[str]
        """

        self._uris = uris

    @property
    def excluded_uris(self):
        """Gets the excluded_uris of this ScientificObjectSearchDTO.  # noqa: E501


        :return: The excluded_uris of this ScientificObjectSearchDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._excluded_uris

    @excluded_uris.setter
    def excluded_uris(self, excluded_uris):
        """Sets the excluded_uris of this ScientificObjectSearchDTO.


        :param excluded_uris: The excluded_uris of this ScientificObjectSearchDTO.  # noqa: E501
        :type: list[str]
        """

        self._excluded_uris = excluded_uris

    @property
    def experiment(self):
        """Gets the experiment of this ScientificObjectSearchDTO.  # noqa: E501


        :return: The experiment of this ScientificObjectSearchDTO.  # noqa: E501
        :rtype: str
        """
        return self._experiment

    @experiment.setter
    def experiment(self, experiment):
        """Sets the experiment of this ScientificObjectSearchDTO.


        :param experiment: The experiment of this ScientificObjectSearchDTO.  # noqa: E501
        :type: str
        """

        self._experiment = experiment

    @property
    def rdf_types(self):
        """Gets the rdf_types of this ScientificObjectSearchDTO.  # noqa: E501


        :return: The rdf_types of this ScientificObjectSearchDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._rdf_types

    @rdf_types.setter
    def rdf_types(self, rdf_types):
        """Sets the rdf_types of this ScientificObjectSearchDTO.


        :param rdf_types: The rdf_types of this ScientificObjectSearchDTO.  # noqa: E501
        :type: list[str]
        """

        self._rdf_types = rdf_types

    @property
    def name(self):
        """Gets the name of this ScientificObjectSearchDTO.  # noqa: E501


        :return: The name of this ScientificObjectSearchDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ScientificObjectSearchDTO.


        :param name: The name of this ScientificObjectSearchDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def parent(self):
        """Gets the parent of this ScientificObjectSearchDTO.  # noqa: E501


        :return: The parent of this ScientificObjectSearchDTO.  # noqa: E501
        :rtype: str
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this ScientificObjectSearchDTO.


        :param parent: The parent of this ScientificObjectSearchDTO.  # noqa: E501
        :type: str
        """

        self._parent = parent

    @property
    def germplasm(self):
        """Gets the germplasm of this ScientificObjectSearchDTO.  # noqa: E501


        :return: The germplasm of this ScientificObjectSearchDTO.  # noqa: E501
        :rtype: str
        """
        return self._germplasm

    @germplasm.setter
    def germplasm(self, germplasm):
        """Sets the germplasm of this ScientificObjectSearchDTO.


        :param germplasm: The germplasm of this ScientificObjectSearchDTO.  # noqa: E501
        :type: str
        """

        self._germplasm = germplasm

    @property
    def factor_levels(self):
        """Gets the factor_levels of this ScientificObjectSearchDTO.  # noqa: E501


        :return: The factor_levels of this ScientificObjectSearchDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._factor_levels

    @factor_levels.setter
    def factor_levels(self, factor_levels):
        """Sets the factor_levels of this ScientificObjectSearchDTO.


        :param factor_levels: The factor_levels of this ScientificObjectSearchDTO.  # noqa: E501
        :type: list[str]
        """

        self._factor_levels = factor_levels

    @property
    def facility(self):
        """Gets the facility of this ScientificObjectSearchDTO.  # noqa: E501


        :return: The facility of this ScientificObjectSearchDTO.  # noqa: E501
        :rtype: str
        """
        return self._facility

    @facility.setter
    def facility(self, facility):
        """Sets the facility of this ScientificObjectSearchDTO.


        :param facility: The facility of this ScientificObjectSearchDTO.  # noqa: E501
        :type: str
        """

        self._facility = facility

    @property
    def existence_date(self):
        """Gets the existence_date of this ScientificObjectSearchDTO.  # noqa: E501


        :return: The existence_date of this ScientificObjectSearchDTO.  # noqa: E501
        :rtype: date
        """
        return self._existence_date

    @existence_date.setter
    def existence_date(self, existence_date):
        """Sets the existence_date of this ScientificObjectSearchDTO.


        :param existence_date: The existence_date of this ScientificObjectSearchDTO.  # noqa: E501
        :type: date
        """

        self._existence_date = existence_date

    @property
    def creation_date(self):
        """Gets the creation_date of this ScientificObjectSearchDTO.  # noqa: E501


        :return: The creation_date of this ScientificObjectSearchDTO.  # noqa: E501
        :rtype: date
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this ScientificObjectSearchDTO.


        :param creation_date: The creation_date of this ScientificObjectSearchDTO.  # noqa: E501
        :type: date
        """

        self._creation_date = creation_date

    @property
    def order_by(self):
        """Gets the order_by of this ScientificObjectSearchDTO.  # noqa: E501


        :return: The order_by of this ScientificObjectSearchDTO.  # noqa: E501
        :rtype: list[OrderBy]
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        """Sets the order_by of this ScientificObjectSearchDTO.


        :param order_by: The order_by of this ScientificObjectSearchDTO.  # noqa: E501
        :type: list[OrderBy]
        """

        self._order_by = order_by

    @property
    def page(self):
        """Gets the page of this ScientificObjectSearchDTO.  # noqa: E501


        :return: The page of this ScientificObjectSearchDTO.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ScientificObjectSearchDTO.


        :param page: The page of this ScientificObjectSearchDTO.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def page_sze(self):
        """Gets the page_sze of this ScientificObjectSearchDTO.  # noqa: E501


        :return: The page_sze of this ScientificObjectSearchDTO.  # noqa: E501
        :rtype: int
        """
        return self._page_sze

    @page_sze.setter
    def page_sze(self, page_sze):
        """Sets the page_sze of this ScientificObjectSearchDTO.


        :param page_sze: The page_sze of this ScientificObjectSearchDTO.  # noqa: E501
        :type: int
        """

        self._page_sze = page_sze

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
        if issubclass(ScientificObjectSearchDTO, dict):
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
        if not isinstance(other, ScientificObjectSearchDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
