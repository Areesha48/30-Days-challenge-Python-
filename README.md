# 🤖 Python for AI Automation — 30-Day Plan

Author: Manus AI  
Repository: Areesha48/30-Days-challenge-Python-  
Date: February 2026  
Level: Beginner

## About
A 30-day, step-by-step plan to learn Python focused on automation and simple AI integration. Daily small tasks build up to a final project: an AI Email Assistant that drafts subject lines and email bodies.

## What's included
- Day-by-day learning plan (basics → APIs → automation → final project)
- Example scripts for mini-projects (greeting bot, quote fetcher, notes saver, simple AI chat)
- Final project: AI Email Assistant (prompt → subject + body → save to file)

## Prerequisites
- Python 3.8+
- Basic command-line knowledge
- (Optional) API key for AI provider (e.g., OpenAI) for AI-powered lessons

## Quick setup
1. Clone:
   git clone https://github.com/Areesha48/30-Days-challenge-Python-.git
   cd 30-Days-challenge-Python-

2. Create and activate a virtual environment:
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS / Linux
   source venv/bin/activate

3. Install dependencies (if provided):
   pip install -r requirements.txt

## Run examples
- Run a day script:
  python day_06_greeting_bot.py
- Run final project (if present):
  python final_ai_email_assistant.py

## Using an AI API (if implementing)
- Store your API key in an environment variable (do not hard-code):
  export OPENAI_API_KEY="your_api_key_here"     # macOS / Linux
  setx OPENAI_API_KEY "your_api_key_here"       # Windows
- Read in Python:
  import os
  api_key = os.getenv("OPENAI_API_KEY")

## File suggestions
- day_01_hello.py
- day_06_greeting_bot.py
- day_12_quote_of_the_day.py
- day_16_notes_saver.py
- day_19_simple_ai_chat.py
- final_ai_email_assistant.py
- requirements.txt (optional)

## Contributing
Add example scripts, translations, tests, or improvements. Open issues or PRs.

## License
Choose a license (MIT recommended for permissive reuse).

~hijabicoder
