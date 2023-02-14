from typing import List

from fb_post_auth.interactors.storage_interfaces.dtos import UserDto
from fb_post_auth.interactors.user_interactor import UserInteractor


class ServiceInterface:

    @staticmethod
    def check_is_user_exists(user_id: int) -> bool:
        from fb_post_auth.storages.user_storage_implementation import \
            UserStorageImplementation

        user_storage = UserStorageImplementation()
        interactor = UserInteractor(user_storage=user_storage)

        return interactor.check_user_exists_or_not(user_id=user_id)

    @staticmethod
    def get_users_details(user_union_list: List[int]) -> List[UserDto]:
        from fb_post_auth.storages.user_storage_implementation import \
            UserStorageImplementation

        user_storage = UserStorageImplementation()
        interactor = UserInteractor(user_storage=user_storage)

        users_dto = interactor.get_users_details_dto(user_union_list)

        return users_dto
