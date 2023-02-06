from dataclasses import dataclass
from typing import List

from fb_post.interactors.storage_interfaces.dtos import PostDto, ReactOnPostDto,\
    CommentOnPostDto, CommentOnCommentDto, ReactionOnCommentDto


@dataclass
class PostDetailsDto:
    posts: List[PostDto]
    reactions_on_posts: List[ReactOnPostDto]
    comments_on_post: List[CommentOnPostDto]
    replies: List[CommentOnCommentDto]
    reactions_on_comments: List[ReactionOnCommentDto]

