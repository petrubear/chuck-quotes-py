from application.service.quote_service import QuoteService
from fastapi import APIRouter

from domain.model.quote import Quote

router = APIRouter(prefix="/api/v1", tags=["Quote"])


class QuoteController:
    def __init__(self, quote_service: QuoteService):
        self.quote_service = quote_service

    @router.get("/quote", response_model=Quote)
    async def get_quote(self):
        return await self.quote_service.get_quote()
