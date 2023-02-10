import pytest
from fb_post.storages.post_storage_implementation import \
    PostStorageImplementation


@pytest.mark.django_db
def test_get_all_posts_with_posts_return_users_dto(users, posts,
                                                   posts_details_dto,
                                                   request_parameters_dto):
    user_id = 1
    expected_output = posts_details_dto
    post_storage = PostStorageImplementation()
    actual_output = post_storage.get_posts(user_id=user_id,
                                           requests_parameters_dto=request_parameters_dto)
    assert actual_output == expected_output


@pytest.mark.django_db
def test_create_post(users):
    user_id = 1
    content = "Hello"
    expected_output = None
    post_storage = PostStorageImplementation()
    actual_output = post_storage.create_post(user_id=user_id, content=content)
    assert actual_output == expected_output


@pytest.mark.django_db
def test_get_all_posts_without_posts_return_empty(users,
                                                  request_parameters_dto):
    user_id = 1
    expected_output = []
    post_storage = PostStorageImplementation()
    actual_output = post_storage.get_posts(user_id=user_id,
                                           requests_parameters_dto=request_parameters_dto)
    assert actual_output == expected_output


@pytest.mark.django_db
def test_get_all_reaction_on_post(users, posts, reaction_details_dto, reacts):
    posts_id = [1]
    expected_output = reaction_details_dto
    post_storage = PostStorageImplementation()
    actual_output = post_storage.get_all_reactions(list_of_post_id=posts_id)
    assert actual_output == expected_output


@pytest.mark.django_db
def test_get_all_reaction_on_post_no_reaction_return_empty(users, posts):
    posts_id = [1]
    expected_output =[]
    post_storage = PostStorageImplementation()
    actual_output = post_storage.get_all_reactions(list_of_post_id=posts_id)
    assert actual_output == expected_output


@pytest.mark.django_db
def test_get_all_comments_on_post(users, posts, comments_details_dto, comments):
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
def test_get_reactions_on_comments(users, posts, comments, reacts_on_comments, reaction_on_comments_details_dto):
    comments_id = [1]
    expected_output = reaction_on_comments_details_dto
    post_storage = PostStorageImplementation()
    actual_output = post_storage.get_reactions_on_comments(list_of_comment_id=comments_id)
    assert actual_output == expected_output
