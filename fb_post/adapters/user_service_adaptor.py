from typing import List

from fb_post_auth.interactors.storage_interfaces.dtos import UserDto


class UserServiceAdaptor:
    @property
    def interface(self):
        from fb_post_auth.app_interfaces.service_interface import \
            ServiceInterface
        return ServiceInterface()

    def check_user_exists_or_not(self, user_id: int) -> bool:
        return self.interface.check_is_user_exists(user_id)

    def get_users_dtos(self, list_of_users_id: List[int]) -> List[UserDto]:
        return self.interface.get_users_details(list_of_users_id)



