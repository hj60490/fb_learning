import pytest
from fb_post.presenters.get_user_posts_presenter_implementation import GetUserPostsPresenterImplementation
from fb_post.interactors.presenter_interfaces.dtos import PostDetailsDto


def test_get_all_posts_of_user_for_user_having_zero_post_return_empty(
        get_user_dto):
    expected_output = {
        "user_posts_details": []
    }
    presenter = GetUserPostsPresenterImplementation()
    user_posts_details_dto = PostDetailsDto(
        users=[get_user_dto],
        posts=[],
        reactions_on_posts=[],
        comments_on_post=[],
        replies=[],
        reactions_on_comments=[]
    )

    actual_output = presenter.get_all_posts_of_user(
        posts_details_dto=user_posts_details_dto
    )

    assert actual_output == expected_output


def test_get_all_posts_of_user_for_user_having_only_posts(
        get_user_dto):
    expected_output = {
        "user_posts_details": []
    }
    presenter = GetUserPostsPresenterImplementation()
    user_posts_details_dto = PostDetailsDto(
        users=[get_user_dto],
        posts=[],
        reactions_on_posts=[],
        comments_on_post=[],
        replies=[],
        reactions_on_comments=[]
    )

    actual_output = presenter.get_all_posts_of_user(
        posts_details_dto=user_posts_details_dto
    )

    assert actual_output == expected_output


