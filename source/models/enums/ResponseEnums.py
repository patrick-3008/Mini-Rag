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
    PROJECT_NOT_FOUND_ERROR = "Project not found"
    INSERT_INTO_VECTORDB_ERROR = "Insert into vectordb error"
    INSERT_INTO_VECTORDB_SUCCESS = "Insert into vectordb success"
    VECTORDB_COLLECTION_RETRIEVED = "VectorDB collection info retrieved"
    VECTORDB_SEARCH_ERROR = "VectorDB search error"
    VECTORDB_SEARCH_SUCCESS = "VectorDB search success"
    RAG_ANSWER_ERROR = "RAG answer error"
    RAG_ANSWER_SUCCESS = " RAG answer success"
