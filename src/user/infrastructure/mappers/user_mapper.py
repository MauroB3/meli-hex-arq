from src.user.domain.model import user


def map_user_to_dict(_user: user):
    return _user.__dict__
