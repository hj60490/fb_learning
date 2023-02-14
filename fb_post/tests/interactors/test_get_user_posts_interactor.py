
from unittest import mock
from fb_post.tests.factories import storage_dtos
import pytest
from django_swagger_utils.drf_server.exceptions import BadRequest


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
        from fb_post.interactors.presenter_interfaces. \
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
            post_storage_mock, presenter_mock
    ):
        # Arrange
        user_id = 1
        requests_parameters_dto = storage_dtos.RequestsParametersDTOFactory(
            offset=0,
            limit=1,
            sort_order="ASC",
            post_content="Hello"
        )
        users_dtos = [
            storage_dtos.UserDTOFactory(),
            storage_dtos.UserDTOFactory()
        ]
        post_dtos = [
            storage_dtos.PostDTOFactory(
                content="Hello")
        ]
        post_reactions_dtos = [
            storage_dtos.ReactOnPostDTOFactory(
                post_id=1)
        ]
        post_comments = [
            storage_dtos.CommentOnPostDTOFactory(
                post_id=post_dtos[0].post_id,
                comment_id=1)
        ]
        comment_replies = [
            storage_dtos.CommentOnCommentDTOFactory(
                comment_id=2,
                commented_by_id=2,
                parent_comment_id=1
            )
        ]
        reactions_on_comments = [
            storage_dtos.ReactOnCommentDTOFactory(comment_id=1),
            storage_dtos.ReactOnCommentDTOFactory(comment_id=2)
        ]

        posts_details_dto = storage_dtos.PostDetailsDtoFactory(
            users=users_dtos,
            posts=post_dtos,
            reactions_on_posts=post_reactions_dtos,
            comments_on_post=post_comments,
            replies=comment_replies,
            reactions_on_comments=reactions_on_comments

        )

        user_storage_mock.check_is_user_exists.return_value = True
        post_storage_mock.get_posts.return_value = post_dtos
        post_storage_mock.get_all_reactions.return_value = post_reactions_dtos
        post_storage_mock.get_comments.return_value = post_comments
        post_storage_mock.get_replies_on_comment.return_value = comment_replies
        post_storage_mock.get_reactions_on_comments.return_value = reactions_on_comments
        user_storage_mock.get_users_details.return_value = users_dtos

        # Act
        interactor.get_user_posts_wrapper(user_id, requests_parameters_dto)

        # Assert
        user_storage_mock.check_is_user_exists.assert_called_once_with(
            user_id=user_id)
        post_storage_mock.get_posts.assert_called_once_with(
            user_id=user_id, requests_parameters_dto=requests_parameters_dto)
        post_storage_mock.get_all_reactions.assert_called_once_with(
            list_of_post_id=[post_dtos[0].post_id])
        post_storage_mock.get_comments.assert_called_once_with(
            [post_dtos[0].post_id])
        post_storage_mock.get_replies_on_comment.assert_called_once_with(
            [post_comments[0].comment_id])
        post_storage_mock.get_reactions_on_comments.assert_called_once_with(
            [post_comments[0].comment_id, comment_replies[0].comment_id])
        user_storage_mock.get_users_details.assert_called_once_with(
            [users_dtos[0].user_id, users_dtos[1].user_id,])
        presenter_mock.get_all_posts_of_user.assert_called_once_with(
            posts_details_dto=posts_details_dto)

    def test_get_user_posts_interactor_with_invalid_offset_raise_exception(
            self, presenter_mock, interactor):
        user_id = 1

        requests_parameters_dto = storage_dtos.RequestsParametersDTOFactory(
            offset=-1,
            limit=1,
        )

        presenter_mock.raise_exception_for_invalid_offset_length.side_effect = BadRequest

        with pytest.raises(BadRequest):
            interactor.get_user_posts_wrapper(
                user_id, requests_parameters_dto
            )

        presenter_mock.raise_exception_for_invalid_offset_length.assert_called_once()

    def test_get_user_posts_interactor_with_invalid_limit_raise_exception(self,
                                                                          presenter_mock,
                                                                          interactor):
        user_id = 1

        requests_parameters_dto = storage_dtos.RequestsParametersDTOFactory(
            offset=0,
            limit=-1,
        )

        presenter_mock.raise_exception_for_invalid_limit_length.side_effect = BadRequest

        with pytest.raises(BadRequest):
            interactor.get_user_posts_wrapper(
                user_id, requests_parameters_dto
            )

        presenter_mock.raise_exception_for_invalid_limit_length.assert_called_once()

    def test_get_user_posts_interactor_when_user_not_found_raise_exception(
            self, presenter_mock, interactor, user_storage_mock):
        user_id = 1
        requests_parameters_dto = storage_dtos.RequestsParametersDTOFactory(
            offset=0,
            limit=0,
        )

        user_storage_mock.check_is_user_exists.return_value = False
        presenter_mock.raise_exception_for_user_not_exist.side_effect = BadRequest

        with pytest.raises(BadRequest):
            interactor.get_user_posts_wrapper(
                user_id, requests_parameters_dto
            )

        user_storage_mock.check_is_user_exists.assert_called_once_with(
            user_id=user_id)
        presenter_mock.raise_exception_for_user_not_exist.assert_called_once()

