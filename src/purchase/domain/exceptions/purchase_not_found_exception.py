class PurchaseNotFoundException(Exception):
    def __init__(self):
        self.message = "Purchase not found."
