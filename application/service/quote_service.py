from application.usecases.get_quote_usecase import GetQuoteUseCase
from domain.model.quote import Quote


class QuoteService:
    def __init__(self, get_quote_usecase: GetQuoteUseCase):
        self.get_quote_usecase = get_quote_usecase

    def get_quote(self) -> Quote:
        return self.get_quote_usecase.get_quote()
