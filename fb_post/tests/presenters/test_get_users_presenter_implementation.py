import pytest
from django_swagger_utils.drf_server.exceptions import BadRequest

from fb_post.constants.exception_messages import INVALID_LIMIT_LENGTH, \
    INVALID_OFFSET_LENGTH
from fb_post.presenters.get_all_users_presenter_implementation import \
    GetUsersPresenterImplementation
from fb_post.tests.factories.storage_dtos import UserDTOFactory, \
    UsersDTOFactory, UsersCountDTOFactory


class TestsGetUsersPresenterImplementation:

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
        users_dto = UsersDTOFactory(
            user_dtos=list_of_user_dtos,
            users_count_dto=UsersCountDTOFactory(users_count=3)
        )
        return users_dto

    def test_get_response_for_get_users_return_users_details_dict(
            self, users_dto, snapshot):
        # Arrange

        presenter = GetUsersPresenterImplementation()

        # Act
        actual_output = presenter.get_response_for_get_all_users(
            users_dto=users_dto
        )

        # Assert
        snapshot.assert_match(actual_output)

    def test_raise_exception_for_invalid_limit_value(self):
        exception_messages = INVALID_LIMIT_LENGTH[0]
        exception_res_status = INVALID_LIMIT_LENGTH[1]
        presenter = GetUsersPresenterImplementation()

        with pytest.raises(BadRequest) as exception:
            presenter.raise_exception_for_invalid_limit_length()

        assert exception.value.message == exception_messages
        assert exception.value.res_status == exception_res_status

    def test_raise_exception_for_invalid_offset_value(self):
        exception_messages = INVALID_OFFSET_LENGTH[0]
        exception_res_status = INVALID_OFFSET_LENGTH[1]
        presenter = GetUsersPresenterImplementation()

        with pytest.raises(BadRequest) as exception:
            presenter.raise_exception_for_invalid_offset_length()

        assert exception.value.message == exception_messages
        assert exception.value.res_status == exception_res_status

