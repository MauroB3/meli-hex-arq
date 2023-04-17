import unittest

from src.main.purchase.domain.builder.purchase_builder import PurchaseBuilder
from src.main.purchase.domain.model.purchase import Purchase
from datetime import datetime


class TestPurchaseBuilderMethods(unittest.TestCase):

    def setUp(self):
        self.builder = PurchaseBuilder()

    def test_build(self):
        prod = self.builder.build()
        self.assertIsInstance(prod, Purchase)

    def test_with_id(self):
        _id = '123'
        purchase = self.builder.with_id(_id).build()
        self.assertEquals(purchase._id, _id)

    def test_with_product_id(self):
        product_id = '123'
        purchase = self.builder.with_product_id(product_id).build()
        self.assertEquals(purchase.product_id, product_id)

    def test_with_buyer_email(self):
        buyer_email = 'test@gmail.com'
        purchase = self.builder.with_buyer_email(buyer_email).build()
        self.assertEquals(purchase.buyer_email, buyer_email)

    def test_with_amount(self):
        amount = 10
        purchase = self.builder.with_amount(amount).build()
        self.assertEquals(purchase.amount, amount)

    def test_with_date(self):
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        purchase = self.builder.with_date(date).build()
        self.assertEquals(purchase.date, date)
