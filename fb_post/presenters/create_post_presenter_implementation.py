from fb_post.interactors.presenter_interfaces.presenter_interface import \
    CreatePostPresenterInterface
from django_swagger_utils.drf_server.exceptions import (
    BadRequest
)
from fb_post.constants.exception_messages import INVALID_USER_ID


class CreatePostPresenterImplementation(CreatePostPresenterInterface):

    def raise_exception_for_user_not_exist(self):
        raise BadRequest(*INVALID_USER_ID)



