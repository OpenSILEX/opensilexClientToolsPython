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


class FormCreationDTO(object):
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
        'type': 'str',
        'timezone': 'str',
        'modified_date': 'str',
        'form_data': 'dict(str, object)'
    }

    attribute_map = {
        'type': 'type',
        'timezone': 'timezone',
        'modified_date': 'modified_date',
        'form_data': 'form_data'
    }

    def __init__(self, type=None, timezone=None, modified_date=None, form_data=None):  # noqa: E501
        """FormCreationDTO - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self._timezone = None
        self._modified_date = None
        self._form_data = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if timezone is not None:
            self.timezone = timezone
        self.modified_date = modified_date
        if form_data is not None:
            self.form_data = form_data

    @property
    def type(self):
        """Gets the type of this FormCreationDTO.  # noqa: E501


        :return: The type of this FormCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FormCreationDTO.


        :param type: The type of this FormCreationDTO.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def timezone(self):
        """Gets the timezone of this FormCreationDTO.  # noqa: E501

        to specify if the offset is not in the date and if the timezone is different from the default one  # noqa: E501

        :return: The timezone of this FormCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this FormCreationDTO.

        to specify if the offset is not in the date and if the timezone is different from the default one  # noqa: E501

        :param timezone: The timezone of this FormCreationDTO.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def modified_date(self):
        """Gets the modified_date of this FormCreationDTO.  # noqa: E501

        timestamp  # noqa: E501

        :return: The modified_date of this FormCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        """Sets the modified_date of this FormCreationDTO.

        timestamp  # noqa: E501

        :param modified_date: The modified_date of this FormCreationDTO.  # noqa: E501
        :type: str
        """
        if modified_date is None:
            raise ValueError("Invalid value for `modified_date`, must not be `None`")  # noqa: E501

        self._modified_date = modified_date

    @property
    def form_data(self):
        """Gets the form_data of this FormCreationDTO.  # noqa: E501


        :return: The form_data of this FormCreationDTO.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._form_data

    @form_data.setter
    def form_data(self, form_data):
        """Sets the form_data of this FormCreationDTO.


        :param form_data: The form_data of this FormCreationDTO.  # noqa: E501
        :type: dict(str, object)
        """

        self._form_data = form_data

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
        if issubclass(FormCreationDTO, dict):
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
        if not isinstance(other, FormCreationDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
