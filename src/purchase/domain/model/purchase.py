from dataclasses import dataclass


@dataclass
class Purchase:
    product: str
    buyer_email: str
    amount: int
    date: str
