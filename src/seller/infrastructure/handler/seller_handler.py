from starlette.responses import JSONResponse

from src.seller.domain.exceptions.seller_already_exists_exception import SellerAlreadyExistsException
from src.seller.domain.exceptions.seller_not_found_exception import SellerNotFoundException
from fastapi import FastAPI, Request


def add_seller_exception_handler(app: FastAPI):

    @app.exception_handler(SellerNotFoundException)
    async def user_not_found_exception_handler(request: Request, exc: SellerNotFoundException):
        return JSONResponse(
            status_code=404,
            content={"message": exc.message},
        )

    @app.exception_handler(SellerAlreadyExistsException)
    async def user_not_found_exception_handler(request: Request, exc: SellerAlreadyExistsException):
        return JSONResponse(
            status_code=400,
            content={"message": exc.message},
        )
