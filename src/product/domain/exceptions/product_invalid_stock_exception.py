class ProductInvalidStockException(Exception):
    def __init__(self):
        self.message = "Stock cant be less than 0."
