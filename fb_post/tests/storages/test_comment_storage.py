import datetime
import pytest
from unittest import mock

from fb_post.storages.comment_storage_implementation import \
    CommentStorageImplementation
from fb_post.storages.post_storage_implementation import \
    PostStorageImplementation
from fb_post.models import Post
from fb_post.tests.factories import storage_dtos
from fb_post.tests.factories.models import ReactFactory, \
    CommentFactory, PostFactory
from fb_post.tests.factories.storage_dtos import ReactOnPostDTOFactory, \
    CommentOnPostDTOFactory, ReactOnCommentDTOFactory, PostDTOFactory, \
    CommentDTOFactory


class TestGetUserPostsStorage:
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
    def test_get_comments_return_comment_dto(self):
        comments_ids = [1, 2, 3]
        PostFactory.create_batch(size=3)
        CommentFactory.create_batch(size=3)
        expected_output = [
            CommentDTOFactory(),
            CommentDTOFactory(),
            CommentDTOFactory()
        ]
        comment_storage = CommentStorageImplementation()
        actual_output = comment_storage.get_comments(comments_ids=comments_ids)

        assert actual_output == expected_output

