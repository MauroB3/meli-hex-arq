from pydantic import BaseModel


class UserDTO(BaseModel):
    name: str
    last_name: str
    email: str
