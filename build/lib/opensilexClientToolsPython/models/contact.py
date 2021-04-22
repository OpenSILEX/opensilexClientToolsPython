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


class Contact(object):
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
        'contact_db_id': 'str',
        'email': 'str',
        'institution_name': 'str',
        'name': 'str',
        'orcid': 'str',
        'type': 'str'
    }

    attribute_map = {
        'contact_db_id': 'contactDbId',
        'email': 'email',
        'institution_name': 'institutionName',
        'name': 'name',
        'orcid': 'orcid',
        'type': 'type'
    }

    def __init__(self, contact_db_id=None, email=None, institution_name=None, name=None, orcid=None, type=None):  # noqa: E501
        """Contact - a model defined in Swagger"""  # noqa: E501

        self._contact_db_id = None
        self._email = None
        self._institution_name = None
        self._name = None
        self._orcid = None
        self._type = None
        self.discriminator = None

        if contact_db_id is not None:
            self.contact_db_id = contact_db_id
        if email is not None:
            self.email = email
        if institution_name is not None:
            self.institution_name = institution_name
        if name is not None:
            self.name = name
        if orcid is not None:
            self.orcid = orcid
        if type is not None:
            self.type = type

    @property
    def contact_db_id(self):
        """Gets the contact_db_id of this Contact.  # noqa: E501


        :return: The contact_db_id of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._contact_db_id

    @contact_db_id.setter
    def contact_db_id(self, contact_db_id):
        """Sets the contact_db_id of this Contact.


        :param contact_db_id: The contact_db_id of this Contact.  # noqa: E501
        :type: str
        """

        self._contact_db_id = contact_db_id

    @property
    def email(self):
        """Gets the email of this Contact.  # noqa: E501


        :return: The email of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Contact.


        :param email: The email of this Contact.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def institution_name(self):
        """Gets the institution_name of this Contact.  # noqa: E501


        :return: The institution_name of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._institution_name

    @institution_name.setter
    def institution_name(self, institution_name):
        """Sets the institution_name of this Contact.


        :param institution_name: The institution_name of this Contact.  # noqa: E501
        :type: str
        """

        self._institution_name = institution_name

    @property
    def name(self):
        """Gets the name of this Contact.  # noqa: E501


        :return: The name of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Contact.


        :param name: The name of this Contact.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def orcid(self):
        """Gets the orcid of this Contact.  # noqa: E501


        :return: The orcid of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._orcid

    @orcid.setter
    def orcid(self, orcid):
        """Sets the orcid of this Contact.


        :param orcid: The orcid of this Contact.  # noqa: E501
        :type: str
        """

        self._orcid = orcid

    @property
    def type(self):
        """Gets the type of this Contact.  # noqa: E501


        :return: The type of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Contact.


        :param type: The type of this Contact.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(Contact, dict):
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
        if not isinstance(other, Contact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
