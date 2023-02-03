from dataclasses import dataclass
from datetime import datetime


@dataclass
class UserDto:
    user_id: int
    name: str
    profile_pic: str


@dataclass
class PostDto:
    post_id: int
    content: str
    posted_by: UserDto
    posted_at: datetime


@dataclass
class ReactOnPostDto:
    reaction_id: int
    post: PostDto
    reaction: str
    reacted_at: datetime
    reacted_by: UserDto


@dataclass
class CommentOnPostDto:
    comment_id: int
    content: str
    commented_at: datetime
    commented_by: UserDto
    post: PostDto


class ReactionOnCommentDto:
    reaction_id: int
    comment: CommentOnPostDto
    reaction: str
    reacted_at: datetime
    reacted_by: UserDto


@dataclass
class CommentOnCommentDto:
    comment_id: int
    content: str
    commented_at: datetime
    commented_by: UserDto
    comment: CommentOnPostDto





