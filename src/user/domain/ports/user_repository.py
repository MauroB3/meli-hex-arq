from src.user.domain.model import user
from abc import ABC, abstractmethod


class UserRepository(ABC):
    @abstractmethod
    def create_user(self, _user: user):
        pass

    @abstractmethod
    def delete_user_by_email(self, email: str):
        pass

    @abstractmethod
    def update_user(self, name: str, last_name: str, email: str):
        pass

    @abstractmethod
    def find_user(self, email: str):
        pass
