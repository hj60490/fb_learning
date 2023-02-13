import pytest
from fb_post.constants.exception_messages import INVALID_USER_ID
from django_swagger_utils.drf_server.exceptions import BadRequest
from fb_post.presenters.create_post_presenter_implementation import \
    CreatePostPresenterImplementation


def test_raise_exception_for_user_not_exists():
    exception_messages = INVALID_USER_ID[0]
    exception_res_status = INVALID_USER_ID[1]
    presenter = CreatePostPresenterImplementation()

    with pytest.raises(BadRequest) as exception:
        presenter.raise_exception_for_user_not_exist()

    assert exception.value.message == exception_messages
    assert exception.value.res_status == exception_res_status
