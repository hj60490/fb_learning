from dataclasses import dataclass
import typing


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

