from domain.model.quote import Quote
from domain.ports.inbound.get_quote_port import GetQuotePort
from domain.ports.outbound.retrieve_quote_port import RetrieveQuotePort


class GetQuoteUseCase(GetQuotePort):
    def __init__(self, retrieve_quote_port: RetrieveQuotePort):
        self.retrieveQuotePort = retrieve_quote_port

    def get_quote(self) -> Quote:
        return self.retrieveQuotePort.get_quote()
