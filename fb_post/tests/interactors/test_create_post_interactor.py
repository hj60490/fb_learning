import pytest
from unittest.mock import create_autospec, patch
from fb_post.interactors.storage_interfaces.user_interface import UserInterface
from fb_post.interactors.storage_interfaces.post_interface import PostInterface
from fb_post.interactors.presenter_interfaces.presenter_interface import \
    CreatePostPresenterInterface
from fb_post.interactors.create_post_interactor import CreatePostInteractor
from django_swagger_utils.drf_server.exceptions import BadRequest


def test_create_post_interactor_when_user_not_found_raise_exception():
    content = "hello"
    user_id = 1

    user_storage = create_autospec(UserInterface)
    post_storage = create_autospec(PostInterface)
    presenter = create_autospec(CreatePostPresenterInterface)
    interactor = CreatePostInteractor(
        user_storage=user_storage,
        post_storage=post_storage,
        presenter=presenter
    )
    user_storage.check_is_user_exists.return_value = False
    presenter.raise_exception_for_user_not_exist.side_effect = BadRequest

    with pytest.raises(BadRequest):
        interactor.create_post_wrapper(
            content, user_id
        )

    user_storage.check_is_user_exists.assert_called_once_with(user_id=user_id)
    presenter.raise_exception_for_user_not_exist.assert_called_once()


def test_create_post_interactor_with_valid_details_creates_post():
    user_id = 1
    content = "hello"
    user_storage = create_autospec(UserInterface)
    post_storage = create_autospec(PostInterface)
    presenter = create_autospec(CreatePostPresenterInterface)
    interactor = CreatePostInteractor(
        user_storage=user_storage,
        post_storage=post_storage,
        presenter=presenter
    )
    user_storage.check_is_user_exists.return_value = True

    assert interactor.create_post_wrapper(user_id=user_id,
                                          content=content) is None


def test_create_post_interactor_post_storage():
    user_id = 1
    content = "hello"
    user_storage = create_autospec(UserInterface)
    post_storage = create_autospec(PostInterface)
    presenter = create_autospec(CreatePostPresenterInterface)
    interactor = CreatePostInteractor(
        user_storage=user_storage,
        post_storage=post_storage,
        presenter=presenter
    )
    user_storage.check_is_user_exists.return_value = True

    interactor.create_post(
        user_id=user_id,
        content=content
    )

    post_storage.create_post.assert_called_once_with(
        user_id=user_id,
        content=content
    )
