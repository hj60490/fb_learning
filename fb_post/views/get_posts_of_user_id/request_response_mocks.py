


RESPONSE_200_JSON = """
{
    "user_posts_details": [
        {
            "post_id": 1,
            "posted_by": {
                "name": "string",
                "user_id": 1,
                "profile_pic": "string"
            },
            "posted_at": "2099-12-31 00:00:00",
            "post_content": "string",
            "reactions": {
                "count": 1,
                "types": [
                    "string"
                ]
            },
            "comments": [
                {
                    "comment_id": 1,
                    "commentator": {
                        "name": "string",
                        "user_id": 1,
                        "profile_pic": "string"
                    },
                    "commented_at": "2099-12-31 00:00:00",
                    "comment_content": "string",
                    "reactions": {
                        "count": 1,
                        "types": [
                            "string"
                        ]
                    },
                    "replies_ids": [
                        1
                    ]
                }
            ],
            "comments_count": 1
        }
    ]
}
"""

