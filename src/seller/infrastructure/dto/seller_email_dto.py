from pydantic import BaseModel


class SellerEmailDTO(BaseModel):
    email: str
