from abc import ABC, abstractmethod

from domain.model.quote import Quote


class RetrieveQuotePort(ABC):
    @abstractmethod
    def get_quote(self) -> Quote:
        pass
