import typing
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
    posted_by_id: int
    posted_at: datetime


@dataclass
class ReactOnPostDto:
    reaction_id: int
    post_id: int
    reaction: str
    reacted_at: datetime
    reacted_by_id: int


@dataclass
class CommentOnPostDto:
    comment_id: int
    content: str
    commented_at: datetime
    commented_by_id: int
    post_id: int


@dataclass
class ReactionOnCommentDto:
    reaction_id: int
    comment_id: int
    reaction: str
    reacted_at: datetime
    reacted_by_id: int


@dataclass
class CommentOnCommentDto:
    comment_id: int
    content: str
    commented_at: datetime
    commented_by_id: int
    parent_comment_id: int


@dataclass
class CommentDTO:
    comment_id: int
    content: str
    commented_at: datetime
    commented_by_id: int
    parent_comment_id: typing.Optional[int]
    post_id: typing.Optional[int]
