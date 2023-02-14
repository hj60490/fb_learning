from django.db import models
from datetime import datetime


# class User(models.Model):
#     name = models.CharField(max_length=100)
#     profile_pic = models.TextField(null=True, blank=True)


class Post(models.Model):
    content = models.TextField(max_length=1000)
    posted_at = models.DateTimeField(default=datetime.now)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    content = models.TextField(max_length=1000)
    commented_at = models.DateTimeField(default=datetime.now)
    commented_by = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE,
                                       null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True,
                             blank=True)


class React(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True,
                             blank=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE,
                                null=True, blank=True)
    reaction = models.TextField(max_length=100)
    reacted_at = models.DateTimeField(default=datetime.now)
    reacted_by = models.ForeignKey(User, on_delete=models.CASCADE)

