from fastapi import FastAPI, APIRouter, Depends
import os
from helpers.config import get_settings, Settings

base_router = APIRouter(
    prefix="/api/v1", # add prefix to all the urls
    tags=["api_v1"] # add tags for documentation
)

# the function will not work if the settings are not found
@base_router.get("/")
async def welcome(app_settings: Settings = Depends(get_settings)):
    app_settings = get_settings()

    app_name = app_settings.APP_NAME
    app_version = app_settings.APP_VERSION

    return {
        "app_name": app_name,
        "app_version": app_version,
    }
