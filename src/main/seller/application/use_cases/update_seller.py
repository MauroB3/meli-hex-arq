from src.main.seller.domain.builder.seller_builder import SellerBuilder
from src.main.seller.domain.ports.seller_repository import SellerRepository


def update_seller(seller_repository: SellerRepository, name: str, email: str):
    seller_db = seller_repository.find_seller_by_email(email)

    seller = SellerBuilder()\
        .with_id(seller_db['_id'])\
        .with_name(name).with_email(email)\
        .build()
    return seller_repository.update_seller(seller)
