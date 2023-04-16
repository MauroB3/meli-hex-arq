from src.product.domain.model.product import Product


def map_product_to_dict(product: Product):
    return product.__dict__