import pymongo as pymongo
from src.config.mongodb_atlas import mongodb_uri, database_name
from src.purchase.domain.model.purchase import Purchase
from src.purchase.domain.ports.purchase_adapter import PurchaseRepository
from src.purchase.infrastructure.mappers.purchase_mapper import map_purchase_to_dict


class MongoDBPurchaseRepository(PurchaseRepository):

    def __init__(self):
        self.client = pymongo.MongoClient(mongodb_uri)
        self.db = self.client[database_name]
        self.collection = self.db["purchase"]

    def create_purchase(self, purchase: Purchase):
        mapped_purchase = map_purchase_to_dict(purchase)
        res = self.collection.insert_one(mapped_purchase)
        return res

    def update_purchase(self, purchase: Purchase):
        pass

    def find_purchases_of_user(self, user_email: str):
        pass

    def find_sales_of_seller(self, seller_email: str):
        pass

    def find_sales_of_product(self, product_id: str):
        pass

