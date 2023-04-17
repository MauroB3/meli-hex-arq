from src.main.user.domain.ports.user_repository import UserRepository


def find_user_by_email(user_repository: UserRepository, email: str):
    return user_repository.find_user_by_email(email)


def find_user_by_id(user_repository: UserRepository, _id: str):
    return user_repository.find_user_by_id(_id)
