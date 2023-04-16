from starlette.responses import JSONResponse
from fastapi import FastAPI, Request
from src.purchase.domain.exceptions.purchase_not_found_exception import PurchaseNotFoundException


def add_purchase_exception_handler(app: FastAPI):

    @app.exception_handler(PurchaseNotFoundException)
    async def purchase_not_found_exception_handler(request: Request, exc: PurchaseNotFoundException):
        return JSONResponse(
            status_code=404,
            content={"message": exc.message},
        )

