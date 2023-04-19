from datetime import datetime

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from src.main.product.domain.ports.product_repository import ProductRepository
from src.main.purchase.domain.ports.purchase_adapter import PurchaseRepository
from src.main.purchase.infrastructure.dto.purchase_buyer_dto import PurchaseBuyerDTO
from src.main.purchase.infrastructure.dto.purchase_id_dto import PurchaseProductIdDTO
from src.main.user.domain.ports.user_repository import UserRepository
from src.main.purchase.infrastructure.dto.purchase_dto import PurchaseDTO
from src.main.purchase.application.use_cases.create_purchase import create_purchase as create_purchase_uc
from src.main.purchase.application.use_cases.find_purchase import find_purchases_of_user as find_purchases_of_user_uc
from src.main.purchase.application.use_cases.find_purchase import find_sales_of_product as find_sales_of_product_uc


class PurchaseController:
    def __init__(self, purchase_repository: PurchaseRepository, user_repository: UserRepository,
                 product_repository: ProductRepository):
        self.purchase_repository = purchase_repository
        self.product_repository = product_repository
        self.user_repository = user_repository
        self.router = APIRouter()
        self.init_routes()

    def init_routes(self):
        self.router.add_api_route("/purchase/create", self.create_purchase, methods=['POST'])
        self.router.add_api_route("/purchase/find_by_user", self.find_purchases_of_user, methods=['POST'])
        self.router.add_api_route("/purchase/find_by_product", self.find_sales_by_product, methods=['POST'])

    def create_purchase(self, purchase: PurchaseDTO):
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        create_purchase_uc(purchase_repository=self.purchase_repository, product_repository=self.product_repository,
                           user_repository=self.user_repository, product_id=purchase.product_id,
                           buyer_email=purchase.buyer_email, amount=purchase.amount, date=date)
        return JSONResponse(status_code=201, content={"message": "Purchase created."})

    def find_purchases_of_user(self, purchase: PurchaseBuyerDTO):
        purchases = find_purchases_of_user_uc(purchase_repository=self.purchase_repository,
                                              user_email=purchase.buyer_email)
        return JSONResponse(status_code=200, content={"message": "Purchases found.", "purchases": purchases})

    def find_sales_by_product(self, purchase: PurchaseProductIdDTO):
        purchases = find_sales_of_product_uc(purchase_repository=self.purchase_repository,
                                             product_id=purchase.product_id)
        return JSONResponse(status_code=200, content={"message": "Purchases found.", "purchases": purchases})
