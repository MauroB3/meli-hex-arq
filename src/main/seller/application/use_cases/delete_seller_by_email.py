from src.main.seller.domain.ports.seller_repository import SellerRepository


def delete_seller_by_email(seller_repository: SellerRepository, email: str):
    return seller_repository.delete_seller_by_email(email)
