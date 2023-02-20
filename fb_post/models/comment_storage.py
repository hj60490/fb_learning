from django.db import models
from datetime import datetime
from fb_post.models import Post


class Comment(models.Model):
    content = models.TextField(max_length=1000)
    commented_at = models.DateTimeField(default=datetime.now)
    commented_by_id = models.IntegerField(null=True, blank=True)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE
                                       , null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True,
                             blank=True)
