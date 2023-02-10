import pytest
from unittest.mock import create_autospec
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

    with pytest.raises(Exception):
        assert interactor.get_user_posts_wrapper(
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

    with pytest.raises(Exception):
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



