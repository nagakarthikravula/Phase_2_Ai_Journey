# Phase 2 — AI/GenAI Engineering Journey

This repository documents my second month of a structured 5-month 
roadmap to become an AI/GenAI Engineer by October-November 2026.

## My Background
Final year BTech Data Science student from a Tier 3 college in India.
Month 1 covered Python fundamentals. This repository covers Month 2 — 
moving from Python into actual AI engineering.

## What I Learned This Month

### Week 5 — LLM Fundamentals
Conceptual understanding of how large language models work:
- How text is broken into tokens and why common words cost fewer tokens
- What the context window is and what happens when it overflows
- How temperature and top-p control randomness in token selection
- The difference between system prompts and user messages
- What hallucination is and why temperature 0 does not eliminate it
- Why training cutoffs matter for real applications

No code this week — pure understanding first.

### Week 6 — Google Gemini API
First real API calls to a live LLM from Python:
- Getting a free API key from Google AI Studio
- Calling Gemini with different temperature settings
- Writing system prompts that control model behavior
- Combining system instructions and temperature in one config
- Reading token usage from API responses

Scripts: `week6/01_first_call.py`, `02_temperature.py`, 
`03_system_prompt.py`, `04_combined.py`

### Week 7 — Prompt Engineering
Four prompting techniques with working code:
- **Zero-shot** — direct instructions, no examples
- **Few-shot** — guiding the model with input/output examples
- **Chain of thought** — forcing step by step reasoning
- **JSON output** — structured responses my code can parse

Final script compares a bad prompt versus a well-engineered prompt 
on the same customer review — showing why prompt engineering 
determines whether an AI app works in production.

Scripts: `week7/01_zeroshot.py`, `02_fewshot.py`, 
`03_json_output.py`, `04_chain_of_thought.py`, `05_comparison.py`

### Week 8 — Streamlit + Deployment
Built and deployed a complete AI web app:
- Learned Streamlit components: text input, selectbox, slider, 
  columns, sidebar, session state
- Connected Streamlit frontend to Gemini API backend
- Added input validation, loading spinner, and error handling
- Improved UX by replacing technical labels with user-friendly language
- Deployed live on Streamlit Community Cloud

Practice scripts: `week8/01_streamlit_basics.py`, 
`02_session_state.py`, `03_layout.py`, `04_gemini_streamlit.py`

## Final Project — AI Writing Assistant

A live web app that generates paragraphs in different tones using 
the Gemini API.

**Live Demo:** https://ai-writing-assistant-karthik-ai-practice.streamlit.app/

**Separate repo:** https://github.com/nagakarthikravula/ai-writing-assistant

### What it does
- User enters any topic
- Selects a tone: Formal, Casual, or Funny
- Adjusts creativity level with a slider
- Gemini generates a clean, well-structured paragraph
- Response persists on screen using Streamlit session state

### Tech Stack
- Python
- Streamlit
- Google Gemini API (gemini-2.5-flash)
- python-dotenv

## Repository Structure
Phase_2_Ai_Journey/
├── week5/
│   └── LLM_notes.md
├── week6/
│   ├── 01_first_call.py
│   ├── 02_temperature.py
│   ├── 03_system_prompt.py
│   ├── 04_combined.py
│   └── .gitignore
├── week7/
│   ├── 01_zeroshot.py
│   ├── 02_fewshot.py
│   ├── 03_json_output.py
│   ├── 04_chain_of_thought.py
│   └── 05_comparison.py
└── week8/
├── 01_streamlit_basics.py
├── 02_session_state.py
├── 03_layout.py
└── 04_gemini_streamlit.py

## Key Concepts I Can Explain

- How an LLM generates text token by token
- Why context window size matters in production apps
- When to use temperature 0 versus temperature 1
- The difference between zero-shot and few-shot prompting
- Why JSON output matters more than impressive free text 
  for real applications
- How Streamlit session state keeps responses on screen

## What Is Next — Month 3

RAG (Retrieval Augmented Generation), LangChain, and ChromaDB.

Goal: Build a document Q&A app where a user uploads a PDF and asks 
questions — the app answers from the actual document content, not 
the model's training memory.

## Connect
GitHub: https://github.com/nagakarthikravula
