from starlette.responses import JSONResponse
from src.main.product.domain.exceptions.product_invalid_price_exception import ProductInvalidPriceException
from src.main.product.domain.exceptions.product_invalid_stock_exception import ProductInvalidStockException
from src.main.product.domain.exceptions.product_not_found_exception import ProductNotFoundException
from src.main.product.domain.exceptions.product_with_duplicated_name_exception import ProductWithDuplicatedEmailException
from fastapi import FastAPI, Request


def add_product_exception_handler(app: FastAPI):

    @app.exception_handler(ProductInvalidPriceException)
    async def product_invalid_price_exception_handler(request: Request, exc: ProductInvalidPriceException):
        return JSONResponse(
            status_code=400,
            content={"message": exc.message},
        )

    @app.exception_handler(ProductInvalidStockException)
    async def product_invalid_stock_exception_handler(request: Request, exc: ProductInvalidStockException):
        return JSONResponse(
            status_code=400,
            content={"message": exc.message},
        )

    @app.exception_handler(ProductWithDuplicatedEmailException)
    async def product_duplicated_email_exception_handler(request: Request, exc: ProductWithDuplicatedEmailException):
        return JSONResponse(
            status_code=409,
            content={"message": exc.message},
        )

    @app.exception_handler(ProductNotFoundException)
    async def product_not_found_exception_handler(request: Request, exc: ProductNotFoundException):
        return JSONResponse(
            status_code=404,
            content={"message": exc.message},
        )