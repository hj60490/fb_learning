import pytest

from fb_post_auth.tests.factories.models import UserFactory


@pytest.fixture(autouse=True)
def reset_storage_dto_factory_sequences():
    UserFactory.reset_sequence()