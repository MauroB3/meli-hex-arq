from pydantic import BaseModel


class ProductCategoryDTO(BaseModel):
    category: str
