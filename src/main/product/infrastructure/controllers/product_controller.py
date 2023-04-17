from fastapi import APIRouter
from fastapi.responses import JSONResponse

from product.infrastructure.dto.product_category_dto import ProductCategoryDTO
from src.main.product.domain.ports.product_repository import ProductRepository
from src.main.product.infrastructure.dto.product_dto import ProductDTO
from src.main.product.infrastructure.dto.product_id_dto import ProductIdDTO
from src.main.product.infrastructure.dto.product_name_dto import ProductNameDTO
from src.main.product.infrastructure.dto.product_seller_dto import ProductSellerDTO
from src.main.product.infrastructure.dto.product_seller_name_dto import ProductNameSellerDTO
from src.main.product.infrastructure.dto.product_update_dto import ProductUpdateDTO
from src.main.seller.domain.ports.seller_repository import SellerRepository
from src.main.product.application.use_cases.create_product import create_product as create_product_uc
from src.main.product.application.use_cases.delete_product import delete_product as delete_product_uc
from src.main.product.application.use_cases.update_product import update_product as update_product_uc
from src.main.product.application.use_cases.find_product import find_product_by_id as find_product_by_id_uc
from src.main.product.application.use_cases.find_product import find_product_by_name as find_product_by_name_uc
from src.main.product.application.use_cases.find_product import find_product_by_seller as find_product_by_seller_uc
from src.main.product.application.use_cases.find_product import find_product_by_category as find_product_by_category_uc


class ProductController:
    def __init__(self, product_repository: ProductRepository, seller_repository: SellerRepository):
        self.product_repository = product_repository
        self.seller_repository = seller_repository
        self.router = APIRouter()
        self.init_routes()

    def init_routes(self):
        self.router.add_api_route("/product/create", self.create_product, methods=['POST'])
        self.router.add_api_route("/product/delete", self.delete_product_by_name_and_seller, methods=['POST'])
        self.router.add_api_route("/product/update", self.update_product, methods=['POST'])
        self.router.add_api_route("/product/find_by_id", self.find_product_by_id, methods=['POST'])
        self.router.add_api_route("/product/find_by_name", self.find_product_by_name, methods=['POST'])
        self.router.add_api_route("/product/find_by_seller", self.find_product_by_seller, methods=['POST'])
        self.router.add_api_route("/product/find_by_category", self.find_product_by_category, methods=['POST'])

    def create_product(self, product: ProductDTO):
        create_product_uc(product_repository=self.product_repository, seller_repository=self.seller_repository,
                          seller_email=product.seller_email, name=product.name, description=product.description,
                          price=product.price, category=product.category, stock=product.stock)
        return JSONResponse(status_code=201, content={"message": "Product created."})

    def delete_product_by_name_and_seller(self, product: ProductNameSellerDTO):
        delete_product_uc(product_repository=self.product_repository, seller_email=product.seller_email,
                          product_name=product.name)
        return JSONResponse(status_code=200, content={"message": "Product deleted."})

    def update_product(self, product: ProductUpdateDTO):
        update_product_uc(product_repository=self.product_repository, product_id=product.id, name=product.name,
                          description=product.description, category=product.category, price=product.price,
                          stock=product.stock)
        return JSONResponse(status_code=200, content={"message": "Product updated."})

    def find_product_by_id(self, product: ProductIdDTO):
        product_res = find_product_by_id_uc(product_repository=self.product_repository, product_id=product.id)
        return JSONResponse(status_code=200, content={"message": "Product found.", "product": product_res})

    def find_product_by_name(self, product: ProductNameDTO):
        product_res = find_product_by_name_uc(product_repository=self.product_repository, name=product.name)
        return JSONResponse(status_code=200, content={"message": "Products found.", "products": product_res})

    def find_product_by_seller(self, product: ProductSellerDTO):
        product_res = find_product_by_seller_uc(product_repository=self.product_repository,
                                                seller_email=product.seller_email)
        return JSONResponse(status_code=200, content={"message": "Products found.", "products": product_res})

    def find_product_by_category(self, product: ProductCategoryDTO):
        product_res = find_product_by_category_uc(product_repository=self.product_repository,
                                                category=product.category)
        return JSONResponse(status_code=200, content={"message": "Products found.", "products": product_res})
