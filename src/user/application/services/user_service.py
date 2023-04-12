from src.user.domain.ports.user_repository import UserRepository
from src.user.domain.builder.user_builder import UserBuilder


class UserService:
    def __init__(self, _repository: UserRepository):
        self._repository = _repository

    def create_user(self, name: str, last_name: str, email: str):
        user = UserBuilder()\
            .with_name(name)\
            .with_last_name(last_name)\
            .with_email(email)\
            .build()
        return self._repository.create_user(user)

    def delete_user_by_email(self, email: str):
        return self._repository.delete_user_by_email(email)

    def update_user(self, name: str, last_name: str, email: str):
        return self._repository.update_user(name, last_name, email)

    def find_user(self, email: str):
        return self._repository.find_user(email)
