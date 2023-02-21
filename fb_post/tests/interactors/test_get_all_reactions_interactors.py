from unittest import mock
from mock import call, Mock

from fb_post.interactors.storage_interfaces.dtos import ReactionDetailsDTO
from fb_post.tests.common_fixtures.adapters import \
    check_user_exists_or_not_mocker, get_users_dtos_mocker
from fb_post.tests.factories import storage_dtos
import pytest
from django_swagger_utils.drf_server.exceptions import BadRequest


class TestGetUserPostsInteractor:

    @pytest.fixture
    def post_storage_mock(self):
        from fb_post.interactors.storage_interfaces.\
            post_storage_interface import \
            PostInterface
        return mock.create_autospec(PostInterface)

    @pytest.fixture
    def comment_storage_mock(self):
        from fb_post.interactors.storage_interfaces.\
            comment_storage_interface import \
            CommentStorageInterface
        return mock.create_autospec(CommentStorageInterface)

    @pytest.fixture
    def reaction_storage_mock(self):
        from fb_post.interactors.storage_interfaces.\
            reaction_storage_interface import \
            ReactionStorageInterface
        return mock.create_autospec(ReactionStorageInterface)

    @pytest.fixture
    def presenter_mock(self):
        from fb_post.interactors.presenter_interfaces.\
            get_all_reaction_presenter_interface import \
            GetAllReactionsPresenterInterface
        return mock.create_autospec(GetAllReactionsPresenterInterface)

    @pytest.fixture
    def interactor(self, post_storage_mock, presenter_mock,
                   comment_storage_mock,
                   reaction_storage_mock):
        from fb_post.interactors.get_all_reactions_interactor import \
            GetAllReactionsInteractor
        return GetAllReactionsInteractor(
            post_storage=post_storage_mock,
            reaction_storage=reaction_storage_mock,
            comment_storage=comment_storage_mock,
            presenter=presenter_mock)

    def test_get_reactions_interactor_with_invalid_offset_raise_exception(
            self, presenter_mock, interactor):
        offset = -1
        limit = 0

        presenter_mock.raise_exception_for_invalid_offset_length.side_effect \
            = BadRequest

        with pytest.raises(BadRequest):
            interactor.get_all_reactions_wrapper(
                limit=limit, offset=offset
            )

        presenter_mock.raise_exception_for_invalid_offset_length.assert_called_once()

    def test_get_reactions_interactor_with_invalid_limit_raise_exception(
            self, presenter_mock, interactor):
        offset = 0
        limit = -1

        presenter_mock.raise_exception_for_invalid_limit_length.side_effect \
            = BadRequest

        with pytest.raises(BadRequest):
            interactor.get_all_reactions_wrapper(
                limit=limit, offset=offset
            )

        presenter_mock.raise_exception_for_invalid_limit_length.assert_called_once()

    def test_get_all_reactions_will_give_reactions_details(
            self, mocker, post_storage_mock, comment_storage_mock,
            reaction_storage_mock, interactor, presenter_mock
    ):
        limit = 3
        offset = 0
        users_dtos = [
            storage_dtos.UserDTOFactory(),
            storage_dtos.UserDTOFactory(),
            storage_dtos.UserDTOFactory()
        ]
        post_dtos = [
            storage_dtos.PostDTOFactory()
        ]
        com = storage_dtos.CommentDTOFactory(post_id=1, comment_id=1)
        replies = [
            [
                com,
                storage_dtos.CommentDTOFactory(parent_comment_id=1)
            ],
            [
                com
            ]

        ]
        comments = [

                storage_dtos.CommentDTOFactory(post_id=1, comment_id=1),
                storage_dtos.CommentDTOFactory(parent_comment_id=1)

        ]
        reactions = [
            storage_dtos.ReactDTOFactory(post_id=1),
            storage_dtos.ReactDTOFactory(comment_id=1),
            storage_dtos.ReactDTOFactory(comment_id=2),
        ]

        reactions_details_dto = ReactionDetailsDTO(
            reactions=reactions,
            users=users_dtos,
            posts=post_dtos,
            comments=comments,
        )

        get_users_dtos_mock = get_users_dtos_mocker(mocker)
        reaction_storage_mock.get_all_reactions.return_value = reactions
        comment_storage_mock.get_comments.side_effect = replies
        post_storage_mock.get_all_posts.return_value = post_dtos
        get_users_dtos_mock.return_value = users_dtos

        interactor.get_all_reactions_wrapper(
            limit=limit, offset=offset
        )

        reaction_storage_mock.get_all_reactions.assert_called_once()
        comment_storage_mock.get_comments.assert_has_calls(
            [call([1, 2]), call([1])], any_order=False
        )
        post_storage_mock.get_all_posts.assert_called_once_with([1, 2])
        get_users_dtos_mock.assert_called_once_with([1, 2, 3])
        presenter_mock.get_response_for_all_reactions(reactions_details_dto)






