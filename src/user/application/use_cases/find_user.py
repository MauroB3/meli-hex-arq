from src.user.domain.ports.user_repository import UserRepository


def find_user(user_repository: UserRepository, email: str):
    return user_repository.find_user(email)
