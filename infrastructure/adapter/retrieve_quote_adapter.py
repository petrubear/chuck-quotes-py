import httpx

from domain.model.quote import Quote
from domain.ports.outbound.retrieve_quote_port import RetrieveQuotePort
from infrastructure.model.chuck_quote import ChuckQuote


class RetrieveQuoteAdapter(RetrieveQuotePort):
    def __init__(self, http_client: httpx.AsyncClient, api_url: str):
        self.http_client = http_client
        self.api_url = api_url

    async def get_quote(self) -> Quote:
        response = await self.http_client.get(self.api_url)
        response.raise_for_status()

        chuck_quote = ChuckQuote(**response.json())

        return chuck_quote.to_quote()
