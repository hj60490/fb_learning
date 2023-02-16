import pytest

from fb_post.tests.factories.models import UserFactory
from fb_post.tests.factories.storage_dtos import UserDTOFactory, \
    UsersDTOFactory, UsersCountDTOFactory


@pytest.fixture(autouse=True)
def reset_storage_dto_factory_sequences():
    UserFactory.reset_sequence()
    UserDTOFactory.reset_sequence()
    UsersDTOFactory.reset_sequence()
    UsersCountDTOFactory.reset_sequence()