from src.main.product.domain.ports.product_repository import ProductRepository


def delete_product(product_repository: ProductRepository, seller_email: str, product_name: str):
    return product_repository.delete_product_by_name_and_seller(seller_email=seller_email, product_name=product_name)
