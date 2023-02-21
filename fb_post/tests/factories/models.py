import datetime

import factory
from fb_post.models import Post, Comment, React


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    content = factory.sequence(lambda n: f"post_{n + 1}")
    posted_at = datetime.datetime(2023, 2, 13, 11, 20, 0)
    posted_by_id = factory.sequence(lambda n: n + 1)


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    commented_at = datetime.datetime(2023, 2, 13, 11, 20)
    commented_by_id = factory.sequence(lambda n: n + 1)
    post_id = factory.sequence(lambda n: n + 1)
    parent_comment = None
    content = factory.sequence(lambda n: f"comment_{n + 1}")


class ReactFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = React

    reacted_at = datetime.datetime(2023, 2, 13, 11, 20)
    post_id = factory.sequence(lambda n: n + 1)
    comment = None
    reacted_by_id = factory.sequence(lambda n: n + 1)
    reaction = factory.Iterator(["HAHA", "SAD", "WOW"])

