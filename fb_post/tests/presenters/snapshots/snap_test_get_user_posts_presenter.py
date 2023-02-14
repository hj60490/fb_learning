# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestsCreatePostPresenter.test_get_all_posts_of_user_for_user_having_zero_post_return_empty 1'] = {
    'user_posts_details': [
    ]
}

snapshots['TestsCreatePostPresenter.test_get_all_posts_of_user_for_user_having_post_but_no_reaction_and_comments 1'] = {
    'user_posts_details': [
        {
            'comments': [
            ],
            'comments_count': 0,
            'post_content': 'post_1',
            'post_id': 1,
            'posted_at': '2023-02-13 11:20:00',
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

snapshots['TestsCreatePostPresenter.test_get_all_posts_of_user_for_user_having_posts_only_reactions 1'] = {
    'user_posts_details': [
        {
            'comments': [
            ],
            'comments_count': 0,
            'post_content': 'post_1',
            'post_id': 1,
            'posted_at': '2023-02-13 11:20:00',
            'posted_by': {
                'name': 'User_1',
                'profile_pic': 'https://profile_pic_url1.com',
                'user_id': 1
            },
            'reactions': {
                'count': 1,
                'types': [
                    'HAHA'
                ]
            }
        }
    ]
}

snapshots['TestsCreatePostPresenter.test_get_all_posts_of_user_for_user_having_posts_only_comments 1'] = {
    'user_posts_details': [
        {
            'comments': [
                {
                    'comment_content': 'comment_1',
                    'comment_id': 1,
                    'commentator': {
                        'name': 'User_1',
                        'profile_pic': 'https://profile_pic_url1.com',
                        'user_id': 1
                    },
                    'commented_at': '2023-02-13 11:20:00',
                    'reactions': {
                        'count': 0,
                        'types': [
                        ]
                    },
                    'replies': [
                    ]
                }
            ],
            'comments_count': 1,
            'post_content': 'post_1',
            'post_id': 1,
            'posted_at': '2023-02-13 11:20:00',
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

snapshots['TestsCreatePostPresenter.test_get_all_posts_of_user_for_user_having_posts_only_comments_and_replies 1'] = {
    'user_posts_details': [
        {
            'comments': [
                {
                    'comment_content': 'comment_1',
                    'comment_id': 1,
                    'commentator': {
                        'name': 'User_1',
                        'profile_pic': 'https://profile_pic_url1.com',
                        'user_id': 1
                    },
                    'commented_at': '2023-02-13 11:20:00',
                    'reactions': {
                        'count': 0,
                        'types': [
                        ]
                    },
                    'replies': [
                        {
                            'comment_content': 'comment_1',
                            'comment_id': 1,
                            'commentator': {
                                'name': 'User_1',
                                'profile_pic': 'https://profile_pic_url1.com',
                                'user_id': 1
                            },
                            'commented_at': '2023-02-13 11:20:00',
                            'reactions': {
                                'count': 0,
                                'types': [
                                ]
                            }
                        }
                    ]
                }
            ],
            'comments_count': 1,
            'post_content': 'post_1',
            'post_id': 1,
            'posted_at': '2023-02-13 11:20:00',
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

snapshots['TestsCreatePostPresenter.test_get_all_posts_of_user_for_user_having_posts_only_comments_with_reaction_and_replies 1'] = {
    'user_posts_details': [
        {
            'comments': [
                {
                    'comment_content': 'comment_1',
                    'comment_id': 1,
                    'commentator': {
                        'name': 'User_1',
                        'profile_pic': 'https://profile_pic_url1.com',
                        'user_id': 1
                    },
                    'commented_at': '2023-02-13 11:20:00',
                    'reactions': {
                        'count': 1,
                        'types': [
                            'HAHA'
                        ]
                    },
                    'replies': [
                        {
                            'comment_content': 'comment_1',
                            'comment_id': 1,
                            'commentator': {
                                'name': 'User_1',
                                'profile_pic': 'https://profile_pic_url1.com',
                                'user_id': 1
                            },
                            'commented_at': '2023-02-13 11:20:00',
                            'reactions': {
                                'count': 1,
                                'types': [
                                    'HAHA'
                                ]
                            }
                        }
                    ]
                }
            ],
            'comments_count': 1,
            'post_content': 'post_1',
            'post_id': 1,
            'posted_at': '2023-02-13 11:20:00',
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

snapshots['TestsCreatePostPresenter.test_get_all_posts_of_user_return_posts_dict 1'] = {
    'user_posts_details': [
        {
            'comments': [
                {
                    'comment_content': 'comment_1',
                    'comment_id': 1,
                    'commentator': {
                        'name': 'User_1',
                        'profile_pic': 'https://profile_pic_url1.com',
                        'user_id': 1
                    },
                    'commented_at': '2023-02-13 11:20:00',
                    'reactions': {
                        'count': 1,
                        'types': [
                            'HAHA'
                        ]
                    },
                    'replies': [
                        {
                            'comment_content': 'comment_1',
                            'comment_id': 1,
                            'commentator': {
                                'name': 'User_1',
                                'profile_pic': 'https://profile_pic_url1.com',
                                'user_id': 1
                            },
                            'commented_at': '2023-02-13 11:20:00',
                            'reactions': {
                                'count': 1,
                                'types': [
                                    'HAHA'
                                ]
                            }
                        }
                    ]
                }
            ],
            'comments_count': 1,
            'post_content': 'post_1',
            'post_id': 1,
            'posted_at': '2023-02-13 11:20:00',
            'posted_by': {
                'name': 'User_1',
                'profile_pic': 'https://profile_pic_url1.com',
                'user_id': 1
            },
            'reactions': {
                'count': 1,
                'types': [
                    'HAHA'
                ]
            }
        }
    ]
}
