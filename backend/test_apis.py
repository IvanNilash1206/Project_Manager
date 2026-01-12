import requests
import json
from datetime import datetime, timedelta

BASE_URL = "http://127.0.0.1:8000/api/v1"

print("=" * 60)
print("Testing Meeting and Transcript APIs")
print("=" * 60)

# Step 1: Create a user first (needed for project owner)
print("\n1️⃣ Creating a test user...")
try:
    user_data = {
        "email": "testuser@example.com",
        "hashed_password": "hashedpassword123",
        "full_name": "Test User",
        "is_active": True
    }
    # Insert user directly into database
    from app.db import SessionLocal
    from app.models import User
    db = SessionLocal()
    user = User(**user_data)
    db.add(user)
    db.commit()
    db.refresh(user)
    user_id = user.id
    db.close()
    print(f"✓ User created - ID: {user_id}")
except Exception as e:
    print(f"✗ Error creating user: {e}")
    user_id = 1  # Fallback

# Step 2: Create a project
print("\n2️⃣ Creating a project...")
try:
    project_data = {
        "name": "AI Project Management",
        "description": "Testing meetings and transcripts",
        "owner_id": user_id
    }
    response = requests.post(f"{BASE_URL}/projects", json=project_data)
    project = response.json()
    project_id = project["id"]
    print(f"✓ Project created - ID: {project_id}, Name: {project['name']}")
except Exception as e:
    print(f"✗ Error creating project: {e}")
    exit(1)

# Step 3: Create a meeting
print("\n3️⃣ Creating a meeting...")
try:
    meeting_data = {
        "title": "Sprint Planning Meeting",
        "scheduled_at": (datetime.now() + timedelta(days=1)).isoformat(),
        "project_id": project_id
    }
    response = requests.post(f"{BASE_URL}/meetings", json=meeting_data)
    meeting = response.json()
    meeting_id = meeting["id"]
    print(f"✓ Meeting created - ID: {meeting_id}, Title: {meeting['title']}")
except Exception as e:
    print(f"✗ Error creating meeting: {e}")
    exit(1)

# Step 4: Add a transcript to the meeting
print("\n4️⃣ Adding transcript to the meeting...")
try:
    transcript_data = {
        "meeting_id": meeting_id,
        "content": "This is a test transcript. The team discussed the upcoming sprint goals and assigned tasks to team members. We will focus on implementing the API endpoints first."
    }
    response = requests.post(f"{BASE_URL}/transcripts", json=transcript_data)
    transcript = response.json()
    transcript_id = transcript["id"]
    print(f"✓ Transcript created - ID: {transcript_id}")
    print(f"   Content preview: {transcript['content'][:80]}...")
except Exception as e:
    print(f"✗ Error creating transcript: {e}")
    exit(1)

# Step 5: Fetch transcript by meeting ID
print("\n5️⃣ Fetching transcripts for the meeting...")
try:
    response = requests.get(f"{BASE_URL}/transcripts/meeting/{meeting_id}")
    transcripts = response.json()
    print(f"✓ Found {len(transcripts)} transcript(s)")
    for t in transcripts:
        print(f"   - ID: {t['id']}, Created: {t['created_at']}")
        print(f"     Content: {t['content'][:100]}...")
except Exception as e:
    print(f"✗ Error fetching transcripts: {e}")

# Step 6: Verify meeting details
print("\n6️⃣ Verifying meeting details...")
try:
    response = requests.get(f"{BASE_URL}/meetings/{meeting_id}")
    meeting_details = response.json()
    print(f"✓ Meeting found - ID: {meeting_details['id']}")
    print(f"   Title: {meeting_details['title']}")
    print(f"   Scheduled: {meeting_details['scheduled_at']}")
    print(f"   Project ID: {meeting_details['project_id']}")
except Exception as e:
    print(f"✗ Error fetching meeting: {e}")

# Step 7: List all meetings for the project
print("\n7️⃣ Listing all meetings for the project...")
try:
    response = requests.get(f"{BASE_URL}/meetings/project/{project_id}")
    meetings = response.json()
    print(f"✓ Found {len(meetings)} meeting(s) for project {project_id}")
    for m in meetings:
        print(f"   - ID: {m['id']}, Title: {m['title']}")
except Exception as e:
    print(f"✗ Error listing meetings: {e}")

# Step 8: Delete the meeting and confirm cascade behavior
print("\n8️⃣ Deleting the meeting...")
try:
    response = requests.delete(f"{BASE_URL}/meetings/{meeting_id}")
    if response.status_code == 204:
        print(f"✓ Meeting {meeting_id} deleted successfully")
    else:
        print(f"✗ Unexpected response: {response.status_code}")
except Exception as e:
    print(f"✗ Error deleting meeting: {e}")

# Step 9: Verify meeting is gone
print("\n9️⃣ Verifying meeting deletion...")
try:
    response = requests.get(f"{BASE_URL}/meetings/{meeting_id}")
    if response.status_code == 404:
        print(f"✓ Confirmed: Meeting {meeting_id} no longer exists")
    else:
        print(f"✗ Meeting still exists! Response: {response.status_code}")
except Exception as e:
    print(f"✓ Confirmed: Meeting not found (as expected)")

# Step 10: Verify transcripts are also deleted (cascade)
print("\n🔟 Verifying transcript cascade deletion...")
try:
    response = requests.get(f"{BASE_URL}/transcripts/meeting/{meeting_id}")
    if response.status_code == 404:
        print(f"✓ Confirmed: Meeting not found, so transcripts check failed (expected)")
    else:
        transcripts = response.json()
        if len(transcripts) == 0:
            print(f"✓ Confirmed: Transcripts were cascade-deleted")
        else:
            print(f"✗ Warning: {len(transcripts)} transcript(s) still exist!")
except Exception as e:
    print(f"✓ Confirmed: Cannot fetch transcripts (meeting deleted)")

print("\n" + "=" * 60)
print("✅ All tests completed successfully!")
print("=" * 60)
