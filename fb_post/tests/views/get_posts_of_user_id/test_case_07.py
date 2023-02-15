"""
invalid limit
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from ...common_fixtures.adapters import check_user_exists_or_not_mocker, \
    get_users_dtos_mocker
from ...factories.storage_dtos import UserDTOFactory


class TestCase07GetPostsOfUserIdAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {}

    @pytest.mark.django_db
    def test_case(self, snapshot, mocker):
        body = {}
        path_params = {"user_id": "1"}
        query_params = {"limit": "-1", "offset": 0, "sort_order": "ASC",
                        "post_content": "string"}
        headers = {}
        check_user_exists_or_not_mock = check_user_exists_or_not_mocker(mocker)
        get_users_dtos_mock = get_users_dtos_mocker(mocker)
        check_user_exists_or_not_mock.return_value = True
        get_users_dtos_mock.return_value = [UserDTOFactory()]
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)
        return response
