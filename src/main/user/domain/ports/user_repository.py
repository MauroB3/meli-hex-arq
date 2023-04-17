from src.main.user.domain.model.user import User
from abc import ABC, abstractmethod


class UserRepository(ABC):
    @abstractmethod
    def create_user(self, user: User):
        pass

    @abstractmethod
    def delete_user_by_email(self, email: str):
        pass

    @abstractmethod
    def update_user(self, user: User):
        pass

    @abstractmethod
    def find_user_by_email(self, email: str):
        pass

    @abstractmethod
    def find_user_by_id(self, _id: str):
        pass
