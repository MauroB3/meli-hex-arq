from src.seller.domain.ports.seller_repository import SellerRepository


def update_seller(seller_repository: SellerRepository, name: str, email: str):
    return seller_repository.update_seller(name, email)
