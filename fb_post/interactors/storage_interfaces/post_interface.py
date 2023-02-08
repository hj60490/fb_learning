from abc import ABC
from .dtos import PostDto, ReactOnPostDto, CommentOnPostDto, \
    ReactionOnCommentDto, CommentOnCommentDto, RequestsParametersDTO
from typing import List
from fb_post.interactors.presenter_interfaces.dtos import PostDetailsDto


class PostInterface(ABC):

    def create_post(self, content: str, user_id: int):
        pass

    def get_posts(
            self, user_id: int, requests_parameters_dto: RequestsParametersDTO
    ) -> List[PostDto]:
        pass

    def get_all_reactions(self, list_of_post_id: List[int]) -> \
            List[ReactOnPostDto]:
        pass

    def get_comments(self, list_of_post_id: List[int]) -> \
            List[CommentOnPostDto]:
        pass

    def get_reactions_on_comments(self, list_of_comment_id: List[int]) -> \
            List[ReactionOnCommentDto]:
        pass

    def get_replies_on_comment(self, list_of_comment_id) -> \
            List[CommentOnCommentDto]:
        pass







