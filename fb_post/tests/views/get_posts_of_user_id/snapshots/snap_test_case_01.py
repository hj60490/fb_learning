# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetPostsOfUserIdAPITestCase.test_case status_code'] = '200'

snapshots['TestCase01GetPostsOfUserIdAPITestCase.test_case body'] = [
    {
        'comments': [
            {
                'comment_content': 'string',
                'comment_id': 1,
                'commentator': {
                    'name': 'string',
                    'profile_pic': 'string',
                    'user_id': 1
                },
                'commented_at': '2099-12-31 00:00:00',
                'reactions': {
                    'count': 1,
                    'types': [
                        'string'
                    ]
                },
                'replies': [
                    {
                        'comment_content': 'string',
                        'comment_id': 1,
                        'commentator': {
                            'name': 'string',
                            'profile_pic': 'string',
                            'user_id': 1
                        },
                        'commented_at': '2099-12-31 00:00:00',
                        'reactions': {
                            'count': 1,
                            'types': [
                                'string'
                            ]
                        }
                    }
                ]
            }
        ],
        'comments_count': 1,
        'post_content': 'string',
        'post_id': 1,
        'posted_at': '2099-12-31 00:00:00',
        'posted_by': {
            'name': 'string',
            'profile_pic': 'string',
            'user_id': 1
        },
        'reactions': {
            'count': 1,
            'types': [
                'string'
            ]
        }
    }
]
