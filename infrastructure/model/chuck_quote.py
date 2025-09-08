from pydantic import BaseModel

from domain.model.quote import Quote


class ChuckQuote(BaseModel):
    categories: list
    created_at: str
    icon_url: str
    id: str
    updated_at: str
    url: str
    value: str

    def to_quote(self) -> Quote:
        return Quote(value=self.value)
