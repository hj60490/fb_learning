from dataclasses import dataclass
from typing import List
from datetime import datetime


@dataclass
class Post:
    content: str
    posted_by: int
    posted_at: datetime


@dataclass
class UserDTO:
    name: str
    profile_pic: str
    user_id: int


@dataclass
class UsersCountDTO:
    users_count: int


@dataclass
class UsersDTO:
    user_dtos: List[UserDTO]
    users_count_dto: UsersCountDTO

