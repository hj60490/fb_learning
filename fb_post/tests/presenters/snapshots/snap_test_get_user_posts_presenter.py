# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_get_all_posts_of_user_for_user_having_zero_post_return_empty 1'] = {
    'user_posts_details': [
    ]
}

snapshots['test_get_all_posts_of_user_for_user_having_post_but_no_reaction_and_comments 1'] = {
    'user_posts_details': [
        {
            'comments': [
            ],
            'comments_count': 0,
            'post_content': 'hello',
            'post_id': 1,
            'posted_at': '2023-02-13 11:20:00',
            'posted_by': {
                'name': 'harsh',
                'profile_pic': 'www.google.com',
                'user_id': 5
            },
            'reactions': {
                'count': 0,
                'types': [
                ]
            }
        }
    ]
}

snapshots['test_get_all_posts_of_user_for_user_having_posts_only_reactions 1'] = {
    'user_posts_details': [
        {
            'comments': [
            ],
            'comments_count': 0,
            'post_content': 'hello',
            'post_id': 1,
            'posted_at': '2023-02-13 11:20:00',
            'posted_by': {
                'name': 'harsh',
                'profile_pic': 'www.google.com',
                'user_id': 5
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

snapshots['test_get_all_posts_of_user_for_user_having_posts_only_comments 1'] = {
    'user_posts_details': [
        {
            'comments': [
                {
                    'comment_content': 'comment',
                    'comment_id': 1,
                    'commentator': {
                        'name': 'harsh',
                        'profile_pic': 'www.google.com',
                        'user_id': 5
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
            'post_content': 'hello',
            'post_id': 1,
            'posted_at': '2023-02-13 11:20:00',
            'posted_by': {
                'name': 'harsh',
                'profile_pic': 'www.google.com',
                'user_id': 5
            },
            'reactions': {
                'count': 0,
                'types': [
                ]
            }
        }
    ]
}

snapshots['test_get_all_posts_of_user_for_user_having_posts_only_comments_and_replies 1'] = {
    'user_posts_details': [
        {
            'comments': [
                {
                    'comment_content': 'comment',
                    'comment_id': 1,
                    'commentator': {
                        'name': 'harsh',
                        'profile_pic': 'www.google.com',
                        'user_id': 5
                    },
                    'commented_at': '2023-02-13 11:20:00',
                    'reactions': {
                        'count': 0,
                        'types': [
                        ]
                    },
                    'replies': [
                        {
                            'comment_content': 'reply',
                            'comment_id': 2,
                            'commentator': {
                                'name': 'harsh',
                                'profile_pic': 'www.google.com',
                                'user_id': 5
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
            'post_content': 'hello',
            'post_id': 1,
            'posted_at': '2023-02-13 11:20:00',
            'posted_by': {
                'name': 'harsh',
                'profile_pic': 'www.google.com',
                'user_id': 5
            },
            'reactions': {
                'count': 0,
                'types': [
                ]
            }
        }
    ]
}

snapshots['test_get_all_posts_of_user_for_user_having_posts_only_comments_with_reaction_and_replies 1'] = {
    'user_posts_details': [
        {
            'comments': [
                {
                    'comment_content': 'comment',
                    'comment_id': 1,
                    'commentator': {
                        'name': 'harsh',
                        'profile_pic': 'www.google.com',
                        'user_id': 5
                    },
                    'commented_at': '2023-02-13 11:20:00',
                    'reactions': {
                        'count': 1,
                        'types': [
                            'WOW'
                        ]
                    },
                    'replies': [
                        {
                            'comment_content': 'reply',
                            'comment_id': 2,
                            'commentator': {
                                'name': 'harsh',
                                'profile_pic': 'www.google.com',
                                'user_id': 5
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
            'post_content': 'hello',
            'post_id': 1,
            'posted_at': '2023-02-13 11:20:00',
            'posted_by': {
                'name': 'harsh',
                'profile_pic': 'www.google.com',
                'user_id': 5
            },
            'reactions': {
                'count': 0,
                'types': [
                ]
            }
        }
    ]
}

snapshots['test_get_all_posts_of_user_return_posts_dict 1'] = {
    'user_posts_details': [
        {
            'comments': [
                {
                    'comment_content': 'comment',
                    'comment_id': 1,
                    'commentator': {
                        'name': 'harsh',
                        'profile_pic': 'www.google.com',
                        'user_id': 5
                    },
                    'commented_at': '2023-02-13 11:20:00',
                    'reactions': {
                        'count': 1,
                        'types': [
                            'WOW'
                        ]
                    },
                    'replies': [
                        {
                            'comment_content': 'reply',
                            'comment_id': 2,
                            'commentator': {
                                'name': 'harsh',
                                'profile_pic': 'www.google.com',
                                'user_id': 5
                            },
                            'commented_at': '2023-02-13 11:20:00',
                            'reactions': {
                                'count': 1,
                                'types': [
                                    'SAD'
                                ]
                            }
                        }
                    ]
                }
            ],
            'comments_count': 1,
            'post_content': 'hello',
            'post_id': 1,
            'posted_at': '2023-02-13 11:20:00',
            'posted_by': {
                'name': 'harsh',
                'profile_pic': 'www.google.com',
                'user_id': 5
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
