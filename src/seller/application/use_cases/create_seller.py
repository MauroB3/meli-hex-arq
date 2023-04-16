from src.seller.domain.builder.seller_builder import SellerBuilder
from src.seller.domain.ports.seller_repository import SellerRepository


def create_seller(seller_repository: SellerRepository, name: str, email: str):
    seller = SellerBuilder() \
        .with_name(name) \
        .with_email(email) \
        .build()

    return seller_repository.create_seller(seller)
