from fastapi import APIRouter
from app.models.invention import InventionRequest
from app.services.query_service import QueryService


router = APIRouter()

query_service = QueryService()


@router.post("/analyze")
def analyze_invention(request: InventionRequest):

    queries = query_service.expand_query(request.idea)

    return {
        "idea": request.idea,
        "queries": queries
    }