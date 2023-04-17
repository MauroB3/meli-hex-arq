from abc import ABC, abstractmethod

from src.main.purchase.domain.model.purchase import Purchase


class PurchaseRepository(ABC):

    @abstractmethod
    def create_purchase(self, purchase: Purchase):
        pass

    @abstractmethod
    def find_purchases_of_user(self, user_email: str):
        pass

    @abstractmethod
    def find_sales_of_product(self, product_id: str):
        pass
