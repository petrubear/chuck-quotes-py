from pydantic import BaseModel


class QuoteResponse(BaseModel):
    quote: str
    length: int
