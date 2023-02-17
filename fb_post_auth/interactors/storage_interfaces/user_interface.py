import abc
from abc import ABC
from typing import List
from fb_post_auth.interactors.storage_interfaces.dtos import UserDto
from fb_post_auth.interactors.storage_interfaces.dtos import UsersDTO


class UserStorageInterface(ABC):

    @abc.abstractmethod
    def check_is_user_exists(self, user_id: int) -> bool:
        pass

    @abc.abstractmethod
    def get_users_details(self, user_ids: List[int]) -> List[UserDto]:
        pass

    @abc.abstractmethod
    def get_all_users(self, limit: int, offset: int) -> UsersDTO:
        pass




