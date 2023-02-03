from dataclasses import dataclass
from typing import List

from fb_post.interactors.storage_interfaces.dtos import PostDto, ReactOnPostDto,\
    CommentOnPostDto, CommentOnCommentDto, ReactionOnCommentDto


@dataclass
class PostDetailsDto:
    PostDtoList: List[PostDto]
    ReactionPostDtoList: List[ReactOnPostDto]
    CommentOnPostDtoList: List[CommentOnPostDto]
    RepliesDtoList: List[CommentOnCommentDto]
    ReactionOnCommentDto: List[ReactionOnCommentDto]

