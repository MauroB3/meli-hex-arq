from dataclasses import dataclass

from src.main.purchase.domain.exceptions.purchase_invalid_amount_exception import PurchaseInvalidAmountException


@dataclass
class Purchase:
    product_id: str
    buyer_email: str
    amount: int
    date: str
    _id: str

    def _validate_amount(self):
        if self.amount <= 0:
            raise PurchaseInvalidAmountException
        return True

    def validate(self):
        return self._validate_amount()
