from fb_post_auth.interactors.storage_interfaces.user_interface import \
    UserStorageInterface
from fb_post_auth.models.user import User
from typing import List
from fb_post_auth.interactors.storage_interfaces.dtos import UserDto, UsersDTO, \
    UsersCountDTO, UserDTO


class UserStorageImplementation(UserStorageInterface):

    def check_is_user_exists(self, user_id: int) -> bool:
        return User.objects.filter(id=user_id).exists()

    def get_users_details(self, user_ids: List[int]) -> List[UserDto]:
        users = User.objects.filter(id__in=user_ids)
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
            user_dtos: List[UserDTO], users_count_dto: UsersCountDTO
    ) -> UsersDTO:
        users_dto = UsersDTO(
            user_dtos=user_dtos,
            users_count_dto=users_count_dto
        )
        return users_dto
