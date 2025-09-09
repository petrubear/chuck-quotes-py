from fastapi import APIRouter, Depends

from application.service.quote_service import QuoteService
from infrastructure.configuration.dependencies import get_quote_service
from infrastructure.model.quote_response import QuoteResponse

router = APIRouter(prefix="/api/v1", tags=["Quote"])


@router.get("/quote", response_model=QuoteResponse)
async def get_quote(quote_service: QuoteService = Depends(get_quote_service)) -> QuoteResponse:
    quote = await quote_service.get_quote()
    return QuoteResponse(quote=quote.value,
                         length=len(quote.value))
