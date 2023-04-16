from pydantic import BaseModel


class UserIdDTO(BaseModel):
    id: str
