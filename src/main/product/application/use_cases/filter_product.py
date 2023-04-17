from src.main.product.domain.ports.product_repository import ProductRepository


def filter_price_between(product_repository: ProductRepository, start_price: float, end_price: float):
    return product_repository.filter_price_between(start_price, end_price)


def filter_price_greater_than(product_repository: ProductRepository, price: float):
    return product_repository.filter_price_greater_than(price)


def filter_price_smaller_than(product_repository: ProductRepository, price: float):
    return product_repository.filter_price_smaller_than(price)
