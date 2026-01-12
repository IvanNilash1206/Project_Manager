from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.models.meeting import Meeting
from app.models.project import Project
from app.schemas.meeting import MeetingCreate, MeetingResponse

router = APIRouter()


@router.post("/", response_model=MeetingResponse, status_code=201)
def create_meeting(meeting: MeetingCreate, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == meeting.project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    db_meeting = Meeting(**meeting.model_dump())
    db.add(db_meeting)
    db.commit()
    db.refresh(db_meeting)
    return db_meeting


@router.get("/project/{project_id}", response_model=List[MeetingResponse])
def list_meetings_by_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    meetings = db.query(Meeting).filter(Meeting.project_id == project_id).all()
    return meetings


@router.get("/{meeting_id}", response_model=MeetingResponse)
def get_meeting(meeting_id: int, db: Session = Depends(get_db)):
    meeting = db.query(Meeting).filter(Meeting.id == meeting_id).first()
    if not meeting:
        raise HTTPException(status_code=404, detail="Meeting not found")
    return meeting


@router.delete("/{meeting_id}", status_code=204)
def delete_meeting(meeting_id: int, db: Session = Depends(get_db)):
    meeting = db.query(Meeting).filter(Meeting.id == meeting_id).first()
    if not meeting:
        raise HTTPException(status_code=404, detail="Meeting not found")
    
    db.delete(meeting)
    db.commit()
    return None
