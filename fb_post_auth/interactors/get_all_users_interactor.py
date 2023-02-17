from typing import List

from fb_post_auth.exceptions.custom_exceptions import InvalidOffsetException, \
    InvalidLimitException
from fb_post_auth.interactors.presenter_interfaces.get_users_presenter_interface import \
    GetUsersPresenterInterface
from fb_post_auth.interactors.storage_interfaces.dtos import UsersDTO
from fb_post_auth.interactors.storage_interfaces.user_interface import UserStorageInterface


class GetUsersInteractor:
    def __init__(
            self, user_storage: UserStorageInterface,
            presenter: GetUsersPresenterInterface
    ):
        self.user_storage = user_storage
        self.presenter = presenter

    def get_all_users_wrapper(self, limit: int, offset: int):
        try:
            users_dto = self.get_all_users(
                limit=limit,
                offset=offset
            )
            return self.presenter.get_response_for_get_all_users(
                users_dto=users_dto
            )
        except InvalidOffsetException:
            self.presenter.raise_exception_for_invalid_offset_length()
        except InvalidLimitException:
            self.presenter.raise_exception_for_invalid_limit_length()

    def get_all_users(self, limit: int, offset: int) -> UsersDTO:

        if offset < 0:
            raise InvalidOffsetException

        if limit < 0:
            raise InvalidLimitException

        users_dto = self.user_storage.get_all_users(
            limit=limit,
            offset=offset
        )

        return users_dto
