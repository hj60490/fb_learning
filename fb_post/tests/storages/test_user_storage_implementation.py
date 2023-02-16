import pytest

from fb_post.interactors.storage_interfaces.dtos import UsersDTO, UsersCountDTO
from fb_post.storages.user_storage_implementation import \
    UserStorageImplementation
from fb_post.tests.factories.models import UserFactory
from fb_post.tests.factories.storage_dtos import UserDTOFactory, \
    UsersDTOFactory, UsersCountDTOFactory


class TestsUserStorage:

    @pytest.fixture()
    def list_of_user_dtos(self):
        user_dtos = [
            UserDTOFactory(),
            UserDTOFactory(),
            UserDTOFactory()
        ]
        return user_dtos

    @pytest.fixture()
    def users_dto(self, list_of_user_dtos):
        users_dto = UsersDTO(user_dtos=list_of_user_dtos,
                             users_count_dto=UsersCountDTO(users_count=3)
                             )
        return users_dto

    @pytest.mark.django_db
    def test_get_all_users_with_users_return_users_dto(self, users_dto):
        # Arrange
        offset = 0
        limit = 10
        UserFactory.create_batch(size=3)
        user_storage = UserStorageImplementation()
        expected_output = users_dto

        # Act
        actual_output = user_storage.get_all_users(offset=offset, limit=limit)

        # Assert
        assert expected_output == actual_output

    @pytest.mark.django_db
    def test_get_all_users_without_users_return_users_dto_empty(self):
        # Arrange
        offset = 0
        limit = 10
        user_storage = UserStorageImplementation()
        users_count_dto = UsersCountDTOFactory(users_count=0)
        expected_output = UsersDTOFactory(user_dtos=[],
                                          users_count_dto=users_count_dto
                                          )

        # Act
        actual_output = user_storage.get_all_users(offset=offset, limit=limit)

        # Assert
        assert expected_output == actual_output
