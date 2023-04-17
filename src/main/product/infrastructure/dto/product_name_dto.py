from pydantic import BaseModel


class ProductNameDTO(BaseModel):
    name: str
