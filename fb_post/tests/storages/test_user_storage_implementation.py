import pytest
from fb_post.storages.user_storage_implementation import \
    UserStorageImplementation


@pytest.mark.django_db
def test_user_exists_return_true(users):
    user_id = 1
    expected_output = True
    user_storage = UserStorageImplementation()

    actual_output = user_storage.check_is_user_exists(user_id=user_id)

    assert expected_output == actual_output


@pytest.mark.django_db
def test_user_not_exists_return_false(users):
    user_id = 7
    expected_output = False
    user_storage = UserStorageImplementation()

    actual_output = user_storage.check_is_user_exists(user_id=user_id)

    assert expected_output == actual_output


@pytest.mark.django_db
def test_get_user_details_with_users_id_return_users_details_dto(
        user, user_details_dto):
    # Arrange
    user_ids = [1]
    expected_user_details_dto = user_details_dto
    storage = UserStorageImplementation()

    # Act
    actual_user_details_dto = storage.get_users_details(
        user_union_list=user_ids)

    # Assert
    assert expected_user_details_dto == actual_user_details_dto


@pytest.mark.django_db
def test_get_user_details_with_users_id_not_exists_return_empty(
        user):
    # Arrange
    user_ids = [8]
    expected_user_details_dto = []
    storage = UserStorageImplementation()

    # Act
    actual_user_details_dto = storage.get_users_details(
        user_union_list=user_ids)

    # Assert
    assert expected_user_details_dto == actual_user_details_dto