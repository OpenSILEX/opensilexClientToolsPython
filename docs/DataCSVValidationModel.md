# DataCSVValidationModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**missing_headers** | **list[str]** |  | [optional] 
**empty_headers** | **list[int]** |  | [optional] 
**invalid_header_uris** | **dict(str, str)** |  | [optional] 
**datatype_errors** | **dict(str, list[CSVDatatypeError])** |  | [optional] 
**uri_not_found_errors** | **dict(str, list[CSVURINotFoundError])** |  | [optional] 
**invalid_uri_errors** | **dict(str, list[CSVCell])** |  | [optional] 
**missing_required_value_errors** | **dict(str, list[CSVCell])** |  | [optional] 
**invalid_value_errors** | **dict(str, list[CSVCell])** |  | [optional] 
**already_existing_uri_errors** | **dict(str, list[CSVCell])** |  | [optional] 
**duplicate_uri_errors** | **dict(str, list[CSVDuplicateURIError])** |  | [optional] 
**invalid_row_size_errors** | **dict(str, list[CSVCell])** |  | [optional] 
**invalid_date_errors** | **dict(str, list[CSVCell])** |  | [optional] 
**nb_object_imported** | **int** |  | [optional] 
**validation_token** | **str** |  | [optional] 
**csv_header** | [**CsvHeader**](CsvHeader.md) |  | [optional] 
**invalid_object_errors** | **dict(str, list[CSVCell])** |  | [optional] 
**invalid_annotation_errors** | **dict(str, list[CSVCell])** |  | [optional] 
**invalid_target_errors** | **dict(str, list[CSVCell])** |  | [optional] 
**invalid_data_type_errors** | **dict(str, list[CSVCell])** |  | [optional] 
**invalid_experiment_errors** | **dict(str, list[CSVCell])** |  | [optional] 
**invalid_device_errors** | **dict(str, list[CSVCell])** |  | [optional] 
**device_choice_ambiguity_errors** | **dict(str, list[CSVCell])** |  | [optional] 
**duplicated_data_errors** | **dict(str, list[CSVCell])** |  | [optional] 
**duplicated_object_errors** | **dict(str, list[CSVCell])** |  | [optional] 
**duplicated_target_errors** | **dict(str, list[CSVCell])** |  | [optional] 
**duplicated_experiment_errors** | **dict(str, list[CSVCell])** |  | [optional] 
**duplicated_device_errors** | **dict(str, list[CSVCell])** |  | [optional] 
**headers** | **list[str]** |  | [optional] 
**headers_labels** | **list[str]** |  | [optional] 
**annotations_on_objects** | [**list[AnnotationModel]**](AnnotationModel.md) |  | [optional] 
**nb_lines_imported** | **int** |  | [optional] 
**nb_lines_to_import** | **int** |  | [optional] 
**validation_step** | **bool** |  | [optional] 
**insertion_step** | **bool** |  | [optional] 
**valid_csv** | **bool** |  | [optional] 
**too_large_dataset** | **bool** |  | [optional] 
**error_message** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


