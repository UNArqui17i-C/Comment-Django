from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Comment(models.Model):
    email = models.CharField(max_length=20)
    comment = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    length = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % self.comment_name
