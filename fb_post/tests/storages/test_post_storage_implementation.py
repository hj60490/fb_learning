import pytest
from freezegun import freeze_time

from fb_post.storages.post_storage_implementation import \
    PostStorageImplementation
from fb_post.models import Post


@pytest.mark.django_db
def test_get_all_posts_with_limit_offset_posts_return_posts_dto(users, posts,
                                                                request_parameters_dto):
    user_id = 1

    post_storage = PostStorageImplementation()
    actual_output = post_storage.get_posts(user_id=user_id,
                                           requests_parameters_dto=request_parameters_dto)

    assert len(actual_output) == request_parameters_dto.limit


@freeze_time("2023-02-08 11:57:29")
@pytest.mark.django_db
def test_get_all_posts_posts_with_post_content_return_posts_dto(users, posts, posts_details_dto_for_content,
                                              request_parameters_dto_for_content):
    user_id = 1
    posts_details_dto_for_content[0].posted_at = "2023-02-08 11:57:29"
    expected_output = posts_details_dto_for_content
    post_storage = PostStorageImplementation()
    actual_output = post_storage.get_posts(user_id=user_id,
                                           requests_parameters_dto=request_parameters_dto_for_content)
    actual_output[0].posted_at = "2023-02-08 11:57:29"
    assert actual_output == expected_output


@pytest.mark.django_db
def test_get_all_posts_with_no_posts_return_empty(users,
                                                  request_parameters_dto):
    user_id = 1
    expected_output = []
    post_storage = PostStorageImplementation()
    actual_output = post_storage.get_posts(user_id=user_id,
                                           requests_parameters_dto=request_parameters_dto)
    assert actual_output == expected_output


@pytest.mark.django_db
def test_create_post_weather_post_created(users):
    user_id = 1
    content = "Hello"
    post_storage = PostStorageImplementation()
    post_storage.create_post(content=content, user_id=user_id)
    assert Post.objects.filter(content=content, posted_by_id=1).exists()

#
# @pytest.mark.django_db
# def test_get_all_posts_with_post_content_posts_return_posts_dto(
#         users, posts, request_parameters_dto1, posts_details_with_all_filter
#
# ):
#     user_id = 1
#     expected_output = posts_details_with_all_filter
#     post_storage = PostStorageImplementation()
#     actual_output = post_storage.get_posts(user_id=user_id,
#                                            requests_parameters_dto=request_parameters_dto1)
#
#     assert actual_output == expected_output


@pytest.mark.django_db
def test_get_all_reaction_on_post_return_reaction_dto(users, posts,
                                                      reaction_details_dto,
                                                      reacts):
    posts_id = [1]
    expected_output = reaction_details_dto
    post_storage = PostStorageImplementation()
    actual_output = post_storage.get_all_reactions(list_of_post_id=posts_id)
    assert actual_output == expected_output


@pytest.mark.django_db
def test_get_all_reaction_on_post_no_reaction_return_empty(users, posts):
    posts_id = [1]
    expected_output = []
    post_storage = PostStorageImplementation()
    actual_output = post_storage.get_all_reactions(list_of_post_id=posts_id)
    assert actual_output == expected_output


@pytest.mark.django_db
def test_get_all_comments_on_post_return_comment_dto(users, posts,
                                                     comments_details_dto,
                                                     comments):
    posts_id = [1]
    expected_output = comments_details_dto
    post_storage = PostStorageImplementation()
    actual_output = post_storage.get_comments(list_of_post_id=posts_id)
    assert actual_output == expected_output


@pytest.mark.django_db
def test_get_all_comments_on_post_no_comment_return_empty(users, posts):
    posts_id = [1]
    expected_output = []
    post_storage = PostStorageImplementation()
    actual_output = post_storage.get_comments(list_of_post_id=posts_id)
    assert actual_output == expected_output


@pytest.mark.django_db
def test_get_reactions_on_comments_return_reaction(users, posts, comments,
                                                   reacts_on_comments,
                                                   reaction_on_comments_details_dto):
    comments_id = [1]
    expected_output = reaction_on_comments_details_dto
    post_storage = PostStorageImplementation()
    actual_output = post_storage.get_reactions_on_comments(
        list_of_comment_id=comments_id)
    assert actual_output == expected_output


@pytest.mark.django_db
def test_get_reactions_on_comments_return_empty(users, posts, comments):
    comments_id = [1]
    expected_output = []
    post_storage = PostStorageImplementation()
    actual_output = post_storage.get_reactions_on_comments(
        list_of_comment_id=comments_id)
    assert actual_output == expected_output


