from fastapi import FastAPI
from api.api.routes import router

api = FastAPI(title="AI Document Intelligence API")

app.include_router(route)
