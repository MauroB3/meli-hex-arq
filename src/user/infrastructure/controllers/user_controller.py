from fastapi import APIRouter
from fastapi.responses import JSONResponse
from src.user.domain.ports.user_repository import UserRepository
from src.user.infrastructure.dto.user_dto import UserDTO
from src.user.infrastructure.dto.user_email_dto import UserEmailDTO
from src.user.application.use_cases.create_user import create_user as create_user_uc
from src.user.application.use_cases.delete_user_by_email import delete_user_by_email as delete_user_by_email_uc
from src.user.application.use_cases.update_user import update_user as update_user_uc
from src.user.application.use_cases.find_user import find_user_by_email as find_user_by_email_uc
from src.user.application.use_cases.find_user import find_user_by_id as find_user_by_id_uc
from src.user.infrastructure.dto.user_id_dto import UserIdDTO


class UserController:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
        self.router = APIRouter()
        self.init_routes()

    def init_routes(self):
        self.router.add_api_route("/user/create", self.create_user, methods=['POST'])
        self.router.add_api_route("/user/delete", self.delete_user_by_email, methods=['POST'])
        self.router.add_api_route("/user/update", self.update_user, methods=['POST'])
        self.router.add_api_route("/user/find_by_email", self.find_user_by_email, methods=['POST'])
        self.router.add_api_route("/user/find_by_id", self.find_user_by_id, methods=['POST'])

    def create_user(self, user: UserDTO):
        create_user_uc(user_repository=self.user_repository, name=user.name, last_name=user.last_name, email=user.email)
        return JSONResponse(status_code=201, content={"message": "User created."})

    def delete_user_by_email(self, user: UserEmailDTO):
        delete_user_by_email_uc(user_repository=self.user_repository, email=user.email)
        return JSONResponse(status_code=200, content={"message": "User deleted."})

    def update_user(self, user: UserDTO):
        update_user_uc(user_repository=self.user_repository, name=user.name, last_name=user.last_name, email=user.email)
        return JSONResponse(status_code=200, content={"message": "User updated."})

    def find_user_by_email(self, user: UserEmailDTO):
        user_res = find_user_by_email_uc(user_repository=self.user_repository, email=user.email)
        return JSONResponse(status_code=200, content={"message": "User found.", "user": user_res})

    def find_user_by_id(self, user: UserIdDTO):
        user_res = find_user_by_id_uc(user_repository=self.user_repository, _id=user.id)
        return JSONResponse(status_code=200, content={"message": "User found.", "user": user_res})
