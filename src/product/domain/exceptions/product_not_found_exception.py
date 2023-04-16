class ProductNotFoundException(Exception):
    def __init__(self):
        self.message = "Product not found."
