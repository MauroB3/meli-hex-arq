from src.seller.domain.model import seller
from abc import ABC, abstractmethod


class SellerRepository(ABC):
    @abstractmethod
    def create_seller(self, _seller: seller):
        pass

    @abstractmethod
    def delete_seller_by_email(self, _mail: str):
        pass

    @abstractmethod
    def update_seller(self, name: str, _mail: str):
        pass

    @abstractmethod
    def find_seller(self, _mail: str):
        pass
