from enum import Enum

class ResponseSignal(Enum):
    FILE_VALIDATED_SUCCESS = "File validated successfully"
    FILE_TYPE_NOT_SUPPORTED = "File type not supported"
    FILE_SIZE_EXCEEDED = "File size exceeded"
    FILE_UPLOAD_SUCCESS = "File uploaded successfully"
    FILE_UPLOAD_FAILED = "File upload failed"
    PROCESSING_SUCCESS = "processing_success"
    PROcESSING_FAILED = "processing_failed"
    NO_FILES_ERROR = "not_found_files"
    FILE_ID_ERROR = "no_file_found_with_this_id"