import unittest
from fb_post.tests.factories.models import UserFactory
import pytest
from unittest.mock import create_autospec
from fb_post.interactors.storage_interfaces.dtos import RequestsParametersDTO
from fb_post.interactors.storage_interfaces.user_interface import UserInterface
from fb_post.interactors.storage_interfaces.post_interface import PostInterface
from fb_post.interactors.presenter_interfaces.get_user_posts_presenter_interface import \
    GetPostsPresenterInterface
from fb_post.interactors.get_user_posts_interactor import GetUserPostsInteractor
from django_swagger_utils.drf_server.exceptions import BadRequest, NotFound


def test_get_user_posts_interactor_with_invalid_offset_raise_exception(
        get_requests_parameters_dto_with_invalid_offset):
    user_id = 1

    user_storage = create_autospec(UserInterface)
    post_storage = create_autospec(PostInterface)
    presenter = create_autospec(GetPostsPresenterInterface)
    interactor = GetUserPostsInteractor(
        user_storage=user_storage,
        post_storages=post_storage,
        presenter=presenter
    )
    presenter.raise_exception_for_invalid_offset_length.side_effect = BadRequest

    with pytest.raises(BadRequest):
        interactor.get_user_posts_wrapper(
            user_id, get_requests_parameters_dto_with_invalid_offset
        )

    presenter.raise_exception_for_invalid_offset_length.assert_called_once()


def test_get_user_posts_interactor_with_invalid_limit_raise_exception(
        get_requests_parameters_dto_with_invalid_limit):
    user_id = 1

    user_storage = create_autospec(UserInterface)
    post_storage = create_autospec(PostInterface)
    presenter = create_autospec(GetPostsPresenterInterface)
    interactor = GetUserPostsInteractor(
        user_storage=user_storage,
        post_storages=post_storage,
        presenter=presenter
    )
    presenter.raise_exception_for_invalid_limit_length.side_effect = BadRequest

    with pytest.raises(BadRequest):
        interactor.get_user_posts_wrapper(
            user_id, get_requests_parameters_dto_with_invalid_limit)

    presenter.raise_exception_for_invalid_limit_length.assert_called_once()


def test_get_user_posts_interactor_when_user_not_found_raise_exception(
        get_requests_parameters_dto):
    user_id = 1

    user_storage = create_autospec(UserInterface)
    post_storage = create_autospec(PostInterface)
    presenter = create_autospec(GetPostsPresenterInterface)
    interactor = GetUserPostsInteractor(
        user_storage=user_storage,
        post_storages=post_storage,
        presenter=presenter
    )
    user_storage.check_is_user_exists.return_value = False
    presenter.raise_exception_for_user_not_exist.side_effect = BadRequest

    with pytest.raises(BadRequest):
        interactor.get_user_posts_wrapper(
            user_id, get_requests_parameters_dto
        )

    user_storage.check_is_user_exists.assert_called_once_with(user_id=user_id)
    presenter.raise_exception_for_user_not_exist.assert_called_once()


@pytest.mark.django_db
def test_get_user_posts_interactor_when_valid_details_given_return_posts_details(
        users, posts,
        reacts, comments, replies, reacts_on_comments, posts_details_response,
        user_details,
        posts_details, reaction_details, comment_details, replies_details,
        reaction_on_comment_details
):
    user_id = 1
    limit = 2
    offset = 0
    expected_output = posts_details_response

    user_storage = create_autospec(UserInterface)
    post_storage = create_autospec(PostInterface)
    presenter = create_autospec(GetPostsPresenterInterface)

    user_storage.check_is_user_exists.return_value = True
    post_storage.get_posts.return_value = posts_details
    post_storage.get_all_reactions.return_value = reaction_details
    post_storage.get_comments.return_value = comment_details
    post_storage.get_replies_on_comment.return_value = replies_details
    post_storage.get_reactions_on_comments.return_value = reaction_on_comment_details
    user_storage.get_users_details.return_value = user_details

    interactor = GetUserPostsInteractor(
        user_storage=user_storage,
        post_storages=post_storage,
        presenter=presenter
    )

    request_parameter_dto = RequestsParametersDTO(
        offset=offset,
        limit=limit,
        sort_order="DESC",
        post_content="Hello"
    )

    actual_output = interactor.get_user_posts(user_id, request_parameter_dto)

    # assert
    user_storage.check_is_user_exists.assert_called_once_with(user_id)
    post_storage.get_posts.assert_called_once_with(user_id,
                                                   request_parameter_dto)
    post_storage.get_all_reactions.assert_called_once_with([3, 4])
    post_storage.get_comments.assert_called_once_with([3, 4])
    post_storage.get_replies_on_comment.assert_called_once_with([2])
    post_storage.get_reactions_on_comments.assert_called_once_with([2])
    user_storage.get_users_details.assert_called_once_with([1, 2])

    # assert expected_output == actual_output
