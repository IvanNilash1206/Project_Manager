AI-Project-Management-System/
│
├── frontend/                     # Lovable frontend
│   ├── lovable.config.json       # Lovable configuration
│   ├── public/                   # Static assets
│   │   ├── icons/
│   │   ├── images/
│   │   └── audio/
│   │
│   ├── src/
│   │   ├── pages/                # Lovable pages
│   │   │   ├── Login/
│   │   │   │   └── index.lovable
│   │   │
│   │   │   ├── ProjectManager/
│   │   │   │   ├── index.lovable
│   │   │   │   ├── AddProject.lovable
│   │   │   │   └── TaskBoard.lovable
│   │   │
│   │   │   ├── Meetings/
│   │   │   │   ├── index.lovable
│   │   │   │   ├── AttendMeeting.lovable
│   │   │   │   └── MeetingSummary.lovable
│   │   │
│   │   │   ├── GenAI/
│   │   │   │   └── index.lovable
│   │   │
│   │   │   └── VoiceAssistant/
│   │   │       └── index.lovable
│   │   │
│   │   ├── components/           # Reusable UI components
│   │   │   ├── Navbar.lovable
│   │   │   ├── Sidebar.lovable
│   │   │   ├── TaskCard.lovable
│   │   │   ├── KanbanColumn.lovable
│   │   │   └── VoiceButton.lovable
│   │   │
│   │   ├── services/             # API communication
│   │   │   ├── apiClient.js
│   │   │   ├── authService.js
│   │   │   ├── projectService.js
│   │   │   ├── meetingService.js
│   │   │   ├── aiService.js
│   │   │   └── voiceService.js
│   │   │
│   │   ├── state/                # Global state management
│   │   │   ├── authStore.js
│   │   │   ├── projectStore.js
│   │   │   └── taskStore.js
│   │   │
│   │   ├── utils/
│   │   │   ├── dateUtils.js
│   │   │   ├── audioUtils.js
│   │   │   └── constants.js
│   │   │
│   │   └── App.lovable
│   │
│   └── package.json
│
├── backend/
│   ├── app/
│   │   ├── main.py               # FastAPI entry point
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   ├── security.py
│   │   │   └── logger.py
│   │   │
│   │   ├── api/
│   │   │   ├── v1/
│   │   │   │   ├── auth.py
│   │   │   │   ├── users.py
│   │   │   │   ├── projects.py
│   │   │   │   ├── tasks.py
│   │   │   │   ├── meetings.py
│   │   │   │   ├── ai.py
│   │   │   │   └── voice.py
│   │   │
│   │   ├── models/               # ORM models
│   │   │   ├── user.py
│   │   │   ├── project.py
│   │   │   ├── task.py
│   │   │   ├── meeting.py
│   │   │   └── transcript.py
│   │   │
│   │   ├── schemas/              # Pydantic schemas
│   │   │   ├── user.py
│   │   │   ├── project.py
│   │   │   ├── task.py
│   │   │   ├── meeting.py
│   │   │   └── ai.py
│   │   │
│   │   ├── services/             # Business logic
│   │   │   ├── auth_service.py
│   │   │   ├── project_service.py
│   │   │   ├── task_service.py
│   │   │   ├── meeting_service.py
│   │   │   ├── calendar_service.py
│   │   │   └── notification_service.py
│   │   │
│   │   ├── ai/
│   │   │   ├── llm_client.py
│   │   │   ├── embeddings.py
│   │   │   ├── summarizer.py
│   │   │   ├── rag_engine.py
│   │   │   └── prompt_templates.py
│   │   │
│   │   ├── voice/
│   │   │   ├── speech_to_text.py
│   │   │   ├── text_to_speech.py
│   │   │   ├── intent_parser.py
│   │   │   └── voice_router.py
│   │   │
│   │   ├── db/
│   │   │   ├── session.py
│   │   │   ├── base.py
│   │   │   └── migrations/
│   │   │
│   │   └── utils/
│   │       ├── audio_utils.py
│   │       ├── time_utils.py
│   │       └── file_utils.py
│   │
│   ├── tests/
│   │   ├── test_auth.py
│   │   ├── test_projects.py
│   │   ├── test_tasks.py
│   │   ├── test_meetings.py
│   │   └── test_ai.py
│   │
│   ├── requirements.txt
│   └── Dockerfile
│
├── ai-assets/
│   ├── embeddings/
│   ├── transcripts/
│   ├── audio/
│   └── vector_index/
│
├── docs/
│   ├── architecture.md
│   ├── api-spec.md
│   ├── ai-workflow.md
│   ├── voice-assistant.md
│   └── demo-flow.md
│
├── scripts/
│   ├── seed_data.py
│   ├── build_embeddings.py
│   └── cleanup_audio.py
│
├── .env.example
├── .gitignore
├── CHECKLIST.md
├── README.md
└── docker-compose.yml
