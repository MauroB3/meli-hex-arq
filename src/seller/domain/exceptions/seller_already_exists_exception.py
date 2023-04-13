class SellerAlreadyExistsException(Exception):
    def __init__(self):
        self.message = "There is already a seller with that email."
