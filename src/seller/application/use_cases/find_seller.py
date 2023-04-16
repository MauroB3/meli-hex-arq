from src.seller.domain.ports.seller_repository import SellerRepository


def find_seller(seller_repository: SellerRepository, email: str):
    return seller_repository.find_seller_by_email(email)
