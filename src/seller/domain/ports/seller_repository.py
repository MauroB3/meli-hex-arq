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
    def save_seller(self, _seller: seller):
        pass
