from fastapi import FastAPI, APIRouter, Depends, UploadFile
from helpers.config import get_settings, Settings
from controllers import DataController

data_router = APIRouter(
    prefix="/api/v1/data", # add prefix to all the urls
    tags=["api_v1", "data"] # add tags for documentation
)

@data_router.post("/upload/{project_id}")
async def upload_data(
    project_id: str, 
    file: UploadFile, 
    app_settings: Settings = Depends(get_settings)
    ):

    # vaildate
    is_vaild = DataController().validate_uploaded_file(file=file)

    return is_vaild