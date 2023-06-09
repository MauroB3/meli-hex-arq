from abc import ABC, abstractmethod
from src.main.product.domain.model.product import Product


class ProductRepository(ABC):
    @abstractmethod
    def create_product(self, product: Product):
        pass

    @abstractmethod
    def delete_product_by_name_and_seller(self, seller_email: str, product_name: str):
        pass

    @abstractmethod
    def update_product(self, product: Product):
        pass

    @abstractmethod
    def find_product_by_id(self, product_id: str):
        pass

    @abstractmethod
    def find_product_by_name(self, name: str):
        pass

    @abstractmethod
    def find_product_by_seller(self, seller_email: str):
        pass

    @abstractmethod
    def find_product_by_category(self, category: str):
        pass

    @abstractmethod
    def filter_price_between(self, start_price: float, end_price: float):
        pass

    @abstractmethod
    def filter_price_greater_than(self, price: float):
        pass

    @abstractmethod
    def filter_price_smaller_than(self, price: float):
        pass
