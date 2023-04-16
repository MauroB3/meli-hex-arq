from src.seller.domain.ports.seller_repository import SellerRepository


def find_seller_by_email(seller_repository: SellerRepository, email: str):
    return seller_repository.find_seller_by_email(email)


def find_seller_by_id(seller_repository: SellerRepository, _id: str):
    return seller_repository.find_seller_by_id(_id)


def find_seller_by_name(seller_repository: SellerRepository, name: str):
    return seller_repository.find_seller_by_name(name)
