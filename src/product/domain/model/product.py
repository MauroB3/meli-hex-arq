from dataclasses import dataclass
from uuid import uuid1

from src.product.domain.exceptions.product_invalid_price_exception import ProductInvalidPriceException
from src.product.domain.exceptions.product_invalid_stock_exception import ProductInvalidStockException


@dataclass
class Product:
    seller_email: str
    name: str
    description: str
    price: float
    stock: int = 0
    _id: str = uuid1().__str__()

    def _validate_stock(self):
        if self.stock < 0:
            raise ProductInvalidStockException()
        return True

    def _validate_price(self):
        if self.price <= 0:
            raise ProductInvalidPriceException()
        return True

    def validate(self):
        return self._validate_stock() and self._validate_price()

    @property
    def id(self):
        return self._id
