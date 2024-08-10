from fastapi import FastAPI
from app.api.main import api_router

app = FastAPI()


@app.get("/")
async def healthcheck():
    return {"message": "Hello, the service is running."}


app.include_router(api_router, prefix="/api/v1")
