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


class BrAPIv1SingleStudyResponse(object):
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
        'metadata': 'MetadataDTO',
        'result': 'BrAPIv1SuperStudyDTO'
    }

    attribute_map = {
        'metadata': 'metadata',
        'result': 'result'
    }
    def __init__(self,
        metadata : 'MetadataDTO' = None,
        result : 'BrAPIv1SuperStudyDTO' = None):  # noqa: E501
        """BrAPIv1SingleStudyResponse - a model defined in Swagger"""  # noqa: E501

        self._metadata = None
        self._result = None
        self.discriminator = None

        if metadata is not None:
            self.metadata = metadata
        if result is not None:
            self.result = result

    @property
    def metadata(self):
        """Gets the metadata of this BrAPIv1SingleStudyResponse.  # noqa: E501


        :return: The metadata of this BrAPIv1SingleStudyResponse.  # noqa: E501
        :rtype: MetadataDTO
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this BrAPIv1SingleStudyResponse.


        :param metadata: The metadata of this BrAPIv1SingleStudyResponse.  # noqa: E501
        :type: MetadataDTO
        """

        self._metadata = metadata

    @property
    def result(self):
        """Gets the result of this BrAPIv1SingleStudyResponse.  # noqa: E501


        :return: The result of this BrAPIv1SingleStudyResponse.  # noqa: E501
        :rtype: BrAPIv1SuperStudyDTO
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this BrAPIv1SingleStudyResponse.


        :param result: The result of this BrAPIv1SingleStudyResponse.  # noqa: E501
        :type: BrAPIv1SuperStudyDTO
        """

        self._result = result

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
        if issubclass(BrAPIv1SingleStudyResponse, dict):
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
        if not isinstance(other, BrAPIv1SingleStudyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other


from opensilexClientToolsPython.models.metadata_dto import MetadataDTO
from opensilexClientToolsPython.models.br_ap_iv1_super_study_dto import BrAPIv1SuperStudyDTO


