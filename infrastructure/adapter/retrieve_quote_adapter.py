import httpx

from domain.model.quote import Quote
from domain.ports.outbound.retrieve_quote_port import RetrieveQuotePort


class RetrieveQuoteAdapter(RetrieveQuotePort):
    def get_quote(self) -> Quote:
        response = httpx.get("https://api.chucknorris.io/jokes/random")
        response.raise_for_status()
        return Quote(value=response.json()["value"])
