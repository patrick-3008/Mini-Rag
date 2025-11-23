from fastapi import FastAPI
from routes import base
from dotenv import load_dotenv

load_dotenv(".env") #load the .env file

app = FastAPI()

app.include_router(base.base_router) # include the base router
