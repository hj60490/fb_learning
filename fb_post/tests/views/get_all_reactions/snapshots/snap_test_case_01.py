# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetAllReactionsAPITestCase.test_case status_code'] = '200'

snapshots['TestCase01GetAllReactionsAPITestCase.test_case body'] = {
    'reactions_details': [
        {
            'comment': None,
            'post': {
                'content': 'post_1',
                'post_id': 1,
                'posted_by': {
                    'name': 'User_1',
                    'profile_pic': 'https://profile_pic_url1.com',
                    'user_id': 1
                }
            },
            'reaction': 'SAD',
            'reaction_id': 1,
            'reply': None
        },
        {
            'comment': {
                'comment_id': 1,
                'commented_by': {
                    'name': 'User_1',
                    'profile_pic': 'https://profile_pic_url1.com',
                    'user_id': 1
                },
                'content': 'comment_1',
                'post': {
                    'content': 'post_1',
                    'post_id': 1,
                    'posted_by': {
                        'name': 'User_1',
                        'profile_pic': 'https://profile_pic_url1.com',
                        'user_id': 1
                    }
                }
            },
            'post': None,
            'reaction': 'SAD',
            'reaction_id': 2,
            'reply': None
        },
        {
            'comment': {
                'comment_id': 2,
                'commented_by': {
                    'name': 'User_2',
                    'profile_pic': 'https://profile_pic_url2.com',
                    'user_id': 2
                },
                'content': 'comment_2',
                'post': {
                    'content': 'post_2',
                    'post_id': 2,
                    'posted_by': {
                        'name': 'User_2',
                        'profile_pic': 'https://profile_pic_url2.com',
                        'user_id': 2
                    }
                }
            },
            'post': None,
            'reaction': 'SAD',
            'reaction_id': 3,
            'reply': None
        }
    ]
}
