from src.product.application.use_cases.find_product import find_product_by_id
from src.product.domain.builder.product_builder import ProductBuilder
from src.product.domain.ports.product_repository import ProductRepository


def reduce_product_stock(product_repository: ProductRepository, product_id: str, amount: int):
    # verificar que exista el producto
    product_db = find_product_by_id(product_repository, product_id)
    product = ProductBuilder()\
        .with_id(product_db['_id'])\
        .with_name(product_db['name'])\
        .with_price(product_db['price'])\
        .with_description(product_db['description'])\
        .with_seller_email(product_db['seller_email'])\
        .with_stock(product_db['stock'])\
        .build()

    # Validar que el stock se pueda reducir
    product.reduce_stock(amount)

    return product_repository.update_product(product)
