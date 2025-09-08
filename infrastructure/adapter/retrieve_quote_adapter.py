import httpx

from domain.model.quote import Quote
from domain.ports.outbound.retrieve_quote_port import RetrieveQuotePort
from infrastructure.model.chuck_quote import ChuckQuote


class RetrieveQuoteAdapter(RetrieveQuotePort):
    def get_quote(self) -> Quote:
        response = httpx.get("https://api.chucknorris.io/jokes/random")
        response.raise_for_status()

        chuck_quote = ChuckQuote(**response.json())

        return chuck_quote.to_quote()
