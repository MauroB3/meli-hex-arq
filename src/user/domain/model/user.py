from dataclasses import dataclass
from uuid import uuid1


@dataclass
class User:
    name: str
    last_name: str
    email: str
    _id: str = uuid1().__str__()
