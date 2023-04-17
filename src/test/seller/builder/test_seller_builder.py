import unittest
from src.main.seller.domain.builder.seller_builder import SellerBuilder
from src.main.seller.domain.model.seller import Seller


class TestSellerBuilderMethods(unittest.TestCase):

    def setUp(self):
        self.builder = SellerBuilder()

    def test_build(self):
        seller = self.builder.build()
        self.assertIsInstance(seller, Seller)

    def test_with_id(self):
        _id = '123'
        user = self.builder.with_id(_id).build()
        self.assertEquals(user._id, _id)

    def test_with_name(self):
        name = 'test'
        user = self.builder.with_name(name).build()
        self.assertEquals(user.name, name)

    def test_with_email(self):
        email = 'test@gmail.com'
        user = self.builder.with_email(email).build()
        self.assertEquals(user.email, email)
