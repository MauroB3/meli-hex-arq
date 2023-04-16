from dataclasses import dataclass
from uuid import uuid1


@dataclass
class Seller:
    email: str
    name: str
    _id: str
