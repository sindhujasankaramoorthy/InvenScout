# 🔎 InvenScout

### *Scout your invention before you build.*

**InvenScout** is an AI-powered prior-art and market research agent that helps inventors, indie hackers, and early-stage startups investigate an idea before investing significant time and resources into building it.

Instead of relying on a single keyword search, InvenScout transforms a plain-English invention idea into multiple search strategies, searches patents and the existing market using **SerpApi**, and uses AI to analyze the retrieved evidence and identify relevant overlaps and potential differentiation areas.

> ⚠️ **Disclaimer:** InvenScout is a preliminary automated research tool, not a substitute for a professional patent search, patent attorney, or legal advice.

---

## 🚀 Problem

Before building an invention, a creator may need to answer:

* Does something similar already exist?
* Have similar inventions already been disclosed in patents?
* Are similar products already being sold?
* How crowded is the technology or product space?
* What aspects of the idea appear different from the retrieved results?

Professional patent research can be expensive and time-consuming, while ordinary web searches often fail to capture patent terminology.

**InvenScout aims to provide an accessible first-pass research layer within minutes.**

---

## 💡 Solution

InvenScout uses an AI-powered research workflow:

```text
                 INVENTION IDEA
                       │
                       ▼
                AI Understanding
                       │
                       ▼
               Query Expansion
          ┌────────────┼────────────┐
          ▼            ▼            ▼
      Consumer      Technical     Adjacent
       Queries       Queries       Queries
          │            │            │
          └────────────┼────────────┘
                       ▼
                    SerpApi
          ┌────────────┼────────────┐
          ▼            ▼            ▼
     Google Patents  Google Search  Shopping
          │            │            │
          └────────────┼────────────┘
                       ▼
               Result Processing
                       │
                       ▼
                 AI Comparison
                       │
                       ▼
                 Research Report
```

---

## 🤖 Key Features

### 🧠 Intelligent Query Expansion

Converts a plain-English invention description into:

* Consumer-oriented queries
* Technical/patent-oriented queries
* Adjacent-concept queries

This helps bridge the vocabulary gap between everyday product descriptions and patent terminology.

### 🔬 Prior-Art Discovery

Searches relevant patent and patent-application results and extracts useful information such as:

* Patent title
* Publication number
* Filing date
* Assignee
* Relevant description
* Source link

### 🛒 Market Discovery

Searches the web and shopping results to identify potentially similar commercial products and existing solutions.

### ⚖️ Evidence-Based Comparison

The AI compares the user's invention features with retrieved evidence and highlights:

* Similar features
* Potential areas of overlap
* Relevant prior-art results
* Features not identified in the retrieved material
* Potential differentiation areas

### 📊 Search Signals

Provides a simple overview of the retrieved research, including the number of related patents and products identified.

### 📄 Structured Research Report

Generates a concise report containing:

* Invention summary
* Closest prior-art results
* Existing products
* Evidence-based feature comparison
* Potential differentiation areas
* Search statistics
* Legal disclaimer

---

## 🏗️ Architecture

InvenScout follows an **MVC architecture** with dedicated service and external API client layers.

```text
                         ┌──────────────┐
                         │    VIEW      │
                         │  Web UI      │
                         └──────┬───────┘
                                │
                                ▼
                         ┌──────────────┐
                         │ CONTROLLER   │
                         │ FastAPI      │
                         └──────┬───────┘
                                │
                                ▼
                         ┌──────────────┐
                         │   SERVICE    │
                         │ Agent Logic  │
                         └──────┬───────┘
                                │
                ┌───────────────┼───────────────┐
                ▼               ▼               ▼
          Query Service   Search Services   Analysis Service
                │               │               │
                ▼               ▼               ▼
             LLM            SerpApi            LLM
                                │
                 ┌──────────────┼──────────────┐
                 ▼              ▼              ▼
             Patents         Search         Shopping
                                │
                                ▼
                            MODEL
                                │
                                ▼
                             VIEW
```

### MVC Responsibilities

| Layer                | Responsibility                                                        |
| -------------------- | --------------------------------------------------------------------- |
| **Model**            | Represents inventions, patents, products, search signals, and reports |
| **View**             | Displays the invention analysis and research report                   |
| **Controller**       | Handles HTTP requests and coordinates application flow                |
| **Service Layer**    | Contains query expansion, search, processing, and analysis logic      |
| **API Client Layer** | Handles communication with SerpApi and LLM providers                  |

---

## 🔄 Agent Workflow

### 1. Invention Intake

The user describes their invention in natural language.

Example:

```text
A smart water bottle that adjusts hydration reminders
based on the user's activity level.
```

### 2. Query Expansion

The AI identifies the important concepts and generates multiple search strategies.

```text
Consumer:
smart hydration reminder bottle

Technical:
beverage container hydration monitoring device

Adjacent:
automated hydration monitoring system
```

### 3. Multi-Source Search

InvenScout uses **SerpApi** to retrieve information from multiple search sources.

```text
Technical queries → Google Patents
Consumer queries  → Google Search
Product queries   → Google Shopping
```

### 4. Result Processing

Retrieved results are:

```text
Collected
   ↓
Normalized
   ↓
Deduplicated
   ↓
Filtered
   ↓
Ranked
```

### 5. AI Analysis

The strongest retrieved evidence is compared against the original invention.

The system focuses on **what was found in the retrieved evidence**, rather than presenting the result as a legal determination.

### 6. Report Generation

The final evidence is transformed into a concise research report that can be reviewed by the user or used as a starting point for discussion with a patent professional.

---

## 🧰 Technology Stack

### Backend

* Python
* FastAPI
* Pydantic

### AI

* Large Language Model
* Query Expansion
* Prior-Art Comparison
* Structured Report Generation

### Search & Data

* **SerpApi**
* Google Patents
* Google Search
* Google Shopping

### Frontend

* HTML
* CSS
* JavaScript

### Architecture

* MVC
* Service Layer
* API Client Layer
* REST API

---

## 📁 Project Structure

```text
InvenScout/
│
├── app/
│   ├── controllers/
│   │   └── patent_controller.py
│   │
│   ├── models/
│   │   ├── invention.py
│   │   ├── patent.py
│   │   ├── product.py
│   │   └── report.py
│   │
│   ├── services/
│   │   ├── query_service.py
│   │   ├── patent_service.py
│   │   ├── product_service.py
│   │   ├── analysis_service.py
│   │   └── report_service.py
│   │
│   ├── clients/
│   │   ├── serpapi_client.py
│   │   └── llm_client.py
│   │
│   ├── views/
│   │   └── report_view.py
│   │
│   ├── config/
│   │   └── settings.py
│   │
│   └── main.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js
│
├── .env.example
├── requirements.txt
└── README.md
```

---

## ⚙️ Getting Started

### Prerequisites

Make sure you have:

* Python 3.10+
* A SerpApi API key
* An API key for your selected LLM provider

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/invenscout.git
cd invenscout
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file:

```env
SERPAPI_API_KEY=your_serpapi_key
LLM_API_KEY=your_llm_key
```

### 5. Start the backend

```bash
uvicorn app.main:app --reload
```

The API will be available locally at:

```text
http://127.0.0.1:8000
```

---

## 📡 Example API

### Request

```http
POST /analyze
```

```json
{
  "idea": "A helmet that detects crashes and automatically sends the rider's location to emergency contacts."
}
```

### Response

```json
{
  "idea": "...",
  "summary": "...",
  "prior_art": [],
  "existing_products": [],
  "search_signals": {
    "patents_found": 0,
    "products_found": 0,
    "high_relevance": 0
  },
  "differentiation": [],
  "disclaimer": "Preliminary automated prior-art search; not legal advice."
}
```

---

## 🎯 Design Goals

InvenScout is designed around four principles:

**Search broadly**
Use multiple query formulations and search sources rather than relying on a single keyword search.

**Use evidence**
Show the patents and products that contributed to the analysis.

**Explain the reasoning**
Make it clear why a result was considered relevant.

**Avoid false certainty**
Present findings as preliminary research signals rather than legal conclusions.

---

## 🔮 Future Scope

Potential future extensions include:

* Patent-family analysis
* Classification-based patent searching
* Claim-level comparison
* Patent timeline visualization
* Assignee/inventor relationship analysis
* Saved research reports
* PDF export
* Search-history comparison
* Additional international patent databases
* Human-in-the-loop review with patent professionals

---

## 🏆 Hackathon Context

**InvenScout** is being developed as a solo project for the **SerpApi India Hackathon 2026**, with SerpApi serving as the primary search infrastructure for discovering patents, web evidence, and commercial products.

The same system is also being developed as an academic software project demonstrating **MVC architecture, REST API design, service-layer separation, external API integration, and AI-assisted research workflows**.

---

## ⚠️ Disclaimer

InvenScout provides preliminary automated research based on publicly retrieved search results. It does **not** determine patentability, infringement, ownership, or legal rights and should not be relied upon as legal advice.

For important intellectual-property decisions, consult a qualified patent professional.
