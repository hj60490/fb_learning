from dataclasses import dataclass
from typing import List

from fb_post.interactors.storage_interfaces.dtos import PostDto, ReactOnPostDto,\
    CommentOnPostDto, CommentOnCommentDto, ReactionOnCommentDto, UserDto


@dataclass
class PostDetailsDto:
    users: List[UserDto]
    posts: List[PostDto]
    reactions_on_posts: List[ReactOnPostDto]
    comments_on_post: List[CommentOnPostDto]
    replies: List[CommentOnCommentDto]
    reactions_on_comments: List[ReactionOnCommentDto]


@dataclass
class PostReactionCommentDto:
    posts: List[PostDto]
    reactions_on_post: List[ReactOnPostDto]
    comments_on_post: List[CommentOnPostDto]
    comments_on_comment: List[CommentOnCommentDto]
    reactions_on_comment: List[ReactionOnCommentDto]


@dataclass
class ReactionAndCommentDto:
    post: PostDto
    reactions_on_post: List[ReactOnPostDto]
    comments_on_post: List[CommentOnPostDto]
    comments_on_comment: List[CommentOnCommentDto]
    reactions_on_comment: List[ReactionOnCommentDto]

