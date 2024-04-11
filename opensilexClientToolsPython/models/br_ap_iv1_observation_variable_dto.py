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


class BrAPIv1ObservationVariableDTO(object):
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
        'context_of_use': 'list[str]',
        'crop': 'str',
        'default_value': 'str',
        'documentation_url': 'str',
        'growth_stage': 'str',
        'institution': 'str',
        'language': 'str',
        'method': 'BrAPIv1MethodDTO',
        'ontology_reference': 'BrAPIv1OntologyReferenceDTO',
        'scale': 'BrAPIv1ScaleDTO',
        'scientist': 'str',
        'status': 'str',
        'submission_timestamp': 'str',
        'synonyms': 'list[str]',
        'trait': 'BrAPIv1TraitDTO',
        'xref': 'str',
        'observation_variable_db_id': 'str',
        'observation_variable_name': 'str',
        'study_db_id': 'str',
        'trial_name': 'str'
    }

    attribute_map = {
        'context_of_use': 'contextOfUse',
        'crop': 'crop',
        'default_value': 'defaultValue',
        'documentation_url': 'documentationURL',
        'growth_stage': 'growthStage',
        'institution': 'institution',
        'language': 'language',
        'method': 'method',
        'ontology_reference': 'ontologyReference',
        'scale': 'scale',
        'scientist': 'scientist',
        'status': 'status',
        'submission_timestamp': 'submissionTimestamp',
        'synonyms': 'synonyms',
        'trait': 'trait',
        'xref': 'xref',
        'observation_variable_db_id': 'observationVariableDbId',
        'observation_variable_name': 'observationVariableName',
        'study_db_id': 'studyDbId',
        'trial_name': 'trialName'
    }
    def __init__(self,
        context_of_use : 'List[str]' = None,
        crop : 'str' = None,
        default_value : 'str' = None,
        documentation_url : 'str' = None,
        growth_stage : 'str' = None,
        institution : 'str' = None,
        language : 'str' = None,
        method : 'BrAPIv1MethodDTO' = None,
        ontology_reference : 'BrAPIv1OntologyReferenceDTO' = None,
        scale : 'BrAPIv1ScaleDTO' = None,
        scientist : 'str' = None,
        status : 'str' = None,
        submission_timestamp : 'str' = None,
        synonyms : 'List[str]' = None,
        trait : 'BrAPIv1TraitDTO' = None,
        xref : 'str' = None,
        observation_variable_db_id : 'str' = None,
        observation_variable_name : 'str' = None,
        study_db_id : 'str' = None,
        trial_name : 'str' = None):  # noqa: E501
        """BrAPIv1ObservationVariableDTO - a model defined in Swagger"""  # noqa: E501

        self._context_of_use = None
        self._crop = None
        self._default_value = None
        self._documentation_url = None
        self._growth_stage = None
        self._institution = None
        self._language = None
        self._method = None
        self._ontology_reference = None
        self._scale = None
        self._scientist = None
        self._status = None
        self._submission_timestamp = None
        self._synonyms = None
        self._trait = None
        self._xref = None
        self._observation_variable_db_id = None
        self._observation_variable_name = None
        self._study_db_id = None
        self._trial_name = None
        self.discriminator = None

        if context_of_use is not None:
            self.context_of_use = context_of_use
        if crop is not None:
            self.crop = crop
        if default_value is not None:
            self.default_value = default_value
        if documentation_url is not None:
            self.documentation_url = documentation_url
        if growth_stage is not None:
            self.growth_stage = growth_stage
        if institution is not None:
            self.institution = institution
        if language is not None:
            self.language = language
        if method is not None:
            self.method = method
        if ontology_reference is not None:
            self.ontology_reference = ontology_reference
        if scale is not None:
            self.scale = scale
        if scientist is not None:
            self.scientist = scientist
        if status is not None:
            self.status = status
        if submission_timestamp is not None:
            self.submission_timestamp = submission_timestamp
        if synonyms is not None:
            self.synonyms = synonyms
        if trait is not None:
            self.trait = trait
        if xref is not None:
            self.xref = xref
        if observation_variable_db_id is not None:
            self.observation_variable_db_id = observation_variable_db_id
        if observation_variable_name is not None:
            self.observation_variable_name = observation_variable_name
        if study_db_id is not None:
            self.study_db_id = study_db_id
        if trial_name is not None:
            self.trial_name = trial_name

    @property
    def context_of_use(self):
        """Gets the context_of_use of this BrAPIv1ObservationVariableDTO.  # noqa: E501


        :return: The context_of_use of this BrAPIv1ObservationVariableDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._context_of_use

    @context_of_use.setter
    def context_of_use(self, context_of_use):
        """Sets the context_of_use of this BrAPIv1ObservationVariableDTO.


        :param context_of_use: The context_of_use of this BrAPIv1ObservationVariableDTO.  # noqa: E501
        :type: list[str]
        """

        self._context_of_use = context_of_use

    @property
    def crop(self):
        """Gets the crop of this BrAPIv1ObservationVariableDTO.  # noqa: E501


        :return: The crop of this BrAPIv1ObservationVariableDTO.  # noqa: E501
        :rtype: str
        """
        return self._crop

    @crop.setter
    def crop(self, crop):
        """Sets the crop of this BrAPIv1ObservationVariableDTO.


        :param crop: The crop of this BrAPIv1ObservationVariableDTO.  # noqa: E501
        :type: str
        """

        self._crop = crop

    @property
    def default_value(self):
        """Gets the default_value of this BrAPIv1ObservationVariableDTO.  # noqa: E501


        :return: The default_value of this BrAPIv1ObservationVariableDTO.  # noqa: E501
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this BrAPIv1ObservationVariableDTO.


        :param default_value: The default_value of this BrAPIv1ObservationVariableDTO.  # noqa: E501
        :type: str
        """

        self._default_value = default_value

    @property
    def documentation_url(self):
        """Gets the documentation_url of this BrAPIv1ObservationVariableDTO.  # noqa: E501


        :return: The documentation_url of this BrAPIv1ObservationVariableDTO.  # noqa: E501
        :rtype: str
        """
        return self._documentation_url

    @documentation_url.setter
    def documentation_url(self, documentation_url):
        """Sets the documentation_url of this BrAPIv1ObservationVariableDTO.


        :param documentation_url: The documentation_url of this BrAPIv1ObservationVariableDTO.  # noqa: E501
        :type: str
        """

        self._documentation_url = documentation_url

    @property
    def growth_stage(self):
        """Gets the growth_stage of this BrAPIv1ObservationVariableDTO.  # noqa: E501


        :return: The growth_stage of this BrAPIv1ObservationVariableDTO.  # noqa: E501
        :rtype: str
        """
        return self._growth_stage

    @growth_stage.setter
    def growth_stage(self, growth_stage):
        """Sets the growth_stage of this BrAPIv1ObservationVariableDTO.


        :param growth_stage: The growth_stage of this BrAPIv1ObservationVariableDTO.  # noqa: E501
        :type: str
        """

        self._growth_stage = growth_stage

    @property
    def institution(self):
        """Gets the institution of this BrAPIv1ObservationVariableDTO.  # noqa: E501


        :return: The institution of this BrAPIv1ObservationVariableDTO.  # noqa: E501
        :rtype: str
        """
        return self._institution

    @institution.setter
    def institution(self, institution):
        """Sets the institution of this BrAPIv1ObservationVariableDTO.


        :param institution: The institution of this BrAPIv1ObservationVariableDTO.  # noqa: E501
        :type: str
        """

        self._institution = institution

    @property
    def language(self):
        """Gets the language of this BrAPIv1ObservationVariableDTO.  # noqa: E501


        :return: The language of this BrAPIv1ObservationVariableDTO.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this BrAPIv1ObservationVariableDTO.


        :param language: The language of this BrAPIv1ObservationVariableDTO.  # noqa: E501
        :type: str
        """

        self._language = language

    @property
    def method(self):
        """Gets the method of this BrAPIv1ObservationVariableDTO.  # noqa: E501


        :return: The method of this BrAPIv1ObservationVariableDTO.  # noqa: E501
        :rtype: BrAPIv1MethodDTO
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this BrAPIv1ObservationVariableDTO.


        :param method: The method of this BrAPIv1ObservationVariableDTO.  # noqa: E501
        :type: BrAPIv1MethodDTO
        """

        self._method = method

    @property
    def ontology_reference(self):
        """Gets the ontology_reference of this BrAPIv1ObservationVariableDTO.  # noqa: E501


        :return: The ontology_reference of this BrAPIv1ObservationVariableDTO.  # noqa: E501
        :rtype: BrAPIv1OntologyReferenceDTO
        """
        return self._ontology_reference

    @ontology_reference.setter
    def ontology_reference(self, ontology_reference):
        """Sets the ontology_reference of this BrAPIv1ObservationVariableDTO.


        :param ontology_reference: The ontology_reference of this BrAPIv1ObservationVariableDTO.  # noqa: E501
        :type: BrAPIv1OntologyReferenceDTO
        """

        self._ontology_reference = ontology_reference

    @property
    def scale(self):
        """Gets the scale of this BrAPIv1ObservationVariableDTO.  # noqa: E501


        :return: The scale of this BrAPIv1ObservationVariableDTO.  # noqa: E501
        :rtype: BrAPIv1ScaleDTO
        """
        return self._scale

    @scale.setter
    def scale(self, scale):
        """Sets the scale of this BrAPIv1ObservationVariableDTO.


        :param scale: The scale of this BrAPIv1ObservationVariableDTO.  # noqa: E501
        :type: BrAPIv1ScaleDTO
        """

        self._scale = scale

    @property
    def scientist(self):
        """Gets the scientist of this BrAPIv1ObservationVariableDTO.  # noqa: E501


        :return: The scientist of this BrAPIv1ObservationVariableDTO.  # noqa: E501
        :rtype: str
        """
        return self._scientist

    @scientist.setter
    def scientist(self, scientist):
        """Sets the scientist of this BrAPIv1ObservationVariableDTO.


        :param scientist: The scientist of this BrAPIv1ObservationVariableDTO.  # noqa: E501
        :type: str
        """

        self._scientist = scientist

    @property
    def status(self):
        """Gets the status of this BrAPIv1ObservationVariableDTO.  # noqa: E501


        :return: The status of this BrAPIv1ObservationVariableDTO.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BrAPIv1ObservationVariableDTO.


        :param status: The status of this BrAPIv1ObservationVariableDTO.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def submission_timestamp(self):
        """Gets the submission_timestamp of this BrAPIv1ObservationVariableDTO.  # noqa: E501


        :return: The submission_timestamp of this BrAPIv1ObservationVariableDTO.  # noqa: E501
        :rtype: str
        """
        return self._submission_timestamp

    @submission_timestamp.setter
    def submission_timestamp(self, submission_timestamp):
        """Sets the submission_timestamp of this BrAPIv1ObservationVariableDTO.


        :param submission_timestamp: The submission_timestamp of this BrAPIv1ObservationVariableDTO.  # noqa: E501
        :type: str
        """

        self._submission_timestamp = submission_timestamp

    @property
    def synonyms(self):
        """Gets the synonyms of this BrAPIv1ObservationVariableDTO.  # noqa: E501


        :return: The synonyms of this BrAPIv1ObservationVariableDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._synonyms

    @synonyms.setter
    def synonyms(self, synonyms):
        """Sets the synonyms of this BrAPIv1ObservationVariableDTO.


        :param synonyms: The synonyms of this BrAPIv1ObservationVariableDTO.  # noqa: E501
        :type: list[str]
        """

        self._synonyms = synonyms

    @property
    def trait(self):
        """Gets the trait of this BrAPIv1ObservationVariableDTO.  # noqa: E501


        :return: The trait of this BrAPIv1ObservationVariableDTO.  # noqa: E501
        :rtype: BrAPIv1TraitDTO
        """
        return self._trait

    @trait.setter
    def trait(self, trait):
        """Sets the trait of this BrAPIv1ObservationVariableDTO.


        :param trait: The trait of this BrAPIv1ObservationVariableDTO.  # noqa: E501
        :type: BrAPIv1TraitDTO
        """

        self._trait = trait

    @property
    def xref(self):
        """Gets the xref of this BrAPIv1ObservationVariableDTO.  # noqa: E501


        :return: The xref of this BrAPIv1ObservationVariableDTO.  # noqa: E501
        :rtype: str
        """
        return self._xref

    @xref.setter
    def xref(self, xref):
        """Sets the xref of this BrAPIv1ObservationVariableDTO.


        :param xref: The xref of this BrAPIv1ObservationVariableDTO.  # noqa: E501
        :type: str
        """

        self._xref = xref

    @property
    def observation_variable_db_id(self):
        """Gets the observation_variable_db_id of this BrAPIv1ObservationVariableDTO.  # noqa: E501


        :return: The observation_variable_db_id of this BrAPIv1ObservationVariableDTO.  # noqa: E501
        :rtype: str
        """
        return self._observation_variable_db_id

    @observation_variable_db_id.setter
    def observation_variable_db_id(self, observation_variable_db_id):
        """Sets the observation_variable_db_id of this BrAPIv1ObservationVariableDTO.


        :param observation_variable_db_id: The observation_variable_db_id of this BrAPIv1ObservationVariableDTO.  # noqa: E501
        :type: str
        """

        self._observation_variable_db_id = observation_variable_db_id

    @property
    def observation_variable_name(self):
        """Gets the observation_variable_name of this BrAPIv1ObservationVariableDTO.  # noqa: E501


        :return: The observation_variable_name of this BrAPIv1ObservationVariableDTO.  # noqa: E501
        :rtype: str
        """
        return self._observation_variable_name

    @observation_variable_name.setter
    def observation_variable_name(self, observation_variable_name):
        """Sets the observation_variable_name of this BrAPIv1ObservationVariableDTO.


        :param observation_variable_name: The observation_variable_name of this BrAPIv1ObservationVariableDTO.  # noqa: E501
        :type: str
        """

        self._observation_variable_name = observation_variable_name

    @property
    def study_db_id(self):
        """Gets the study_db_id of this BrAPIv1ObservationVariableDTO.  # noqa: E501


        :return: The study_db_id of this BrAPIv1ObservationVariableDTO.  # noqa: E501
        :rtype: str
        """
        return self._study_db_id

    @study_db_id.setter
    def study_db_id(self, study_db_id):
        """Sets the study_db_id of this BrAPIv1ObservationVariableDTO.


        :param study_db_id: The study_db_id of this BrAPIv1ObservationVariableDTO.  # noqa: E501
        :type: str
        """

        self._study_db_id = study_db_id

    @property
    def trial_name(self):
        """Gets the trial_name of this BrAPIv1ObservationVariableDTO.  # noqa: E501


        :return: The trial_name of this BrAPIv1ObservationVariableDTO.  # noqa: E501
        :rtype: str
        """
        return self._trial_name

    @trial_name.setter
    def trial_name(self, trial_name):
        """Sets the trial_name of this BrAPIv1ObservationVariableDTO.


        :param trial_name: The trial_name of this BrAPIv1ObservationVariableDTO.  # noqa: E501
        :type: str
        """

        self._trial_name = trial_name

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
        if issubclass(BrAPIv1ObservationVariableDTO, dict):
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
        if issubclass(BrAPIv1ObservationVariableDTO, dict):
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
        if not isinstance(other, BrAPIv1ObservationVariableDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other


from opensilexClientToolsPython.models.br_ap_iv1_method_dto import BrAPIv1MethodDTO
from opensilexClientToolsPython.models.br_ap_iv1_ontology_reference_dto import BrAPIv1OntologyReferenceDTO
from opensilexClientToolsPython.models.br_ap_iv1_scale_dto import BrAPIv1ScaleDTO
from opensilexClientToolsPython.models.br_ap_iv1_trait_dto import BrAPIv1TraitDTO


