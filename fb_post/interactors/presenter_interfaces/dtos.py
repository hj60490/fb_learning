from dataclasses import dataclass
from typing import List
import typing

from fb_post.interactors.storage_interfaces.dtos import PostDto, ReactOnPostDto, \
    CommentOnPostDto, CommentOnCommentDto, ReactionOnCommentDto, CommentDTO


@dataclass
class UserDto:
    user_id: int
    name: str
    profile_pic: typing.Optional[str]


@dataclass
class PostDetailsDto:
    users: List[UserDto]
    posts: List[PostDto]
    reactions_on_posts: List[ReactOnPostDto]
    comments: List[CommentDTO]
    reactions_on_comments: List[ReactionOnCommentDto]


@dataclass
class PostReactionCommentDto:
    posts: List[PostDto]
    reactions_on_post: List[ReactOnPostDto]
    comments: List[CommentDTO]
    reactions_on_comment: List[ReactionOnCommentDto]


@dataclass
class ReactionAndCommentDto:
    post: PostDto
    reactions_on_post: List[ReactOnPostDto]
    comments: List[CommentDTO]
    reactions_on_comment: List[ReactionOnCommentDto]

