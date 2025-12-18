# CareGraph - AI Mental Health Companion

**Your intelligent AI companion for mental wellness support.** CareGraph combines advanced AI with real-world safety tools to provide empathetic conversations, crisis detection, and emergency response capabilities.

## ✨ Features

- 🤖 **AI-Powered Conversations**: Uses MedGemma healthcare model for therapeutic, evidence-based responses
- 🚨 **Emergency Detection**: Automatically identifies mental health crises and initiates emergency calls
- 💬 **Multi-Platform Support**: Web chat interface and WhatsApp integration
- 📍 **Therapist Finder**: Location-based search for nearby mental health professionals
- 🔒 **Privacy-Focused**: Local processing with minimal data collection
- ⚡ **Real-time Responses**: Fast, contextual AI interactions

## 🔍 How CareGraph Works

CareGraph operates through a sophisticated AI agent architecture:

### 🏗️ System Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Streamlit     │    │    FastAPI      │    │   LangGraph     │
│   Frontend      │◄──►│   Backend       │◄──►│   AI Agent      │
│                 │    │                 │    │                 │
│ - Chat UI       │    │ - /ask endpoint │    │ - ReAct Agent   │
│ - Message hist. │    │ - /whatsapp_ask │    │ - Tool calling  │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                              │                        │
                              ▼                        ▼
                       ┌─────────────────┐    ┌─────────────────┐
                       │   Specialized   │    │   External      │
                       │    Tools        │    │   Services      │
                       │                 │    │                 │
                       │ - MedGemma AI   │    │ - Twilio Calls  │
                       │ - Crisis Detect │    │ - Google Maps   │
                       └─────────────────┘    └─────────────────┘
```

### 🤖 AI Agent Flow

1. **User Input** → Received via web form or WhatsApp
2. **Context Processing** → System prompt + user message fed to LangGraph agent
3. **Tool Selection** → Agent decides which tool to use:
   - **MedGemma Tool**: For general mental health conversations
   - **Emergency Tool**: For crisis situations (triggers Twilio call)
   - **Location Tool**: For finding nearby therapists
4. **Response Generation** → AI generates empathetic, helpful response
5. **Output Delivery** → Response sent back to user interface

### 🛠️ Key Components

- **Frontend (`frontend.py`)**: Streamlit app with chat interface
- **Backend (`backend/main.py`)**: FastAPI server with REST endpoints
- **AI Agent (`backend/ai_agent.py`)**: LangGraph ReAct agent with custom tools
- **Tools (`backend/tools.py`)**: MedGemma integration and Twilio calling
- **Config (`backend/config.py`)**: API keys and settings (create from `config.example.py`)

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- [UV](https://github.com/astral-sh/uv) package manager
- [Ollama](https://ollama.ai/) for local AI model

### Installation

1. **Clone & Setup**:
   ```bash
   git clone https://github.com/Mahesh-git888/CAREGRAPH.git
   cd CAREGRAPH
   uv sync
   ```

2. **Install MedGemma Model**:
   ```bash
   ollama pull alibayram/medgemma:4b
   ```

3. **Configure API Keys**:
   ```bash
   cp backend/config.example.py backend/config.py
   # Edit backend/config.py with your API keys
   ```

### Running CareGraph

1. **Start Backend**:
   ```bash
   uv run uvicorn backend.main:app --reload
   ```

2. **Start Frontend** (new terminal):
   ```bash
   uv run streamlit run frontend.py
   ```

3. **Open** `http://localhost:8501` in your browser

## ⚙️ Configuration

Edit `backend/config.py` with your credentials:

```python
# Required API Keys
GROQ_API_KEY = "your_groq_api_key"          # For AI model
TWILIO_ACCOUNT_SID = "your_twilio_sid"      # For emergency calls
TWILIO_AUTH_TOKEN = "your_twilio_token"     # For emergency calls
TWILIO_FROM_NUMBER = "+1234567890"         # Your Twilio number
EMERGENCY_CONTACT = "+0987654321"           # Emergency contact number
GOOGLE_MAPS_API_KEY = "your_maps_key"       # For therapist search
```

## 📡 API Endpoints

### Web Chat
```http
POST /ask
Content-Type: application/json

{
  "message": "I'm feeling anxious today"
}
```

**Response**:
```json
{
  "response": "I hear that anxiety can be really challenging...",
  "tool_called": "ask_mental_health_specialist"
}
```

### WhatsApp Integration
```http
POST /whatsapp_ask
Content-Type: application/x-www-form-urlencoded

Body=I'm+not+feeling+well
```

## 🔧 Development

### Testing Tools
```bash
# Test emergency calling
uv run python backend/test_location_tool.py

# Check syntax
uv run python -m py_compile backend/*.py
```

### Code Structure
```
CAREGRAPH/
├── frontend.py              # Streamlit web interface
├── backend/
│   ├── main.py             # FastAPI server & endpoints
│   ├── ai_agent.py         # LangGraph AI agent setup
│   ├── tools.py            # MedGemma & Twilio integrations
│   ├── config.py           # API keys (create from example)
│   └── config.example.py   # Configuration template
├── pyproject.toml          # Project dependencies
└── README.md              # This file
```

## ⚠️ Important Safety Notes

- **Not a Substitute**: CareGraph is AI assistance, not professional therapy
- **Emergency Protocol**: System calls emergency contacts for crisis situations
- **Data Privacy**: Conversations processed locally, no data stored
- **Crisis Resources**: Always contact qualified professionals for mental health emergencies

## 🤝 Contributing

We welcome contributions! Please:
1. Fork the repository
2. Create a feature branch
3. Test your changes thoroughly
4. Submit a pull request

## 📄 License

[Specify your license here]

---

**Built with ❤️ for mental wellness support**