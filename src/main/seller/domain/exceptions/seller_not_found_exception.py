class SellerNotFoundException(Exception):
    def __init__(self):
        self.message = "Seller not found."
