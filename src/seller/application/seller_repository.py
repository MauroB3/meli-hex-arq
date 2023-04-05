from src.seller.model import seller
from abc import ABC, abstractmethod


class SellerRepository(ABC):
    @abstractmethod
    def create_seller(self, _seller: seller):
        pass
