class PurchaseNotFoundForUserException(Exception):
    def __init__(self):
        self.message = "There is no purchases from that user."
