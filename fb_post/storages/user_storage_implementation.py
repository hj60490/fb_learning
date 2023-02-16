from typing import List

from fb_post.interactors.storage_interfaces.dtos import UsersDTO, UsersCountDTO, \
    UserDTO
from fb_post.interactors.storage_interfaces.user_interface import UserInterface
from fb_post.models.models import User


class UserStorageImplementation(UserInterface):

    def check_is_user_exists(self, user_id: int) -> bool:
        return User.objects.filter(id=user_id).exists()

    def get_all_users(self, offset: int, limit: int) -> UsersDTO:
        users = User.objects.all()
        total_users = users.count()
        users = list(users)
        users = users[offset: offset + limit]

        users_count_dto = UsersCountDTO(users_count=total_users)
        user_dtos = [
            self._convert_user_obj_to_user_dto(user)
            for user in users
        ]
        users_dto = self._prepare_users_dto_with_all_user_dtos(
            user_dtos=user_dtos,
            users_count_dto=users_count_dto
        )
        return users_dto

    @staticmethod
    def _convert_user_obj_to_user_dto(user) -> UserDTO:
        user_dto = UserDTO(name=user.name,
                           profile_pic=user.profile_pic,
                           user_id=user.id
                           )
        return user_dto

    @staticmethod
    def _prepare_users_dto_with_all_user_dtos(
            user_dtos: List[UserDTO],  users_count_dto: UsersCountDTO
    ) -> UsersDTO:
        users_dto = UsersDTO(
            user_dtos=user_dtos,
            users_count_dto=users_count_dto
        )
        return users_dto
