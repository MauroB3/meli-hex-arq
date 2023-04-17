from src.main.user.domain.ports.user_repository import UserRepository


def delete_user_by_email(user_repository: UserRepository, email: str):
    return user_repository.delete_user_by_email(email)
