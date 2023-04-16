from src.product.domain.builder.product_builder import ProductBuilder
from src.product.domain.ports.product_repository import ProductRepository
from src.purchase.domain.builder.purchase_builder import PurchaseBuilder
from src.purchase.domain.ports.purchase_adapter import PurchaseRepository
from src.user.domain.ports.user_repository import UserRepository


def create_purchase(purchase_repository: PurchaseRepository, user_repository: UserRepository,
                    product_repository: ProductRepository, product_id: str, buyer_email: str, amount: int, date: str):

    # verificar que exista el comprador
    user_db = user_repository.find_user_by_email(buyer_email)

    # verificar que exista el producto
    product_db = product_repository.find_product_by_id(product_id)
    product = ProductBuilder()\
        .with_id(product_db['_id'])\
        .with_name(product_db['name'])\
        .with_price(product_db['price'])\
        .with_description(product_db['description'])\
        .with_seller_email(product_db['seller_email'])\
        .with_stock(product_db['stock'])\
        .build()

    # validar que el producto se pueda comprar
    product.reduce_stock(amount)
    product_repository.update_product(product)

    # crear y guardar orden de compra
    purchase = PurchaseBuilder() \
        .with_buyer_email(buyer_email) \
        .with_product_id(product_id) \
        .with_date(date) \
        .with_amount(amount)
    return purchase_repository.create_purchase(purchase)
