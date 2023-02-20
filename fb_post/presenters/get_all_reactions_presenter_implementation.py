from typing import List

from django_swagger_utils.drf_server.exceptions import BadRequest

from fb_post.adapters.dtos import UserDto
from fb_post.constants.exception_messages import INVALID_LIMIT_LENGTH
from fb_post.interactors.presenter_interfaces.get_all_reaction_presenter_interface import \
    GetAllReactionsPresenterInterface
from fb_post.interactors.storage_interfaces.dtos import PostDto, CommentDTO
from fb_post_auth.constants.exception_messages import INVALID_OFFSET_LENGTH


class GetAllReactionsPresenterImplementation(GetAllReactionsPresenterInterface):

    def raise_exception_for_invalid_limit_length(self):
        raise BadRequest(*INVALID_LIMIT_LENGTH)

    def raise_exception_for_invalid_offset_length(self):
        raise BadRequest(*INVALID_OFFSET_LENGTH)

    def get_response_for_all_reactions(self, reactions_details):
        users_dict = self._make_users_details_dict(reactions_details.users)
        posts_dict = self._make_posts_details_dict(
            reactions_details.posts, users_dict
        )
        comments_dict = self._make_comments_dict(
            reactions_details.comments, users_dict, posts_dict
        )

        replies_dict = self._make_replies_dict(
            reactions_details.comments, users_dict, comments_dict
        )

        list_of_reactions = []
        for reaction in reactions_details.reactions:
            if reaction.post_id:
                list_of_reactions.append({
                    "reaction_id": reaction.reaction_id,
                    "reaction": reaction.reaction,
                    "post": posts_dict[reaction.post_id]
                })
            else:
                if reaction.comment_id in comments_dict:
                    list_of_reactions.append({
                        "reaction_id": reaction.reaction_id,
                        "reaction": reaction.reaction,
                        "comment": comments_dict[reaction.comment_id]
                    })
                else:

                    list_of_reactions.append({
                        "reaction_id": reaction.reaction_id,
                        "reaction": reaction.reaction,
                        "reply": replies_dict[reaction.comment_id]
                    })

        return {
            "reactions_details": list_of_reactions
        }

    @staticmethod
    def _make_users_details_dict(users: List[UserDto]):
        dict_of_users = {}
        for user in users:
            if user.user_id not in dict_of_users:
                dict_of_users[user.user_id] = {
                    "name": user.name,
                    "user_id": user.user_id,
                    "profile_pic": user.profile_pic
                }
        return dict_of_users

    @staticmethod
    def _make_posts_details_dict(posts: List[PostDto], users_dict):
        dict_of_posts = {}
        for post in posts:
            if post.post_id not in dict_of_posts:
                dict_of_posts[post.post_id] = {
                    "post_id": post.post_id,
                    "content": post.content,
                    "posted_by": users_dict[post.posted_by_id]
                }
        return dict_of_posts

    @staticmethod
    def _make_comments_dict(comments: List[CommentDTO], users_dict, posts_dict):
        dict_of_comments = {}
        for comment in comments:
            if comment.post_id:
                dict_of_comments[comment.comment_id] = {
                    "comment_id": comment.comment_id,
                    "content": comment.content,
                    "commented_by": users_dict[comment.commented_by_id],
                    "post": posts_dict[comment.post_id]
                }
        return dict_of_comments

    @staticmethod
    def _make_replies_dict(
            comments: List[CommentDTO], users_dict, comments_dict
    ):
        dict_of_replies = {}
        for comment in comments:
            if comment.parent_comment_id:
                dict_of_replies[comment.comment_id] = {
                    "reply_id": comment.comment_id,
                    "content": comment.content,
                    "commented_by": users_dict[comment.commented_by_id],
                    "comment": comments_dict[comment.parent_comment_id]
                }
        return dict_of_replies




