from dataclasses import dataclass


@dataclass(frozen=True)
class Quote:
    value: str
