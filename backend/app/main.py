from fastapi import FastAPI
from app.core.config import settings
from app.core.logger import logger
from app.api.v1 import projects, tasks, meetings, transcripts


app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG
)

app.include_router(projects.router, prefix=f"{settings.API_V1_STR}/projects", tags=["projects"])
app.include_router(tasks.router, prefix=f"{settings.API_V1_STR}/tasks", tags=["tasks"])
app.include_router(meetings.router, prefix=f"{settings.API_V1_STR}/meetings", tags=["meetings"])
app.include_router(transcripts.router, prefix=f"{settings.API_V1_STR}/transcripts", tags=["transcripts"])


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
