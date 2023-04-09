from src.product.domain.model.money import Money
from src.seller.domain.model import seller
from dataclasses import dataclass
from uuid import uuid1


@dataclass
class Product:
    _id: uuid1()
    name: str
    description: str
    money: Money
    _seller: seller
    stock: int = 0
