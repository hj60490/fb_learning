"""
# valid case
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from ...common_fixtures.adapters import check_user_exists_or_not_mocker

REQUEST_BODY = """"
{
   "content":"string",
   "user_id":"integer"
}
"""
TEST_CASE = {
    "request": {
        "path_params": {},
        "query_params": {},
        "header_params": {},
        "securities": {"oauth": {
            "tokenUrl": "http://auth.ibtspl.com/oauth2/",
            "flow": "password",
            "scopes": {
                "read": "read users",
                "write": "create users",
                "update": "update users",
                "delete": "delete users"
            },
            "type": "oauth2"
        }},
        "body": REQUEST_BODY,
    },
}


class TestCase03CreatePostAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {}


    @pytest.mark.django_db
    def test_case(self, snapshot, mocker):
        body = {'content': "Hello" 'string', 'user_id': 1}
        path_params = {}
        query_params = {}
        headers = {}
        check_user_exists_or_not_mock = check_user_exists_or_not_mocker(mocker)
        check_user_exists_or_not_mock.return_value = True
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)

