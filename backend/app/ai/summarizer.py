from typing import List, Dict
from app.ai.llm_client import llm_client
from app.ai.prompt_templates import MEETING_SUMMARY_PROMPT, ACTION_ITEMS_PROMPT


def summarize_meeting(transcript_text: str) -> Dict[str, any]:
    summary_prompt = MEETING_SUMMARY_PROMPT.format(transcript=transcript_text)
    summary = llm_client.generate(summary_prompt)
    
    action_items_prompt = ACTION_ITEMS_PROMPT.format(transcript=transcript_text)
    action_items_text = llm_client.generate(action_items_prompt)
    
    action_items = [
        item.strip().lstrip("- ").strip()
        for item in action_items_text.split("\n")
        if item.strip() and item.strip().startswith("-")
    ]
    
    return {
        "summary": summary,
        "action_items": action_items
    }
