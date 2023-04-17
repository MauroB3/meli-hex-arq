from src.main.seller.domain.model.seller import Seller
from uuid import uuid1


class SellerBuilder:
    def __init__(self):
        self.seller = Seller(name="", email="", _id=uuid1().__str__())

    def with_id(self, _id: str):
        self.seller._id = _id
        return self

    def with_name(self, name: str):
        self.seller.name = name
        return self

    def with_email(self, email: str):
        self.seller.email = email
        return self

    def build(self):
        return self.seller
