from fb_post.interactors.storage_interfaces.post_interface import PostInterface
from fb_post.interactors.storage_interfaces.dtos import PostDto, ReactOnPostDto, \
    CommentOnPostDto, ReactionOnCommentDto, CommentOnCommentDto, UserDto, \
    RequestsParametersDTO
from typing import List
from fb_post.models.models import Post, Comment, React


class PostStorageImplementation(PostInterface):
    def create_post(self, content: str, user_id: int):
        Post.objects.create(content=content, posted_by_id=user_id)
        return

    def get_posts(
            self, user_id: int, requests_parameters_dto: RequestsParametersDTO
    ) -> List[PostDto]:
        limit = requests_parameters_dto.limit
        offset = requests_parameters_dto.offset
        sort_order = requests_parameters_dto.sort_order
        post_content = requests_parameters_dto.post_content

        posts_objs = Post.objects.filter(posted_by_id=user_id)
        if post_content:
            posts_objs = posts_objs.filter(content__icontains=post_content)

        if sort_order:
            if sort_order == "ASC":
                posts_objs = posts_objs.order_by('posted_at')
            else:
                posts_objs = posts_objs.order_by('-posted_at')

        posts_objs = posts_objs[offset: limit+offset]

        post_dtos = [
            self._convert_post_obj_to_dto(post)
            for post in posts_objs
        ]
        return post_dtos

    @staticmethod
    def _convert_post_obj_to_dto(post: Post) -> PostDto:
        post_dto = PostDto(
            post_id=post.id,
            content=post.content,
            posted_by_id=post.posted_by_id,
            posted_at=post.posted_at
        )
        return post_dto


    def get_all_reactions(self, list_of_post_id: List[int]) -> \
            List[ReactOnPostDto]:
        react_objs = React.objects.filter(post_id__in=list_of_post_id)

        reaction_on_post = [
            self._convert_react_obj_to_dto(react)
            for react in react_objs
        ]

        return reaction_on_post

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

    @staticmethod
    def _convert_comment_obj_to_dto(comment: Comment) -> \
            CommentOnPostDto:
        comment_dto = CommentOnPostDto(
            comment_id=comment.id,
            content=comment.content,
            commented_at=comment.commented_at,
            commented_by_id=comment.commented_by_id,
            post_id=comment.post_id
        )
        return comment_dto

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

    # todo: tests
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

