# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0-rc+7.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from typing import List, Dict

from opensilexClientToolsPython.models.csv_header import CsvHeader



class DataCSVValidationModel(object):
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
        'missing_headers': 'list[str]',
        'empty_headers': 'list[int]',
        'invalid_header_ur_is': 'dict(str, str)',
        'datatype_errors': 'dict(str, list[CSVDatatypeError])',
        'uri_not_found_errors': 'dict(str, list[CSVURINotFoundError])',
        'invalid_uri_errors': 'dict(str, list[CSVCell])',
        'missing_required_value_errors': 'dict(str, list[CSVCell])',
        'invalid_value_errors': 'dict(str, list[CSVCell])',
        'already_existing_uri_errors': 'dict(str, list[CSVCell])',
        'duplicate_uri_errors': 'dict(str, list[CSVDuplicateURIError])',
        'invalid_row_size_errors': 'dict(str, list[CSVCell])',
        'invalid_date_errors': 'dict(str, list[CSVCell])',
        'nb_object_imported': 'int',
        'validation_token': 'str',
        'csv_header': 'CsvHeader',
        'invalid_object_errors': 'dict(str, list[CSVCell])',
        'invalid_target_errors': 'dict(str, list[CSVCell])',
        'invalid_data_type_errors': 'dict(str, list[CSVCell])',
        'invalid_experiment_errors': 'dict(str, list[CSVCell])',
        'invalid_device_errors': 'dict(str, list[CSVCell])',
        'device_choice_ambiguity_errors': 'dict(str, list[CSVCell])',
        'duplicated_data_errors': 'dict(str, list[CSVCell])',
        'duplicated_object_errors': 'dict(str, list[CSVCell])',
        'duplicated_target_errors': 'dict(str, list[CSVCell])',
        'duplicated_experiment_errors': 'dict(str, list[CSVCell])',
        'duplicated_device_errors': 'dict(str, list[CSVCell])',
        'headers': 'list[str]',
        'headers_labels': 'list[str]',
        'nb_lines_imported': 'int',
        'nb_lines_to_import': 'int',
        'validation_step': 'bool',
        'insertion_step': 'bool',
        'valid_csv': 'bool',
        'too_large_dataset': 'bool',
        'error_message': 'str'
    }

    attribute_map = {
        'missing_headers': 'missingHeaders',
        'empty_headers': 'emptyHeaders',
        'invalid_header_ur_is': 'invalidHeaderURIs',
        'datatype_errors': 'datatypeErrors',
        'uri_not_found_errors': 'uriNotFoundErrors',
        'invalid_uri_errors': 'invalidURIErrors',
        'missing_required_value_errors': 'missingRequiredValueErrors',
        'invalid_value_errors': 'invalidValueErrors',
        'already_existing_uri_errors': 'alreadyExistingURIErrors',
        'duplicate_uri_errors': 'duplicateURIErrors',
        'invalid_row_size_errors': 'invalidRowSizeErrors',
        'invalid_date_errors': 'invalidDateErrors',
        'nb_object_imported': 'nbObjectImported',
        'validation_token': 'validationToken',
        'csv_header': 'csvHeader',
        'invalid_object_errors': 'invalidObjectErrors',
        'invalid_target_errors': 'invalidTargetErrors',
        'invalid_data_type_errors': 'invalidDataTypeErrors',
        'invalid_experiment_errors': 'invalidExperimentErrors',
        'invalid_device_errors': 'invalidDeviceErrors',
        'device_choice_ambiguity_errors': 'deviceChoiceAmbiguityErrors',
        'duplicated_data_errors': 'duplicatedDataErrors',
        'duplicated_object_errors': 'duplicatedObjectErrors',
        'duplicated_target_errors': 'duplicatedTargetErrors',
        'duplicated_experiment_errors': 'duplicatedExperimentErrors',
        'duplicated_device_errors': 'duplicatedDeviceErrors',
        'headers': 'headers',
        'headers_labels': 'headersLabels',
        'nb_lines_imported': 'nbLinesImported',
        'nb_lines_to_import': 'nbLinesToImport',
        'validation_step': 'validationStep',
        'insertion_step': 'insertionStep',
        'valid_csv': 'validCSV',
        'too_large_dataset': 'tooLargeDataset',
        'error_message': 'errorMessage'
    }
    def __init__(self,
        missing_headers : 'List[str]' = None,
        empty_headers : 'List[int]' = None,
        invalid_header_ur_is : 'Dict[str, str]' = None,
        datatype_errors : 'Dict[str, list]' = None,
        uri_not_found_errors : 'Dict[str, list]' = None,
        invalid_uri_errors : 'Dict[str, list]' = None,
        missing_required_value_errors : 'Dict[str, list]' = None,
        invalid_value_errors : 'Dict[str, list]' = None,
        already_existing_uri_errors : 'Dict[str, list]' = None,
        duplicate_uri_errors : 'Dict[str, list]' = None,
        invalid_row_size_errors : 'Dict[str, list]' = None,
        invalid_date_errors : 'Dict[str, list]' = None,
        nb_object_imported : 'int' = None,
        validation_token : 'str' = None,
        csv_header : 'CsvHeader' = None,
        invalid_object_errors : 'Dict[str, list]' = None,
        invalid_target_errors : 'Dict[str, list]' = None,
        invalid_data_type_errors : 'Dict[str, list]' = None,
        invalid_experiment_errors : 'Dict[str, list]' = None,
        invalid_device_errors : 'Dict[str, list]' = None,
        device_choice_ambiguity_errors : 'Dict[str, list]' = None,
        duplicated_data_errors : 'Dict[str, list]' = None,
        duplicated_object_errors : 'Dict[str, list]' = None,
        duplicated_target_errors : 'Dict[str, list]' = None,
        duplicated_experiment_errors : 'Dict[str, list]' = None,
        duplicated_device_errors : 'Dict[str, list]' = None,
        headers : 'List[str]' = None,
        headers_labels : 'List[str]' = None,
        nb_lines_imported : 'int' = None,
        nb_lines_to_import : 'int' = None,
        validation_step : 'bool' = None,
        insertion_step : 'bool' = None,
        valid_csv : 'bool' = None,
        too_large_dataset : 'bool' = None,
        error_message : 'str' = None):  # noqa: E501
        """DataCSVValidationModel - a model defined in Swagger"""  # noqa: E501

        self._missing_headers = None
        self._empty_headers = None
        self._invalid_header_ur_is = None
        self._datatype_errors = None
        self._uri_not_found_errors = None
        self._invalid_uri_errors = None
        self._missing_required_value_errors = None
        self._invalid_value_errors = None
        self._already_existing_uri_errors = None
        self._duplicate_uri_errors = None
        self._invalid_row_size_errors = None
        self._invalid_date_errors = None
        self._nb_object_imported = None
        self._validation_token = None
        self._csv_header = None
        self._invalid_object_errors = None
        self._invalid_target_errors = None
        self._invalid_data_type_errors = None
        self._invalid_experiment_errors = None
        self._invalid_device_errors = None
        self._device_choice_ambiguity_errors = None
        self._duplicated_data_errors = None
        self._duplicated_object_errors = None
        self._duplicated_target_errors = None
        self._duplicated_experiment_errors = None
        self._duplicated_device_errors = None
        self._headers = None
        self._headers_labels = None
        self._nb_lines_imported = None
        self._nb_lines_to_import = None
        self._validation_step = None
        self._insertion_step = None
        self._valid_csv = None
        self._too_large_dataset = None
        self._error_message = None
        self.discriminator = None

        if missing_headers is not None:
            self.missing_headers = missing_headers
        if empty_headers is not None:
            self.empty_headers = empty_headers
        if invalid_header_ur_is is not None:
            self.invalid_header_ur_is = invalid_header_ur_is
        if datatype_errors is not None:
            self.datatype_errors = datatype_errors
        if uri_not_found_errors is not None:
            self.uri_not_found_errors = uri_not_found_errors
        if invalid_uri_errors is not None:
            self.invalid_uri_errors = invalid_uri_errors
        if missing_required_value_errors is not None:
            self.missing_required_value_errors = missing_required_value_errors
        if invalid_value_errors is not None:
            self.invalid_value_errors = invalid_value_errors
        if already_existing_uri_errors is not None:
            self.already_existing_uri_errors = already_existing_uri_errors
        if duplicate_uri_errors is not None:
            self.duplicate_uri_errors = duplicate_uri_errors
        if invalid_row_size_errors is not None:
            self.invalid_row_size_errors = invalid_row_size_errors
        if invalid_date_errors is not None:
            self.invalid_date_errors = invalid_date_errors
        if nb_object_imported is not None:
            self.nb_object_imported = nb_object_imported
        if validation_token is not None:
            self.validation_token = validation_token
        if csv_header is not None:
            self.csv_header = csv_header
        if invalid_object_errors is not None:
            self.invalid_object_errors = invalid_object_errors
        if invalid_target_errors is not None:
            self.invalid_target_errors = invalid_target_errors
        if invalid_data_type_errors is not None:
            self.invalid_data_type_errors = invalid_data_type_errors
        if invalid_experiment_errors is not None:
            self.invalid_experiment_errors = invalid_experiment_errors
        if invalid_device_errors is not None:
            self.invalid_device_errors = invalid_device_errors
        if device_choice_ambiguity_errors is not None:
            self.device_choice_ambiguity_errors = device_choice_ambiguity_errors
        if duplicated_data_errors is not None:
            self.duplicated_data_errors = duplicated_data_errors
        if duplicated_object_errors is not None:
            self.duplicated_object_errors = duplicated_object_errors
        if duplicated_target_errors is not None:
            self.duplicated_target_errors = duplicated_target_errors
        if duplicated_experiment_errors is not None:
            self.duplicated_experiment_errors = duplicated_experiment_errors
        if duplicated_device_errors is not None:
            self.duplicated_device_errors = duplicated_device_errors
        if headers is not None:
            self.headers = headers
        if headers_labels is not None:
            self.headers_labels = headers_labels
        if nb_lines_imported is not None:
            self.nb_lines_imported = nb_lines_imported
        if nb_lines_to_import is not None:
            self.nb_lines_to_import = nb_lines_to_import
        if validation_step is not None:
            self.validation_step = validation_step
        if insertion_step is not None:
            self.insertion_step = insertion_step
        if valid_csv is not None:
            self.valid_csv = valid_csv
        if too_large_dataset is not None:
            self.too_large_dataset = too_large_dataset
        if error_message is not None:
            self.error_message = error_message

    @property
    def missing_headers(self):
        """Gets the missing_headers of this DataCSVValidationModel.  # noqa: E501


        :return: The missing_headers of this DataCSVValidationModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._missing_headers

    @missing_headers.setter
    def missing_headers(self, missing_headers):
        """Sets the missing_headers of this DataCSVValidationModel.


        :param missing_headers: The missing_headers of this DataCSVValidationModel.  # noqa: E501
        :type: list[str]
        """

        self._missing_headers = missing_headers

    @property
    def empty_headers(self):
        """Gets the empty_headers of this DataCSVValidationModel.  # noqa: E501


        :return: The empty_headers of this DataCSVValidationModel.  # noqa: E501
        :rtype: list[int]
        """
        return self._empty_headers

    @empty_headers.setter
    def empty_headers(self, empty_headers):
        """Sets the empty_headers of this DataCSVValidationModel.


        :param empty_headers: The empty_headers of this DataCSVValidationModel.  # noqa: E501
        :type: list[int]
        """

        self._empty_headers = empty_headers

    @property
    def invalid_header_ur_is(self):
        """Gets the invalid_header_ur_is of this DataCSVValidationModel.  # noqa: E501


        :return: The invalid_header_ur_is of this DataCSVValidationModel.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._invalid_header_ur_is

    @invalid_header_ur_is.setter
    def invalid_header_ur_is(self, invalid_header_ur_is):
        """Sets the invalid_header_ur_is of this DataCSVValidationModel.


        :param invalid_header_ur_is: The invalid_header_ur_is of this DataCSVValidationModel.  # noqa: E501
        :type: dict(str, str)
        """

        self._invalid_header_ur_is = invalid_header_ur_is

    @property
    def datatype_errors(self):
        """Gets the datatype_errors of this DataCSVValidationModel.  # noqa: E501


        :return: The datatype_errors of this DataCSVValidationModel.  # noqa: E501
        :rtype: dict(str, list[CSVDatatypeError])
        """
        return self._datatype_errors

    @datatype_errors.setter
    def datatype_errors(self, datatype_errors):
        """Sets the datatype_errors of this DataCSVValidationModel.


        :param datatype_errors: The datatype_errors of this DataCSVValidationModel.  # noqa: E501
        :type: dict(str, list[CSVDatatypeError])
        """

        self._datatype_errors = datatype_errors

    @property
    def uri_not_found_errors(self):
        """Gets the uri_not_found_errors of this DataCSVValidationModel.  # noqa: E501


        :return: The uri_not_found_errors of this DataCSVValidationModel.  # noqa: E501
        :rtype: dict(str, list[CSVURINotFoundError])
        """
        return self._uri_not_found_errors

    @uri_not_found_errors.setter
    def uri_not_found_errors(self, uri_not_found_errors):
        """Sets the uri_not_found_errors of this DataCSVValidationModel.


        :param uri_not_found_errors: The uri_not_found_errors of this DataCSVValidationModel.  # noqa: E501
        :type: dict(str, list[CSVURINotFoundError])
        """

        self._uri_not_found_errors = uri_not_found_errors

    @property
    def invalid_uri_errors(self):
        """Gets the invalid_uri_errors of this DataCSVValidationModel.  # noqa: E501


        :return: The invalid_uri_errors of this DataCSVValidationModel.  # noqa: E501
        :rtype: dict(str, list[CSVCell])
        """
        return self._invalid_uri_errors

    @invalid_uri_errors.setter
    def invalid_uri_errors(self, invalid_uri_errors):
        """Sets the invalid_uri_errors of this DataCSVValidationModel.


        :param invalid_uri_errors: The invalid_uri_errors of this DataCSVValidationModel.  # noqa: E501
        :type: dict(str, list[CSVCell])
        """

        self._invalid_uri_errors = invalid_uri_errors

    @property
    def missing_required_value_errors(self):
        """Gets the missing_required_value_errors of this DataCSVValidationModel.  # noqa: E501


        :return: The missing_required_value_errors of this DataCSVValidationModel.  # noqa: E501
        :rtype: dict(str, list[CSVCell])
        """
        return self._missing_required_value_errors

    @missing_required_value_errors.setter
    def missing_required_value_errors(self, missing_required_value_errors):
        """Sets the missing_required_value_errors of this DataCSVValidationModel.


        :param missing_required_value_errors: The missing_required_value_errors of this DataCSVValidationModel.  # noqa: E501
        :type: dict(str, list[CSVCell])
        """

        self._missing_required_value_errors = missing_required_value_errors

    @property
    def invalid_value_errors(self):
        """Gets the invalid_value_errors of this DataCSVValidationModel.  # noqa: E501


        :return: The invalid_value_errors of this DataCSVValidationModel.  # noqa: E501
        :rtype: dict(str, list[CSVCell])
        """
        return self._invalid_value_errors

    @invalid_value_errors.setter
    def invalid_value_errors(self, invalid_value_errors):
        """Sets the invalid_value_errors of this DataCSVValidationModel.


        :param invalid_value_errors: The invalid_value_errors of this DataCSVValidationModel.  # noqa: E501
        :type: dict(str, list[CSVCell])
        """

        self._invalid_value_errors = invalid_value_errors

    @property
    def already_existing_uri_errors(self):
        """Gets the already_existing_uri_errors of this DataCSVValidationModel.  # noqa: E501


        :return: The already_existing_uri_errors of this DataCSVValidationModel.  # noqa: E501
        :rtype: dict(str, list[CSVCell])
        """
        return self._already_existing_uri_errors

    @already_existing_uri_errors.setter
    def already_existing_uri_errors(self, already_existing_uri_errors):
        """Sets the already_existing_uri_errors of this DataCSVValidationModel.


        :param already_existing_uri_errors: The already_existing_uri_errors of this DataCSVValidationModel.  # noqa: E501
        :type: dict(str, list[CSVCell])
        """

        self._already_existing_uri_errors = already_existing_uri_errors

    @property
    def duplicate_uri_errors(self):
        """Gets the duplicate_uri_errors of this DataCSVValidationModel.  # noqa: E501


        :return: The duplicate_uri_errors of this DataCSVValidationModel.  # noqa: E501
        :rtype: dict(str, list[CSVDuplicateURIError])
        """
        return self._duplicate_uri_errors

    @duplicate_uri_errors.setter
    def duplicate_uri_errors(self, duplicate_uri_errors):
        """Sets the duplicate_uri_errors of this DataCSVValidationModel.


        :param duplicate_uri_errors: The duplicate_uri_errors of this DataCSVValidationModel.  # noqa: E501
        :type: dict(str, list[CSVDuplicateURIError])
        """

        self._duplicate_uri_errors = duplicate_uri_errors

    @property
    def invalid_row_size_errors(self):
        """Gets the invalid_row_size_errors of this DataCSVValidationModel.  # noqa: E501


        :return: The invalid_row_size_errors of this DataCSVValidationModel.  # noqa: E501
        :rtype: dict(str, list[CSVCell])
        """
        return self._invalid_row_size_errors

    @invalid_row_size_errors.setter
    def invalid_row_size_errors(self, invalid_row_size_errors):
        """Sets the invalid_row_size_errors of this DataCSVValidationModel.


        :param invalid_row_size_errors: The invalid_row_size_errors of this DataCSVValidationModel.  # noqa: E501
        :type: dict(str, list[CSVCell])
        """

        self._invalid_row_size_errors = invalid_row_size_errors

    @property
    def invalid_date_errors(self):
        """Gets the invalid_date_errors of this DataCSVValidationModel.  # noqa: E501


        :return: The invalid_date_errors of this DataCSVValidationModel.  # noqa: E501
        :rtype: dict(str, list[CSVCell])
        """
        return self._invalid_date_errors

    @invalid_date_errors.setter
    def invalid_date_errors(self, invalid_date_errors):
        """Sets the invalid_date_errors of this DataCSVValidationModel.


        :param invalid_date_errors: The invalid_date_errors of this DataCSVValidationModel.  # noqa: E501
        :type: dict(str, list[CSVCell])
        """

        self._invalid_date_errors = invalid_date_errors

    @property
    def nb_object_imported(self):
        """Gets the nb_object_imported of this DataCSVValidationModel.  # noqa: E501


        :return: The nb_object_imported of this DataCSVValidationModel.  # noqa: E501
        :rtype: int
        """
        return self._nb_object_imported

    @nb_object_imported.setter
    def nb_object_imported(self, nb_object_imported):
        """Sets the nb_object_imported of this DataCSVValidationModel.


        :param nb_object_imported: The nb_object_imported of this DataCSVValidationModel.  # noqa: E501
        :type: int
        """

        self._nb_object_imported = nb_object_imported

    @property
    def validation_token(self):
        """Gets the validation_token of this DataCSVValidationModel.  # noqa: E501


        :return: The validation_token of this DataCSVValidationModel.  # noqa: E501
        :rtype: str
        """
        return self._validation_token

    @validation_token.setter
    def validation_token(self, validation_token):
        """Sets the validation_token of this DataCSVValidationModel.


        :param validation_token: The validation_token of this DataCSVValidationModel.  # noqa: E501
        :type: str
        """

        self._validation_token = validation_token

    @property
    def csv_header(self):
        """Gets the csv_header of this DataCSVValidationModel.  # noqa: E501


        :return: The csv_header of this DataCSVValidationModel.  # noqa: E501
        :rtype: CsvHeader
        """
        return self._csv_header

    @csv_header.setter
    def csv_header(self, csv_header):
        """Sets the csv_header of this DataCSVValidationModel.


        :param csv_header: The csv_header of this DataCSVValidationModel.  # noqa: E501
        :type: CsvHeader
        """

        self._csv_header = csv_header

    @property
    def invalid_object_errors(self):
        """Gets the invalid_object_errors of this DataCSVValidationModel.  # noqa: E501


        :return: The invalid_object_errors of this DataCSVValidationModel.  # noqa: E501
        :rtype: dict(str, list[CSVCell])
        """
        return self._invalid_object_errors

    @invalid_object_errors.setter
    def invalid_object_errors(self, invalid_object_errors):
        """Sets the invalid_object_errors of this DataCSVValidationModel.


        :param invalid_object_errors: The invalid_object_errors of this DataCSVValidationModel.  # noqa: E501
        :type: dict(str, list[CSVCell])
        """

        self._invalid_object_errors = invalid_object_errors

    @property
    def invalid_target_errors(self):
        """Gets the invalid_target_errors of this DataCSVValidationModel.  # noqa: E501


        :return: The invalid_target_errors of this DataCSVValidationModel.  # noqa: E501
        :rtype: dict(str, list[CSVCell])
        """
        return self._invalid_target_errors

    @invalid_target_errors.setter
    def invalid_target_errors(self, invalid_target_errors):
        """Sets the invalid_target_errors of this DataCSVValidationModel.


        :param invalid_target_errors: The invalid_target_errors of this DataCSVValidationModel.  # noqa: E501
        :type: dict(str, list[CSVCell])
        """

        self._invalid_target_errors = invalid_target_errors

    @property
    def invalid_data_type_errors(self):
        """Gets the invalid_data_type_errors of this DataCSVValidationModel.  # noqa: E501


        :return: The invalid_data_type_errors of this DataCSVValidationModel.  # noqa: E501
        :rtype: dict(str, list[CSVCell])
        """
        return self._invalid_data_type_errors

    @invalid_data_type_errors.setter
    def invalid_data_type_errors(self, invalid_data_type_errors):
        """Sets the invalid_data_type_errors of this DataCSVValidationModel.


        :param invalid_data_type_errors: The invalid_data_type_errors of this DataCSVValidationModel.  # noqa: E501
        :type: dict(str, list[CSVCell])
        """

        self._invalid_data_type_errors = invalid_data_type_errors

    @property
    def invalid_experiment_errors(self):
        """Gets the invalid_experiment_errors of this DataCSVValidationModel.  # noqa: E501


        :return: The invalid_experiment_errors of this DataCSVValidationModel.  # noqa: E501
        :rtype: dict(str, list[CSVCell])
        """
        return self._invalid_experiment_errors

    @invalid_experiment_errors.setter
    def invalid_experiment_errors(self, invalid_experiment_errors):
        """Sets the invalid_experiment_errors of this DataCSVValidationModel.


        :param invalid_experiment_errors: The invalid_experiment_errors of this DataCSVValidationModel.  # noqa: E501
        :type: dict(str, list[CSVCell])
        """

        self._invalid_experiment_errors = invalid_experiment_errors

    @property
    def invalid_device_errors(self):
        """Gets the invalid_device_errors of this DataCSVValidationModel.  # noqa: E501


        :return: The invalid_device_errors of this DataCSVValidationModel.  # noqa: E501
        :rtype: dict(str, list[CSVCell])
        """
        return self._invalid_device_errors

    @invalid_device_errors.setter
    def invalid_device_errors(self, invalid_device_errors):
        """Sets the invalid_device_errors of this DataCSVValidationModel.


        :param invalid_device_errors: The invalid_device_errors of this DataCSVValidationModel.  # noqa: E501
        :type: dict(str, list[CSVCell])
        """

        self._invalid_device_errors = invalid_device_errors

    @property
    def device_choice_ambiguity_errors(self):
        """Gets the device_choice_ambiguity_errors of this DataCSVValidationModel.  # noqa: E501


        :return: The device_choice_ambiguity_errors of this DataCSVValidationModel.  # noqa: E501
        :rtype: dict(str, list[CSVCell])
        """
        return self._device_choice_ambiguity_errors

    @device_choice_ambiguity_errors.setter
    def device_choice_ambiguity_errors(self, device_choice_ambiguity_errors):
        """Sets the device_choice_ambiguity_errors of this DataCSVValidationModel.


        :param device_choice_ambiguity_errors: The device_choice_ambiguity_errors of this DataCSVValidationModel.  # noqa: E501
        :type: dict(str, list[CSVCell])
        """

        self._device_choice_ambiguity_errors = device_choice_ambiguity_errors

    @property
    def duplicated_data_errors(self):
        """Gets the duplicated_data_errors of this DataCSVValidationModel.  # noqa: E501


        :return: The duplicated_data_errors of this DataCSVValidationModel.  # noqa: E501
        :rtype: dict(str, list[CSVCell])
        """
        return self._duplicated_data_errors

    @duplicated_data_errors.setter
    def duplicated_data_errors(self, duplicated_data_errors):
        """Sets the duplicated_data_errors of this DataCSVValidationModel.


        :param duplicated_data_errors: The duplicated_data_errors of this DataCSVValidationModel.  # noqa: E501
        :type: dict(str, list[CSVCell])
        """

        self._duplicated_data_errors = duplicated_data_errors

    @property
    def duplicated_object_errors(self):
        """Gets the duplicated_object_errors of this DataCSVValidationModel.  # noqa: E501


        :return: The duplicated_object_errors of this DataCSVValidationModel.  # noqa: E501
        :rtype: dict(str, list[CSVCell])
        """
        return self._duplicated_object_errors

    @duplicated_object_errors.setter
    def duplicated_object_errors(self, duplicated_object_errors):
        """Sets the duplicated_object_errors of this DataCSVValidationModel.


        :param duplicated_object_errors: The duplicated_object_errors of this DataCSVValidationModel.  # noqa: E501
        :type: dict(str, list[CSVCell])
        """

        self._duplicated_object_errors = duplicated_object_errors

    @property
    def duplicated_target_errors(self):
        """Gets the duplicated_target_errors of this DataCSVValidationModel.  # noqa: E501


        :return: The duplicated_target_errors of this DataCSVValidationModel.  # noqa: E501
        :rtype: dict(str, list[CSVCell])
        """
        return self._duplicated_target_errors

    @duplicated_target_errors.setter
    def duplicated_target_errors(self, duplicated_target_errors):
        """Sets the duplicated_target_errors of this DataCSVValidationModel.


        :param duplicated_target_errors: The duplicated_target_errors of this DataCSVValidationModel.  # noqa: E501
        :type: dict(str, list[CSVCell])
        """

        self._duplicated_target_errors = duplicated_target_errors

    @property
    def duplicated_experiment_errors(self):
        """Gets the duplicated_experiment_errors of this DataCSVValidationModel.  # noqa: E501


        :return: The duplicated_experiment_errors of this DataCSVValidationModel.  # noqa: E501
        :rtype: dict(str, list[CSVCell])
        """
        return self._duplicated_experiment_errors

    @duplicated_experiment_errors.setter
    def duplicated_experiment_errors(self, duplicated_experiment_errors):
        """Sets the duplicated_experiment_errors of this DataCSVValidationModel.


        :param duplicated_experiment_errors: The duplicated_experiment_errors of this DataCSVValidationModel.  # noqa: E501
        :type: dict(str, list[CSVCell])
        """

        self._duplicated_experiment_errors = duplicated_experiment_errors

    @property
    def duplicated_device_errors(self):
        """Gets the duplicated_device_errors of this DataCSVValidationModel.  # noqa: E501


        :return: The duplicated_device_errors of this DataCSVValidationModel.  # noqa: E501
        :rtype: dict(str, list[CSVCell])
        """
        return self._duplicated_device_errors

    @duplicated_device_errors.setter
    def duplicated_device_errors(self, duplicated_device_errors):
        """Sets the duplicated_device_errors of this DataCSVValidationModel.


        :param duplicated_device_errors: The duplicated_device_errors of this DataCSVValidationModel.  # noqa: E501
        :type: dict(str, list[CSVCell])
        """

        self._duplicated_device_errors = duplicated_device_errors

    @property
    def headers(self):
        """Gets the headers of this DataCSVValidationModel.  # noqa: E501


        :return: The headers of this DataCSVValidationModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this DataCSVValidationModel.


        :param headers: The headers of this DataCSVValidationModel.  # noqa: E501
        :type: list[str]
        """

        self._headers = headers

    @property
    def headers_labels(self):
        """Gets the headers_labels of this DataCSVValidationModel.  # noqa: E501


        :return: The headers_labels of this DataCSVValidationModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._headers_labels

    @headers_labels.setter
    def headers_labels(self, headers_labels):
        """Sets the headers_labels of this DataCSVValidationModel.


        :param headers_labels: The headers_labels of this DataCSVValidationModel.  # noqa: E501
        :type: list[str]
        """

        self._headers_labels = headers_labels

    @property
    def nb_lines_imported(self):
        """Gets the nb_lines_imported of this DataCSVValidationModel.  # noqa: E501


        :return: The nb_lines_imported of this DataCSVValidationModel.  # noqa: E501
        :rtype: int
        """
        return self._nb_lines_imported

    @nb_lines_imported.setter
    def nb_lines_imported(self, nb_lines_imported):
        """Sets the nb_lines_imported of this DataCSVValidationModel.


        :param nb_lines_imported: The nb_lines_imported of this DataCSVValidationModel.  # noqa: E501
        :type: int
        """

        self._nb_lines_imported = nb_lines_imported

    @property
    def nb_lines_to_import(self):
        """Gets the nb_lines_to_import of this DataCSVValidationModel.  # noqa: E501


        :return: The nb_lines_to_import of this DataCSVValidationModel.  # noqa: E501
        :rtype: int
        """
        return self._nb_lines_to_import

    @nb_lines_to_import.setter
    def nb_lines_to_import(self, nb_lines_to_import):
        """Sets the nb_lines_to_import of this DataCSVValidationModel.


        :param nb_lines_to_import: The nb_lines_to_import of this DataCSVValidationModel.  # noqa: E501
        :type: int
        """

        self._nb_lines_to_import = nb_lines_to_import

    @property
    def validation_step(self):
        """Gets the validation_step of this DataCSVValidationModel.  # noqa: E501


        :return: The validation_step of this DataCSVValidationModel.  # noqa: E501
        :rtype: bool
        """
        return self._validation_step

    @validation_step.setter
    def validation_step(self, validation_step):
        """Sets the validation_step of this DataCSVValidationModel.


        :param validation_step: The validation_step of this DataCSVValidationModel.  # noqa: E501
        :type: bool
        """

        self._validation_step = validation_step

    @property
    def insertion_step(self):
        """Gets the insertion_step of this DataCSVValidationModel.  # noqa: E501


        :return: The insertion_step of this DataCSVValidationModel.  # noqa: E501
        :rtype: bool
        """
        return self._insertion_step

    @insertion_step.setter
    def insertion_step(self, insertion_step):
        """Sets the insertion_step of this DataCSVValidationModel.


        :param insertion_step: The insertion_step of this DataCSVValidationModel.  # noqa: E501
        :type: bool
        """

        self._insertion_step = insertion_step

    @property
    def valid_csv(self):
        """Gets the valid_csv of this DataCSVValidationModel.  # noqa: E501


        :return: The valid_csv of this DataCSVValidationModel.  # noqa: E501
        :rtype: bool
        """
        return self._valid_csv

    @valid_csv.setter
    def valid_csv(self, valid_csv):
        """Sets the valid_csv of this DataCSVValidationModel.


        :param valid_csv: The valid_csv of this DataCSVValidationModel.  # noqa: E501
        :type: bool
        """

        self._valid_csv = valid_csv

    @property
    def too_large_dataset(self):
        """Gets the too_large_dataset of this DataCSVValidationModel.  # noqa: E501


        :return: The too_large_dataset of this DataCSVValidationModel.  # noqa: E501
        :rtype: bool
        """
        return self._too_large_dataset

    @too_large_dataset.setter
    def too_large_dataset(self, too_large_dataset):
        """Sets the too_large_dataset of this DataCSVValidationModel.


        :param too_large_dataset: The too_large_dataset of this DataCSVValidationModel.  # noqa: E501
        :type: bool
        """

        self._too_large_dataset = too_large_dataset

    @property
    def error_message(self):
        """Gets the error_message of this DataCSVValidationModel.  # noqa: E501


        :return: The error_message of this DataCSVValidationModel.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this DataCSVValidationModel.


        :param error_message: The error_message of this DataCSVValidationModel.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

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
        if issubclass(DataCSVValidationModel, dict):
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
        if not isinstance(other, DataCSVValidationModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

