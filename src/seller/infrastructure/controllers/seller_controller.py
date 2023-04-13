from bson.json_util import dumps
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from src.seller.application.services.seller_service import SellerService
from src.seller.infrastructure.dto.seller_dto import SellerDTO
from src.seller.infrastructure.dto.seller_email_dto import SellerEmailDTO


class SellerController:
    def __init__(self, seller_service: SellerService):
        self.seller_service = seller_service
        self.router = APIRouter()
        self.init_routes()

    def init_routes(self):
        self.router.add_api_route("/seller/create", self.create_seller, methods=['POST'])
        self.router.add_api_route("/seller/delete", self.delete_seller_by_email, methods=['POST'])
        self.router.add_api_route("/seller/update", self.update_seller, methods=['POST'])
        self.router.add_api_route("/seller/find", self.find_seller, methods=['POST'])

    def create_seller(self, seller: SellerDTO):
        self.seller_service.create_seller(name=seller.name, email=seller.email)
        return JSONResponse(status_code=201, content={"message": "Seller created."})

    def delete_seller_by_email(self, seller: SellerEmailDTO):
        self.seller_service.delete_seller_by_email(seller.email)
        return JSONResponse(status_code=200, content={"message": "Seller deleted."})

    def update_seller(self, seller: SellerDTO):
        self.seller_service.update_seller(name=seller.name, email=seller.email)
        return JSONResponse(status_code=200, content={"message": "Seller updated."})

    def find_seller(self, seller: SellerEmailDTO):
        seller = self.seller_service.find_seller(seller.email)
        return JSONResponse(status_code=200, content={"message": "Seller found.", "seller": dumps(seller)})
