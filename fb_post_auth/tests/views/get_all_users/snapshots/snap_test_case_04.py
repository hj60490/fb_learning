# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase04GetAllUsersAPITestCase.test_case status_code'] = '200'

snapshots['TestCase04GetAllUsersAPITestCase.test_case body'] = {
    'total_users': 3,
    'users_details': [
        {
            'name': 'User_1',
            'user_id': 1
        },
        {
            'name': 'User_2',
            'user_id': 2
        }
    ]
}
