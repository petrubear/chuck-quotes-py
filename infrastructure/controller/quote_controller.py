from fastapi import APIRouter, Depends

from application.service.quote_service import QuoteService
from domain.model.quote import Quote
from infrastructure.configuration.dependencies import get_quote_service

router = APIRouter(prefix="/api/v1", tags=["Quote"])


@router.get("/quote", response_model=Quote)
async def get_quote(quote_service: QuoteService = Depends(get_quote_service)) -> Quote:
    return quote_service.get_quote()