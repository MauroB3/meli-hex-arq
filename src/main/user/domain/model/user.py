from dataclasses import dataclass


@dataclass
class User:
    name: str
    last_name: str
    email: str
    _id: str
