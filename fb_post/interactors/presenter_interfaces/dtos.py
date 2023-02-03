from dataclasses import dataclass
from typing import List
from datetime import datetime
from fb_post.interactors.storage_interfaces.dtos import PostDto, ReactOnPostDto,\
    CommentOnPostDto, CommentOnCommentDto, ReactionOnCommentDto, UserDto


@dataclass
class PostDetailsDto:
    PostDtoList: List[PostDto]
    ReactionPostDtoList: List[ReactOnPostDto]
    CommentOnPostDtoList: List[CommentOnPostDto]
    RepliesDtoList: List[CommentOnCommentDto]
    ReactionOnCommentDto: List[ReactionOnCommentDto]


@dataclass
class ReactionDto:
    count: int
    type: List[str]


@dataclass
class RepliesDto:
    comment_id: int
    commentator: UserDto
    commented_at: datetime
    comment_content: str
    reactions: ReactionDto


@dataclass
class CommentDescriptionDto:
    comment_id: int
    commentator: UserDto
    commented_at: datetime
    comment_content: str
    reactions: ReactionDto
    replies: List[RepliesDto]
    comment_count: int


@dataclass
class PostResponseDto:
    post_id: int
    posted_by: UserDto
    posted_at: datetime
    post_content: str
    reactions: ReactionDto
    comments: List[CommentDescriptionDto]
