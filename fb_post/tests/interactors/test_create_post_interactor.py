import pytest
from fb_post.interactors.presenter_interfaces.presenter_interface import \
    CreatePostPresenterInterface
from fb_post.interactors.create_post_interactor import CreatePostInteractor
from django_swagger_utils.drf_server.exceptions import BadRequest
from unittest import mock


class TestGetUserPostsInteractor:

    @pytest.fixture
    def user_storage_mock(self):
        from fb_post.interactors.storage_interfaces.user_interface import \
            UserInterface
        return mock.create_autospec(UserInterface)

    @pytest.fixture
    def post_storage_mock(self):
        from fb_post.interactors.storage_interfaces.post_interface import \
            PostInterface
        return mock.create_autospec(PostInterface)

    @pytest.fixture
    def presenter_mock(self):
        return mock.create_autospec(CreatePostPresenterInterface)

    @pytest.fixture
    def interactor(self, post_storage_mock, user_storage_mock, presenter_mock):
        return CreatePostInteractor(
            post_storage=post_storage_mock,
            user_storage=user_storage_mock,
            presenter=presenter_mock)

    def test_create_post_interactor_when_user_not_found_raise_exception(
            self, user_storage_mock, interactor, presenter_mock):
        content = "hello"
        user_id = 1

        user_storage_mock.check_is_user_exists.return_value = False
        presenter_mock.raise_exception_for_user_not_exist.side_effect = BadRequest

        with pytest.raises(BadRequest):
            interactor.create_post_wrapper(
                content, user_id
            )

        user_storage_mock.check_is_user_exists.assert_called_once_with(
            user_id=user_id)
        presenter_mock.raise_exception_for_user_not_exist.assert_called_once()

    def test_create_post_interactor_with_valid_details_creates_post(
            self,  interactor, presenter_mock, user_storage_mock,
            post_storage_mock
    ):
        user_id = 1
        content = "hello"

        user_storage_mock.check_is_user_exists.return_value = True

        interactor.create_post_wrapper(user_id=user_id,
                                       content=content)

        user_storage_mock.check_is_user_exists.assert_called_once_with(user_id)
        post_storage_mock.create_post.assert_called_once_with(
            user_id=user_id,
            content=content
        )
