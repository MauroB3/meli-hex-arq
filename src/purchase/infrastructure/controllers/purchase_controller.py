from datetime import datetime

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from src.product.domain.ports.product_repository import ProductRepository
from src.purchase.domain.ports.purchase_adapter import PurchaseRepository
from src.purchase.infrastructure.dto.purchase_dto import PurchaseDTO
from src.purchase.application.use_cases.create_purchase import create_purchase as create_purchase_uc
from src.user.domain.ports.user_repository import UserRepository


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

    def create_purchase(self, purchase: PurchaseDTO):
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        create_purchase_uc(purchase_repository=self.purchase_repository, product_repository=self.product_repository,
                           user_repository=self.user_repository, product_id=purchase.product_id,
                           buyer_email=purchase.buyer_email, amount=purchase.amount, date=date)
        return JSONResponse(status_code=201, content={"message": "Purchase created."})
