from abc import ABC

from fb_post_auth.interactors.storage_interfaces.dtos import UsersDTO


class GetUsersPresenterInterface(ABC):

    def raise_exception_for_invalid_offset_length(self):
        pass

    def raise_exception_for_invalid_limit_length(self):
        pass

    def get_response_for_get_all_users(self, users_dto: UsersDTO):
        pass

