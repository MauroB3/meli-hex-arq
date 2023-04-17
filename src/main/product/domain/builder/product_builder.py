from src.main.product.domain.model.product import Product
from uuid import uuid1


class ProductBuilder:
    def __init__(self):
        self.product = Product(seller_email='', name='', description='', stock=0, price=0, category='',
                               _id=uuid1().__str__())

    def with_id(self, _id: str):
        self.product._id = _id
        return self

    def with_seller_email(self, seller_email: str):
        self.product.seller_email = seller_email
        return self

    def with_name(self, name: str):
        self.product.name = name
        return self

    def with_description(self, description: str):
        self.product.description = description
        return self

    def with_stock(self, stock: int):
        self.product.stock = stock
        return self

    def with_price(self, price: float):
        self.product.price = price
        return self

    def with_category(self, category: str):
        self.product.category = category
        return self

    def build(self):
        return self.product
