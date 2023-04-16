from src.user.domain.model.user import User
from uuid import uuid1


class UserBuilder:
    def __init__(self):
        self.user = User(name="", last_name="", email="", _id=uuid1().__str__())

    def with_id(self, _id: str):
        self.user._id = _id
        return self

    def with_name(self, name: str):
        self.user.name = name
        return self

    def with_last_name(self, last_name: str):
        self.user.last_name = last_name
        return self

    def with_email(self, email: str):
        self.user.email = email
        return self

    def build(self):
        return self.user
