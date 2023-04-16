import pymongo as pymongo
from src.user.domain.exceptions.user_already_exists_exception import UserAlreadyExistsException
from src.user.domain.exceptions.user_not_found_exception import UserNotFoundException
from src.user.domain.model.user import User
from src.user.domain.ports.user_repository import UserRepository
from src.config.mongodb_atlas import mongodb_uri, database_name
from src.user.infrastructure.mappers.user_mapper import map_user_to_dict


class MongoDBUserRepository(UserRepository):

    def __init__(self):
        self.client = pymongo.MongoClient(mongodb_uri)
        self.db = self.client[database_name]
        self.collection = self.db["user"]

    def create_user(self, _user: User):
        query = {"email": _user.email}
        if self.collection.find_one(query):
            raise UserAlreadyExistsException()

        mapped_user = map_user_to_dict(_user)
        res = self.collection.insert_one(mapped_user)
        return res.inserted_id

    def delete_user_by_email(self, email: str):
        query = {"email": email}
        res = self.collection.delete_one(query)
        if not res.deleted_count:
            raise UserNotFoundException()

        return True

    def update_user(self, user: User):
        query = {"email": user.email}
        new_values = {"$set": {"name": user.name, "last_name": user.last_name}}
        res = self.collection.update_one(query, new_values)
        if not res.modified_count:
            raise UserNotFoundException()

        return True

    def find_user_by_email(self, email: str):
        query = {"email": email}
        res = self.collection.find_one(query)
        if not res:
            raise UserNotFoundException()

        return res

    def find_user_by_id(self, _id: str):
        query = {"_id": _id}
        res = self.collection.find_one(query)
        if not res:
            raise UserNotFoundException

        return res
