class ProductWithDuplicatedEmailException(Exception):
    def __init__(self):
        self.message = "A product with that name already exists for that seller."
