import pytest

from fb_post_auth.storages.user_storage_implementation import \
    UserStorageImplementation
from fb_post_auth.tests.factories.models import UserFactory
from fb_post_auth.tests.factories.storage_dtos import UserDTOFactory


class TestsUserStorage:

    @pytest.mark.django_db
    def test_get_user_details_with_users_id_return_users_details_dto(
            self):
        # Arrange
        user_ids = [1, 2]
        UserFactory()
        UserFactory()
        users_list = [UserDTOFactory(), UserDTOFactory()]
        expected_user_details_dto = users_list
        storage = UserStorageImplementation()

        # Act
        actual_user_details_dto = storage.get_users_details(
            user_union_list=user_ids)

        # Assert
        assert expected_user_details_dto == actual_user_details_dto

    @pytest.mark.django_db
    def test_user_exists_return_true(self):
        user_id = 1
        expected_output = True
        UserFactory.create_batch(size=3)
        user_storage = UserStorageImplementation()

        actual_output = user_storage.check_is_user_exists(user_id=user_id)

        assert expected_output == actual_output

    @pytest.mark.django_db
    def test_user_not_exists_return_false(self):
        user_id = 1
        expected_output = False

        user_storage = UserStorageImplementation()

        actual_output = user_storage.check_is_user_exists(user_id=user_id)

        assert expected_output == actual_output

    @pytest.mark.django_db
    def test_get_user_details_when_users_not_exists_return_empty(self):
        # Arrange
        user_ids = [8]
        expected_user_details_dto = []
        storage = UserStorageImplementation()

        # Act
        actual_user_details_dto = storage.get_users_details(
            user_union_list=user_ids)

        # Assert
        assert expected_user_details_dto == actual_user_details_dto
