from src.seller.model import seller
from dataclasses import dataclass
from uuid import uuid1


@dataclass
class Product:
    _id: uuid1()
    name: str
    description: str
    price: float
    _seller: seller
    stock: int = 0
