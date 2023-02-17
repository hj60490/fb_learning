from typing import Dict, Any, List

from django_swagger_utils.drf_server.exceptions import BadRequest

from fb_post.constants.exception_messages import INVALID_OFFSET_LENGTH, \
    INVALID_LIMIT_LENGTH
from fb_post_auth.interactors.presenter_interfaces.get_users_presenter_interface import \
    GetUsersPresenterInterface
from fb_post_auth.interactors.storage_interfaces.dtos import UsersDTO


class GetUsersPresenterImplementation(GetUsersPresenterInterface):

    def raise_exception_for_invalid_offset_length(self):
        raise BadRequest(*INVALID_OFFSET_LENGTH)

    def raise_exception_for_invalid_limit_length(self):
        raise BadRequest(*INVALID_LIMIT_LENGTH)

    def get_response_for_get_all_users(self, users_dto: UsersDTO):
        user_dtos = users_dto.user_dtos
        users_count = users_dto.users_count

        users_dict = [
            self._prepare_user_details_dict(user)
            for user in user_dtos
        ]
        users_details_with_count = \
            self._prepare_users_details_with_count(
                users_details=users_dict, users_count=users_count
            )
        return users_details_with_count

    @staticmethod
    def _prepare_user_details_dict(user) -> Dict[str, str]:
        user_dict = {
            'name': user.name,
            'profile_pic': user.profile_pic,
            'user_id': user.user_id
        }
        return user_dict

    @staticmethod
    def _prepare_users_details_with_count(users_details,
                                          users_count: int) -> Dict[str, Any]:
        users_details = {
            "total_users": users_count,
            "users_details": users_details
        }
        return users_details