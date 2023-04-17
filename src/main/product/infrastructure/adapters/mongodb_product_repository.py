import pymongo

from src.main.config.mongodb_atlas import mongodb_uri, database_name
from src.main.product.domain.exceptions.product_not_found_exception import ProductNotFoundException
from src.main.product.domain.exceptions.product_with_duplicated_name_exception import ProductWithDuplicatedEmailException
from src.main.product.domain.mappers.product_mapper import map_product_to_dict
from src.main.product.domain.model.product import Product
from src.main.product.domain.ports.product_repository import ProductRepository


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
        query = {"_id": product._id}
        new_values = {"$set": {"name": product.name, "price": product.price, "description": product.description,
                               "stock": product.stock}}
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
        query = {"name": {'$regex': name, '$options': 'i'}}
        q_res = self.collection.find(query)
        res = list(q_res)
        if not res:
            raise ProductNotFoundException()

        return res

    def find_product_by_seller(self, seller_email: str):
        query = {"seller_email": {'$regex': seller_email, '$options': 'i'}}
        q_res = self.collection.find(query)
        res = list(q_res)
        if not res:
            raise ProductNotFoundException

        return res

    def find_product_by_category(self, category: str):
        query = {"category": {'$regex': category, '$options': 'i'}}
        q_res = self.collection.find(query)
        res = list(q_res)
        if not res:
            raise ProductNotFoundException

        return res
