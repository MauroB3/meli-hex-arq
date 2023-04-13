from fastapi import FastAPI
import uvicorn

from src.seller.application.services.seller_service import SellerService
from src.seller.infrastructure.adapters.mongodb_seller_repository import MongoDBSellerRepository
from src.seller.infrastructure.controllers.seller_controller import SellerController
from src.user.application.services.user_service import UserService
from src.user.infrastructure.adapters.mongodb_user_repository import MongoDBUserRepository
from src.user.infrastructure.controllers.user_controller import UserController
from src.user.infrastructure.handler.user_handler import add_user_exception_handler
from src.seller.infrastructure.handler.seller_handler import add_seller_exception_handler

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hola"}


def setup_handlers():
    add_user_exception_handler(app)
    add_seller_exception_handler(app)


def setup_user_routes():
    user_repository = MongoDBUserRepository()
    user_service = UserService(user_repository)
    user_controller = UserController(user_service)
    app.include_router(user_controller.router)


def setup_seller_routes():
    seller_repository = MongoDBSellerRepository()
    seller_service = SellerService(seller_repository)
    seller_controller = SellerController(seller_service)
    app.include_router(seller_controller.router)


if __name__ == "__main__":
    setup_user_routes()
    setup_seller_routes()
    setup_handlers()
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
