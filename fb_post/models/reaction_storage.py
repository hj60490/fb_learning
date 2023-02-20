from django.db import models
from datetime import datetime

from fb_post.models import Post, Comment


class React(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             null=True, blank=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE,
                                null=True, blank=True)
    reaction = models.TextField(max_length=100)
    reacted_at = models.DateTimeField(default=datetime.now)
    reacted_by_id = models.IntegerField(null=True, blank=True)
