from unittest import mock

import pytest
from django_swagger_utils.drf_server.exceptions import BadRequest

from fb_post.interactors.storage_interfaces.dtos import UsersDTO, UsersCountDTO, \
    UserDTO
from fb_post.tests.factories.storage_dtos import UserDTOFactory


class TestsGetAllUsersInteractor:

    @pytest.fixture
    def user_storage_mock(self):
        from fb_post.interactors.storage_interfaces.user_interface import \
            UserInterface
        return mock.create_autospec(UserInterface)

    @pytest.fixture
    def presenter_mock(self):
        from fb_post.interactors.presenter_interfaces.get_users_presenter_interface import \
            GetUsersPresenterInterface

        return mock.create_autospec(GetUsersPresenterInterface)

    @pytest.fixture
    def interactor(self, user_storage_mock, presenter_mock):
        from fb_post.interactors.get_users_interactor import GetUsersInteractor

        return GetUsersInteractor(
            user_storage=user_storage_mock,
            presenter=presenter_mock
        )

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

    def test_get_all_users_interactor_with_invalid_offset_raise_exception(
            self, presenter_mock, interactor
    ):
        # Arrange
        offset = -1
        limit = 10

        presenter_mock.raise_exception_for_invalid_offset_length.side_effect = \
            BadRequest

        # Act
        with pytest.raises(BadRequest):
            interactor.get_all_users_wrapper(limit=limit, offset=offset)

        # Assert
        presenter_mock.raise_exception_for_invalid_offset_length.assert_called_once()

    def test_get_all_users_interactor_with_invalid_limit_raise_exception(
            self, presenter_mock, user_storage_mock, interactor
    ):
        # Arrange
        offset = 0
        limit = -1

        presenter_mock.raise_exception_for_invalid_limit_length.side_effect = \
            BadRequest

        # Act
        with pytest.raises(BadRequest):
            interactor.get_all_users_wrapper(offset=offset, limit=limit)

        # Assert
        presenter_mock.raise_exception_for_invalid_limit_length.assert_called_once()

    def test_get_all_users_interactor_with_users_return_users_details(
            self, presenter_mock, user_storage_mock, interactor, users_dto):
        # Arrange
        offset = 0
        limit = 10

        user_storage_mock.get_all_users.return_value = users_dto

        # Act
        interactor.get_all_users_wrapper(offset=offset, limit=limit)

        # Assert

        user_storage_mock.get_all_users.assert_called_once()
        presenter_mock.get_response_for_get_all_users.assert_called_once_with(
            users_dto=users_dto
        )
