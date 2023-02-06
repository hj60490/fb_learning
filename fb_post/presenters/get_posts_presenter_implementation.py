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

    def get_all_post_of_user(self, posts_details_dto: PostDetailsDto):

        posts_dto_list = posts_details_dto.post_dto_list
        reactions_on_post = posts_details_dto.reaction_post_dto_list
        comments_on_post = posts_details_dto.comment_on_post_dto_list
        replies = posts_details_dto.replies_dto_list
        reaction_on_comments = posts_details_dto.reaction_on_comment_dto

        list_of_post_dict = [
            self._get_dict_for_post_details(post_dto, reactions_on_post, comments_on_post,
                                            replies, reaction_on_comments)
            for post_dto in posts_dto_list
        ]

        return list_of_post_dict

    def _get_dict_for_post_details(self,
                                   post_dto, reactions_on_post_dtos_list,
                                   comments_on_post, replies,
                                   reaction_on_comments):
        post_dict = {
            "post_id": post_dto.post_id,
            "posted_by": {
                "name": post_dto.posted_by.name,
                "user_id": post_dto.posted_by.id,
                "profile_pic": post_dto.posted_by.profile_pic
            },
            "posted_at": post_dto.posted_at,
            "post_content": post_dto.content,
            "reactions": self._get_reactions_dict(
                reactions_on_post_dtos_list, post_dto),
            "comments": self._get_comments_list(comments_on_post, replies,
                                                reaction_on_comments, post_dto),
        }
        post_dict['comments_count'] = len(post_dict['comments'])
        # print("***************** THIS IS REPLY v1*********************")
        # print(post_dto.post_id)
        # print(len(replies))
        return post_dict

    def _get_comments_list(self, comments_on_post, replies,
                           reaction_on_comments, post_dto):
        # print("***************** THIS IS REPLY v2*********************")
        # print(len(replies))
        list_of_comments = [
            self._prepare_comments_list_of_dict(comment_dto,
                                                reaction_on_comments, replies)
            for comment_dto in comments_on_post if
            comment_dto.post_id == post_dto.post_id
        ]
        return list_of_comments

    def _prepare_comments_list_of_dict(self, comment_dto, reaction_on_comments,
                                       replies):
        comment_dict = {
            "comment_id": comment_dto.comment_id,
            "commentator": {
                "user_id": comment_dto.commented_by.id,
                "name": comment_dto.commented_by.name,
                "profile_pic": comment_dto.commented_by.profile_pic
            },
            "commented_at": comment_dto.commented_at,
            "comment_content": comment_dto.content,
            "reactions": self._get_reactions_dict_of_comments(
                reaction_on_comments, comment_dto),
            "replies": self._get_list_of_replies(replies, comment_dto,
                                                 reaction_on_comments)
        }
        # print("***************** THIS IS REPLY *********************")
        # print(len(replies))
        return comment_dict

    @staticmethod
    def _get_reactions_dict(reactions_on_post_dtos_list, post_dto):
        reaction_type_set = set()
        for reaction_dto in reactions_on_post_dtos_list:
            if reaction_dto.post_id == post_dto.post_id:
                reaction_type_set.add(reaction_dto.reaction)
        list_of_types = list(reaction_type_set)
        reactions_dict = {
            "count": len(reactions_on_post_dtos_list),
            "types": list_of_types
        }
        if not len(list_of_types):
            reactions_dict['types'] = []
        return reactions_dict

    @staticmethod
    def _get_reactions_dict_of_comments(reaction_on_comments, comment_dto):
        reaction_type_set = set()
        for reaction_dto in reaction_on_comments:
            if reaction_dto.comment_id == comment_dto.comment_id:
                reaction_type_set.add(reaction_dto.reaction)
        list_of_types = list(reaction_type_set)
        reactions_dict = {
            "count": len(reaction_on_comments),
            "type": list_of_types
        }
        return reactions_dict

    def _get_list_of_replies(self, replies, comment_dto, reaction_on_comment):
        list_of_replies = [
            self._prepare_replies_list_of_dict(comment_on_comment,
                                               comment_dto, reaction_on_comment)
            for comment_on_comment in replies
            if comment_on_comment.parent_comment_id == comment_dto.comment_id
        ]
        # print("***************** THIS IS REPLY *********************")
        # print(list_of_replies)

        return list_of_replies

    def _prepare_replies_list_of_dict(self, comment_on_comment, comment_dto,
                                      reaction_on_comments):
        reply_dict = {
            "comment_id": comment_on_comment.comment_id,
            "commentator": {
                "user_id": comment_dto.commented_by.id,
                "name": comment_dto.commented_by.name,
                "profile_pic": comment_dto.commented_by.profile_pic
            },
            "commented_at": comment_dto.commented_at,
            "comment_content": comment_dto.content,
            "reactions": self._get_reactions_dict_of_replies(
                reaction_on_comments, comment_on_comment)
        }
        # print("***************** THIS IS REPLY *********************")
        # print(reply_dict)
        return reply_dict

    @staticmethod
    def _get_reactions_dict_of_replies(reaction_on_comments,
                                       comment_on_comment):
        reaction_type_set = set()
        for reaction_dto in reaction_on_comments:
            if reaction_dto.comment_id == comment_on_comment.comment_id:
                reaction_type_set.add(reaction_dto.reaction)
        list_of_types = list(reaction_type_set)
        reactions_dict = {
            "count": len(reaction_on_comments),
            "type": list_of_types
        }
        return reactions_dict

