import unittest

from src.main.purchase.domain.exceptions.purchase_invalid_amount_exception import PurchaseInvalidAmountException
from src.main.purchase.domain.model.purchase import Purchase


class TestPurchaseMethods(unittest.TestCase):

    def setUp(self):
        self.purchase = Purchase("", "", 1, "", "")

    def test_validate_purchase(self):
        self.purchase.amount = 10
        self.assertTrue(self.purchase.validate())

    def test_invalid_purchase(self):
        self.purchase.amount = 0
        with self.assertRaises(PurchaseInvalidAmountException):
            self.purchase.validate()
