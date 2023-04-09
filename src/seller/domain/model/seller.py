from dataclasses import dataclass

from src.address.domain.address import Address


@dataclass
class Seller:
    email: str
    name: str
    address: Address
