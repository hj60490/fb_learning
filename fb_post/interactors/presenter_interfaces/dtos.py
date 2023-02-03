from dataclasses import dataclass
from typing import List

from fb_post.interactors.storage_interfaces.dtos import PostDto, ReactOnPostDto,\
    CommentOnPostDto, CommentOnCommentDto, ReactionOnCommentDto


@dataclass
class PostDetailsDto:
    post_dto_list: List[PostDto]
    reaction_post_dto_list: List[ReactOnPostDto]
    comment_on_post_dto_list: List[CommentOnPostDto]
    replies_dto_list: List[CommentOnCommentDto]
    reaction_on_comment_dto: List[ReactionOnCommentDto]

