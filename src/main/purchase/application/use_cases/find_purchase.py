from src.main.purchase.domain.ports.purchase_adapter import PurchaseRepository


def find_purchases_of_user(purchase_repository: PurchaseRepository, user_email: str):
    return purchase_repository.find_purchases_of_user(user_email)


def find_sales_of_product(purchase_repository: PurchaseRepository, product_id: str):
    return purchase_repository.find_sales_of_product(product_id)
