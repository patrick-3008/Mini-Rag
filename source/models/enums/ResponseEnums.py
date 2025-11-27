from enum import Enum

class ResponseSignal(Enum):

    FILE_VALIDATED_SUCCESS = "File validate successfully"
    FILE_TYPE_NOT_SUPPORTED = "File type not supported"
    FILE_SIZE_EXCEEDED = "File size exceeded"
    FILE_UPLOAD_SUCCESS = "File uploaded successfully"
    FILE_UPLOAD_FAILED = "File upload failed"
    PROCESSING_SUCCESS = "File processed successfully"
    PROCESSING_FAILED = "File processing failed"
    NO_ASSETS_FOUND = "No assets found"
    ASSET_ID_ERROR = "No asset found with the provided file ID"
