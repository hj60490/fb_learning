import pytest

from unittest import mock
from fb_post.tests.factories import storage_dtos
from fb_post.tests.factories import presenter_dtos


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
        from fb_post.interactors.presenter_interfaces.\
            get_user_posts_presenter_interface import \
            GetPostsPresenterInterface
        return mock.create_autospec(GetPostsPresenterInterface)

    @pytest.fixture
    def interactor(self, post_storage_mock, user_storage_mock, presenter_mock):
        from fb_post.interactors.get_user_posts_interactor import \
            GetUserPostsInteractor
        return GetUserPostsInteractor(
            post_storages=post_storage_mock,
            user_storage=user_storage_mock,
            presenter=presenter_mock)

    def test_user_has_posts_will_give_posts_details(
            self, interactor, user_storage_mock,
            post_storage_mock, presenter_mock):
        # Arrange
        user_id = 1
        requests_parameters_dto = storage_dtos.RequestsParametersDTOFactory(
            offset=1,
            limit=10,
            sort_order="ASC")

        post_dtos = [
            storage_dtos.PostDTOFactory(
                post_id=1,
                posted_by_id=user_id),
            storage_dtos.PostDTOFactory(
                post_id=2,
                posted_by_id=user_id),
        ]
        post_reactions_dtos = [
            storage_dtos.ReactOnPostDTOFactory(
                post_id=post_dtos[0].post_id),
            storage_dtos.ReactOnPostDTOFactory(
                post_id=post_dtos[0].post_id),
            storage_dtos.ReactOnPostDTOFactory(
                post_id=post_dtos[1].post_id),
        ]
        post_comments = [
            storage_dtos.CommentOnPostDTOFactory(
                post_id=post_dtos[0].post_id,
                comment_id=1),
            storage_dtos.CommentOnPostDTOFactory(
                post_id=post_dtos[0].post_id,
                comment_id=2)
        ]
        posts_details_dto = []

        user_storage_mock.check_is_user_exists.return_value = True
        post_storage_mock.get_posts.return_value = post_dtos
        post_storage_mock.get_all_reactions.return_value = post_reactions_dtos

        # Act

        # Assert
        user_storage_mock.check_is_user_exists.assert_called_once_with(
            user_id=user_id)
        post_storage_mock.get_posts.assert_called_once_with(
            user_id=user_id)
        post_storage_mock.get_all_reactions.assert_called_once_with(
            post_ids=[post_dtos[0].post_id, post_dtos[1].post_id])
        presenter_mock.get_all_posts_of_user.assert_called_once_with(
            posts_details_dto=posts_details_dto)
