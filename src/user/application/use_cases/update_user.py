from src.user.domain.ports.user_repository import UserRepository


def update_user(user_repository: UserRepository, name: str, last_name: str, email: str):
    return user_repository.update_user(name, last_name, email)
