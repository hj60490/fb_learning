from fb_post.interactors.presenter_interfaces.presenter_interface import \
    PresenterInterface
from fb_post.exceptions.custom_exceptions import InvalidUserException


class PresenterImplementation(PresenterInterface):

    def raise_exception_for_user_not_exist(self):
        raise InvalidUserException



