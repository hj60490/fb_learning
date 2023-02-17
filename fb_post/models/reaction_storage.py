from django.db import models
from datetime import datetime


class React(models.Model):
    post_id = models.IntegerField(null=True, blank=True)
    comment = models.IntegerField(null=True, blank=True)
    reaction = models.TextField(max_length=100)
    reacted_at = models.DateTimeField(default=datetime.now)
    reacted_by_id = models.IntegerField(null=True, blank=True)
