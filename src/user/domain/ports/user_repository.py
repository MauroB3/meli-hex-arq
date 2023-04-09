from src.user.domain.model import user
from abc import ABC, abstractmethod


class UserRepository(ABC):
    @abstractmethod
    def create_user(self, _user: user):
        pass

    @abstractmethod
    def delete_user_by_email(self, _mail: str):
        pass

    @abstractmethod
    def save_user(self, _user: user):
        pass
