from abc import ABC, abstractmethod

from domain.model.quote import Quote


class RetrieveQuotePort(ABC):
    @abstractmethod
    async def get_quote(self) -> Quote:
        pass
