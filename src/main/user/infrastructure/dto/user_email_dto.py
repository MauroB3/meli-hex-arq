from pydantic import BaseModel


class UserEmailDTO(BaseModel):
    email: str
