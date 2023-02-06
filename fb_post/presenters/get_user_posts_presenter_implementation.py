from fb_post.interactors.presenter_interfaces.get_user_posts_presenter_interface \
    import GetPostsPresenterInterface
from django_swagger_utils.drf_server.exceptions import (
    BadRequest
)
from fb_post.constants.exception_messages import INVALID_USER_ID
from fb_post.interactors.presenter_interfaces.dtos import PostDetailsDto
from typing import List
from fb_post.interactors.storage_interfaces.dtos import PostDto, ReactOnPostDto, \
    CommentOnPostDto, CommentOnCommentDto, ReactionOnCommentDto


class GetUserPostsPresenterImplementation(GetPostsPresenterInterface):

    def raise_exception_for_user_not_exist(self):
        raise BadRequest(*INVALID_USER_ID)

    def get_all_post_of_user(self, posts_details_dto: PostDetailsDto):
        users = posts_details_dto.users
        posts = posts_details_dto.posts
        reactions_on_post = posts_details_dto.reactions_on_posts
        comments_on_post = posts_details_dto.comments_on_post
        replies = posts_details_dto.replies
        reaction_on_comments = posts_details_dto.reactions_on_comments

        users_details_dict = self._make_users_details_dict(users)

        list_of_post_dict = [
            self._get_dict_for_post_details(post_dto, reactions_on_post,
                                            comments_on_post, replies,
                                            reaction_on_comments,
                                            users_details_dict)
            for post_dto in posts
        ]

        return list_of_post_dict

    @staticmethod
    def _make_users_details_dict(users):
        dict_of_users = {}
        for user in users:
            if user.user_id not in dict_of_users:
                dict_of_users[user.user_id] = {
                    "user_id": user.user_id,
                    "name": user.name,
                    "profile_pic": user.profile_pic
                }
        return dict_of_users

    def _get_dict_for_post_details(self, post_dto: PostDto,
                                   reactions_on_post_dtos_list: List[
                                       ReactOnPostDto],
                                   comments_on_post: List[CommentOnPostDto],
                                   replies: List[CommentOnCommentDto],
                                   reaction_on_comments: List[
                                       ReactionOnCommentDto],
                                   users_details_dict):
        # print("*****************")
        # print(users_details_dict[post_dto.posted_by_id])
        post_dict = {
            "post_id": post_dto.post_id,
            "posted_by": users_details_dict[post_dto.posted_by_id],
            "posted_at": post_dto.posted_at,
            "post_content": post_dto.content,
            "reactions": self._get_reactions_dict(
                reactions_on_post_dtos_list, post_dto),
            "comments": self._get_comments_list(comments_on_post, replies,
                                                reaction_on_comments, post_dto,
                                                users_details_dict),
        }
        post_dict['comments_count'] = len(post_dict['comments'])
        # print("***************** THIS IS REPLY v1*********************")
        # print(post_dto.post_id)
        # print(len(replies))
        return post_dict

    def _get_comments_list(self, comments_on_post, replies,
                           reaction_on_comments, post_dto, users_details_dict):
        # print("***************** THIS IS REPLY v2*********************")
        # print(len(replies))
        list_of_comments = [
            self._prepare_comments_list_of_dict(comment_dto,
                                                reaction_on_comments, replies,
                                                users_details_dict)
            for comment_dto in comments_on_post if
            comment_dto.post_id == post_dto.post_id
        ]
        return list_of_comments

    def _prepare_comments_list_of_dict(self, comment_dto, reaction_on_comments,
                                       replies, users_details_list):
        comment_dict = {
            "comment_id": comment_dto.comment_id,
            "commentator": users_details_list[comment_dto.commented_by_id],
            "commented_at": comment_dto.commented_at,
            "comment_content": comment_dto.content,
            "reactions": self._get_reactions_dict_of_comments(
                reaction_on_comments, comment_dto),
            "replies": self._get_list_of_replies(replies, comment_dto,
                                                 reaction_on_comments,
                                                 users_details_list)
        }
        # print("***************** THIS IS REPLY *********************")
        # print(len(replies))
        return comment_dict

    @staticmethod
    def _get_reactions_dict(reactions_on_post: List[ReactOnPostDto],
                            post_dto: PostDto):
        reaction_type_set = set()
        reactions_count = 0
        for reaction in reactions_on_post:
            if reaction.post_id == post_dto.post_id:
                reactions_count += 1
                reaction_type_set.add(reaction.reaction)
        list_of_types = list(reaction_type_set)
        reactions_dict = {
            "count": reactions_count,
            "types": list_of_types
        }
        # if not len(list_of_types):
        #     reactions_dict['types'] = []
        return reactions_dict

    @staticmethod
    def _get_reactions_dict_of_comments(reaction_on_comments,
                                        comment_dto):
        reaction_type_set = set()
        reactions_count = 0
        # print("*******************")
        for reaction_dto in reaction_on_comments:
            if reaction_dto.comment_id == comment_dto.comment_id:
                reactions_count += 1
                reaction_type_set.add(reaction_dto.reaction)
                # print("*******************")
                # print(reaction_dto.reaction)
        list_of_types = list(reaction_type_set)
        reactions_dict = {
            "count": reactions_count,
            "types": list_of_types
        }
        if not len(list_of_types):
            reactions_dict['types'] = []
        return reactions_dict

    def _get_list_of_replies(self, replies, comment_dto, reaction_on_comment,
                             users_details_list):
        list_of_replies = [
            self._prepare_replies_list_of_dict(reply,
                                               comment_dto, reaction_on_comment,
                                               users_details_list)
            for reply in replies if reply.parent_comment_id == comment_dto.comment_id
        ]
        print("***************** THIS IS REPLY *********************")
        print(list_of_replies)

        return list_of_replies

    def _prepare_replies_list_of_dict(self,
                                      reply: CommentOnCommentDto,
                                      comment_dto,
                                      reaction_on_comments, users_details_list):
        reply_dict = {
            "comment_id": reply.comment_id,
            "commentator": users_details_list[
                reply.commented_by_id],
            "commented_at": comment_dto.commented_at,
            "comment_content": comment_dto.content,
            "reactions": self._get_reactions_dict_of_replies(
                reaction_on_comments, reply)
        }
        # print("***************** THIS IS REPLY *********************")
        # print(reply_dict)
        return reply_dict

    @staticmethod
    def _get_reactions_dict_of_replies(reaction_on_comments,
                                       comment_on_comment):
        reaction_type_set = set()
        reactions_count = 0
        for reaction_dto in reaction_on_comments:
            if reaction_dto.comment_id == comment_on_comment.comment_id:
                reactions_count += 1
                reaction_type_set.add(reaction_dto.reaction)
                print(len(reaction_type_set))
                print("******************")
        list_of_types = list(reaction_type_set)
        reactions_dict = {
            "count": len(reaction_on_comments),
            "types": list_of_types
        }
        if not len(reaction_type_set):
            reactions_dict['types'] = []
        return reactions_dict
