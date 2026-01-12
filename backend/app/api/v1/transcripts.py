from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.models.transcript import Transcript
from app.models.meeting import Meeting
from app.schemas.transcript import TranscriptCreate, TranscriptResponse

router = APIRouter()


@router.post("/", response_model=TranscriptResponse, status_code=201)
def create_transcript(transcript: TranscriptCreate, db: Session = Depends(get_db)):
    meeting = db.query(Meeting).filter(Meeting.id == transcript.meeting_id).first()
    if not meeting:
        raise HTTPException(status_code=404, detail="Meeting not found")
    
    db_transcript = Transcript(**transcript.model_dump())
    db.add(db_transcript)
    db.commit()
    db.refresh(db_transcript)
    return db_transcript


@router.get("/meeting/{meeting_id}", response_model=List[TranscriptResponse])
def get_transcripts_by_meeting(meeting_id: int, db: Session = Depends(get_db)):
    meeting = db.query(Meeting).filter(Meeting.id == meeting_id).first()
    if not meeting:
        raise HTTPException(status_code=404, detail="Meeting not found")
    
    transcripts = db.query(Transcript).filter(Transcript.meeting_id == meeting_id).all()
    return transcripts
