from typing import List

from fb_post.exceptions.custom_exceptions import InvalidLimitValue, \
    InvalidOffsetValue
from fb_post.interactors.storage_interfaces.dtos import ReactionDTO, CommentDTO, \
    PostDto
from fb_post.interactors.storage_interfaces.reaction_storage_interface import \
    ReactionStorageInterface
from fb_post.interactors.storage_interfaces.comment_storage_interface import \
    CommentStorageInterface
from fb_post.interactors.storage_interfaces.post_storage_interface import \
    PostInterface
from fb_post.interactors.presenter_interfaces.get_all_reaction_presenter_interface import \
    GetAllReactionsPresenterInterface


class GetAllReactionsInteractor:
    def __init__(
            self, post_storage: PostInterface,
            reaction_storage: ReactionStorageInterface,
            comment_storage: CommentStorageInterface,
            presenter: GetAllReactionsPresenterInterface
    ):
        self.post_storage = post_storage
        self.reaction_storage = reaction_storage
        self.comment_storage = comment_storage
        self.presenter = presenter

    def get_all_reactions_wrapper(self, limit: int, offset: int):
        try:
            reactions_details = self.get_all_reactions(
                limit=limit, offset=offset
            )

            return self.presenter.get_response_for_all_reactions(
                reactions_details
            )
        except InvalidLimitValue:
            self.presenter.raise_exception_for_invalid_limit_length()
        except InvalidOffsetValue:
            self.presenter.raise_exception_for_invalid_limit_length()

    def get_all_reactions(
            self, limit: int, offset: int
    ):
        self._validate_limit_and_offset(limit=limit, offset=offset)
        # 1st db hit
        reactions = self.reaction_storage.get_all_reactions(
            limit=limit, offset=offset
        )

        reactions_comments_ids = self._get_reactions_on_comments(reactions)

        # 2nd db hit
        comments = self.comment_storage.get_comments_on_reactions(
            reactions_comments_ids
        )

        # comment on comment
        parent_comment_ids_for_reply = self._get_parent_comment_ids_for_reply(
            comments
        )

        # 3rd db hit
        parent_comments = self.comment_storage.get_comments_on_reactions(
            parent_comment_ids_for_reply
        )

        # finding posts
        posts_ids = self._post_ids_from_reaction(reactions)
        posts_ids.extend(self._post_ids_from_comments(parent_comments))

        posts = self.post_storage.get_all_posts(posts_ids)





        return reactions

    @staticmethod
    def _get_reactions_on_posts(reactions: List[ReactionDTO]) -> List[int]:
        reactions_on_posts = [
            reaction.reaction_id
            for reaction in reactions if reaction.post_id
        ]
        return reactions_on_posts

    @staticmethod
    def _get_reactions_on_comments(reactions: List[ReactionDTO]) -> List[int]:
        reactions_on_comments = [
            reaction.comment_id
            for reaction in reactions if reaction.comment_id
        ]
        return reactions_on_comments

    @staticmethod
    def _validate_limit_and_offset(limit: int, offset: int):

        if limit < 0:
            raise InvalidLimitValue

        if offset < 0:
            raise InvalidOffsetValue

    @staticmethod
    def _get_reactions_on_reply(comments: List[CommentDTO]) -> List[int]:
        reactions_on_reply_ids = [
            comment.comment_id
            for comment in comments if comment.parent_comment_id
        ]
        return reactions_on_reply_ids

    @staticmethod
    def _get_reactions_on_parent_comments(comments: List[CommentDTO]) ->\
            List[int]:
        reactions_on_posts_comments_ids = [
            comment.comment_id
            for comment in comments if comment.post_id
        ]
        return reactions_on_posts_comments_ids

    @staticmethod
    def _get_parent_comment_ids_for_reply(comments: List[CommentDTO]) -> \
            List[int]:
        parent_comment_ids = [
            comment.parent_comment_id
            for comment in comments if comment.parent_comment_id
        ]
        return parent_comment_ids

    @staticmethod
    def _post_ids_from_reaction(reactions: List[ReactionDTO]) -> List[int]:
        post_ids = [
            reaction.post_id
            for reaction in reactions if reaction.post_id
        ]
        return post_ids

    @staticmethod
    def _post_ids_from_comments(parent_comments: List[CommentDTO]) -> List[int]:
        post_ids = [
            comment.post_id
            for comment in parent_comments
        ]
        return post_ids

