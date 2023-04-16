from src.product.domain.builder.product_builder import ProductBuilder
from src.product.domain.ports.product_repository import ProductRepository
from src.seller.application.use_cases.find_seller import find_seller_by_email
from src.seller.domain.ports.seller_repository import SellerRepository


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
    print(product._id)
    return product_repository.create_product(product)
