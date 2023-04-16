from src.product.application.use_cases.reduce_product_stock import reduce_product_stock
from src.product.domain.ports.product_repository import ProductRepository
from src.purchase.domain.builder.purchase_builder import PurchaseBuilder
from src.purchase.domain.ports.purchase_adapter import PurchaseRepository
from src.user.application.use_cases.find_user import find_user_by_email
from src.user.domain.ports.user_repository import UserRepository


def create_purchase(purchase_repository: PurchaseRepository, user_repository: UserRepository,
                    product_repository: ProductRepository, product_id: str, buyer_email: str, amount: int, date: str):

    # verificar que exista el comprador
    user_db = find_user_by_email(user_repository, buyer_email)

    # crear y guardar orden de compra
    purchase = PurchaseBuilder() \
        .with_buyer_email(buyer_email) \
        .with_product_id(product_id) \
        .with_date(date) \
        .with_amount(amount)\
        .build()

    purchase.validate()

    # Reducir stock del producto
    reduce_product_stock(product_repository, product_id, amount)

    # Finalmente se guarda la compra
    return purchase_repository.create_purchase(purchase)
