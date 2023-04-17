import unittest
from src.main.product.domain.model.product import Product
from src.main.product.domain.exceptions.product_invalid_stock_exception import ProductInvalidStockException
from src.main.product.domain.exceptions.product_invalid_price_exception import ProductInvalidPriceException


class TestProductMethods(unittest.TestCase):

    def setUp(self):
        self.product = Product("", "", "", 1, "", 0)

    def test_valid_product(self):
        self.product.price = 1
        self.product.stock = 1
        self.assertTrue(self.product.validate())

    def test_invalid_price_product(self):
        self.product.price = 0
        self.assertRaises(ProductInvalidPriceException, self.product.validate)

    def test_invalid_stock_product(self):
        self.product.stock = -1
        self.assertRaises(ProductInvalidStockException, self.product.validate)

    def test_valid_reduce_stock(self):
        self.product.stock = 10
        self.product.reduce_stock(5)
        self.assertEquals(self.product.stock, 5)

    def test_invalid_reduce_stock(self):
        self.product.stock = 1
        with self.assertRaises(ProductInvalidStockException):
            self.product.reduce_stock(2)
