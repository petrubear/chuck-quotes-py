from abc import ABC, abstractmethod


class GetQuotePort(ABC):
    @abstractmethod
    def get_quote(self) -> str:
        pass
