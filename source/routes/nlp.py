from fastapi import FastAPI, APIRouter, status, Request
from fastapi.responses import JSONResponse
from source.routes.schemes.nlp_schema import PushRequest
from models.project_model import ProjectModel
from models.chunk_model import ChunkModel
from controllers import NLPController

import logging

logger = logging.getLogger('uvicorn.error')

nlp_router = APIRouter(
    prefix = "/api/v1/nlp",
    tags = ["api_v1", "nlp"],
)

@nlp_router.post("/index/push/{project_id}")
async def index_project(request: Request, project_id: str, push_request: PushRequest):

    project_model = await ProjectModel.create_instance(
        db_client = request.app.db_client
    )

    project = await project_model.get_project_or_create_one(
        project_id = project_id
    )

    chunk_model = await ChunkModel.create_instance(
        db_client = request.app.db_client
    )
