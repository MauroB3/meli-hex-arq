from bson.json_util import dumps
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from src.user.application.services.user_service import UserService
from src.user.infrastructure.dto.user_dto import UserDTO
from src.user.infrastructure.dto.user_email_dto import UserEmailDTO


class UserController:
    def __init__(self, user_service: UserService):
        self.user_service = user_service
        self.router = APIRouter()
        self.init_routes()

    def init_routes(self):
        self.router.add_api_route("/user/create", self.create_user, methods=['POST'])
        self.router.add_api_route("/user/delete", self.delete_user_by_email, methods=['POST'])
        self.router.add_api_route("/user/update", self.update_user, methods=['POST'])
        self.router.add_api_route("/user/find", self.find_user, methods=['POST'])

    def create_user(self, user: UserDTO):
        self.user_service.create_user(name=user.name, last_name=user.last_name, email=user.email)
        return JSONResponse(status_code=201, content={"message": "User created."})

    def delete_user_by_email(self, user: UserEmailDTO):
        self.user_service.delete_user_by_email(user.email)
        return JSONResponse(status_code=200, content={"message": "User deleted."})

    def update_user(self, user: UserDTO):
        self.user_service.update_user(name=user.name, last_name=user.last_name, email=user.email)
        return JSONResponse(status_code=200, content={"message": "User updated."})

    def find_user(self, user: UserEmailDTO):
        user = self.user_service.find_user(user.email)
        return JSONResponse(status_code=200, content={"message": "User found.", "user": dumps(user)})
