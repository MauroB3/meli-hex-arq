from src.main.purchase.domain.model.purchase import Purchase


def map_purchase_to_dict(purchase: Purchase):
    return purchase.__dict__
