
from fb_post.interactors.presenter_interfaces.presenter_interface import\
    CreatePostPresenterInterface
from fb_post.interactors.storage_interfaces.post_storage_interface import PostInterface
from fb_post.exceptions.custom_exceptions import InvalidUserException
from fb_post.adapters.service_adapter import get_service_adapter


class CreatePostInteractor:
    def __init__(self, post_storage: PostInterface,
                 presenter: CreatePostPresenterInterface):
        self.post_storage = post_storage
        self.presenter = presenter

    def create_post_wrapper(self, content: str, user_id: int):
        try:
            self.create_post(
                content=content,
                user_id=user_id
            )
        except InvalidUserException:
            self.presenter.raise_exception_for_user_not_exist()

    def create_post(self, content: str, user_id: int):
        adaptor = get_service_adapter()
        is_user_exists_adaptor = adaptor.fb_post_auth.check_user_exists_or_not(
            user_id)

        if not is_user_exists_adaptor:
            raise InvalidUserException

        self.post_storage.create_post(
            content=content, user_id=user_id
        )
        return



