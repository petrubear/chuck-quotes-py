from domain.model.quote import Quote
from domain.ports.outbound.retrieve_quote_port import RetrieveQuotePort


class RetrieveQuoteAdapter(RetrieveQuotePort):
    def get_quote(self) -> Quote:
        return Quote(value="Hello World")
