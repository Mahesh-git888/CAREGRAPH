# SafeSpace AI Therapist

Your compassionate AI companion for emotional support, built with care and real-world tools. SafeSpace listens, understands, and responds with empathy — and knows when to escalate to emergency help.

Equipped with an AI agent architecture, specialist healthcare models (MedGemma), and life-saving tools like emergency calling via Twilio, SafeSpace is designed to support mental well-being — safely and responsibly.

## Features

- **Empathetic AI Conversations**: Powered by MedGemma healthcare model running locally via Ollama, providing therapeutic responses with emotional attunement and practical guidance.
- **Emergency Response**: Automatically detects mental health crises and initiates emergency calls via Twilio to designated safety contacts.
- **Multi-Channel Support**: Available through web interface (Streamlit) and WhatsApp integration.
- **Therapist Finder**: Location-based search for nearby licensed therapists using Google Maps API.
- **Privacy-First**: All conversations are processed locally with configurable API integrations.
- **Responsible AI**: Implements safety protocols and escalation procedures for mental health emergencies.

## Architecture

The application consists of three main components:

- **Frontend**: Streamlit web interface for user interactions
- **Backend**: FastAPI server handling requests and AI processing
- **AI Agent**: LangGraph-based ReAct agent with specialized tools:
  - Mental health specialist (MedGemma via Ollama)
  - Emergency calling (Twilio)
  - Therapist location finder (Google Maps)

## Prerequisites

- Python 3.11+
- [UV](https://github.com/astral-sh/uv) package manager
- [Ollama](https://ollama.ai/) for running MedGemma model
- API keys for Twilio, Groq, and Google Maps

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Mahesh-git888/CAREGRAPH.git
   cd CAREGRAPH
   ```

2. **Install UV** (if not already installed):
   ```bash
   # Follow instructions at https://github.com/astral-sh/uv
   ```

3. **Set up the environment**:
   ```bash
   uv sync
   ```

4. **Install and set up Ollama**:
   ```bash
   # Install Ollama from https://ollama.ai/
   ollama pull alibayram/medgemma:4b
   ```

## Configuration

1. **Copy the configuration template**:
   ```bash
   cp backend/config.example.py backend/config.py
   ```

2. **Configure your API keys and settings** in `backend/config.py`:
   ```python
   TWILIO_ACCOUNT_SID = "your_twilio_account_sid"
   TWILIO_AUTH_TOKEN = "your_twilio_auth_token"
   TWILIO_FROM_NUMBER = "your_twilio_phone_number"
   EMERGENCY_CONTACT = "emergency_phone_number"
   GROQ_API_KEY = "your_groq_api_key"
   GOOGLE_MAPS_API_KEY = "your_google_maps_api_key"
   ```

3. **Set up environment variables** (recommended):
   Create a `.env` file in the root directory:
   ```
   TWILIO_ACCOUNT_SID=your_twilio_account_sid
   TWILIO_AUTH_TOKEN=your_twilio_auth_token
   TWILIO_FROM_NUMBER=your_twilio_phone_number
   EMERGENCY_CONTACT=emergency_phone_number
   GROQ_API_KEY=your_groq_api_key
   GOOGLE_MAPS_API_KEY=your_google_maps_api_key
   ```

## Usage

### Running the Application

1. **Start the backend server**:
   ```bash
   uv run uvicorn backend.main:app --reload
   ```

2. **Start the frontend** (in a new terminal):
   ```bash
   uv run streamlit run frontend.py
   ```

3. **Access the web interface** at `http://localhost:8501`

### WhatsApp Integration

The backend includes WhatsApp support via Twilio. Configure your Twilio webhook to point to `/whatsapp_ask` endpoint.

## API Endpoints

- `POST /ask`: Main chat endpoint for web interface
  - Request: `{"message": "user message"}`
  - Response: `{"response": "AI response", "tool_called": "tool_name"}`

- `POST /whatsapp_ask`: WhatsApp integration endpoint
  - Handles incoming WhatsApp messages via Twilio

## Development

### Running Tests

```bash
uv run pytest
```

### Code Quality

```bash
uv run ruff check .
uv run ruff format .
```

## Deployment

### Local Deployment

Follow the installation and usage instructions above.

### Production Deployment

1. Set up a production server (e.g., using Docker or cloud services)
2. Configure environment variables securely
3. Set up proper logging and monitoring
4. Ensure Ollama is running with sufficient resources for MedGemma

### Docker (Optional)

```dockerfile
# Add Dockerfile content here if implemented
```

## Safety and Ethics

SafeSpace is designed with mental health safety in mind:

- **Crisis Detection**: Monitors conversations for signs of mental health emergencies
- **Emergency Escalation**: Automatically contacts emergency services when needed
- **Professional Boundaries**: Clearly identifies as AI, not a replacement for professional therapy
- **Data Privacy**: Processes conversations locally, minimizes data collection

**Important**: This application is not a substitute for professional mental health care. Users experiencing mental health crises should contact qualified professionals or emergency services immediately.

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and add tests
4. Run code quality checks
5. Submit a pull request

## License

[Add appropriate license here]

## Acknowledgments

- MedGemma model by Google
- LangChain and LangGraph for AI agent framework
- Twilio for communication services
- Streamlit for web interface