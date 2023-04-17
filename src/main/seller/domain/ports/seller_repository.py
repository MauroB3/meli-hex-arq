from abc import ABC, abstractmethod
from src.main.seller.domain.model import Seller


class SellerRepository(ABC):
    @abstractmethod
    def create_seller(self, _seller: Seller):
        pass

    @abstractmethod
    def delete_seller_by_email(self, _mail: str):
        pass

    @abstractmethod
    def update_seller(self, seller: Seller):
        pass

    @abstractmethod
    def find_seller_by_email(self, _mail: str):
        pass

    @abstractmethod
    def find_seller_by_id(self, _id: str):
        pass

    @abstractmethod
    def find_seller_by_name(self, name: str):
        pass
