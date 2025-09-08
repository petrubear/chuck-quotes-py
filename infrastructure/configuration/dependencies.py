from fastapi import Depends

from application.service.quote_service import QuoteService
from application.usecases.get_quote_usecase import GetQuoteUseCase
from domain.ports.outbound.retrieve_quote_port import RetrieveQuotePort
from infrastructure.adapter.retrieve_quote_adapter import RetrieveQuoteAdapter


def get_retrieve_quote_adapter() -> RetrieveQuotePort:
    return RetrieveQuoteAdapter()


def get_get_quote_use_case(
    retrieve_quote_port: RetrieveQuotePort = Depends(get_retrieve_quote_adapter),
) -> GetQuoteUseCase:
    return GetQuoteUseCase(retrieve_quote_port)


def get_quote_service(
    get_quote_use_case: GetQuoteUseCase = Depends(get_get_quote_use_case),
) -> QuoteService:
    return QuoteService(get_quote_use_case)