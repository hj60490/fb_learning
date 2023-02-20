# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestsGetAllReactionsPresenter.test_get_response_for_all_reactions_on_post 1'] = {
    'reactions_details': [
        {
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
            'reaction_id': 1
        }
    ]
}

snapshots['TestsGetAllReactionsPresenter.test_get_response_for_all_reactions_on_comment 1'] = {
    'reactions_details': [
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
            'reaction': 'SAD',
            'reaction_id': 1
        }
    ]
}

snapshots['TestsGetAllReactionsPresenter.test_get_response_for_all_reactions_on_reply 1'] = {
    'reactions_details': [
        {
            'reaction': 'SAD',
            'reaction_id': 1,
            'reply': {
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
                'commented_by': {
                    'name': 'User_1',
                    'profile_pic': 'https://profile_pic_url1.com',
                    'user_id': 1
                },
                'content': 'comment_2',
                'reply_id': 2
            }
        }
    ]
}
