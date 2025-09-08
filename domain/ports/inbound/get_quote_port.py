from abc import ABC, abstractmethod


class GetQuotePort(ABC):
    @abstractmethod
    async def get_quote(self) -> str:
        pass
