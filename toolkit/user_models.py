from dataclasses import dataclass
from enum import Enum


class UserStatus(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"


@dataclass
class User:
    id: int
    name: str
    email: str
    age: int
    status: UserStatus = UserStatus.ACTIVE
