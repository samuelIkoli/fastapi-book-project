import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from api.router import api_router
from core.config import settings

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_PREFIX)


@app.get("/healthcheck")
async def health_check():
    """Checks if server is active."""
    return {"status": "active"}

@app.get("/stage2")
async def stage2():
    return {"message": "welcome to stage 2"}

@app.get("/telex-webhook")
async def get_json():
    with open("telex.json", "r") as json_file:
        data = json.load(json_file)
    return JSONResponse(content=data)
