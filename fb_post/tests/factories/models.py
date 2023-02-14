import datetime

import factory
from fb_post.models import User, Post, Comment, React


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    name = factory.Sequence(lambda n: f"User_{n + 1}")
    profile_pic = factory.Sequence(
        lambda n: f"https://profile_pic_url{n + 1}.com")


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    content = factory.sequence(lambda n: f"post_{n + 1}")
    posted_at = datetime.datetime(2023, 2, 13, 11, 20, 0)
    posted_by = factory.SubFactory(UserFactory)


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    commented_at = datetime.datetime(2023, 2, 13, 11, 20)
    commented_by = factory.SubFactory(UserFactory)
    post = factory.SubFactory(PostFactory)
    parent_comment = None
    content = factory.sequence(lambda n: f"comment_{n + 1}")


class ReactFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = React

    reacted_at = datetime.datetime(2023, 2, 13, 11, 20)
    post = factory.SubFactory(PostFactory)
    comment = None
    reacted_by = factory.SubFactory(UserFactory)
    reaction = factory.Iterator(["HAHA", "SAD", "WOW"])
