import pytest
from fb_post.interactors.storage_interfaces.dtos import RequestsParametersDTO, \
    UserDto, PostDto, ReactOnPostDto, CommentOnPostDto, CommentOnCommentDto, \
    ReactionOnCommentDto
from fb_post.interactors.presenter_interfaces.dtos import PostDetailsDto
from datetime import datetime
from freezegun import freeze_time
from fb_post.models import User, Post, React, Comment
import datetime
from fb_post.tests.factories.models import UserFactory, PostFactory, \
    ReactFactory, CommentFactory
from fb_post.tests.factories.storage_dtos import PostDTOFactory, UserDTOFactory, \
    ReactOnPostDTOFactory, ReactOnCommentDTOFactory, CommentOnCommentDTOFactory, \
    CommentOnPostDTOFactory, RequestsParametersDTOFactory, \
    PostDetailsDtoFactory, PostReactionCommentDtoFactory, \
    ReactionAndCommentDtoFactory


@pytest.fixture()
def users():
    return UserFactory.create_batch(size=3)


@pytest.fixture()
def posts():
    return [
        PostFactory(content="Hello", posted_by_id=1),
        PostFactory(content="Hello",
                    posted_by_id=1,
                    posted_at=datetime.datetime(2023, 2, 13, 11, 20, 15)),
        PostFactory(content="Hello",
                    posted_by_id=1,
                    posted_at=datetime.datetime(2023, 2, 13, 11, 20, 20)),
        PostFactory(content="Harsh",
                    posted_by_id=1,
                    posted_at=datetime.datetime(2023, 2, 13, 11, 20, 25))
    ]


@pytest.fixture()
def user():
    return UserFactory()


@pytest.fixture(autouse=True)
def reset_storage_dto_factory_sequences():
    UserFactory.reset_sequence()
    PostFactory.reset_sequence()
    ReactFactory.reset_sequence()
    CommentFactory.reset_sequence()
    UserDTOFactory.reset_sequence()
    PostDTOFactory.reset_sequence()
    CommentOnCommentDTOFactory.reset_sequence()
    CommentOnPostDTOFactory.reset_sequence()
    ReactOnPostDTOFactory.reset_sequence()
    ReactOnCommentDTOFactory.reset_sequence()
    RequestsParametersDTOFactory.reset_sequence()
    PostDetailsDtoFactory.reset_sequence()
    PostReactionCommentDtoFactory.reset_sequence()
    ReactionAndCommentDtoFactory.reset_sequence()
    ReactOnPostDTOFactory.reaction.reset()
    ReactOnCommentDTOFactory.reaction.reset()
    RequestsParametersDTOFactory.offset.reset()
    RequestsParametersDTOFactory.limit.reset()









