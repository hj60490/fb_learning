from django.db import models
from datetime import datetime


class Comment(models.Model):
    content = models.TextField(max_length=1000)
    commented_at = models.DateTimeField(default=datetime.now)
    commented_by_id = models.IntegerField(null=True, blank=True)
    parent_comment_id = models.IntegerField(null=True, blank=True)
    post_id = models.IntegerField(null=True, blank=True)