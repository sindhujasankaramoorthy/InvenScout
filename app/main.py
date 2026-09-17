from fastapi import FastAPI
from app.controllers.patent_controller import router as patent_router


app = FastAPI(
    title="InvenScout",
    description="AI-powered prior-art and market research agent",
    version="0.1.0"
)


app.include_router(patent_router)


@app.get("/")
def root():
    return {
        "message": "InvenScout API is running"
    }