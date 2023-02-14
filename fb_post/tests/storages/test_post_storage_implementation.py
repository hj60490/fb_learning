import datetime
import pytest
from unittest import mock

from fb_post.storages.post_storage_implementation import \
    PostStorageImplementation
from fb_post.models import Post
from fb_post.tests.factories import storage_dtos
from fb_post.tests.factories.models import UserFactory, ReactFactory, \
    CommentFactory
from fb_post.tests.factories.storage_dtos import ReactOnPostDTOFactory, \
    CommentOnPostDTOFactory, ReactOnCommentDTOFactory


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

    @pytest.mark.django_db
    def test_create_post_weather_post_created(self):
        user_id = 1
        content = "Hello"
        UserFactory.create_batch(size=3)
        post_storage = PostStorageImplementation()
        post_storage.create_post(content=content, user_id=user_id)
        assert Post.objects.filter(content=content, posted_by_id=1).exists()

    @pytest.mark.django_db
    def test_get_all_posts_with_limit_offset_posts_return_posts_dto(self,
                                                                    posts):
        user_id = 1
        UserFactory.create_batch(size=3)
        post_dtos = [
            storage_dtos.PostDTOFactory(
                post_id=3,
                content="Hello",
                posted_by_id=1,
                posted_at=datetime.datetime(2023, 2, 13, 11, 20, 20)
            ),
            storage_dtos.PostDTOFactory(
                post_id=2,
                content="Hello",
                posted_by_id=1,
                posted_at=datetime.datetime(2023, 2, 13, 11, 20, 15)
            )
        ]
        requests_parameters_dto = storage_dtos.RequestsParametersDTOFactory(
            offset=0,
            limit=2,
            sort_order="DESC",
            post_content="Hello"
        )
        post_storage = PostStorageImplementation()
        expected_output = post_dtos
        actual_output = post_storage.get_posts(user_id=user_id,
                                               requests_parameters_dto=requests_parameters_dto)

        assert actual_output == expected_output

    @pytest.mark.django_db
    def test_get_all_posts_with_no_posts_return_empty(self):
        user_id = 1
        expected_output = []
        UserFactory.create_batch(size=3)
        requests_parameters_dto = storage_dtos.RequestsParametersDTOFactory(
            offset=0,
            limit=2,

        )
        post_storage = PostStorageImplementation()
        actual_output = post_storage.get_posts(
            user_id=user_id, requests_parameters_dto=requests_parameters_dto)
        assert actual_output == expected_output

    @pytest.mark.django_db
    def test_get_all_reaction_on_post_return_reaction_dto(self, posts):
        posts_id = [1]
        ReactFactory(post_id=1, reacted_by_id=1)
        reactions_details_dto = [ReactOnPostDTOFactory(reaction_id=1)]
        expected_output = reactions_details_dto
        post_storage = PostStorageImplementation()
        actual_output = post_storage.get_all_reactions(list_of_post_id=posts_id)
        assert actual_output == expected_output

    @pytest.mark.django_db
    def test_get_all_reaction_on_post_no_reaction_return_empty(self, posts):
        posts_id = [1]
        expected_output = []
        UserFactory.create_batch(size=3)
        post_storage = PostStorageImplementation()
        actual_output = post_storage.get_all_reactions(list_of_post_id=posts_id)
        assert actual_output == expected_output

    @pytest.mark.django_db
    def test_get_all_comments_on_post_return_comment_dto(self, posts):
        posts_id = [1]
        UserFactory.create_batch(size=3)
        CommentFactory(post_id=1, commented_by_id=1)
        comments_details_dto = [CommentOnPostDTOFactory(
            post_id=1,
            commented_by_id=1,

        )]
        expected_output = comments_details_dto
        post_storage = PostStorageImplementation()
        actual_output = post_storage.get_comments(list_of_post_id=posts_id)
        assert actual_output == expected_output

    @pytest.mark.django_db
    def test_get_all_comments_on_post_no_comment_return_empty(self, posts):
        posts_id = [1]
        expected_output = []
        UserFactory.create_batch(size=3)
        post_storage = PostStorageImplementation()
        actual_output = post_storage.get_comments(list_of_post_id=posts_id)
        assert actual_output == expected_output

    @pytest.mark.django_db
    def test_get_reactions_on_comments_return_reaction(self, posts):
        comments_id = [1]
        UserFactory.create_batch(size=3)
        CommentFactory()
        ReactFactory(comment_id=1, reacted_by_id=1)
        comments_details_dto = [ReactOnCommentDTOFactory(
            reacted_by_id=1,
            comment_id=1,

        )]
        expected_output = comments_details_dto
        post_storage = PostStorageImplementation()
        actual_output = post_storage.get_reactions_on_comments(
            list_of_comment_id=comments_id)
        assert actual_output == expected_output

    @pytest.mark.django_db
    def test_get_reactions_on_comments_return_empty(self, posts):
        comments_id = [1]
        UserFactory.create_batch(size=3)
        CommentFactory()
        expected_output = []
        post_storage = PostStorageImplementation()
        actual_output = post_storage.get_reactions_on_comments(
            list_of_comment_id=comments_id)
        assert actual_output == expected_output



