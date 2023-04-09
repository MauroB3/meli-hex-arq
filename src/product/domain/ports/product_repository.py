from src.product.domain.model import product
from abc import ABC, abstractmethod


class ProductRepository(ABC):
    @abstractmethod
    def create_product(self, _product: product):
        pass

    @abstractmethod
    def delete_product_by_id(self, _id: str):
        pass

    @abstractmethod
    def save_product(self, _product: product):
        pass
