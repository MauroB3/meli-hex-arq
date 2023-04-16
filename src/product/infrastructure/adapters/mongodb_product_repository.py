import pymongo

from src.config.mongodb_atlas import mongodb_uri, database_name
from src.product.domain.exceptions.product_not_found_exception import ProductNotFoundException
from src.product.domain.exceptions.product_with_duplicated_name_exception import ProductWithDuplicatedEmailException
from src.product.domain.mappers.product_mapper import map_product_to_dict
from src.product.domain.model.product import Product
from src.product.domain.ports.product_repository import ProductRepository


class MongoDBProductRepository(ProductRepository):

    def __init__(self):
        self.client = pymongo.MongoClient(mongodb_uri)
        self.db = self.client[database_name]
        self.collection = self.db["product"]

    def create_product(self, product: Product):
        query = {"seller_email": product.seller_email, "name": product.name}
        if self.collection.find_one(query):
            raise ProductWithDuplicatedEmailException()

        mapped_product = map_product_to_dict(product)
        res = self.collection.insert_one(mapped_product)

        return res.inserted_id

    def delete_product_by_name_and_seller(self, seller_email: str, product_name: str):
        query = {"seller_email": seller_email, "name": product_name}
        res = self.collection.delete_one(query)
        if not res.deleted_count:
            raise ProductNotFoundException()

        return True

    def update_product(self, product: Product):
        product.validate()
        query = {"_id": product._id}
        print(product._id)
        new_values = {"$set": {"name": product.name, "price": product.price, "description": product.description}}
        res = self.collection.update_one(query, new_values)
        if not res.modified_count:
            raise ProductNotFoundException

        return True

    def find_product_by_id(self, product_id: str):
        query = {"_id": product_id}
        res = self.collection.find_one(query)
        if not res:
            raise ProductNotFoundException

        return res

    def find_product_by_name(self, name: str):
        pass

    def find_product_by_seller(self, seller_email: str):
        pass
