from fastapi import FastAPI
from app.core.config import settings
from app.core.logger import logger


app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG
)


@app.on_event("startup")
async def startup_event():
    logger.info(f"Starting {settings.APP_NAME}")


@app.on_event("shutdown")
async def shutdown_event():
    logger.info(f"Shutting down {settings.APP_NAME}")


@app.get("/")
async def root():
    return {
        "message": "Welcome to AI Project Management System",
        "status": "running"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "app_name": settings.APP_NAME
    }
