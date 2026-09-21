# Agentic AI Career Assistant

An AI-powered career assistant that helps students plan, track, and improve their journey toward their target career.

The application uses Google Gemini, agentic tool calling, user memory, and Streamlit to provide personalized career guidance and learning support.

## Project Overview

The Agentic AI Career Assistant is designed to act as a personalized career companion.

Instead of functioning as a basic question-and-answer chatbot, the system can understand the user's request, determine when a specific tool is required, execute the tool, store relevant information, retrieve previously saved information, and generate responses based on the user's career goals and learning progress.

## Features

- Career goal management
- User profile management
- Persistent user memory
- Conversation tracking
- Personalized study plan generation
- Learning task tracking
- Completed task management
- Progress-based recommendations
- AI tool calling
- Gemini-powered responses
- Streamlit web interface
- GitHub-based source code management

## Agentic AI Capabilities

The application demonstrates core agentic AI concepts.

The agent can:

1. Understand the user's request
2. Determine whether a tool is required
3. Select the appropriate tool
4. Execute the selected tool
5. Store relevant information
6. Retrieve previously stored information
7. Use stored information to personalize responses
8. Generate recommendations based on the user's current progress

## Example Interactions

### Career Goal

User:

    My career goal is AI Engineer

The system stores the career goal and can retrieve it during future interactions.

### Study Plan

User:

    Create a 7 day study plan for becoming an AI Engineer

The system generates a structured study plan based on the user's career goal.

### Progress Tracking

User:

    Mark Python basics as completed

The system updates the user's learning progress.

### Personalized Recommendation

User:

    Based on my goal of becoming an AI Engineer and my completed Python basics, what should I learn next?

The system uses the stored career goal and completed learning task to generate a personalized recommendation.

## Project Architecture

```text
User
  |
  v
Streamlit Interface
  |
  v
Agent
  |
  +----------------------+
  |                      |
  v                      v
Gemini AI             Tool Calling
                         |
              +----------+----------+
              |          |          |
              v          v          v
           Memory    Study Plan   Progress
              |
              v
        User Information
```

## Project Structure

```text
agentic-ai-career-assistant/
│
├── app.py
├── agent.py
├── memory.py
├── tools.py
├── config.py
├── requirements.txt
├── .gitignore
└── README.md
```

## File Description

### app.py

Provides the Streamlit user interface and connects the frontend with the AI agent.

### agent.py

Contains the main AI agent logic, Gemini integration, system instructions, tool definitions, tool calling, and response generation.

### memory.py

Handles user information, conversation data, career goals, and learning progress.

### tools.py

Contains the tools that the AI agent can execute for tasks such as career profile updates, study-plan generation, and progress tracking.

### config.py

Handles application configuration and Gemini API key access.

### requirements.txt

Contains the Python dependencies required to run the application.

### .gitignore

Prevents sensitive files and unnecessary Python-generated files from being uploaded to GitHub.

## Technologies Used

- Python
- Google Gemini API
- Google GenAI SDK
- Streamlit
- Python-dotenv
- JSON
- Git
- GitHub

## Requirements

The project requires the following Python packages:

```text
streamlit
google-genai
python-dotenv
```

These dependencies are listed in requirements.txt and can be installed using:

```bash
pip install -r requirements.txt
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/agentic-ai-career-assistant.git
```

### 2. Open the Project Directory

```bash
cd agentic-ai-career-assistant
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

## API Configuration

Create a `.env` file in the project directory.

```env
GEMINI_API_KEY=your_api_key_here
```

Do not upload the `.env` file or your actual API key to GitHub.

The `.env` file is excluded from Git using `.gitignore`.

## Run the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

The application will open in your browser.

## Deployment

The application is deployed using Streamlit, and the source code is maintained on GitHub.

Streamlit Secrets are used to securely provide the Gemini API key during deployment.

## Security

Sensitive credentials are not stored directly in the source code.

The following files and directories are excluded from Git:

```text
.env
.venv/
venv/
__pycache__/
*.pyc
```

## Current Capabilities

The current version supports:

- AI-powered career conversations
- Career goal storage
- Memory retrieval
- Study-plan generation
- Learning progress tracking
- Tool-based agent execution
- Personalized recommendations
- Streamlit deployment

## Future Improvements

The project can be extended with:

- Resume analysis
- Resume improvement suggestions
- Job recommendation
- Interview preparation
- Technical interview practice
- Skill-gap analysis
- Job description analysis
- Career roadmap generation
- Integration with job portals
- Advanced long-term memory
- Voice-based interaction
- Multi-agent career assistance

## Learning Outcomes

This project demonstrates practical experience with:

- Generative AI
- Agentic AI
- LLM integration
- Function and tool calling
- Prompt engineering
- Memory management
- API integration
- Python application development
- Streamlit development
- Git and GitHub
- AI application deployment

## Author

**Anitha S**

BE Computer Science and Engineering

## Project Status

The project is currently deployed and functional, with core agentic AI, memory, tool-calling, study-planning, and progress-tracking features implemented.
