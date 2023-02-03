from fb_post.interactors.presenter_interfaces.presenter_interface import \
    PresenterInterface
from fb_post.exceptions.custom_exceptions import InvalidUserException
from django_swagger_utils.drf_server.exceptions import (
    BadRequest, NotFound, Forbidden, ExpectationFailed, Unauthorized
)
from fb_post.constants.exception_messages import INVALID_USER_ID, CONTENT_EMPTY


class PresenterImplementation(PresenterInterface):

    def raise_exception_for_user_not_exist(self):
        raise BadRequest(*INVALID_USER_ID)

    def raise_exception_for_giving_content(self):
        raise BadRequest(*CONTENT_EMPTY)

