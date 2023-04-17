from pydantic import BaseModel


class ProductIdDTO(BaseModel):
    id: str
