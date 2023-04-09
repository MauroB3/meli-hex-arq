from dataclasses import dataclass


@dataclass
class Money:
    amount: float
    currency: str
