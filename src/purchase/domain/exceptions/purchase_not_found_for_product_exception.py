class PurchaseNotFoundForProductException(Exception):
    def __init__(self):
        self.message = "There is no purchases for that product."
