from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.meeting import Meeting
from app.models.transcript import Transcript
from app.ai.summarizer import summarize_meeting
from app.core.logger import logger


router = APIRouter()


@router.post("/summarize/meeting/{meeting_id}")
async def summarize_meeting_endpoint(meeting_id: int, db: Session = Depends(get_db)):
    meeting = db.query(Meeting).filter(Meeting.id == meeting_id).first()
    
    if not meeting:
        raise HTTPException(status_code=404, detail="Meeting not found")
    
    transcript = db.query(Transcript).filter(Transcript.meeting_id == meeting_id).first()
    
    if not transcript:
        raise HTTPException(status_code=404, detail="No transcript found for this meeting")
    
    if not transcript.content or not transcript.content.strip():
        raise HTTPException(status_code=400, detail="Transcript content is empty")
    
    try:
        logger.info(f"Summarizing meeting {meeting_id}")
        result = summarize_meeting(transcript.content)
        
        return {
            "meeting_id": meeting_id,
            "meeting_title": meeting.title,
            "summary": result["summary"],
            "action_items": result["action_items"]
        }
    except Exception as e:
        logger.error(f"Error summarizing meeting {meeting_id}: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to summarize meeting: {str(e)}")
