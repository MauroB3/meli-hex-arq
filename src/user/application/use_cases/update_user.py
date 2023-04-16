from src.user.application.use_cases.find_user import find_user_by_email
from src.user.domain.builder.user_builder import UserBuilder
from src.user.domain.ports.user_repository import UserRepository


def update_user(user_repository: UserRepository, name: str, last_name: str, email: str):
    user_db = find_user_by_email(user_repository=user_repository, email=email)
    user = UserBuilder()\
        .with_id(user_db['_id'])\
        .with_name(name)\
        .with_last_name(last_name)\
        .with_email(user_db['email'])\
        .build()
    return user_repository.update_user(user)
