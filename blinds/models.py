from django.db import models
from django.utils.translation import ugettext as _

"""
STATUS CATEGORIES
1 - normal
2 - temp
3 - notice
4 - warning
5 - hidden
6 - deleted
7 - spam
"""


class Article(models.Model):
    ARTICLE_STATUS = {
        ('1normal',  _('status_published')),
        ('2temp',    _('status_draft')),
        ('5hidden',  _('status_pending')),
        ('6deleted', _('status_deleted')),
    }
    status = models.CharField(max_length=10, choices=ARTICLE_STATUS, default='1normal')
    board_id = models.IntegerField(default=0)
    title = models.CharField(max_length=1000, blank=False)
    body = models.TextField()
    views = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)


class Comment(models.Model):
    COMMENT_STATUS = {
        ('1normal',  _('status_normal')),
        ('4deleted', _('status_deleted')),
        ('7spam',    _('status_spam')),
    }

    status = models.CharField(max_length=10, choices=COMMENT_STATUS, default='1normal')
    article_id = models.IntegerField(default=0)
    comment_id = models.IntegerField(default=0)
    body = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
