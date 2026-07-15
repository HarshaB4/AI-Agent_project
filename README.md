**AI Person Profile Generator**
An AI-powered application that generates a detailed profile of a public figure using publicly available information. The system uses Search, Web Scraping, RAG (Retrieval-Augmented Generation), Gemini AI, ChromaDB, and HTML/PDF report generation.

**Features**
Search public information about a person
Scrape relevant web pages
Store documents in ChromaDB
Retrieve relevant context using RAG
Generate structured profile using Gemini AI
Validate generated profile
Download profile image automatically
Generate HTML report
Generate PDF report
Save output as JSON
**Project Structure**

person-profile-ai/
│
├── app.py
│
├── agents/
│   ├── search_agent.py
│   ├── extractor_agent.py
│   ├── validator_agent.py
│   └── profile_agent.py
│
├── services/
│   ├── gemini_service.py
│   ├── search_service.py
│   ├── scraper.py
│   ├── image_service.py
│   ├── html_service.py
│   └── pdf_service.py
│
├── rag/
│   ├── embeddings.py
│   ├── vector_store.py
│   └── retriever.py
│
├── templates/
│   └── report.html
│
├── images/
│
├── output/
│   ├── profile.json
│   ├── profile.html
│   └── profile_1.pdf
│
├── requirements.txt
└── README.md

**Technologies Used**
**AI / LLM**
Google Gemini API
Agentic AI Workflow
RAG Architecture
**Backend**
Python
FastAPI
**Vector Database**
ChromaDB
**Embeddings**
Sentence Transformers
**Search**
DDGS (DuckDuckGo Search)
**PDF Generation**
Playwright
**HTML Templates**
Jinja2


**Install all libraries:**

pip install -r requirements.txt
Install Playwright Browser:

playwright install
or

python -m playwright install
Workflow
**Step 1: User Input**

User enters:
Name: Virat Kohli
Context: Indian Cricketer
**Step 2: Search Agent**

File:

agents/search_agent.py


**Responsibilities:**

Search the web
Collect URLs
Pass URLs for scraping
Output:

25 Documents Found
**Step 3: Scraper**

File:

services/scraper.py
Responsibilities:

Scrape page content
Extract text
Clean HTML
Output:

{
    "title": "...",
    "url": "...",
    "content": "..."
}
**Step 4: Store Documents in ChromaDB**

File:

rag/vector_store.py
Responsibilities:

Convert documents to embeddings
Store vectors
Store metadata
**Step 5: Retrieve Relevant Context**
File:

rag/retriever.py
Responsibilities:

Query ChromaDB
Retrieve Top-K documents
Output:

Top 5 Relevant Documents

**Step 6: Extractor Agent**
File:

agents/extractor_agent.py
**Responsibilities:**

Create Gemini Prompt
Send context to Gemini
Generate structured JSON
Generated Fields:

{
  "executive_summary": "",
  "basic_details": {},
  "biography": "",
  "career_timeline": [],
  "education": [],
  "interests": [],
  "estimated_net_worth": "",
  "recent_news": [],
  "references": []
}
**Step 7: Validator Agent**

File:

agents/validator_agent.py

**Responsibilities:**

Check missing fields
Generate warnings
Example:

{
  "validation_warnings": [
    "Net worth information unavailable"
  ]
}
**Step 8: Download Image**

File:

services/image_service.py

Responsibilities:

Search person image
Download image
Save image
Example:

images/
└── Virat_Kohli.jpg
Step 9: Save JSON
Output:

output/profile.json
Example:

{
  "full_name": "Virat Kohli"
}
Step 10: Generate HTML Report
File:

services/html_service.py
Uses:

templates/report.html
Output:

output/profile.html
Contains:
Executive Summary
Basic Details
Biography
Career Timeline
Education
Interests
Net Worth
Recent News
References
Validation Warnings
Profile Image
**Step 11: Generate PDF Report**

File:

services/pdf_service.py
**Responsibilities:**


Convert HTML → PDF
Output:

output/profile_1.pdf
output/profile_2.pdf
output/profile_3.pdf
Running the Application
Option 1: Run Using Terminal
Create test file:

from agents.profile_agent import generate_profile

generate_profile(
    "Virat Kohli",
    "Indian Cricketer"
)
Run:

python test_profile.py
Option 2: Run FastAPI
Start server:

uvicorn app:app --reload
Open:

http://127.0.0.1:8000/docs
Use:

POST /generate-profile
Example Request:

{
  "name": "Virat Kohli",
  "context": "Indian Cricketer"
}
Generated Outputs
output/
│
├── profile.json
├── profile.html
├── profile_1.pdf
├── profile_2.pdf
└── profile_3.pdf

**Harsha Vardhan**

**AI Engineer | Python Developer | Agentic AI Enthusiast**

