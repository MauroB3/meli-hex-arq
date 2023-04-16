class ProductInvalidPriceException(Exception):
    def __init__(self):
        self.message = "Price must be greater than 0."
