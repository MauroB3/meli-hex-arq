from uuid import uuid1
from datetime import datetime

from src.main.purchase.domain.model.purchase import Purchase


class PurchaseBuilder:
    def __init__(self):
        self.purchase = Purchase(_id=uuid1().__str__(), product_id='', buyer_email='', amount=0,
                                 date=datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

    def with_id(self, _id: str):
        self.purchase._id = _id
        return self

    def with_product_id(self, product_id: str):
        self.purchase.product_id = product_id
        return self

    def with_buyer_email(self, buyer_email):
        self.purchase.buyer_email = buyer_email
        return self

    def with_amount(self, amount: int):
        self.purchase.amount = amount
        return self

    def with_date(self, date: str):
        self.purchase.date = date
        return self

    def build(self):
        return self.purchase
