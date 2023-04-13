from src.seller.domain.ports.seller_repository import SellerRepository
from src.seller.domain.builder.seller_builder import SellerBuilder


class SellerService:
    def __init__(self, _repository: SellerRepository):
        self._repository = _repository

    def create_seller(self, name: str, email: str):
        seller = SellerBuilder()\
            .with_name(name)\
            .with_email(email)\
            .build()
        return self._repository.create_seller(seller)

    def delete_seller_by_email(self, email: str):
        return self._repository.delete_seller_by_email(email)

    def update_seller(self, name: str, email: str):
        return self._repository.update_seller(name, email)

    def find_seller(self, email: str):
        return self._repository.find_seller(email)
