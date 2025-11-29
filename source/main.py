from fastapi import FastAPI
from routes import base, data
from motor.motor_asyncio import AsyncIOMotorClient
from helpers.config import get_settings
from stores.llm.llm_provider_factory import LLMProviderFactory

app = FastAPI()

# @app.on_event("startup")
async def startup_db_client():
    settings = get_settings()

    app.mongodb_connection = AsyncIOMotorClient(settings.MONGO_URI)
    app.db_client = app.mongodb_connection[settings.MONGO_DB_NAME]

    llm_provider_factory = LLMProviderFactory(settings)

    # generation client
    app.generation_client = llm_provider_factory.create(provider=settings.GENERATION_BACKEND)
    app.generation_client.set_generation_model(model_id = settings.GENERATION_MODEL_ID)

    # embedding client
    app.embedding_client = llm_provider_factory.create(provider=settings.EMBEDDING_BACKEND)
    app.embedding_client.set_embedding_model(model_id=settings.EMBEDDING_MODEL_ID,
                                             embedding_size=settings.EMBEDDING_MODEL_SIZE)

# @app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_connection.close()

app.include_router(base.base_router) # include the base router
app.include_router(data.data_router) # include the data router

app.router.lifespan.on_startup.append(startup_db_client) # register startup event
app.router.lifespan.on_shutdown.append(shutdown_db_client) # register shutdown event
