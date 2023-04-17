from src.main.product.domain.builder.product_builder import ProductBuilder
from src.main.product.domain.ports.product_repository import ProductRepository
from src.main.seller.application.use_cases.find_seller import find_seller_by_email
from src.main.seller.domain.ports.seller_repository import SellerRepository


def create_product(product_repository: ProductRepository, seller_repository: SellerRepository, seller_email: str,
                   name: str, description: str,
                   price: float, stock: int = 0):

    find_seller_by_email(seller_repository, seller_email)

    product = ProductBuilder(). \
        with_seller_email(seller_email). \
        with_name(name).with_description(description) \
        .with_price(price) \
        .with_stock(stock) \
        .build()

    product.validate()
    return product_repository.create_product(product)
