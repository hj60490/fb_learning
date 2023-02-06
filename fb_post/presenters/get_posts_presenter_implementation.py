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

    def _get_reactions_dict(self, reactions_on_post_dtos_list, post_dto):
        reaction_type_set = set()
        for reaction_dto in reactions_on_post_dtos_list:
            if reaction_dto.post_id == post_dto.post_id:
                reaction_type_set.add(reaction_dto.reaction)

        reactions_dict = {
            "count": len(reactions_on_post_dtos_list),
            "type": list(reaction_type_set)
        }
        return reactions_dict

    def _get_reactions_dict_of_comments(self, reaction_on_comments, comment_dto):
        reaction_type_set = set()
        for reaction_dto in reaction_on_comments:
            if reaction_dto.comment_id == comment_dto.comment_id:
                reaction_type_set.add(reaction_dto.reaction)

        reactions_dict = {
            "count": len(reaction_on_comments),
            "type": list(reaction_type_set)
        }
        return reactions_dict



    def _prepare_comments_list_of_dict(self, comment_dto, replies, reaction_on_comments,
                                       post_dto):
        comment_dict = {
            "commend_id": comment_dto.comment_id,
            "commentator": {
                "user_id": comment_dto.commented_by.user_id,
                "name": comment_dto.commented_by.name,
                "profile_pic": comment_dto.commented_by.profile_pic
            },
            "commented_at": comment_dto.commented_at,
            "comment_content": comment_dto.content,
            "reactions": self._get_reactions_dict_of_comments(reaction_on_comments, comment_dto),
            "replies": self._get_list_of_replies(replies, comment_dto)

        }
        return comment_dict

    def _get_comments_list(self, comments_on_post, replies, reaction_on_comments, postdto):
        list_of_comments = [
            self._prepare_comments_list_of_dict(comment_dto,reaction_on_comments, replies)
            for comment_dto in comments_on_post if comment_dto.post_id == postdto.post_id
        ]

        return list_of_comments

    def _get_dict_for_post_details(self, post_dto, reactions_on_post_dtos_list, comments_on_post,
                                   replies, reaction_on_comments):
        post_dict = {
            "post_id": post_dto.post_id,
            "posted_by": {
                "user_id": post_dto.posted_by.user_id,
                "name": post_dto.posted_by.name,
                "profile_pic": post_dto.posted_by.profile_pic
            },
            "posted_at": post_dto.posted_at,
            "post_content": post_dto.content,
            "reactions": self._get_reactions_dict(
                reactions_on_post_dtos_list, post_dto),
            "comments": self._get_comments_list(comments_on_post, replies,
                                                reaction_on_comments, post_dto),
            "comments_count": len(comments_on_post)
        }
        return post_dict

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