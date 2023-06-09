from fastapi import FastAPI
import uvicorn
from src.main.product.infrastructure.adapters.mongodb_product_repository import MongoDBProductRepository
from src.main.product.infrastructure.controllers.product_controller import ProductController
from src.main.product.infrastructure.handler.product_handler import add_product_exception_handler
from src.main.purchase.infrastructure.adapters.purchase_adapter import MongoDBPurchaseRepository
from src.main.purchase.infrastructure.controllers.purchase_controller import PurchaseController
from src.main.purchase.infrastructure.handler.purchase_handler import add_purchase_exception_handler
from src.main.seller.infrastructure.adapters.mongodb_seller_repository import MongoDBSellerRepository
from src.main.seller.infrastructure.controllers.seller_controller import SellerController
from src.main.user.infrastructure.adapters.mongodb_user_repository import MongoDBUserRepository
from src.main.user.infrastructure.controllers.user_controller import UserController
from src.main.user.infrastructure.handler.user_handler import add_user_exception_handler
from src.main.seller.infrastructure.handler.seller_handler import add_seller_exception_handler

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Meli - Arquitectura de Software"}


def setup():
    # Repositories
    user_repository = MongoDBUserRepository()
    seller_repository = MongoDBSellerRepository()
    product_repository = MongoDBProductRepository()
    purchase_repository = MongoDBPurchaseRepository()

    # Controllers
    user_controller = UserController(user_repository)
    seller_controller = SellerController(seller_repository)
    product_controller = ProductController(product_repository, seller_repository)
    purchase_controller = PurchaseController(purchase_repository, user_repository, product_repository)

    # Routers
    app.include_router(user_controller.router)
    app.include_router(seller_controller.router)
    app.include_router(product_controller.router)
    app.include_router(purchase_controller.router)

    # Handlers
    add_user_exception_handler(app)
    add_seller_exception_handler(app)
    add_product_exception_handler(app)
    add_purchase_exception_handler(app)


if __name__ == "__main__":
    setup()
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
