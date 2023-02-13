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


def test_get_all_posts_of_user_for_user_having_zero_post_return_empty(
        get_no_posts_dto, snapshot):
    presenter = GetUserPostsPresenterImplementation()
    actual_output = presenter.get_all_posts_of_user(
        posts_details_dto=get_no_posts_dto
    )

    snapshot.assert_match(actual_output)


def test_get_all_posts_of_user_for_user_having_post_but_no_reaction_and_comments(
        get_posts_with_no_reaction_and_comments_dto, snapshot):
    presenter = GetUserPostsPresenterImplementation()
    actual_output = presenter.get_all_posts_of_user(
        posts_details_dto=get_posts_with_no_reaction_and_comments_dto
    )

    snapshot.assert_match(actual_output)


def test_get_all_posts_of_user_for_user_having_posts_only_reactions(
        get_posts_with_only_reactions, snapshot):
    presenter = GetUserPostsPresenterImplementation()
    actual_output = presenter.get_all_posts_of_user(
        posts_details_dto=get_posts_with_only_reactions
    )

    snapshot.assert_match(actual_output)


def test_get_all_posts_of_user_for_user_having_posts_only_comments(
        get_posts_with_only_comments, snapshot):
    presenter = GetUserPostsPresenterImplementation()
    actual_output = presenter.get_all_posts_of_user(
        posts_details_dto=get_posts_with_only_comments
    )

    snapshot.assert_match(actual_output)


def test_get_all_posts_of_user_for_user_having_posts_only_comments_and_replies(
        get_posts_with_only_comments_with_reply, snapshot):
    presenter = GetUserPostsPresenterImplementation()
    actual_output = presenter.get_all_posts_of_user(
        posts_details_dto=get_posts_with_only_comments_with_reply
    )

    snapshot.assert_match(actual_output)


def test_get_all_posts_of_user_for_user_having_posts_only_comments_with_reaction_and_replies(
        get_posts_with_only_comments_with_reaction, snapshot):
    presenter = GetUserPostsPresenterImplementation()
    actual_output = presenter.get_all_posts_of_user(
        posts_details_dto=get_posts_with_only_comments_with_reaction
    )

    snapshot.assert_match(actual_output)


def test_get_all_posts_of_user_return_posts_dict(
        get_posts_details, snapshot):
    presenter = GetUserPostsPresenterImplementation()
    actual_output = presenter.get_all_posts_of_user(
        posts_details_dto=get_posts_details
    )

    snapshot.assert_match(actual_output)


def test_raise_exception_for_user_not_exists():
    exception_messages = INVALID_USER_ID[0]
    exception_res_status = INVALID_USER_ID[1]
    presenter = GetUserPostsPresenterImplementation()

    with pytest.raises(BadRequest) as exception:
        presenter.raise_exception_for_user_not_exist()

    assert exception.value.message == exception_messages
    assert exception.value.res_status == exception_res_status


def test_raise_exception_for_invalid_limit_value():
    exception_messages = INVALID_LIMIT_LENGTH[0]
    exception_res_status = INVALID_LIMIT_LENGTH[1]
    presenter = GetUserPostsPresenterImplementation()

    with pytest.raises(BadRequest) as exception:
        presenter.raise_exception_for_invalid_limit_length()

    assert exception.value.message == exception_messages
    assert exception.value.res_status == exception_res_status


def test_raise_exception_for_invalid_offset_value():
    exception_messages = INVALID_OFFSET_LENGTH[0]
    exception_res_status = INVALID_OFFSET_LENGTH[1]
    presenter = GetUserPostsPresenterImplementation()

    with pytest.raises(BadRequest) as exception:
        presenter.raise_exception_for_invalid_offset_length()

    assert exception.value.message == exception_messages
    assert exception.value.res_status == exception_res_status
