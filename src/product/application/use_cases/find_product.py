from src.product.domain.ports.product_repository import ProductRepository


def find_product_by_id(product_repository: ProductRepository, product_id: str):
    return product_repository.find_product_by_id(product_id)


def find_product_by_name(product_repository: ProductRepository, name: str):
    return product_repository.find_product_by_name(name)


def find_product_by_seller(product_repository: ProductRepository, seller_email: str):
    return product_repository.find_product_by_seller(seller_email)
