
from .presenter_interfaces.presenter_interface import PresenterInterface
from .storage_interfaces.post_interface import PostInterface
from .storage_interfaces.user_interface import UserInterface


class CreatePostInteractor:
    def __init__(self, post_storage: PostInterface, user_storage: UserInterface,
                 presenter: PresenterInterface):
        self.post_storage = post_storage
        self.user_storage = user_storage
        self.presenter = presenter

    def create_post(self,content: str, user_id: int):
        is_user_exists = not self.user_storage.check_is_user_exists(user_id)

        post_dtos = self.post_storage.create_post_object(
            content=content, user_id=user_id
        )

        return self.presenter.get_response_for_create_post(
            post_dtos=post_dtos
        )


