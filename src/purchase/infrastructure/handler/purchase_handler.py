from starlette.responses import JSONResponse
from fastapi import FastAPI, Request

from src.purchase.domain.exceptions.purchase_invalid_amount_exception import PurchaseInvalidAmountException
from src.purchase.domain.exceptions.purchase_not_found_exception import PurchaseNotFoundException
from src.purchase.domain.exceptions.purchase_not_found_for_product_exception import PurchaseNotFoundForProductException
from src.purchase.domain.exceptions.purchase_not_found_for_user_exception import PurchaseNotFoundForUserException


def add_purchase_exception_handler(app: FastAPI):

    @app.exception_handler(PurchaseNotFoundException)
    async def purchase_not_found_exception_handler(request: Request, exc: PurchaseNotFoundException):
        return JSONResponse(
            status_code=404,
            content={"message": exc.message},
        )

    @app.exception_handler(PurchaseInvalidAmountException)
    async def purchase_invalid_amount_exception_handler(request: Request, exc: PurchaseInvalidAmountException):
        return JSONResponse(
            status_code=400,
            content={"message": exc.message},
        )

    @app.exception_handler(PurchaseNotFoundForProductException)
    async def purchase_not_found_for_product_exception_handler(request: Request, exc: PurchaseNotFoundForProductException):
        return JSONResponse(
            status_code=404,
            content={"message": exc.message},
        )

    @app.exception_handler(PurchaseNotFoundForUserException)
    async def purchase_not_found_for_user_exception_handler(request: Request, exc: PurchaseNotFoundForUserException):
        return JSONResponse(
            status_code=404,
            content={"message": exc.message},
        )

