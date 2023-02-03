from fb_post.interactors.presenter_interfaces.presenter_interface import \
    PresenterInterface


class PresenterImplementation(PresenterInterface):

    def raise_exception_for_user_not_exist(self):
        raise ValueError("User id not found")



