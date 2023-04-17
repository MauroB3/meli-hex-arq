class UserAlreadyExistsException(Exception):
    def __init__(self):
        self.message = "There is already a user with that email."
