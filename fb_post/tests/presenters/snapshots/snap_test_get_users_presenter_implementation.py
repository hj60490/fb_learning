# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestsGetUsersPresenterImplementation.test_get_response_for_get_users_return_users_details_dict 1'] = {
    'total_users': 3,
    'users_details': [
        {
            'name': 'User_1',
            'profile_pic': 'https://profile_pic_url1.com',
            'user_id': 1
        },
        {
            'name': 'User_2',
            'profile_pic': 'https://profile_pic_url2.com',
            'user_id': 2
        },
        {
            'name': 'User_3',
            'profile_pic': 'https://profile_pic_url3.com',
            'user_id': 3
        }
    ]
}
