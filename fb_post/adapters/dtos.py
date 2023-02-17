from dataclasses import dataclass
import typing


@dataclass
class UserDto:
    user_id: int
    name: str
    profile_pic: typing.Optional[str]
