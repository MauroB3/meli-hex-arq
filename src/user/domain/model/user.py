from dataclasses import dataclass

from src.address.domain.address import Address


@dataclass
class User:
    name: str
    last_name: str
    email: str
    address: Address
