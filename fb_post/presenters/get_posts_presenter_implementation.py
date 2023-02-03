from fb_post.interactors.presenter_interfaces.get_posts_presenter_interface \
    import GetPostsPresenterInterface
from django_swagger_utils.drf_server.exceptions import (
    BadRequest
)
from fb_post.constants.exception_messages import INVALID_USER_ID
from fb_post.interactors.presenter_interfaces.dtos import PostDetailsDto


class GetPostsPresenterImplementation(GetPostsPresenterInterface):

    def raise_exception_for_user_not_exist(self):
        raise BadRequest(*INVALID_USER_ID)

    @staticmethod
    def get_reactions_dict(reactions):
        reaction_types = [reaction.reaction for reaction in reactions]
        set(reaction_types)
        list(reaction_types)
        reactions_dict = {
            "count": len(reactions),
            "type": reaction_types
        }
        return reactions_dict

    def get_comments_dict(self, comments_on_post, replies, reaction_on_comments):
        list_of_comments = []
        for comment in comments_on_post:
            comment_dict = {
                "commend_id": comment.comment_id,
                "commentator": {
                    "user_id": comment.commented_by.user_id,
                    "name": comment.commented_by.name,
                    "profile_pic": comment.commented_by.profile_pic
                },
                "commented_at": comment.commented_at,
                "comment_content": comment.content,
                "reactions": self.get_reactions_dict(reaction_on_comments)

            }

    def get_all_post_of_user(self, posts_details_dto: PostDetailsDto):
        posts = posts_details_dto.post_dto_list
        reactions_on_post = posts_details_dto.reaction_post_dto_list
        comments_on_post = posts_details_dto.comment_on_post_dto_list
        replies = posts_details_dto.replies_dto_list
        reaction_on_comments = posts_details_dto.reaction_on_comment_dto

        list_of_post = []
        for post in posts:
            post_dict = {
                "post_id": post.post_id,
                "posted_by": {
                    "user_id": post.posted_by.user_id,
                    "name": post.posted_by.name,
                    "profile_pic": post.posted_by.profile_pic
                },
                "posted_at": post.posted_at,
                "post_content": post.content,
                "reactions": self.get_reactions_dict(
                    reactions_on_post),
                "comments": self.get_comments_dict(comments_on_post, replies,
                                                   reaction_on_comments),
                "comments_count": len(comments_on_post)
            }
            list_of_post.append(post_dict)
        return list_of_post


