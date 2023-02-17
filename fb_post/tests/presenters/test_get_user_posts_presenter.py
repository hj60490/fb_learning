import datetime

import pytest
from fb_post.presenters.get_user_posts_presenter_implementation import \
    GetUserPostsPresenterImplementation
from fb_post.interactors.presenter_interfaces.dtos import PostDetailsDto
import json
from fb_post.constants.exception_messages import INVALID_USER_ID, \
    INVALID_LIMIT_LENGTH, INVALID_OFFSET_LENGTH
from django_swagger_utils.drf_server.exceptions import (
    BadRequest
)

from fb_post.tests.factories.storage_dtos import UserDTOFactory, PostDTOFactory, \
    ReactOnPostDTOFactory, CommentOnPostDTOFactory, CommentOnCommentDTOFactory, \
    ReactOnCommentDTOFactory


class TestsCreatePostPresenter:

    def test_get_all_posts_of_user_for_user_having_zero_post_return_empty(
           self, snapshot):
        user_posts_details_dto = PostDetailsDto(
            users=[UserDTOFactory()],
            posts=[],
            reactions_on_posts=[],
            comments_on_post=[],
            replies=[],
            reactions_on_comments=[]
        )
        presenter = GetUserPostsPresenterImplementation()
        actual_output = presenter.get_all_posts_of_user(
            posts_details_dto=user_posts_details_dto
        )

        snapshot.assert_match(actual_output)

    def test_get_all_posts_of_user_for_user_having_post_but_no_reaction_and_comments(
            self, snapshot):
        user_posts_details_dto = PostDetailsDto(
            users=[UserDTOFactory()],
            posts=[PostDTOFactory()],
            reactions_on_posts=[],
            comments_on_post=[],
            replies=[],
            reactions_on_comments=[]
        )
        presenter = GetUserPostsPresenterImplementation()
        actual_output = presenter.get_all_posts_of_user(
            posts_details_dto=user_posts_details_dto
        )

        snapshot.assert_match(actual_output)

    def test_get_all_posts_of_user_for_user_having_posts_only_reactions(
            self, snapshot):
        user_posts_details_dto = PostDetailsDto(
            users=[UserDTOFactory()],
            posts=[PostDTOFactory()],
            reactions_on_posts=[ReactOnPostDTOFactory()],
            comments_on_post=[],
            replies=[],
            reactions_on_comments=[]
        )
        presenter = GetUserPostsPresenterImplementation()
        actual_output = presenter.get_all_posts_of_user(
            posts_details_dto=user_posts_details_dto
        )

        snapshot.assert_match(actual_output)

    def test_get_all_posts_of_user_for_user_having_posts_only_comments(
            self, snapshot):
        user_posts_details_dto = PostDetailsDto(
            users=[UserDTOFactory()],
            posts=[PostDTOFactory()],
            reactions_on_posts=[],
            comments_on_post=[CommentOnPostDTOFactory()],
            replies=[],
            reactions_on_comments=[]
        )
        presenter = GetUserPostsPresenterImplementation()
        actual_output = presenter.get_all_posts_of_user(
            posts_details_dto=user_posts_details_dto
        )

        snapshot.assert_match(actual_output)

    def test_get_all_posts_of_user_for_user_having_posts_only_comments_and_replies(
            self, snapshot):
        user_posts_details_dto = PostDetailsDto(
            users=[UserDTOFactory()],
            posts=[PostDTOFactory()],
            reactions_on_posts=[],
            comments_on_post=[CommentOnPostDTOFactory()],
            replies=[CommentOnCommentDTOFactory()],
            reactions_on_comments=[]
        )
        presenter = GetUserPostsPresenterImplementation()
        actual_output = presenter.get_all_posts_of_user(
            posts_details_dto=user_posts_details_dto
        )

        snapshot.assert_match(actual_output)

    def test_get_all_posts_of_user_for_user_having_posts_only_comments_with_reaction_and_replies(
            self, snapshot):
        user_posts_details_dto = PostDetailsDto(
            users=[UserDTOFactory()],
            posts=[PostDTOFactory()],
            reactions_on_posts=[],
            comments_on_post=[CommentOnPostDTOFactory()],
            replies=[CommentOnCommentDTOFactory()],
            reactions_on_comments=[ReactOnCommentDTOFactory()]
        )
        presenter = GetUserPostsPresenterImplementation()
        actual_output = presenter.get_all_posts_of_user(
            posts_details_dto=user_posts_details_dto
        )

        snapshot.assert_match(actual_output)

    def test_get_all_posts_of_user_return_posts_dict(self, snapshot):
        user_posts_details_dto = PostDetailsDto(
            users=[UserDTOFactory()],
            posts=[PostDTOFactory()],
            reactions_on_posts=[ReactOnPostDTOFactory()],
            comments_on_post=[CommentOnPostDTOFactory()],
            replies=[CommentOnCommentDTOFactory()],
            reactions_on_comments=[ReactOnCommentDTOFactory()]
        )
        presenter = GetUserPostsPresenterImplementation()
        actual_output = presenter.get_all_posts_of_user(
            posts_details_dto=user_posts_details_dto
        )

        snapshot.assert_match(actual_output)

    def test_raise_exception_for_user_not_exists(self):
        exception_messages = INVALID_USER_ID[0]
        exception_res_status = INVALID_USER_ID[1]
        presenter = GetUserPostsPresenterImplementation()

        with pytest.raises(BadRequest) as exception:
            presenter.raise_exception_for_user_not_exist()

        assert exception.value.message == exception_messages
        assert exception.value.res_status == exception_res_status

    def test_raise_exception_for_invalid_limit_value(self):
        exception_messages = INVALID_LIMIT_LENGTH[0]
        exception_res_status = INVALID_LIMIT_LENGTH[1]
        presenter = GetUserPostsPresenterImplementation()

        with pytest.raises(BadRequest) as exception:
            presenter.raise_exception_for_invalid_limit_length()

        assert exception.value.message == exception_messages
        assert exception.value.res_status == exception_res_status

    def test_raise_exception_for_invalid_offset_value(self):
        exception_messages = INVALID_OFFSET_LENGTH[0]
        exception_res_status = INVALID_OFFSET_LENGTH[1]
        presenter = GetUserPostsPresenterImplementation()

        with pytest.raises(BadRequest) as exception:
            presenter.raise_exception_for_invalid_offset_length()

        assert exception.value.message == exception_messages
        assert exception.value.res_status == exception_res_status
