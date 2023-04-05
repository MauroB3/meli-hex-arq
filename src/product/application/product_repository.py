from src.product.model import product
from abc import ABC, abstractmethod


class ProductRepository(ABC):
    @abstractmethod
    def create_product(self, _product: product):
        pass