# Financial Document Analyzer (CrewAI Debug Challenge)

## 1. Overview

This project is a corrected and improved version of a financial document analysis system built using CrewAI.
The original codebase contained multiple issues including dependency conflicts, broken components, and inefficient prompt design.

The system has been debugged, simplified, and made fully functional. It now processes financial PDF documents and generates structured analytical insights.

---

## 2. Bugs Identified and Fixes

### 2.1 Dependency Conflicts

* The original project included incompatible libraries such as `crewai-tools`, `langchain-openai`, and `litellm`
* These caused version conflicts with `openai` and `crewai`
* Fix:

  * Removed unnecessary and conflicting dependencies
  * Standardized environment using compatible versions

---

### 2.2 Incorrect LLM Initialization

* The code contained invalid or undefined LLM assignments (e.g., `llm = llm`)
* Fix:

  * Removed incorrect initialization
  * Used CrewAI’s default LLM configuration

---

### 2.3 Broken PDF Processing

* The project used an invalid PDF loader (`Pdf`)
* Fix:

  * Replaced with `pypdf` for reliable text extraction

---

### 2.4 Inefficient and Incorrect Prompts

* Prompts were vague and produced hallucinated or unrealistic outputs
* Fix:

  * Redesigned prompts to produce structured, factual financial analysis
  * Output now includes summary, insights, metrics, risks, and conclusion

---

### 2.5 Improper Data Flow

* The connection between API, tools, and agents was inconsistent
* Fix:

  * Rebuilt the pipeline:
    API → PDF extraction → Agent → Structured output

---

## 3. Improvements Made

* Simplified multi-agent system into a single reliable agent
* Added fallback mechanism to handle API failures gracefully
* Enabled automatic analysis using a default financial document when no file is uploaded
* Added SQLite database integration to store analysis results
* Cleaned and modularized the codebase

---

## 4. Setup Instructions

### 4.1 Prerequisites

* Python 3.11

---

### 4.2 Create Virtual Environment

```bash
py -3.11 -m venv venv
venv\Scripts\activate
```

---

### 4.3 Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4.4 Environment Variables

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your_api_key
```

---

## 5. Running the Application

```bash
uvicorn main:app --reload
```

Access the API documentation at:

```
http://127.0.0.1:8000/docs
```

---

## 6. API Documentation

### Endpoint: POST /analyze

#### Description

Analyzes a financial document and returns structured insights.

---

### Request Parameters

* file (optional): PDF file
* query (optional): Text query (default: "Analyze this financial document")

---

### Behavior

* If a file is uploaded → the uploaded file is analyzed
* If no file is provided → a default financial document from the repository is used

---

### Response Format

```
{
  "status": "success",
  "analysis": "Generated financial analysis..."
}
```

---

## 7. Database Integration

* SQLite database (`analysis.db`) is used
* Stores:

  * Query
  * Result
  * Timestamp

This enables persistence and future retrieval of analysis results.

---

## 8. Project Structure

```
project/
├── main.py
├── agents.py
├── task.py
├── tools.py
├── database.py
├── requirements.txt
├── README.md
└── data/
```

---

## 9. Conclusion

The system has been transformed from a non-functional codebase into a stable and usable financial document analyzer.
All major bugs were resolved, prompts were improved, and additional features such as fallback handling and database storage were introduced to enhance reliability and usability.
