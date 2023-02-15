import factory

from fb_post_auth.tests.factories.models import UserFactory
from fb_post_auth.interactors.storage_interfaces.dtos import UserDto


class UserDTOFactory(factory.Factory):
    class Meta:
        model = UserDto

    user_id = factory.sequence(lambda n: n + 1)
    name = factory.Sequence(lambda n: f"User_{n + 1}")
    profile_pic = factory.Sequence(
        lambda n: f"https://profile_pic_url{n + 1}.com")