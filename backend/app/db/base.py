from sqlalchemy.ext.declarative import declarative_base

# Create declarative base
Base = declarative_base()

# Import all models here so they are registered with Base.metadata
# This is important for migrations and creating tables
from app.models.user import User  # noqa: F401
from app.models.project import Project  # noqa: F401
from app.models.task import Task  # noqa: F401
from app.models.meeting import Meeting  # noqa: F401
from app.models.transcript import Transcript  # noqa: F401
