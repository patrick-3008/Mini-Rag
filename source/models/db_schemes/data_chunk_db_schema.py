from pydantic import BaseModel, Field
from typing import Optional
from bson.objectid import ObjectId

class DataChunkDBSchema(BaseModel):
    id: Optional[ObjectId] = Field(None, alias="_id") # not required
    chunk_text: str = Field(..., min_length=1) # "..." means that the variable is reqired
    chunk_metadata: dict
    chunk_order: int = Field(..., gt=0)
    chunk_project_id: ObjectId
    chunk_asset_id: ObjectId
    
    class Config:
        arbitrary_types_allowed = True

    # static method to get indexes
    @classmethod
    def get_indexes(cls):
        return [
            {
                "key": [ ("chunk_project_id", 1) ], # ascending index
                "name": "chunk_project_id_index_1",
                "unique": False
            }
        ]


class RetrievedDocumentDBSchema(BaseModel):
    text: str
    score: float