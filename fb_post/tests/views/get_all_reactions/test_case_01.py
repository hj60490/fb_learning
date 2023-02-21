"""
# valid limit and offset is given
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from ...common_fixtures.adapters import get_users_dtos_mocker
from ...factories.models import PostFactory, ReactFactory, CommentFactory
from ...factories.storage_dtos import UserDTOFactory


class TestCase01GetAllReactionsAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {}

    @pytest.mark.django_db
    def test_case(self, snapshot, mocker):
        body = {}
        path_params = {}
        query_params = {'offset': 0, 'limit': 3}
        headers = {}
        PostFactory.create_batch(size=2)
        ReactFactory(post_id=1, reaction="SAD")
        CommentFactory()
        CommentFactory(parent_comment_id=1)
        ReactFactory(post_id=None, comment_id=1, reaction="SAD")
        ReactFactory(post_id=None, comment_id=2, reaction="SAD")
        get_users_dtos_mock = get_users_dtos_mocker(mocker)
        get_users_dtos_mock.return_value = [UserDTOFactory(), UserDTOFactory(),
                                            UserDTOFactory()]
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)
