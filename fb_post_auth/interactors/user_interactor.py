from typing import List

from fb_post_auth.interactors.storage_interfaces.dtos import UserDto
from fb_post_auth.interactors.storage_interfaces.user_interface import UserStorageInterface


class UserInteractor:
    def __init__(self, user_storage: UserStorageInterface):
        self.user_storage = user_storage

    def check_user_exists_or_not(self, user_id: int) -> bool:
        return self.user_storage.check_is_user_exists(user_id)

    def get_users_details_dtos(self, user_ids: List[int]) -> \
            List[UserDto]:
        return self.user_storage.get_users_details(user_ids)

