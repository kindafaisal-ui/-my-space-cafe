# AI Content Creator — My Space Cafe

> An intelligent content generation system that produces authentic, brand-aligned content — demonstrably unique from generic AI output.

## Live Demo
https://web-production-5d04de.up.railway.app

## Setup Instructions

### 1. Clone the repository
git clone https://github.com/kindafaisal-ui/-my-space-cafe.git

### 2. Create virtual environment
python -m venv venv
source venv/bin/activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Configure API keys
Add your OpenAI API key to .env:
OPENAI_API_KEY=sk-your-key-here

### 5. Run locally
python app.py

## Project Structure
- src/ — Python modules for document processing, LLM integration, content pipeline
- knowledge_base/primary/ — Brand guidelines, past content, portfolio
- knowledge_base/secondary/ — Market trends, competitor analysis, customer research
- config/ — VSCode agent configuration
- demo/ — Landing page with live AI demo

## Knowledge Base Architecture

### Primary Knowledge Base
- brand_guidelines.md — My Space Cafe voice, tone, values
- past_content/examples.md — Past successful content
- portfolio_and_skills.md — Company positioning

### Secondary Research Layer
- market_trends.md — Cafe and third-place economy trends
- competitor_analysis.md — Starbucks and competitor positioning
- customer_research.md — Target audience insights
- industry_reports.md — Industry data and benchmarks

## Content Pipeline
Document to Monitor to Brief to Publish to Iterate

## Uniqueness Strategy
The live demo shows side-by-side comparison of generic AI vs our knowledge-based system.
Every prompt is injected with brand guidelines and competitor context.

## Tech Stack
- Backend: Python 3.8+, Flask
- LLM: OpenAI GPT-4o-mini
- Deployment: Railway
- Version Control: Git/GitHub

## API Endpoints
- GET / — Landing page
- POST /api/generate — Generate brand content
- GET /health — Health check
