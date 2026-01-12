MEETING_SUMMARY_PROMPT = """You are an AI assistant that summarizes meeting transcripts.

Given the following meeting transcript, provide a concise summary in bullet points.

Transcript:
{transcript}

Provide a summary with key points discussed in the meeting."""


ACTION_ITEMS_PROMPT = """You are an AI assistant that extracts action items from meeting transcripts.

Given the following meeting transcript, extract all action items as a list.

Transcript:
{transcript}

Extract action items as clear, task-like sentences. Return each action item on a new line starting with "- "."""
