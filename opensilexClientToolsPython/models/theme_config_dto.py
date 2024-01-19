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


class ThemeConfigDTO(object):
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
        'has_style': 'bool',
        'fonts': 'list[FontConfigDTO]',
        'icon_classes_rdf': 'dict(str, str)',
        'component_overrides': 'dict(str, str)'
    }

    attribute_map = {
        'has_style': 'hasStyle',
        'fonts': 'fonts',
        'icon_classes_rdf': 'iconClassesRDF',
        'component_overrides': 'componentOverrides'
    }
    def __init__(self,
        has_style : 'bool' = None,
        fonts : 'List[FontConfigDTO]' = None,
        icon_classes_rdf : 'Dict[str, str]' = None,
        component_overrides : 'Dict[str, str]' = None):  # noqa: E501
        """ThemeConfigDTO - a model defined in Swagger"""  # noqa: E501

        self._has_style = None
        self._fonts = None
        self._icon_classes_rdf = None
        self._component_overrides = None
        self.discriminator = None

        if has_style is not None:
            self.has_style = has_style
        if fonts is not None:
            self.fonts = fonts
        if icon_classes_rdf is not None:
            self.icon_classes_rdf = icon_classes_rdf
        if component_overrides is not None:
            self.component_overrides = component_overrides

    @property
    def has_style(self):
        """Gets the has_style of this ThemeConfigDTO.  # noqa: E501


        :return: The has_style of this ThemeConfigDTO.  # noqa: E501
        :rtype: bool
        """
        return self._has_style

    @has_style.setter
    def has_style(self, has_style):
        """Sets the has_style of this ThemeConfigDTO.


        :param has_style: The has_style of this ThemeConfigDTO.  # noqa: E501
        :type: bool
        """

        self._has_style = has_style

    @property
    def fonts(self):
        """Gets the fonts of this ThemeConfigDTO.  # noqa: E501


        :return: The fonts of this ThemeConfigDTO.  # noqa: E501
        :rtype: list[FontConfigDTO]
        """
        return self._fonts

    @fonts.setter
    def fonts(self, fonts):
        """Sets the fonts of this ThemeConfigDTO.


        :param fonts: The fonts of this ThemeConfigDTO.  # noqa: E501
        :type: list[FontConfigDTO]
        """

        self._fonts = fonts

    @property
    def icon_classes_rdf(self):
        """Gets the icon_classes_rdf of this ThemeConfigDTO.  # noqa: E501


        :return: The icon_classes_rdf of this ThemeConfigDTO.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._icon_classes_rdf

    @icon_classes_rdf.setter
    def icon_classes_rdf(self, icon_classes_rdf):
        """Sets the icon_classes_rdf of this ThemeConfigDTO.


        :param icon_classes_rdf: The icon_classes_rdf of this ThemeConfigDTO.  # noqa: E501
        :type: dict(str, str)
        """

        self._icon_classes_rdf = icon_classes_rdf

    @property
    def component_overrides(self):
        """Gets the component_overrides of this ThemeConfigDTO.  # noqa: E501


        :return: The component_overrides of this ThemeConfigDTO.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._component_overrides

    @component_overrides.setter
    def component_overrides(self, component_overrides):
        """Sets the component_overrides of this ThemeConfigDTO.


        :param component_overrides: The component_overrides of this ThemeConfigDTO.  # noqa: E501
        :type: dict(str, str)
        """

        self._component_overrides = component_overrides

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
        if issubclass(ThemeConfigDTO, dict):
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
        if not isinstance(other, ThemeConfigDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other


from opensilexClientToolsPython.models.font_config_dto import FontConfigDTO


