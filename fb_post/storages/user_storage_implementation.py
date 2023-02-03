from fb_post.interactors.storage_interfaces.user_interface import UserInterface
from fb_post.models.models import User


class UserStorageImplementation(UserInterface):

    def check_is_user_exists(self, user_id: int) -> bool:
        return User.objects.get(id=user_id).exists()
