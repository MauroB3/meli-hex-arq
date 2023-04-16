from abc import ABC, abstractmethod

from src.purchase.domain.model.purchase import Purchase


class PurchaseRepository(ABC):

    @abstractmethod
    def create_purchase(self, purchase: Purchase):
        pass

    @abstractmethod
    def update_purchase(self, purchase: Purchase):
        pass
