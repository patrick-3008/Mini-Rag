from fastapi import FastAPI
from routes import base, data

app = FastAPI()
app.include_router(base.base_router) # include the base router
app.include_router(data.data_router) # include the data router

