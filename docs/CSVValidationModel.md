# CSVValidationModel

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

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


