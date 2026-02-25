# main.py

from fastapi import FastAPI, File, UploadFile, Form, HTTPException
import os
import uuid

from crewai import Crew, Process

from agents import financial_analyst
from task import analyze_financial_document
from tools import FinancialDocumentTool
from database import init_db, save_analysis  

app = FastAPI(title="Financial Document Analyzer")


init_db()


def run_crew(query: str, file_path: str):
    """Run crew with document content"""

   
    document_text = FinancialDocumentTool.read_data_tool(file_path)

    financial_crew = Crew(
        agents=[financial_analyst],
        tasks=[analyze_financial_document],
        process=Process.sequential,
    )

    try:
        result = financial_crew.kickoff({
            "query": query,
            "document": document_text
        })
    except Exception:
        
        result = f"""
Fallback Analysis (AI unavailable):

Document Preview:
{document_text[:1000]}

Basic Insights:
- The document contains financial-related information.
- It likely includes revenue, expenses, or performance metrics.

Conclusion:
Detailed AI analysis could not be generated due to API limitations.
"""

    return result


@app.get("/")
async def root():
    return {"message": "API is running"}


@app.post("/analyze")
async def analyze(
    file: UploadFile = File(None),  
    query: str = Form(default="Analyze this financial document")
):
    file_path = ""

    try:
        os.makedirs("data", exist_ok=True)

        
        if file:
            file_id = str(uuid.uuid4())
            file_path = f"data/{file_id}.pdf"

            with open(file_path, "wb") as f:
                f.write(await file.read())

       
        else:
            file_path = "data/TSLA-Q2-2025-Update.pdf"

            if not os.path.exists(file_path):
                raise HTTPException(
                    status_code=400,
                    detail="Default Tesla PDF not found in data folder"
                )

        
        result = run_crew(query, file_path)

       
        save_analysis(query, str(result))

        return {
            "status": "success",
            "analysis": str(result)
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        
        if file and os.path.exists(file_path):
            os.remove(file_path)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
