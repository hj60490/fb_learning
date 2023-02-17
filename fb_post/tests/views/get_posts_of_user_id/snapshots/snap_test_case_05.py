# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase05GetPostsOfUserIdAPITestCase.test_case status_code'] = '200'

snapshots['TestCase05GetPostsOfUserIdAPITestCase.test_case body'] = {
    'user_posts_details': [
        {
            'comments': [
            ],
            'comments_count': 0,
            'post_content': 'Harsh',
            'post_id': 4,
            'posted_at': '2023-02-13 11:20:25',
            'posted_by': {
                'name': 'User_1',
                'profile_pic': 'https://profile_pic_url1.com',
                'user_id': 1
            },
            'reactions': {
                'count': 0,
                'types': [
                ]
            }
        }
    ]
}
