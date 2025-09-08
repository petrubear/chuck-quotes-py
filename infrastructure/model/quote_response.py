from pydantic import BaseModel

from application.service.quote_service import QuoteService


class QuoteResponse(BaseModel):
    quote: str
    len: int
