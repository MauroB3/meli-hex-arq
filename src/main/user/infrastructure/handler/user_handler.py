from starlette.responses import JSONResponse

from src.main.user.domain.exceptions.user_already_exists_exception import UserAlreadyExistsException
from src.main.user.domain.exceptions.user_not_found_exception import UserNotFoundException
from fastapi import FastAPI, Request


def add_user_exception_handler(app: FastAPI):

    @app.exception_handler(UserNotFoundException)
    async def user_not_found_exception_handler(request: Request, exc: UserNotFoundException):
        return JSONResponse(
            status_code=404,
            content={"message": exc.message},
        )

    @app.exception_handler(UserAlreadyExistsException)
    async def user_not_found_exception_handler(request: Request, exc: UserAlreadyExistsException):
        return JSONResponse(
            status_code=400,
            content={"message": exc.message},
        )
