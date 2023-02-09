import pytest
from fb_post.interactors.storage_interfaces.dtos import RequestsParametersDTO, \
    UserDto, PostDto, ReactOnPostDto, CommentOnPostDto, CommentOnCommentDto, \
    ReactionOnCommentDto
from fb_post.interactors.presenter_interfaces.dtos import PostDetailsDto
from datetime import datetime
from freezegun import freeze_time
from fb_post.models import User


@pytest.fixture()
def user():
    user = User.objects.create(
        name="Harsh",
        profile_pic="www.google.com"
    )
    user.save()
    return user


@pytest.fixture()
def users():
    users = [
        {
            "name": "User 1",
        },
        {
            "name": "User 2",
        },
        {
            "name": "User 3",
        }
    ]

    users_list = []
    for user in users:
        users_list.append(
            User(name=user['name'])
        )
    User.objects.bulk_create(users_list)


@pytest.fixture()
def user_details_dto():
    users_list = [UserDto(user_id=1,
                          name="Harsh",
                          profile_pic="www.google.com"
                          )]
    return users_list


@pytest.fixture()
def get_requests_parameters_dto_with_invalid_offset():
    get_requests_parameters_dto = RequestsParametersDTO(
        offset=-1, limit=2, sort_order="", post_content="")
    return get_requests_parameters_dto


@pytest.fixture()
def get_requests_parameters_dto_with_invalid_limit():
    get_requests_parameters_dto = RequestsParametersDTO(
        offset=1, limit=-1, sort_order="", post_content="")
    return get_requests_parameters_dto


@pytest.fixture()
def get_requests_parameters_dto():
    get_requests_parameters_dto = RequestsParametersDTO(
        offset=0, limit=2, sort_order="", post_content="")
    return get_requests_parameters_dto


@pytest.fixture()
def get_user_dto():
    get_user_dto = UserDto(
        user_id=5,
        name="harsh",
        profile_pic="www.google.com"
    )
    return get_user_dto


@pytest.fixture()
def get_no_posts_dto():
    user_posts_details_dto = PostDetailsDto(
        users=[UserDto(
            user_id=5,
            name="harsh",
            profile_pic="www.google.com"
        )],
        posts=[],
        reactions_on_posts=[],
        comments_on_post=[],
        replies=[],
        reactions_on_comments=[]
    )
    return user_posts_details_dto


@pytest.fixture()
@freeze_time("2023-02-08 11:57:29")
def get_posts_with_no_reaction_and_comments_dto():
    user_posts_details_dto = PostDetailsDto(
        users=[UserDto(
            user_id=5,
            name="harsh",
            profile_pic="www.google.com"
        )],
        posts=[PostDto(
            post_id=1,
            content="hello",
            posted_at=datetime.now(),
            posted_by_id=5

        )],
        reactions_on_posts=[],
        comments_on_post=[],
        replies=[],
        reactions_on_comments=[]
    )
    return user_posts_details_dto


@pytest.fixture()
@freeze_time("2023-02-08 11:57:29")
def get_posts_with_only_reactions():
    user_posts_details_dto = PostDetailsDto(
        users=[UserDto(
            user_id=5,
            name="harsh",
            profile_pic="www.google.com"
        )],
        posts=[PostDto(
            post_id=1,
            content="hello",
            posted_at=datetime.now(),
            posted_by_id=5

        )],
        reactions_on_posts=[ReactOnPostDto(
            reaction_id=1,
            post_id=1,
            reaction="HAHA",
            reacted_at=datetime.now(),
            reacted_by_id=5
        )],
        comments_on_post=[],
        replies=[],
        reactions_on_comments=[]
    )
    return user_posts_details_dto


@pytest.fixture()
@freeze_time("2023-02-08 11:57:29")
def get_posts_with_only_comments():
    user_posts_details_dto = PostDetailsDto(
        users=[UserDto(
            user_id=5,
            name="harsh",
            profile_pic="www.google.com"
        )],
        posts=[PostDto(
            post_id=1,
            content="hello",
            posted_at=datetime.now(),
            posted_by_id=5

        )],
        reactions_on_posts=[],
        comments_on_post=[CommentOnPostDto(
            comment_id=1,
            commented_by_id=5,
            content="comment",
            post_id=1,
            commented_at=datetime.now()

        )],
        replies=[],
        reactions_on_comments=[]
    )
    return user_posts_details_dto


@pytest.fixture()
@freeze_time("2023-02-08 11:57:29")
def get_posts_with_only_comments_with_reply():
    user_posts_details_dto = PostDetailsDto(
        users=[UserDto(
            user_id=5,
            name="harsh",
            profile_pic="www.google.com"
        )],
        posts=[PostDto(
            post_id=1,
            content="hello",
            posted_at=datetime.now(),
            posted_by_id=5

        )],
        reactions_on_posts=[],
        comments_on_post=[CommentOnPostDto(
            comment_id=1,
            commented_by_id=5,
            content="comment",
            post_id=1,
            commented_at=datetime.now()

        )],
        replies=[CommentOnCommentDto(
            commented_at=datetime.now(),
            comment_id=2,
            commented_by_id=5,
            content="reply",
            parent_comment_id=1
        )],
        reactions_on_comments=[]
    )
    return user_posts_details_dto


@pytest.fixture()
@freeze_time("2023-02-08 11:57:29")
def get_posts_with_only_comments_with_reaction():
    user_posts_details_dto = PostDetailsDto(
        users=[UserDto(
            user_id=5,
            name="harsh",
            profile_pic="www.google.com"
        )],
        posts=[PostDto(
            post_id=1,
            content="hello",
            posted_at=datetime.now(),
            posted_by_id=5

        )],
        reactions_on_posts=[],
        comments_on_post=[CommentOnPostDto(
            comment_id=1,
            commented_by_id=5,
            content="comment",
            post_id=1,
            commented_at=datetime.now()

        )],
        replies=[CommentOnCommentDto(
            commented_at=datetime.now(),
            comment_id=2,
            commented_by_id=5,
            content="reply",
            parent_comment_id=1
        )],
        reactions_on_comments=[ReactionOnCommentDto(
            reaction_id=1,
            reaction="WOW",
            comment_id=1,
            reacted_at=datetime.now(),
            reacted_by_id=5
        )]
    )
    return user_posts_details_dto


@pytest.fixture()
@freeze_time("2023-02-08 11:57:29")
def get_posts_details():
    user_posts_details_dto = PostDetailsDto(
        users=[UserDto(
            user_id=5,
            name="harsh",
            profile_pic="www.google.com"
        )],
        posts=[PostDto(
            post_id=1,
            content="hello",
            posted_at=datetime.now(),
            posted_by_id=5

        )],
        reactions_on_posts=[ReactOnPostDto(
            reaction_id=1,
            post_id=1,
            reaction="HAHA",
            reacted_at=datetime.now(),
            reacted_by_id=5
        )],
        comments_on_post=[CommentOnPostDto(
            comment_id=1,
            commented_by_id=5,
            content="comment",
            post_id=1,
            commented_at=datetime.now()

        )],
        replies=[CommentOnCommentDto(
            commented_at=datetime.now(),
            comment_id=2,
            commented_by_id=5,
            content="reply",
            parent_comment_id=1
        )],
        reactions_on_comments=[ReactionOnCommentDto(
            reaction_id=1,
            reaction="WOW",
            comment_id=1,
            reacted_at=datetime.now(),
            reacted_by_id=5
        ),
            ReactionOnCommentDto(
                reaction_id=2,
                reaction="SAD",
                comment_id=2,
                reacted_at=datetime.now(),
                reacted_by_id=5,
            )]
    )
    return user_posts_details_dto
