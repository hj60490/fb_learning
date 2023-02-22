import datetime
import pytest
from unittest import mock

from fb_post.storages.post_storage_implementation import \
    PostStorageImplementation
from fb_post.models import Post
from fb_post.storages.reaction_storage_implementation import \
    ReactionStorageImplementation
from fb_post.tests.factories import storage_dtos
from fb_post.tests.factories.models import ReactFactory, \
    CommentFactory, PostFactory
from fb_post.tests.factories.storage_dtos import ReactOnPostDTOFactory, \
    CommentOnPostDTOFactory, ReactOnCommentDTOFactory, PostDTOFactory, \
    ReactDTOFactory


class TestGetReactionsReactStorage:

    @pytest.fixture
    def post_storage_mock(self):
        from fb_post.interactors.storage_interfaces.post_storage_interface import \
            PostInterface
        return mock.create_autospec(PostInterface)

    @pytest.fixture
    def presenter_mock(self):
        from fb_post.interactors.presenter_interfaces. \
            get_user_posts_presenter_interface import \
            GetPostsPresenterInterface
        return mock.create_autospec(GetPostsPresenterInterface)

    @pytest.fixture
    def interactor(self, post_storage_mock, presenter_mock):
        from fb_post.interactors.get_user_posts_interactor import \
            GetUserPostsInteractor
        return GetUserPostsInteractor(
            post_storages=post_storage_mock,
            presenter=presenter_mock)

    @pytest.mark.django_db
    def test_get_reactions_return_reactions(self):
        limit = 2
        offset = 0

        PostFactory()
        CommentFactory()
        CommentFactory(post_id=1, parent_comment_id=1)
        ReactFactory(post_id=1, reaction="SAD")
        ReactFactory(comment_id=1, post_id=None, reaction="SAD")
        ReactFactory(comment_id=2, post_id=None, reaction="SAD")
        excepted_output = [
            ReactDTOFactory(post_id=1, reaction="SAD"),
            ReactDTOFactory(comment_id=1, reaction="SAD")
        ]

        react_storage = ReactionStorageImplementation()
        actual_output = react_storage.get_all_reactions(
            limit=limit, offset=offset
        )
        assert actual_output == excepted_output
