from src.product.application.use_cases.find_product import find_product_by_id
from src.product.domain.builder.product_builder import ProductBuilder
from src.product.domain.ports.product_repository import ProductRepository


def update_product(product_repository: ProductRepository, product_id: str, name: str, description: str, price: float):
    find_product_by_id(product_repository=product_repository, product_id=product_id)
    product = ProductBuilder()\
        .with_id(product_id)\
        .with_name(name)\
        .with_description(description)\
        .with_price(price)\
        .build()

    product.validate()
    return product_repository.update_product(product)
