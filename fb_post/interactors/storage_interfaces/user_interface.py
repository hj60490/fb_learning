from abc import ABC
from typing import List
from fb_post.interactors.storage_interfaces.dtos import UserDto


class UserInterface(ABC):

    def check_is_user_exists(self, user_id: int) -> bool:
        pass

    def get_users_details(self, user_union_list: List[int]) -> List[UserDto]:
        pass




