from fb_post.interactors.storage_interfaces.post_interface import PostInterface
from fb_post.interactors.storage_interfaces.dtos import PostDto, ReactOnPostDto, \
    CommentOnPostDto, ReactionOnCommentDto, CommentOnCommentDto, UserDto
from typing import List
from fb_post.models.models import Post, Comment, React, User


class PostStorageImplementation(PostInterface):
    def create_post(self, content: str, user_id: int):
        Post.objects.create(content=content, posted_by_id=user_id)
        return

    def get_posts(self, user_id: int) -> List[PostDto]:
        post_objs = Post.objects.filter(posted_by_id=user_id)

        post_dtos = [
            self._convert_post_obj_to_dto(post)
            for post in post_objs
        ]

        return post_dtos

    @staticmethod
    def _convert_post_obj_to_dto(post: Post) -> PostDto:
        post_dto = PostDto(
            post_id=post.id,
            content=post.content,
            posted_by_id=post.posted_by.id,
            posted_at=post.posted_at
        )
        return post_dto

    @staticmethod
    def _get_user_dto_for_post(posted_by: User) -> UserDto:
        user = UserDto(
            user_id=posted_by.id,
            name=posted_by.name,
            profile_pic=posted_by.profile_pic
        )
        return user

    def get_all_reactions(self, list_of_post_id: List[int]) -> \
            List[ReactOnPostDto]:
        react_objs = React.objects.filter(post_id__in=list_of_post_id)

        reaction_on_post_dtos = [
            self._convert_react_obj_to_dto(react)
            for react in react_objs
        ]

        return reaction_on_post_dtos

    @staticmethod
    def _convert_react_obj_to_dto(react: React) -> \
            ReactOnPostDto:
        react_dto = ReactOnPostDto(
            reaction_id=react.id,
            post_id=react.post_id,
            reaction=react.reaction,
            reacted_at=react.reacted_at,
            reacted_by_id=react.reacted_by_id
        )

        return react_dto

    def get_comments(self, list_of_post_id: List[int]) -> \
            List[CommentOnPostDto]:
        comment_objs = Comment.objects.filter(post_id__in=list_of_post_id)

        comment_dtos = [
            self._convert_comment_obj_to_dto(comment)
            for comment in comment_objs
        ]

        return comment_dtos

    def _convert_comment_obj_to_dto(self, comment: Comment) -> \
            CommentOnPostDto:
        user = self._get_user_dto_for_comment(comment.commented_by)
        comment_dto = CommentOnPostDto(
            comment_id=comment.id,
            content=comment.content,
            commented_at=comment.commented_at,
            commented_by_id=comment.commented_by_id,
            post_id=comment.post_id
        )
        return comment_dto

    @staticmethod
    def _get_user_dto_for_comment(commented_by: User) -> UserDto:
        user = UserDto(
            user_id=commented_by.id,
            name=commented_by.name,
            profile_pic=commented_by.profile_pic
        )
        return user

    def get_reactions_on_comments(self, list_of_comment_id: List[int]) -> \
            List[ReactionOnCommentDto]:
        react_on_comments_objs = React.objects.filter(
            comment_id__in=list_of_comment_id)

        react_on_comment_dtos = [
            self._convert_comment_react_obj_to_dto(react)
            for react in react_on_comments_objs
        ]

        return react_on_comment_dtos

    @staticmethod
    def _convert_comment_react_obj_to_dto(react: React) -> \
            ReactionOnCommentDto:
        react_on_comment_dto = ReactionOnCommentDto(
            reaction_id=react.id,
            comment_id=react.comment_id,
            reaction=react.reaction,
            reacted_at=react.reacted_at,
            reacted_by_id=react.reacted_by_id

        )
        return react_on_comment_dto

    def get_replies_on_comment(self, list_of_comment_id) -> \
            List[CommentOnCommentDto]:
        comment_on_comment_obj = Comment.objects.filter(
            parent_comment_id__in=list_of_comment_id)

        replies_dtos = [
            self._convert_replies_obj_to_dto(comment)
            for comment in comment_on_comment_obj
        ]

        return replies_dtos

    @staticmethod
    def _convert_replies_obj_to_dto(comment: Comment) \
            -> CommentOnCommentDto:
        reply_dto = CommentOnCommentDto(
            comment_id=comment.id,
            content=comment.content,
            commented_at=comment.commented_at,
            commented_by_id=comment.commented_by_id,
            parent_comment_id=comment.parent_comment_id
        )
        return reply_dto
