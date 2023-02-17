from django.db import models
from datetime import datetime


class Post(models.Model):
    content = models.TextField(max_length=1000)
    posted_at = models.DateTimeField(default=datetime.now)
    posted_by_id = models.IntegerField(null=True, blank=True)



