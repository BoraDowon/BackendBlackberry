from django.db import models


class Article(models.Model):
    board_id = models.IntegerField()
    title = models.CharField(max_length=1000, blank=False)
    body = models.CharField(max_length=2000, blank=False)
    views = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)
