from dataclasses import dataclass
import typing
from datetime import datetime


@dataclass
class UserAuthTokensDTO:
    user_id: str
    access_token: str
    refresh_token: str
    expires_in: int = None


@dataclass
class TokensDTO:
    access_token: str
    refresh_token: str
    expires_in: int


@dataclass
class UserDto:
    user_id: int
    name: str
    profile_pic: typing.Optional[str]


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
    user_dtos: typing.List[UserDTO]
    users_count: int
