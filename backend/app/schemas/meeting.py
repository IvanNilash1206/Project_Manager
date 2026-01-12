from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class MeetingCreate(BaseModel):
    title: str
    scheduled_at: datetime
    project_id: int


class MeetingResponse(BaseModel):
    id: int
    title: str
    scheduled_at: datetime
    project_id: int
    created_at: datetime

    class Config:
        from_attributes = True
