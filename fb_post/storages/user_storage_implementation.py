from fb_post.interactors.storage_interfaces.user_interface import UserInterface
from fb_post.models.models import User
from typing import List
from fb_post.interactors.storage_interfaces.dtos import UserDto


class UserStorageImplementation(UserInterface):

    def check_is_user_exists(self, user_id: int) -> bool:
        return User.objects.filter(id=user_id).exists()

    def get_users_details(self, user_union_list: List[int]) -> List[UserDto]:
        users = User.objects.filter(id__in=user_union_list)
        users = [
            self._convert_user_object_to_dto(user)
            for user in users
        ]
        return users

    @staticmethod
    def _convert_user_object_to_dto(user):
        user = UserDto(
            user_id=user.id,
            name=user.name,
            profile_pic=user.profile_pic
        )
        return user
