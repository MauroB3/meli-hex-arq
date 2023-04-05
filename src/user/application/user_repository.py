from src.user.model import user
from abc import ABC, abstractmethod


class UserRepository(ABC):
    @abstractmethod
    def create_user(self, _user: user):
        pass
