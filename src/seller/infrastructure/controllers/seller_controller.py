from fastapi import APIRouter
from fastapi.responses import JSONResponse
from src.seller.domain.ports.seller_repository import SellerRepository
from src.seller.infrastructure.dto.seller_dto import SellerDTO
from src.seller.infrastructure.dto.seller_email_dto import SellerEmailDTO
from src.seller.infrastructure.dto.seller_id_dto import SellerIdDTO
from src.seller.infrastructure.dto.seller_name_dto import SellerNameDTO
from src.seller.application.use_cases.create_seller import create_seller as create_seller_uc
from src.seller.application.use_cases.delete_seller_by_email import delete_seller_by_email as delete_seller_by_email_uc
from src.seller.application.use_cases.update_seller import update_seller as update_seller_uc
from src.seller.application.use_cases.find_seller import find_seller_by_email as find_seller_by_email_uc
from src.seller.application.use_cases.find_seller import find_seller_by_id as find_seller_by_id_uc
from src.seller.application.use_cases.find_seller import find_seller_by_name as find_seller_by_name_uc


class SellerController:
    def __init__(self, seller_repository: SellerRepository):
        self.seller_repository = seller_repository
        self.router = APIRouter()
        self.init_routes()

    def init_routes(self):
        self.router.add_api_route("/seller/create", self.create_seller, methods=['POST'])
        self.router.add_api_route("/seller/delete", self.delete_seller_by_email, methods=['POST'])
        self.router.add_api_route("/seller/update", self.update_seller, methods=['POST'])
        self.router.add_api_route("/seller/find_by_email", self.find_by_email, methods=['POST'])
        self.router.add_api_route("/seller/find_by_id", self.find_by_id, methods=['POST'])
        self.router.add_api_route("/seller/find_by_name", self.find_by_name, methods=['POST'])

    def create_seller(self, seller: SellerDTO):
        create_seller_uc(seller_repository=self.seller_repository, name=seller.name, email=seller.email)
        return JSONResponse(status_code=201, content={"message": "Seller created."})

    def delete_seller_by_email(self, seller: SellerEmailDTO):
        delete_seller_by_email_uc(seller_repository=self.seller_repository, email=seller.email)
        return JSONResponse(status_code=200, content={"message": "Seller deleted."})

    def update_seller(self, seller: SellerDTO):
        update_seller_uc(seller_repository=self.seller_repository, name=seller.name, email=seller.email)
        return JSONResponse(status_code=200, content={"message": "Seller updated."})

    def find_by_email(self, seller: SellerEmailDTO):
        seller = find_seller_by_email_uc(seller_repository=self.seller_repository, email=seller.email)
        return JSONResponse(status_code=200, content={"message": "Seller found.", "seller": seller})

    def find_by_id(self, seller: SellerIdDTO):
        seller = find_seller_by_id_uc(seller_repository=self.seller_repository, _id=seller.id)
        return JSONResponse(status_code=200, content={"message": "Seller found.", "seller": seller})

    def find_by_name(self, seller: SellerNameDTO):
        sellers = find_seller_by_name_uc(seller_repository=self.seller_repository, name=seller.name)
        return JSONResponse(status_code=200, content={"message": "Sellers found.", "sellers": sellers})
