class PurchaseInvalidAmountException(Exception):
    def __init__(self):
        self.message = "Purchase amount must be greater than 0."
