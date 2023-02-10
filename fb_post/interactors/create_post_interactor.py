
from fb_post.interactors.presenter_interfaces.presenter_interface import\
    CreatePostPresenterInterface
from fb_post.interactors.storage_interfaces.post_interface import PostInterface
from fb_post.interactors.storage_interfaces.user_interface import UserInterface
from fb_post.exceptions.custom_exceptions import InvalidUserException, InvalidContentException


class CreatePostInteractor:
    def __init__(self, post_storage: PostInterface, user_storage: UserInterface,
                 presenter: CreatePostPresenterInterface):
        self.post_storage = post_storage
        self.user_storage = user_storage
        self.presenter = presenter

    def create_post_wrapper(self, content: str, user_id: int):
        try:
            self.create_post(
                content=content,
                user_id=user_id
            )
        except InvalidUserException:
            self.presenter.raise_exception_for_user_not_exist()
        except InvalidContentException:
            self.presenter.raise_exception_for_invalid_content()

    def create_post(self, content: str, user_id: int):
        is_user_exists = self.user_storage.check_is_user_exists(user_id)

        if not is_user_exists:
            raise InvalidUserException

        self.post_storage.create_post(
            content=content, user_id=user_id
        )
        return



