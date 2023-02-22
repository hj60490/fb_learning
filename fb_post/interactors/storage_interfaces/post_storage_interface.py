import abc
from abc import ABC
from .dtos import PostDto, ReactOnPostDto, CommentOnPostDto, \
    ReactionOnCommentDto, CommentOnCommentDto, RequestsParametersDTO, CommentDTO
from typing import List


class PostInterface(ABC):
    @abc.abstractmethod
    def create_post(self, content: str, user_id: int):
        pass

    @abc.abstractmethod
    def get_posts(
            self, user_id: int, requests_parameters_dto: RequestsParametersDTO
    ) -> List[PostDto]:
        pass

    @abc.abstractmethod
    def get_all_reactions(self, list_of_post_id: List[int]) -> \
            List[ReactOnPostDto]:
        pass

    @abc.abstractmethod
    def get_comments(self, list_of_post_id: List[int]) -> \
            List[CommentDTO]:
        pass

    @abc.abstractmethod
    def get_reactions_on_comments(self, list_of_comment_id: List[int]) -> \
            List[ReactionOnCommentDto]:
        pass

    @abc.abstractmethod
    def get_all_posts(self, post_ids: List[int]) -> List[PostDto]:
        pass

