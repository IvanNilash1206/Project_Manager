from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class TranscriptCreate(BaseModel):
    meeting_id: int
    content: str


class TranscriptResponse(BaseModel):
    id: int
    meeting_id: int
    content: str
    created_at: datetime

    class Config:
        from_attributes = True
