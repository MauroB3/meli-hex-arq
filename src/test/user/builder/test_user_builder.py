import unittest

from src.main.user.domain.builder.user_builder import UserBuilder
from src.main.user.domain.model.user import User


class TestUserBuilderMethods(unittest.TestCase):

    def setUp(self):
        self.builder = UserBuilder()

    def test_build(self):
        user = self.builder.build()
        self.assertIsInstance(user, User)

    def test_with_id(self):
        _id = '123'
        user = self.builder.with_id(_id).build()
        self.assertEquals(user._id, _id)

    def test_with_name(self):
        name = 'test'
        user = self.builder.with_name(name).build()
        self.assertEquals(user.name, name)

    def test_with_id(self):
        last_name = 'test'
        user = self.builder.with_last_name(last_name).build()
        self.assertEquals(user.last_name, last_name)

    def test_with_email(self):
        email = 'test@gmail.com'
        user = self.builder.with_email(email).build()
        self.assertEquals(user.email, email)
