import pymongo as pymongo

from src.seller.domain.exceptions.seller_already_exists_exception import SellerAlreadyExistsException
from src.seller.domain.exceptions.seller_not_found_exception import SellerNotFoundException
from src.seller.domain.model import seller
from src.seller.domain.ports.seller_repository import SellerRepository
from src.config.mongodb_atlas import mongodb_uri
from src.seller.infrastructure.mappers.seller_mapper import map_seller_to_dict


class MongoDBSellerRepository(SellerRepository):

    def __init__(self):
        self.client = pymongo.MongoClient(mongodb_uri)
        self.db = self.client['arq-hex']
        self.collection = self.db["seller"]

    def create_seller(self, _seller: seller):
        query = {"email": _seller.email}
        if self.collection.find_one(query):
            raise SellerAlreadyExistsException()

        mapped_seller = map_seller_to_dict(_seller)
        res = self.collection.insert_one(mapped_seller)
        return res.inserted_id

    def delete_seller_by_email(self, email: str):
        query = {"email": email}
        res = self.collection.delete_one(query)
        if not res.deleted_count:
            raise SellerNotFoundException()

        return True

    def update_seller(self, name: str, email: str):
        query = {"email": email}
        new_values = {"$set": {"name": name}}
        res = self.collection.update_one(query, new_values)
        if not res.modified_count:
            raise SellerNotFoundException()

        return True

    def find_seller(self, email: str):
        query = {"email": email}
        res = self.collection.find_one(query)
        if not res:
            raise SellerNotFoundException()

        return res
