import httpx
from functools import lru_cache
from fastapi import Depends, Request
from application.service.quote_service import QuoteService
from application.usecases.get_quote_usecase import GetQuoteUseCase
from domain.ports.outbound.retrieve_quote_port import RetrieveQuotePort
from infrastructure.adapter.retrieve_quote_adapter import RetrieveQuoteAdapter
from infrastructure.configuration.config import Settings


def get_http_client(request: Request) -> httpx.AsyncClient:
    return request.app.state.http_client


@lru_cache()
def get_settings() -> Settings:
    return Settings()


def get_retrieve_quote_adapter(
        http_client: httpx.AsyncClient = Depends(get_http_client),
        settings: Settings = Depends(get_settings)

) -> RetrieveQuotePort:
    return RetrieveQuoteAdapter(http_client, settings.chuck_api_url)


def get_get_quote_use_case(
        retrieve_quote_port: RetrieveQuotePort = Depends(get_retrieve_quote_adapter),
) -> GetQuoteUseCase:
    return GetQuoteUseCase(retrieve_quote_port)


def get_quote_service(
        get_quote_use_case: GetQuoteUseCase = Depends(get_get_quote_use_case),
) -> QuoteService:
    return QuoteService(get_quote_use_case)
