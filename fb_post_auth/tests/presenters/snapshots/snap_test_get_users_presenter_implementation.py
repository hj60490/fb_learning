# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestsGetUsersPresenterImplementation.test_get_response_for_get_users_return_users_details_dict 1'] = {
    'total_users': 3,
    'users_details': [
        {
            'name': 'User_6',
            'profile_pic': 'https://profile_pic_url6.com',
            'user_id': 6
        },
        {
            'name': 'User_7',
            'profile_pic': 'https://profile_pic_url7.com',
            'user_id': 7
        },
        {
            'name': 'User_8',
            'profile_pic': 'https://profile_pic_url8.com',
            'user_id': 8
        }
    ]
}
