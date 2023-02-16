from abc import ABC

from fb_post.interactors.storage_interfaces.dtos import UsersDTO


class UserInterface(ABC):

    def check_is_user_exists(self, user_id: int) -> bool:
        pass

    def get_all_users(self, limit: int, offset: int) -> UsersDTO:
        pass

