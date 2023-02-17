import factory
import datetime
from fb_post.interactors.storage_interfaces.dtos import UserDto, PostDto, \
    CommentOnPostDto, CommentOnCommentDto, ReactOnPostDto, ReactionOnCommentDto, \
    RequestsParametersDTO
from fb_post.interactors.presenter_interfaces.dtos import PostDetailsDto, \
    PostReactionCommentDto, ReactionAndCommentDto


class UserDTOFactory(factory.Factory):
    class Meta:
        model = UserDto

    user_id = factory.sequence(lambda n: n + 1)
    name = factory.Sequence(lambda n: f"User_{n + 1}")
    profile_pic = factory.Sequence(
        lambda n: f"https://profile_pic_url{n + 1}.com")


class PostDTOFactory(factory.Factory):
    class Meta:
        model = PostDto

    post_id = factory.sequence(lambda n: n + 1)
    content = factory.sequence(lambda n: f"post_{n + 1}")
    posted_at = datetime.datetime(2023, 2, 13, 11, 20, 0)
    posted_by_id = factory.sequence(lambda n: n + 1)


class CommentOnPostDTOFactory(factory.Factory):
    class Meta:
        model = CommentOnPostDto

    comment_id = factory.sequence(lambda n: n + 1)
    commented_at = datetime.datetime(2023, 2, 13, 11, 20, 0)
    commented_by_id = factory.sequence(lambda n: n + 1)
    post_id = factory.sequence(lambda n: n + 1)
    content = factory.sequence(lambda n: f"comment_{n + 1}")


class CommentOnCommentDTOFactory(factory.Factory):
    class Meta:
        model = CommentOnCommentDto

    comment_id = factory.sequence(lambda n: n + 1)
    commented_at = datetime.datetime(2023, 2, 13, 11, 20, 0)
    commented_by_id = factory.sequence(lambda n: n + 1)
    parent_comment_id = factory.sequence(lambda n: n + 1)
    content = factory.sequence(lambda n: f"comment_{n + 1}")


class ReactOnPostDTOFactory(factory.Factory):
    class Meta:
        model = ReactOnPostDto

    reaction_id = factory.sequence(lambda n: n + 1)
    reacted_at = datetime.datetime(2023, 2, 13, 11, 20, 0)
    post_id = factory.sequence(lambda n: n + 1)
    reacted_by_id = factory.sequence(lambda n: n + 1)
    reaction = factory.Iterator(["HAHA", "SAD", "WOW"])


class ReactOnCommentDTOFactory(factory.Factory):
    class Meta:
        model = ReactionOnCommentDto

    reaction_id = factory.sequence(lambda n: n + 1)
    reacted_at = datetime.datetime(2023, 2, 13, 11, 20, 0)
    comment_id = factory.sequence(lambda n: n + 1)
    reacted_by_id = factory.sequence(lambda n: n + 1)
    reaction = factory.Iterator(["HAHA", "SAD", "WOW"])


class RequestsParametersDTOFactory(factory.Factory):
    class Meta:
        model = RequestsParametersDTO

    offset = factory.Iterator([0, 1, 2, 3])
    limit = factory.Iterator([2, 3])
    sort_order = None
    post_content = None


class PostDetailsDtoFactory(factory.Factory):
    class Meta:
        model = PostDetailsDto

    users = factory.List([
        factory.SubFactory(UserDTOFactory) for i in range(2)
    ])
    posts = factory.List([
        factory.SubFactory(PostDTOFactory) for i in range(2)
    ])
    reactions_on_posts = factory.List([
        factory.SubFactory(ReactOnPostDto) for i in range(2)
    ])
    comments_on_post = factory.List([
        factory.SubFactory(CommentOnPostDto) for i in range(2)
    ])
    replies = factory.List([
        factory.SubFactory(CommentOnCommentDto) for i in range(2)
    ])
    reactions_on_comments = factory.List([
        factory.SubFactory(ReactionOnCommentDto) for i in range(2)
    ])


class PostReactionCommentDtoFactory(factory.Factory):
    class Meta:
        model = PostReactionCommentDto

    posts = factory.List([
        factory.SubFactory(PostDTOFactory) for i in range(2)
    ])
    reactions_on_post = factory.List([
        factory.SubFactory(ReactOnPostDto) for i in range(2)
    ])
    comments_on_post = factory.List([
        factory.SubFactory(CommentOnPostDto) for i in range(2)
    ])
    comments_on_comment = factory.List([
        factory.SubFactory(CommentOnCommentDto) for i in range(2)
    ])
    reactions_on_comment = factory.List([
        factory.SubFactory(ReactionOnCommentDto) for i in range(2)
    ])


class ReactionAndCommentDtoFactory(factory.Factory):
    class Meta:
        model = ReactionAndCommentDto

    posts = factory.SubFactory(PostDTOFactory)
    reactions_on_post = factory.List([
        factory.SubFactory(ReactOnPostDto) for i in range(2)
    ])
    comments_on_post = factory.List([
        factory.SubFactory(CommentOnPostDto) for i in range(2)
    ])
    comments_on_comment = factory.List([
        factory.SubFactory(CommentOnCommentDto) for i in range(2)
    ])
    reactions_on_comment = factory.List([
        factory.SubFactory(ReactionOnCommentDto) for i in range(2)
    ])
