from src.main.user.domain.builder.user_builder import UserBuilder
from src.main.user.domain.ports.user_repository import UserRepository


def create_user(user_repository: UserRepository, name: str, last_name: str, email: str):
    user = UserBuilder() \
        .with_name(name) \
        .with_last_name(last_name) \
        .with_email(email) \
        .build()
    return user_repository.create_user(user)
