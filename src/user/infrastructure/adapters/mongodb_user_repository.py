import pymongo as pymongo

from src.user.domain.exceptions.user_not_found_exception import UserNotFoundException
from src.user.domain.model import user
from src.user.domain.ports.user_repository import UserRepository
from src.config.mongodb_atlas import mongodb_uri
from src.user.infrastructure.mappers.user_mapper import map_user_to_dict


class MongoDBUserRepository(UserRepository):

    def __init__(self):
        self.client = pymongo.MongoClient(mongodb_uri)
        self.db = self.client['arq-hex']
        self.collection = self.db["user"]

    def create_user(self, _user: user):
        mapped_user = map_user_to_dict(_user)
        self.collection.insert_one(mapped_user)

    def delete_user_by_email(self, email: str):
        query = {"email": email}
        return self.collection.delete_one(query).deleted_count

    def update_user(self, name: str, last_name: str, email: str):
        query = {"email": email}
        new_values = {"$set": {"name": name, "last_name": last_name}}
        res = self.collection.update_one(query, new_values)
        if not res.modified_count:
            raise UserNotFoundException()

        return True
