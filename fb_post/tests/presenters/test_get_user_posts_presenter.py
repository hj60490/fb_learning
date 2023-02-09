import pytest
from fb_post.presenters.get_user_posts_presenter_implementation import \
    GetUserPostsPresenterImplementation
from fb_post.interactors.presenter_interfaces.dtos import PostDetailsDto
import json


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



