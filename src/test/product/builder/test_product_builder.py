import unittest

from src.main.product.domain.builder.product_builder import ProductBuilder
from src.main.product.domain.model.product import Product


class TestProductBuilderMethods(unittest.TestCase):

    def setUp(self):
        self.builder = ProductBuilder()

    def test_build(self):
        prod = self.builder.build()
        self.assertIsInstance(prod, Product)

    def test_with_id(self):
        _id = '123'
        prod = self.builder.with_id(_id).build()
        self.assertEquals(prod._id, _id)

    def test_with_seller_email(self):
        seller_email = '123@gmail.com'
        prod = self.builder.with_seller_email(seller_email).build()
        self.assertEquals(prod.seller_email, seller_email)

    def test_with_name(self):
        name = 'test'
        prod = self.builder.with_name(name).build()
        self.assertEquals(prod.name, name)

    def test_with_description(self):
        description = 'description'
        prod = self.builder.with_description(description).build()
        self.assertEquals(prod.description, description)

    def test_with_stock(self):
        stock = 10
        prod = self.builder.with_stock(stock).build()
        self.assertEquals(prod.stock, stock)

    def test_with_price(self):
        price = 100
        prod = self.builder.with_price(price).build()
        self.assertEquals(prod.price, price)

    def test_with_category(self):
        category = 'test'
        prod = self.builder.with_category(category).build()
        self.assertEquals(prod.category, category)
