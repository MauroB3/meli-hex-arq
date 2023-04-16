from src.seller.domain.model.seller import Seller


class SellerBuilder:
    def __init__(self):
        self.seller = Seller(name="", email="")

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
