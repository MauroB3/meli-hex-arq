from dataclasses import dataclass


@dataclass
class Purchase:
    product_id: str
    buyer_email: str
    amount: int
    date: str
    _id: str
